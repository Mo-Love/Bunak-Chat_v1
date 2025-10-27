import streamlit as st
import requests

st.set_page_config(page_title="Bunak Chat", layout="wide")
st.title("🗣️ Bunak Chat — Омніканальний консультант")

# Хедер
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("**Live-чат + інструменти для клієнтів**")
with col2:
    st.markdown("[Донат ☕](https://buymeacoffee.com/molove)")

# Чат
st.header("💬 Спілкування")
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Привіт! Як допомогти?"}]
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
if prompt := st.chat_input("Повідомлення..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)
    response = f"Відповідь на '{prompt}': Готовий до омніканалу!"
    with st.chat_message("assistant"): st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

# PDF (з репо)
st.header("📄 Резюме PDF")
token = st.text_input("renderToken з resume.io")
if st.button("Генерувати") and token:
    try:
        resp = requests.get(f"https://api.resume.io/render/{token}/pdf")
        st.download_button("Скачати", resp.content, "resume.pdf", "application/pdf")
    except Exception as e:
        st.error(f"Помилка: {e}")

st.markdown("---")
st.markdown("**Канали:** Веб | Telegram (скоро)")
