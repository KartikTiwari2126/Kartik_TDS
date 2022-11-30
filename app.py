import streamlit as st
st.title("Odd Even Tracker")
num = st.number_input("Enter a number !",min_value = 1,step = 1)
if (num % 2 == 0):
         st.write("The number is even 👍")
else:
         st.write("The number is odd 👍")
st.write("A project by Kartikeya Tiwari")
