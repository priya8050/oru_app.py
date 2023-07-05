#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st

def Kaadhal():
    st.title("Thangamey, unna thaan thedi vandhe naaneee")
    st.subheader('I LOVE YOU, Reflo Ponnu heheheh')
    image = Image.open('C:/Users/admin/Downloads/IMG_20220703_212621_423.jpg')
    st.image(image, caption='Thangamey <3', use_column_width=True)
    ia = st.sidebar.radio('whats special:', ["Cake vetra naal", "Treat kudukra naal"])


# In[ ]:




