FROM python:3.11-slim
# ... (lib'и)
CMD ["streamlit", "run", "app.py", "--server.port=$PORT", ...]  # ← Ознака frontend
