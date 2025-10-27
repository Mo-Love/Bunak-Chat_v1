import streamlit as st
import requests

st.set_page_config(page_title="Bunak Chat", layout="wide")
st.title("🗣️ Bunak Chat — Твій онлайн-консультант")

# Хедер з донатом
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("**Омніканальний чат для клієнтів + інструменти**")
with col2:
    st.markdown("[Донат ☕](https://buymeacoffee.com/molove)")

# Чат-секція
st.header("💬 Почніть спілкування")
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Привіт! Розкажіть, як можу допомогти?"}]
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
if prompt := st.chat_input("Ваше повідомлення..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    # Проста відповідь (додай AI пізніше)
    response = f"Дякую за '{prompt}'! Ось ідея: спробуйте PDF-резюме для кар'єри."
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

# PDF-секція (з твого оригінального репо)
st.header("📄 Завантажити резюме-PDF")
token = st.text_input("Введіть renderToken з resume.io")
if st.button("Генерувати") and token:
    try:
        url = f"https://api.resume.io/render/{token}/pdf"
        resp = requests.get(url)
        if resp.status_code == 200:
            st.download_button("Скачати PDF", resp.content, "resume.pdf", "application/pdf")
        else:
            st.error("Помилка API. Перевірте токен.")
    except Exception as e:
        st.error(f"Помилка: {e}")

# Футер з омніканалом
st.markdown("---")
st.markdown("**Канали:** Веб-чат | Telegram (скоро) | Email")
