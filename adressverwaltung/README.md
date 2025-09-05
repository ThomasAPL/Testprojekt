# Adressverwaltung (Django, django-tables2, django-filter)

Diese App verwaltet Adressen (Kunden, Lieferanten, allgemein) und stellt sie tabellarisch dar – ohne React und ohne JavaScript. Die Tabelle ist sortierbar/paginierbar (query-parameter-basiert), und Filter/Suche erfolgen über django-filter.

## Setup

1) Virtuelle Umgebung und Abhängigkeiten installieren:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

2) Datenbank migrieren und Admin-Nutzer anlegen:

```bash
python manage.py migrate
python manage.py createsuperuser
```

3) Entwicklungsserver starten:

```bash
python manage.py runserver
```

4) Öffne im Browser:
- http://127.0.0.1:8000/ für die Adressliste
- http://127.0.0.1:8000/admin/ für das Admin-Backend

## Routen

- `/` – alle Adressen (Tabelle mit Filtern)
- `/kunden/` – gefilterte Sicht auf Kunden
- `/lieferanten/` – gefilterte Sicht auf Lieferanten
- `/allgemein/` – gefilterte Sicht auf allgemeine Adressen
- `/neu/` – neue Adresse anlegen
- `/<id>/bearbeiten/` – Adresse bearbeiten
- `/<id>/loeschen/` – Adresse löschen

## Technologien

- Django 5
- django-tables2
- django-filter
- Bootstrap 5 (nur CSS, kein JS)

## Hinweise

- Es wird bewusst auf JavaScript verzichtet. Sortierung und Pagination erfolgen per Query-Parametern (Server-seitig).
- Für produktiven Betrieb `DEBUG=False` setzen und `ALLOWED_HOSTS` konfigurieren.