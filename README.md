# Cyfrowa Biblioteka

Projekt **Cyfrowa Biblioteka** to aplikacja stworzona w Django, umożliwiająca zarządzanie książkami, ich wypożyczeniami oraz rejestrację i logowanie użytkowników. Aplikacja korzysta z bazy danych PostgreSQL oraz Docker do łatwego uruchomienia projektu w kontenerach.

## Wymagania

- **Docker** i **Docker Compose**
- **Python 3.x** (jeśli planujesz uruchomić projekt bez Docker)
- **Django** i inne zależności (jeśli uruchamiasz bez Docker)

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
docker-compose exec web python manage.py loaddata fixtures.json
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

## Testy

Aby uruchomić testy, po uruchomieniu kontenerów, użyj poniższego polecenia:

```bash
docker-compose exec web python manage.py test
```

Testy sprawdzą działanie aplikacji, w tym modele, widoki i formularze.


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