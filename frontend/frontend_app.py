import streamlit as st
from queries import Query

if __name__ == "__main__":
    st.title("Users Management System (UMS)")
    querier_instance = Query()

    with st.expander("Register a user", expanded=False):
        with st.form(key="create_user_form"):
            username = st.text_input(label="Username: ")
            birth_date = st.date_input(label="Birth Date: ")
            email = st.text_input(label="Email: ")

            submit_btn = st.form_submit_button(label="Submit")
            if submit_btn:
                querier_instance.create_user(
                    username=username,
                    birth_date=birth_date,
                    email=email,
                )

    with st.expander("Search User", expanded=False):
        user_id = st.number_input(label="ID", min_value=0, max_value=100, step=1)
        search_btn = st.button(label="Search")

        if search_btn:
            response = querier_instance.read_user(user_id=user_id)
            st.dataframe(response)

    with st.expander("Update User", expanded=False):
        with st.form(key="update_user_form"):
            user_id = st.number_input(label="ID", min_value=0, max_value=100, step=1)
            username = st.text_input(label="Username: ")
            birth_date = st.date_input(label="Birth Date: ")
            email = st.text_input(label="Email: ")

            submit_btn = st.form_submit_button(label="Update User")
            if submit_btn:
                querier_instance.update_user(
                    user_id=user_id,
                    username=username,
                    birth_date=birth_date,
                    email=email,
                )

    with st.expander("Delete User", expanded=False):
        user_id = st.number_input(label=" ID", min_value=0, max_value=100, step=1)
        search_btn = st.button(label="Delete")

        if search_btn:
            response = querier_instance.delete_user(user_id=user_id)
