FROM python:3.11-slim

# Встановлюємо системні lib'и для Pillow (до pip, обходить read-only)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libjpeg62-turbo-dev \
    libpng-dev \
    libtiff5-dev \
    libwebp-dev \
    zlib1g-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir --upgrade pip

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE $PORT

# Запуск Streamlit на $PORT (Render-стандарт)
CMD ["streamlit", "run", "app.py", \
     "--server.port=$PORT", \
     "--server.address=0.0.0.0", \
     "--server.headless=true", \
     "--server.enableCORS=false"]
