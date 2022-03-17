from PIL import Image
import streamlit as st
import os

def st_icons(employment_value, contraceptive_value, education_value, marriage_value):
    images_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')

    employment_image = Image.open(os.path.join(images_path, 'job-search.png'))
    contraceptive_image = Image.open(os.path.join(images_path, 'contraceptive.png'))
    education_image = Image.open(os.path.join(images_path, 'mortarboard.png'))
    marriage_image = Image.open(os.path.join(images_path, 'wedding-rings.png'))

    image_cols = st.columns(4)

    image_cols[0].image(employment_image)
    image_cols[1].image(education_image)
    image_cols[2].image(contraceptive_image)
    image_cols[3].image(marriage_image)

    value_cols = st.columns(4)

    st.markdown("""
    <style>
    .numbers-font {
        font-family:"Crimson Text";
        font-size:80px !important;
        font_weight:bold
    }
    .unit-font {
        font-family:"Crimson Text";
        font-size:40px;
        font_weight:bold
    }
    </style>
    """, unsafe_allow_html=True)

    value_cols[0].markdown(
        f'<p class="numbers-font">{str(employment_value)} <span class="unit-font"> % </span></p>', unsafe_allow_html=True)
    value_cols[1].markdown(
        f'<p class="numbers-font">{str(education_value)} <span class="unit-font"> % </span></p>', unsafe_allow_html=True)
    value_cols[2].markdown(
        f'<p class="numbers-font">{str(contraceptive_value)} <span class="unit-font"> % </span></p>', unsafe_allow_html=True)
    value_cols[3].markdown(
        f'<p class="numbers-font">{str(marriage_value)} <span class="unit-font"> y.o </span> </p>', unsafe_allow_html=True)





