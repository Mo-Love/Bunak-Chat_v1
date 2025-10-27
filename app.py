import streamlit as st
import requests
import os

st.set_page_config(page_title="Bunak Chat", layout="wide")
st.title("🗣️ Bunak Chat — Омніканальний консультант")

# Хедер
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("**Live-чат для сайтів + інструменти для резюме**")
with col2:
    st.markdown("[Донат ☕](https://buymeacoffee.com/molove)")

# Секція чату (проста, з сесією)
st.header("💬 Почни чат")
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Привіт! Як можу допомогти з кар'єрою чи чатом?"}]
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
if prompt := st.chat_input("Введи повідомлення..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    # Симуляція відповіді (заміни на AI пізніше)
    response = f"Дякую за запит: '{prompt}'. Ось базова відповідь. Хочеш PDF-резюме?"
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

# Секція PDF (з твого репо)
st.header("📄 Завантаж резюме")
token = st.text_input("Введи renderToken з resume.io")
if st.button("Генерувати PDF") and token:
    try:
        url = f"https://api.resume.io/render/{token}/pdf"  # Або твій ендпоінт
        resp = requests.get(url)
        st.download_button("Скачай PDF", resp.content, "resume.pdf", "application/pdf")
    except Exception as e:
        st.error(f"Помилка: {e}")

# Футер
st.markdown("---")
st.markdown("**Канали:** Веб | Telegram (скоро) | Email")
