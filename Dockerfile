# 1. Używamy oficjalnego obrazu Pythona
FROM python:3.11-slim

# 2. Ustawiamy katalog roboczy w kontenerze
WORKDIR /app

# 3. Kopiujemy pliki
COPY requirements.txt .

# 4. Instalujemy zależności
RUN pip install --no-cache-dir -r requirements.txt

# 5. Kopiujemy resztę projektu
COPY . .

# 6. Otwieramy port i uruchamiamy serwer
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
