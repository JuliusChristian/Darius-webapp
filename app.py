import streamlit as st
import pandas as pd
import numpy as np

# Initialize web app with simple table and comment
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

# Create text and table in streamlit web app
st.write("This is my first streamlit web application. Here's a sample dataframe:")

st.write(df)

# Line charts
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)

# Widgets
x = st.slider('x')
st.write(x, 'Squared is', x * x)

# Text input
st.text_input("Your name", key='name')

st.session_state.name

#For Sidebar
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home Phone', 'Mobile Phone')
)
