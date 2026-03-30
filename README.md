## Uruchomienie lokalne

1. Instalacja zależności:
pip install -r requirements.txt

2. Uruchomienie serwera:
uvicorn app:app --reload

3. Test działania:
curl http://localhost:8000/health

## Uruchomienie za pomocą Docker

1. Budowanie obrazu:
docker build -t lab4pd .

2. Uruchomienie kontenera:
docker run -p 8000:8000 lab4pd

3. Test:
curl http://localhost:8000/health

## Uruchomienie za pomocą Docker Compose

1. Start aplikacji:
docker compose up --build

2. Test:
curl http://localhost:8000/health

Aplikacja działa na porcie 8000.  
W konfiguracji Docker Compose wykorzystano dodatkowy serwis Redis.  
Nie są wymagane dodatkowe zmienne środowiskowe do uruchomienia aplikacji.

## Endpointy

- GET / – sprawdzenie działania API  
- POST /predict – wykonanie predykcji modelu ML  
- GET /info – informacje o modelu  
- GET /health – status aplikacji

