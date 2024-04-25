import streamlit as st
import requests
import pandas as pd
# Daten anhand des Strassennamens von der API abrufen
def fetch_data_for_street(street_name):
    encoded_street_name = requests.utils.quote(street_name)
    api_url = f"https://daten.stadt.sg.ch/api/records/1.0/search/?dataset=abfuhrdaten-stadt-stgallen&q={encoded_street_name}&rows=20"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"API-Antwort: {response.status_code}, Inhalt: {response.text}")
        return None
# Outputs anzeigen
def display_results(data):
    if "records" in data:
        # Liste für die Tabelle Erstellen
        df_data = []
        for record in data["records"]:
            fields = record["fields"]
            # Sammelart mit Hilfe der 'sammelung_id' hinzufügen
            df_data.append({
                "Gebietsbezeichnung": fields.get("gebietsbezeichnung", "Nicht verfügbar"),
                "Sammelart": fields.get("sammlung_id", "Nicht verfügbar"),
                "Datum": fields.get("datum", "Nicht verfügbar"),
                "Startzeitpunkt": fields.get("startzeitpunkt", "Nicht verfügbar")
            })
        # Liste in ein Data Frame konvertieren, da einfacher zu handhaben
        df = pd.DataFrame(df_data)
        # Data Frame als Tabelle anzeigen
        st.table(df)
    else:
        st.error("Keine Daten für diese Straße gefunden.")

def main(): # Um Benutzer-Inputs zu sammeln
    st.title("Müllabfuhr-Daten Stadt St.Gallen") # Titel auf der Seite
    street = st.text_input("Gib deine Strasse ein", "") # Suchfeld
    if st.button("Informationen suchen"): # Suche per Klick auf button ausführen
        if not street:
            st.error("Bitte gib eine Strasse ein.")
        else:
            data = fetch_data_for_street(street) # Zurückgreifen auf API-Daten, siehe oben
            if data:
                display_results(data)
            else:
                st.error("Es konnten keine Daten abgerufen werden.")

if __name__ == "__main__":
    main()
