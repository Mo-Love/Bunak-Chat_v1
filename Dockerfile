FROM python:3.11-slim

# Встановлюємо системні залежності для Pillow (lib'и)
RUN apt-get update && apt-get install -y \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*  # Очищуємо кеш, щоб уникнути read-only issues

WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# Експонуємо порт (Render використає $PORT)
EXPOSE $PORT

# Запуск Streamlit з headless mode для серверу
CMD ["streamlit", "run", "app.py", \
     "--server.port=$PORT", \
     "--server.address=0.0.0.0", \
     "--server.headless=true"]
