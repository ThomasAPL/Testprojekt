# Adressverwaltung

Eine einfache Webanwendung zur Verwaltung von Adressen.

## Setup

### Voraussetzungen
- Python 3.8+
- Virtuelle Umgebung (empfohlen)

### Installation
```bash
# Virtuelle Umgebung erstellen
python -m venv venv

# Virtuelle Umgebung aktivieren
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Abhängigkeiten installieren (wenn requirements.txt verfügbar)
pip install -r requirements.txt
```

## Routen

Die Anwendung wird folgende Hauptrouten bereitstellen:

- `/` - Startseite
- `/addresses/` - Adressliste anzeigen
- `/addresses/add/` - Neue Adresse hinzufügen
- `/addresses/<id>/` - Adresse anzeigen
- `/addresses/<id>/edit/` - Adresse bearbeiten
- `/addresses/<id>/delete/` - Adresse löschen

## Technologien

- **Backend**: Python
- **Framework**: Django (geplant)
- **Datenbank**: SQLite (Entwicklung), PostgreSQL (Produktion)
- **Frontend**: HTML, CSS, JavaScript (Bootstrap geplant)

## Module

### addressbook
Das `addressbook` Modul enthält die Hauptlogik der Adressbuch-Anwendung.

### addresses
Das `addresses` Modul verwaltet die Adress-Entitäten und deren Operationen.

## Entwicklungshinweise

### Nächste Schritte
1. Django-Projekt initialisieren
2. Modelle für Adressen erstellen
3. Views und Templates implementieren
4. Tabellen- und Filter-Funktionalität hinzufügen
5. Tests schreiben
6. Styling und UX verbessern

### Projektstruktur
```
adressverwaltung/
├── README.md
├── addressbook/
│   └── __init__.py
└── addresses/
    └── __init__.py
```

### Coding Standards
- Verwende deutsche Kommentare und Dokumentation
- Folge PEP 8 für Python-Code
- Schreibe Tests für alle neuen Funktionen
- Verwende aussagekräftige Commit-Messages

## Beitragen

Bei Fragen oder Problemen bitte ein Issue erstellen oder einen Pull Request einreichen.