# Web Crawler Tool

Een asynchrone webcrawler die een opgegeven website doorzoekt en het aantal woorden telt, waarna de resultaten worden opgeslagen in een JSON-bestand.

## Functies

- Crawlt een website tot een door de gebruiker opgegeven diepte.
- Extraheert tekstinhoud van bezochte pagina's.
- Telt het aantal keer dat elk woord voorkomt.
- Slaat de resultaten op in een `output.json` bestand.

## Wat betekent crawl-diepte?

De crawler volgt links tot de opgegeven diepte:
- **Diepte 0**: Alleen de startpagina.
- **Diepte 1**: Startpagina en alle links op die pagina.
- **Diepte 2**: Startpagina, links op de startpagina, en links op die tweede laag.

Na de opgegeven diepte stopt de crawler automatisch.

## Installatie

1. **Clone deze repository**  
```bash
git clone https://github.com/Sirehtea/Web_Crawler
cd Web_Crawler
```

2. **Installeer dependencies**  
```bash
pip install -r requirements.txt
```

3. **Start de crawler**  
```bash
python main.py
```

## Bestandstructuur

```bash
Web_Crawler/
├── main.py
├── output.json
├── README.md
├── requirements.txt
```

