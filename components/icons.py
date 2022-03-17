from PIL import Image
import streamlit as st
import os

def st_icons():
    images_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')

    employment_image = Image.open(os.path.join(images_path, 'employment.png'))
    contraceptive_image = Image.open(os.path.join(images_path, 'contraceptive.png'))
    education_image = Image.open(os.path.join(images_path, 'mortarboard.png'))
    marriage_image = Image.open(os.path.join(images_path, 'wedding-rings.png'))

    st.image([employment_image, contraceptive_image,
             marriage_image, education_image])


