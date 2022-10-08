#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 00:07:32 2022

@author: gaditek
"""


import streamlit as st
from PIL import Image

st.title("Main page")

image = Image.open('data/logo.png')
st.image(image, caption='stlite logo')
