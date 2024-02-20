import satreamlit

print(streamlit.__version__)

h = streamlit.header('My web Site')
s = streamlit.subheader('เส็บไซต์ส้วนตัวของฉัน')
p = streamlit.write('เว็บไซต์นี้แลกมาด้วยหยาดน้ำตา')
banner = streamlit.image('https://i.pinimg.com/originals/09/85/17/09851707a43cb4810ca148dfdf4a54ba.jpg')
b = streamlit.button('click')