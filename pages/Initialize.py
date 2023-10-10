import streamlit as st
from service.InitializeSevice import InitializeSevice

initializeSevice = InitializeSevice()

if st.button('Initialize'):
    st.write(initializeSevice.initialize())

if st.button('Reset'):
    st.write(initializeSevice.reset())