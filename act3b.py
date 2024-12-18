import streamlit as st
import pandas as pd

st.title("Fetch and Display Data from a URL")

url = 'https://storage.dosm.gov.my/population_state.csv'
url_data = pd.read_csv(url)

st.subheader("Display Data from URL")
st.dataframe(url_data, use_container_width=True)
st.caption("Displaying Data fetched from an online source")
