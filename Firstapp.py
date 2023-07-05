#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np

from PIL import Image


# In[18]:


import streamlit as st

# Define function for each page
def Pyaar():
    st.title(' The DORA ' )
    st.button('Hello 👋 Paithyam ')
image = Image.open('C:/Users/admin/Downloads/IMG_20220521_182026_139.jpg')
st.image(image, caption='How lucky are you ?', use_column_width=True)

def prema():
    st.title('Beginning ')
    # Add content for Page 2
with st.expander("illi click maadu le"):
    st.write("It all started back then in 1947, 2016 Jnc puc.")
    st.write("Tholiye, en kaadhaliye, Appo pudicha saniye, nee ennai innu ennum vidalyyyye.")
    st.checkbox('You have no choice of leaving me , so click , I agree'),
# Load and display the image
image = Image.open('C:/Users/admin/Downloads/Screenshot_20211226_085943.jpg')
st.image(image, caption='Congratulations for having the worlds best ponnu as your friend')

        
def Kaadhal():
    st.title( "Thangamey , unna thaan thedi vandhe naaneee")
st.subheader('I  LOVE YOU , Reflo Ponnu  heheheh')
image = Image.open('C:/Users/admin/Downloads/IMG_20220703_212621_423.jpg')
st.image(image, caption='Thangamey <3')
ia = st.radio('whats special  :', ["Cake vetra naal" , "Treat kudukra naal"])
        
                      
def avlothaa():
    st.title('Happy Porandhanaal menaminiki')
    st.header('Happy 23 kov <3')
st.write("Please contact me to for more love!")

# Add an audio file
audio_file = open(r'C:\Users\admin\Downloads\Dorothy.mp3','rb')
audio_bytes = audio_file.read()

# Display the audio player
st.audio(audio_bytes, format='audio/mp3')

# Create a dictionary to map page names to their respective functions
pages = {
    'Pyaar': Pyaar,
    'Prema': prema,
    'kaadhal': Kaadhal,
    'avlothaa': avlothaa
    
}



# Display a selection box to choose the page
selection = st.sidebar.selectbox('Select a page', list(pages.keys()))
# Call the selected page function
pages[selection]()




# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




