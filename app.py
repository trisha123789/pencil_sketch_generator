from PIL import Image
import cv2
import numpy as np
import streamlit as st
import io

st.title("Image to sketch app") 
st.write("upload an image to convert into pencil-sketch image")
uploaded_file = st.file_uploader("upload an image",type=["jpg","jpeg","png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image_np = np.array(image)
    st.subheader("original image")
    st.image(image,use_container_width = True)
    gray = cv2.cvtColor(image_np,cv2.COLOR_BGR2GRAY)
    inverted = 255 - gray
    blurred = cv2.GaussianBlur(inverted,(21,21),0)
    inverted_blur = 255 - blurred
    sketch = cv2.divide(gray,inverted_blur,scale =256.0)
    st.subheader("PENCIL SKETCH")
    buf = io.BytesIO()
    st.image(sketch,clamp =True,use_container_width=True)
    sketch_pil = Image.fromarray(sketch)
    
    sketch_pil.save(buf, format="PNG")

    st.download_button(
        label="Download Sketch",
        data=buf.getvalue(),
        file_name="sketch.png",
        mime="image/png"
    )