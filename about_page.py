import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image


def show_devs():
    st.write("# Hello!")
    st.image("data//s.png", width = 200)  
    st.write("## I'm **Saif**")  
    st.header("I'm a fellow student @ **Daffodil International University**")
    st.write("### This is my first Machine Learning Project, **PROJECT : Salary-Prediction**. \
    Salary-Prediction is based on the data collected from various StackOverflow users of the year 2020.")
    
    st.latex("Certifications :")
    st.image("data//Python for beginners - Learn all the basics of python.jpg", width = 800)
    st.image("data//Python for beginners - Learn all the basics of python - 2.jpg", width = 800)
    st.image("data//Programming_Hero_Certificate_fundamental.jpg", width = 800)
    st.image("data//cert-17238243-1157.png", width = 800)