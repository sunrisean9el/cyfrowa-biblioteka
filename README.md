# Cyfrowa Biblioteka

Projekt **Cyfrowa Biblioteka** to aplikacja stworzona w Django, umożliwiająca zarządzanie książkami, ich wypożyczeniami oraz rejestrację i logowanie użytkowników. Aplikacja korzysta z bazy danych PostgreSQL oraz Docker do łatwego uruchomienia projektu w kontenerach.

---

## 📌 Spis treści

- [Opis projektu](#opis-projektu)
- [Wymagania](#wymagania)
- [Funkcjonalności](#funkcjonalności)
- [Technologie i biblioteki](#technologie-i-biblioteki)
- [Instrukcja uruchomienia](#instrukcja-uruchomienia)
  - [1. Klonowanie repozytorium](#1-pobierz-projekt)
  - [2. Uruchomienie aplikacji z Docker](#2-skonfiguruj-docker-i-uruchom-kontenery)
  - [3. Uruchomienie bazy danych](#3-skonfiguruj-bazę-danych)
  - [4. Załadowanie danych przykładowych](#4-załaduj-dane-przykładowe)
  - [5. Stworzenie konta administratora](#5-utwórz-konto-administratora)
  - [6. Uruchomienie aplikacji](#6-uruchom-aplikację)
  - [7. Zarządzanie bazą danych](#7-zarządzanie-bazą-danych)
  - [8. Zatrzymanie kontenerów](#8-zatrzymanie-kontenerów)
- [Struktura projektu](#struktura-projektu)
- [Przykładowe dane (fixtures)](#przykładowe-dane)
- [Testy](#testy)
- [Walidacja i bezpieczeństwo](#walidacja-i-bezpieczeństwo)
- [Problemy](#problemy)
- [Autor](#autor)

---

## Opis projektu

Projekt zrealizowany w ramach zaliczenia przedmiotu. Ma na celu weryfikację umiejętności w pracy z aplikacją webową opartą o wzorzec MVC. Umożliwia podstawowe operacje CRUD na modelu książki, obsługuje użytkowników oraz wspiera wdrożenie z Dockerem i testowaniem.

## Wymagania

- **Docker** i **Docker Compose**
- **Python 3.x** (jeśli planujesz uruchomić projekt bez Docker)
- **Django** i inne zależności (jeśli uruchamiasz bez Docker)

## Funkcjonalności

- Rejestracja i logowanie użytkownika
- Lista książek z możliwością filtrowania po dostępności
- Dodawanie, edycja i usuwanie książek (tylko dla zalogowanych)
- Powiadomienia systemowe i walidacja formularzy
- Przykładowe dane ładowane automatycznie
- Estetyczny interfejs Bootstrap 5
- Testy jednostkowe
- Obsługa języka polskiego w interfejsie
- Uruchomienie projektu poprzez Docker

## Technologie i biblioteki

- **Python 3.11**
- **Django 5.2.2**
- **PostgreSQL**
- **Docker & Docker Compose**
- **Bootstrap 5**
- **crispy-bootstrap5** – stylowanie formularzy
- **psycopg2-binary** – połączenie z bazą danych PostgreSQL

## Instrukcja uruchomienia

### 1. **Pobierz projekt**

Najpierw pobierz projekt z GitHub:

```bash
git clone https://github.com/twoje-konto/cyfrowa-biblioteka.git
cd cyfrowa-biblioteka
```

### 2. **Skonfiguruj Docker i uruchom kontenery**

Upewnij się, że masz zainstalowane **Docker** i **Docker Compose**. W projekcie używamy **Docker Compose**, aby uruchomić aplikację i bazę danych PostgreSQL w osobnych kontenerach.

W terminalu uruchom następujące polecenie:

```bash
docker-compose up --build
```

To polecenie:
- Zbuduje obrazy Docker dla aplikacji i bazy danych.
- Uruchomi kontenery dla aplikacji Django oraz bazy danych PostgreSQL.
- Udostępni aplikację pod adresem `http://localhost:8000`.

### 3. **Skonfiguruj bazę danych**

Po uruchomieniu kontenerów musisz uruchomić migracje bazy danych, aby stworzyć odpowiednie tabele w bazie PostgreSQL.

W terminalu uruchom:

```bash
docker-compose exec web python manage.py migrate
```

### 4. **Załaduj dane przykładowe**

Jeśli chcesz załadować przykładowe dane, takie jak książki, możesz to zrobić, uruchamiając poniższe polecenie:

```bash
docker-compose exec web python manage.py loaddata sample_data.json
```

### 5. **Utwórz konto administratora**

Aby utworzyć konto administratora (superuser) i mieć dostęp do panelu administracyjnego, uruchom poniższe polecenie:

```bash
docker-compose exec web python manage.py createsuperuser
```

Podaj nazwę użytkownika, e-mail oraz hasło. To konto będzie miało dostęp do panelu administratora, gdzie będziesz mógł zarządzać książkami, użytkownikami itp.

### 6. **Uruchom aplikację**

Aplikacja powinna teraz być dostępna na porcie `8000` na Twoim komputerze. Otwórz przeglądarkę i wpisz:

```
http://localhost:8000
```

### 7. **Zarządzanie bazą danych**

Jeśli chcesz zalogować się do bazy danych PostgreSQL i wykonywać zapytania bezpośrednio na bazie, uruchom poniższe polecenie:

```bash
docker-compose exec db psql -U bibliouser -d bibliodb
```

Po tym poleceniu będziesz mógł wydawać zapytania do bazy danych z poziomu konsoli PostgreSQL.

### 8. **Zatrzymanie kontenerów**

Po zakończeniu pracy z projektem, aby zatrzymać kontenery, użyj:

```bash
docker-compose down
```

Aby usunąć wszystkie dane (kontenery, sieci, wolumeny), użyj:

```bash
docker-compose down -v
```

## Struktura projektu

Kod źródlowy aplikacji znajduje się w folderach:

```bash
cyfrowa-biblioteka/
│
├── biblioteka/             # Ustawienia Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── books/                  # Aplikacja Django - model książek, widoki, formularze
│   ├── migrations/
│   ├── fixtures/           # sample_data.json
│   ├── templates/          # Szablony HTML
│   ├── forms.py
│   ├── models.py           # Modele
│   ├── tests.py            # Testy
│   ├── views.py
│   └── urls.py
│
├── Dockerfile              # Definicja obrazu aplikacji Django
├── docker-compose.yml      # Konfiguracja kontenerów (web + db)
├── wait_for_db.py          # Skrypt oczekujący na bazę PostgreSQL
├── requirements.txt        # Wymagane paczki
├── README.md               # Dokumentacja w formie pliku readme
└── manage.py
```

## Przykładowe dane

Przykład danych wejściowych (fixture):

```json
[
  {
    "model": "books.book",
    "pk": 1,
    "fields": {
      "title": "Pan Tadeusz",
      "author": "Adam Mickiewicz",
      "year": 1834,
      "is_available": true
    }
  }
]
```

## Testy

Aby uruchomić testy, po uruchomieniu kontenerów, użyj poniższego polecenia:

```bash
docker-compose exec web python manage.py test
```

Testy sprawdzą działanie aplikacji, w tym modele, widoki i formularze.

## Walidacja i bezpieczeństwo

- Walidacja formularzy po stronie serwera (Django forms + validators)
- Walidacja po stronie klienta (HTML5 + Bootstrap alerts)
- Obsługa sesji użytkownika
- Dostęp do panelu admina i edycji tylko dla zalogowanych

## Problemy

Jeśli napotkałeś jakiekolwiek problemy, sprawdź poniższe kroki:

1. Upewnij się, że masz uruchomiony Docker oraz Docker Compose.
2. Jeśli pojawią się problemy z bazą danych, spróbuj uruchomić migracje ponownie:
   ```bash
   docker-compose exec web python manage.py migrate
   ```
3. Jeśli masz jakiekolwiek inne pytania lub potrzebujesz pomocy, skontaktuj się z twórcą projektu.

---

To wszystko! Teraz możesz korzystać z aplikacji Cyfrowa Biblioteka na swoim komputerze. Jeśli masz jakiekolwiek pytania, nie wahaj się skontaktować!

## Autor

Karolina Karczewska
nr albumu: 53835
kontakt: kkarolina.0207@gmail.com