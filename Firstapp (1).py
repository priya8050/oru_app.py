#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np

from PIL import Image


# In[3]:


import streamlit as st



# Define function for each page
def page1():
    st.title(' The DORA ' )
base="dark"
primaryColor="purple"
font="serif"
primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"

def page2():
    st.title('pyaar ')
    # Add content for Page 2
    with st.sidebar:
        st.button('Hello 👋 Paithyam ')
        st.checkbox('You have no choice of leaving me , so click , I agree')

        
def page3():
    st.title( "prema Kaadhal")
    # Two equal columns:
col1, col2 = st.columns(2)
st.subheader('I  LOVE YOU , Reflo Ponnu  heheheh')
a = st.sidebar.radio('Na Unaku evlo pudikum  :', ["too muchhhh", "Romba Rombaa"])


# You can also use "with" notation:
with col1:
        st.radio('whats special Today ?:', ["Cake vetra naal" , "Treat kudukra naal"])
        
def page4():
    st.title('Happy Porandhanaal menaminiki')
    st.header('Happy Birthday')
    # Load and display the image
image = Image.open('C:/Users/admin/Downloads/IMG_20220521_182026_139.jpg')
st.image(image, caption='Image Caption', use_column_width=True)
st.write("Please contact me to for more love!")



# Create a dictionary to map page names to their respective functions
pages = {
    'Page 1': page1,
    'Page 2': page2,
    'page 3': page3,
    'page 4': page4
    
}


# Display a selection box to choose the page
selection = st.sidebar.selectbox('Select a page', list(pages.keys()))
# Call the selected page function
pages[selection]()


# Add a "Next" button to move to the next page
if selection != list(pages.keys())[-1]:
    if st.button('Next'):
        next_page_index = list(pages.keys()).index(selection) + 1
        next_page = list(pages.keys())[next_page_index]
        pages[next_page]()
        # Add a "Next" button to move to the next page
if selection != list(pages.keys())[-1]:
    if st.button('Next'):
        next_page_index = list(pages.keys()).index(selection) + 1
        next_page = list(pages.keys())[next_page_index]
        pages[next_page]()



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




