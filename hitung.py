import streamlit as st

x = st.number_input( " Insert a number ", value = None)
sx = st.text_input(" Satuan ", "C")
st.write( " the current number is  = " , x, " " ,sx)

