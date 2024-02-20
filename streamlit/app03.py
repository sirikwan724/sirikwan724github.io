import streamlit as st

h = st.header('My web Site')
s = st.subheader('เส็บไซต์ส้วนตัวของฉัน')
p = st.write('เว็บไซต์นี้แลกมาด้วยหยาดน้ำตา')
banner = st.image('https://i.pinimg.com/originals/09/85/17/09851707a43cb4810ca148dfdf4a54ba.jpg')
b = st.button('click')
text = st.text_input('prompt: ')
if text:
    st.image('https://i.pinimg.com/originals/1d/ba/8a/1dba8ab973ccb3b35ae56d00a632c372.jpg')
    b = st.button('พอเถอะ....')