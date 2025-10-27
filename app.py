import streamlit as st
import requests

st.set_page_config(page_title="Bunak Chat", layout="wide")
st.title("🗣️ Bunak Chat — Омніканальний консультант")

col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("**Live-чат для клієнтів + PDF-інструменти**")
with col2:
    st.markdown("[Донат ☕](https://buymeacoffee.com/molove)")

st.header("💬 Почни чат")
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Привіт! Розкажи, як допомогти з консультацією?"}]
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
if prompt := st.chat_input("Твоє повідомлення..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)
    response = f"Дякую за '{prompt}'! Готовий до омніканалу — веб, Telegram тощо."
    with st.chat_message("assistant"): st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

st.header("📄 Завантаж резюме-PDF")
token = st.text_input("Введи renderToken з resume.io")
if st.button("Генерувати") and token:
    try:
        resp = requests.get(f"https://api.resume.io/render/{token}/pdf")
        if resp.status_code == 200:
            st.download_button("Скачай", resp.content, "resume.pdf", "application/pdf")
        else:
            st.error("Невірний токен.")
    except Exception as e:
        st.error(f"Помилка: {e}")

st.markdown("---")
st.markdown("**Омніканал:** Веб-віджет | Telegram (скоро) | Email")
