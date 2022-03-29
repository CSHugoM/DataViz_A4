from PIL import Image
import streamlit as st
import os
import math

def st_icons(list_numbers : list, container):

    assert len(list_numbers) == 4, "We only need 4 numbers !"

    # Path of images
    images_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')

    employment_image = Image.open(os.path.join(images_path, 'job-search.png'))
    contraceptive_image = Image.open(os.path.join(images_path, 'contraceptive.png'))
    education_image = Image.open(os.path.join(images_path, 'mortarboard.png'))
    marriage_image = Image.open(os.path.join(images_path, 'wedding-rings.png'))

    # Create a container for icons
    
    employment_nb = str(list_numbers[0]) + "%"
    contraceptive_nb = str(list_numbers[1]) + "%"
    education_nb = str(list_numbers[2]) + "%"
    marriage_nb = str(list_numbers[3]) + "y.o."
    
    if(math.isnan(list_numbers[0])):
        employment_nb = "Not Available"
    if(math.isnan(list_numbers[2])):
        education_nb = "Not Available"
    if(math.isnan(list_numbers[1])):
        contraceptive_nb = "Not Available"
    if(math.isnan(list_numbers[3])):
        marriage_nb = "Not Available"
        


    with container.container():

        image_cols = st.columns(8)

        image_cols[2].image(employment_image)
        image_cols[3].image(education_image)
        image_cols[4].image(contraceptive_image)
        image_cols[5].image(marriage_image)

        value_cols = st.columns(8)

        st.markdown("""
        <style>
        .numbers-font {
            font-family:"sans serif";
            font-size:45px !important;
            font_weight:bold
        }
        .unit-font {
            font-family:"sans serif";
            font-size:30px;
            font_weight:bold
        }
        </style>
        """, unsafe_allow_html=True)

        value_cols[2].markdown(
            f'<p class="numbers-font"> {employment_nb}<span class="unit-font"></span></p>', unsafe_allow_html=True)
        value_cols[3].markdown(
            f'<p class="numbers-font"> {education_nb}<span class="unit-font"></span></p>', unsafe_allow_html=True)
        value_cols[4].markdown(
            f'<p class="numbers-font"> {contraceptive_nb}<span class="unit-font"></span></p>', unsafe_allow_html=True)
        value_cols[5].markdown(
            f'<p class="numbers-font"> {marriage_nb}<span class="unit-font"></span></p>', unsafe_allow_html=True)
        
        legend_cols = st.columns(8)
        
        legend_cols[2].markdown("_Female share of employment in senior and middle magement (%)_")
        legend_cols[3].markdown("_Educational attainment, at least Bachelor's or equiv., female (%)_")
        legend_cols[4].markdown("_Contraceptive prevalence, any method (% of married women ages 15-49)_")
        legend_cols[5].markdown("_Age at first marriage, female_")





