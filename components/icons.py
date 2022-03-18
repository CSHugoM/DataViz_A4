from PIL import Image
import streamlit as st
import os

def st_icons(employment_value : float, contraceptive_value : float, education_value : float, marriage_value : float):

    # Path of images
    images_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')

    employment_image = Image.open(os.path.join(images_path, 'job-search.png'))
    contraceptive_image = Image.open(os.path.join(images_path, 'contraceptive.png'))
    education_image = Image.open(os.path.join(images_path, 'mortarboard.png'))
    marriage_image = Image.open(os.path.join(images_path, 'wedding-rings.png'))

    # Create a container for icons

    icons_container = st.container()

    with icons_container:

        image_cols = st.columns(8)

        image_cols[2].image(employment_image)
        image_cols[3].image(education_image)
        image_cols[4].image(contraceptive_image)
        image_cols[5].image(marriage_image)

        value_cols = st.columns(8)

        st.markdown("""
        <style>
        .numbers-font {
            font-family:"Crimson Text";
            font-size:50px !important;
            font_weight:bold
        }
        .unit-font {
            font-family:"Crimson Text";
            font-size:30px;
            font_weight:bold
        }
        </style>
        """, unsafe_allow_html=True)

        value_cols[2].markdown(
            f'<p class="numbers-font"> {str(employment_value)}<span class="unit-font">%</span></p>', unsafe_allow_html=True)
        value_cols[3].markdown(
            f'<p class="numbers-font"> {str(education_value)}<span class="unit-font">%</span></p>', unsafe_allow_html=True)
        value_cols[4].markdown(
            f'<p class="numbers-font"> {str(contraceptive_value)}<span class="unit-font">%</span></p>', unsafe_allow_html=True)
        value_cols[5].markdown(
            f'<p class="numbers-font"> {str(marriage_value)}<span class="unit-font">y.o.</span></p>', unsafe_allow_html=True)





