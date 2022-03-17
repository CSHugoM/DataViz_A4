from PIL import Image
import streamlit as st
import os

def st_icons():
    images_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')

    employment_image = Image.open(os.path.join(images_path, 'employment.png'))
    contraceptive_image = Image.open(os.path.join(images_path, 'contraceptive.png'))
    education_image = Image.open(os.path.join(images_path, 'mortarboard.png'))
    marriage_image = Image.open(os.path.join(images_path, 'wedding-rings.png'))

    cols = st.columns(4)

    cols[0].image(employment_image)
    cols[1].image(contraceptive_image)
    cols[2].image(education_image)
    cols[3].image(marriage_image)


