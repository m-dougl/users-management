import streamlit as st 
import requests 
import pandas as pd 

api_url = '0.0.0.0'

if __name__ == "__main__":
    st.title("Users Management System (UMS)")
    
    with st.expander('Register a user', expanded=False):
        with st.form(key='user_form'):
            id = st.number_input(label='ID')
            username = st.text_input(label='Username: ')
            birth_date = st.date_input(label='Birth Date: ')
            email = st.text_input(label='Email: ')
            
            submit_btn = st.button('Submit')
            if submit_btn:
                requests.post(
                    url=api_url+f'/user/{id}',
                    data={
                        ""
                    }
                )