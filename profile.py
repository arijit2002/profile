import streamlit as st
from PIL import Image


st.title("PROFILE")
#st.balloons()

col1, col2 = st.columns(2)

#col1.header('Profile Pic')
img=Image.open('1619024802820.jfif')
col1.image(img,width=200)

col2.header("About")
col2.markdown("Hi, I am Arijit Das. Currently, I am studying BCA (Bachelor of Computer Applications) in IEM, Kolkata.")



st.sidebar.markdown("# Explore")
st.sidebar.markdown("Education & Qualification")
st.sidebar.markdown("Projects")
st.sidebar.markdown("Certificates")
st.sidebar.markdown("Contact")
#link = '[GitHub](http://github.com)'
#st.markdown(link, unsafe_allow_html=True)

options=['Education & Qualification','Projects','Certificates','Contact']
choice=st.sidebar.selectbox('View', options)
if(choice=='Education & Qualification'):
    st.markdown("# Education & Qualification:")
    st.subheader("ICSE --10th:")
    st.markdown("Psssing Year : 2018\n\nPercentage : 87.6%\n\nSchool : Julien Day School, Ganganagar")
    st.subheader("ISC --12th:")
    st.markdown("Psssing Year : 2020\n\nPercentage : 88.5% (Science)\n\nSchool : Julien Day School, Ganganagar")

if(choice=='Projects'):
    st.markdown('# Projects')

if(choice=='Certificates'):
    st.markdown('# Certificates')

if(choice=='Contact'):
    st.markdown('# Contact')
    github= '[GitHub](https://github.com/arijit2002)'
    st.markdown(github, unsafe_allow_html=True)
    twitter='[Twitter](https://twitter.com/ARIJITDAS2002)'
    st.markdown(twitter, unsafe_allow_html=True)

