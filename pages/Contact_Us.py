import streamlit as st

st.header("Contact Me")

class ComponentKeys:
    EMAIL_FORM = "__email__form__"
    EMAIL_INPUT = "__email__input__"
    MESSAGE_BOX = "__message__box__"
    SUBMIT_BTN = "__submit__btn__"

with st.form(key=ComponentKeys.EMAIL_FORM):
    user_email = st.text_input("Please, enter your email", placeholder="Your email", key=ComponentKeys.EMAIL_INPUT)
    message_box = st.text_area("Please, enter your message", placeholder="Your message", key=ComponentKeys.MESSAGE_BOX)
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        print("Submit button pressed")
