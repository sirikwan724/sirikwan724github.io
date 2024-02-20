import torch
import streamlit as st
from PIL import Image
from diffusers import DiffusionPeline as DP
h = st.header('Diffusion.AI')
s = st.subheader('เว็บไซต์สำหรับแปลงข้อความเป็นภาพ')
p = st.write('เว็บไซตนี้แลกมาด้วยหยาดเหงื่อและความอดทน')
text = st.text_input('prompt: ')
if text:
    dp = Dp.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float16)
    Image_data = dp(text).images[0]
    Image = Image.fromarray(Image_data)
    Image.show()
    #st.image('https://picsum.photos/400/200')
    b = st.button('จะไปต่อหรือ...')