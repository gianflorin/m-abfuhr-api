def display_results(data):
    if "records" in data:
        # Erstelle eine Liste für die Tabelle
        df_data = []
        for record in data["records"]:
            fields = record["fields"]
            # Hier fügst du jetzt den Schlüssel 'sammel_id' ein
            df_data.append({
                "Gebietsbezeichnung": fields.get("gebietsbezeichnung", "Nicht verfügbar"),
                "Sammelart": fields.get("sammel_id", "Nicht verfügbar"),
                "Datum": fields.get("datum", "Nicht verfügbar"),
                "Startzeitpunkt": fields.get("startzeitpunkt", "Nicht verfügbar")
            })
        # Konvertiere die Liste in ein DataFrame und zeige es als Tabelle an
        st.table(df_data)
    else:
        st.error("Keine Daten für diese Straße gefunden.")

# Der Rest des Codes bleibt unverändert
# ...

if __name__ == "__main__":
    main()
