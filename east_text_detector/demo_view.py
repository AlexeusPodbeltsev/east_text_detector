import numpy as np
import streamlit as st

from demo import detect_text_on_image

st.title('Demo page')

data = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])
img = None

if data is not None:
    file_bytes = np.asarray(bytearray(data.read()), dtype=np.uint8)
    rec, img = detect_text_on_image(file_bytes)
else:
    st.error('please upload an image with text')
    print(data)

if img is not None:
    st.text('Result')
    st.image(img)
