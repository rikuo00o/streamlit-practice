import streamlit as st

st.title("Hello, Streamlit!")
st.write("This is a simple web application using Streamlit.")

input_num_1 = st.number_input("Enter a number_1", value=0)
input_num_2 = st.number_input("Enter a number_2", value=0)

st.write(f"{input_num_1} × {input_num_2} = {input_num_1 * input_num_2}")