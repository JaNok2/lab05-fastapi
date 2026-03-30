FROM python:3.9-slim

# katalog roboczy
WORKDIR /app

# kopiowanie plików
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# uruchomienie serwera
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
