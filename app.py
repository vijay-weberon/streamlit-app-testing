import streamlit as st

st.title("Sample app")
password = st.text_input("Enter password:",key="password",type="password")
if password and password == st.secrets.PASSWORD:
    st.success("Congrats! You can see the secret content",icon="🎉")
else:
    st.warning("Sorry, the passwords didn't match")