import streamlit as st

st.title('This is title')
st.header('This is header')
st.subheader('This is subheader')
st.write('Displays plain text or any object with st.write()')
st.text('insert text')
st.caption('insert caption')

st.divider()

body = """
import numpy as np
def generate_random(size):
    rand = np.random.random(size=size)
    return rand
number = generate_random(10)
"""
st.code(body, language='python')

formula = """
a + ar + ar^2 + a r^3 + \cdots + a r^{n-1} = \sum_{k=0}^{n-1} a r^k
"""
st.latex(formula)

st.markdown(
    "<h3 style='text-align: center; color: red; background-color:lightgrey'>"
    "Dashboard Development with Phyton and Streamlit</h3>",
    unsafe_allow_html=True
)

st.page_link("http://www.google.com", label="Google Link", icon"🌏")
st.image("http://news.umpsa.edu.my/sites/default/files/gallery-article/UMPSA%20Solar_0.jpg")