import os
import datetime
import requests
import streamlit as st
from typing import Union
from dotenv import load_dotenv

load_dotenv()


class Query:
    def __init__(self):
        """
        Initialize a Query object with the API URL and a requests Session.

        The API URL is obtained from the environment variable "API_URL".
        A requests Session is created to persist certain parameters across requests.

        Parameters:
        None

        Returns:
        None
        """
        self.api_url = os.getenv("API_URL")
        self.session = requests.Session()

    def create_user(
        self, username: str, birth_date: datetime.date, email: str
    ) -> Union[st.success, st.error]:
        """
        Creates a new user in the system using the provided username, birth date, and email.

        Parameters:
        username (str): The username of the new user.
        birth_date (datetime.date): The birth date of the new user.
        email (str): The email of the new user.

        Returns:
        st.success: If the user is successfully created, a success message is returned.
        st.error: If an error occurs during the user creation process, an error message is returned.
        """
        try:
            response = self.session.post(
                url=f"{self.api_url}/users/",
                json={
                    "username": username,
                    "birth_date": birth_date.isoformat(),
                    "email": email,
                },
            )
            return st.success("Successfully created user!")

        except requests.exceptions.RequestException as e:
            return st.error(f"Could not create user: {e}")

    def update_user(
        self, user_id: int, username: str, birth_date: datetime.date, email: str
    ) -> Union[st.success, st.error]:
        """
        Updates an existing user in the system using the provided user ID, username, birth date, and email.

        Parameters:
        user_id (int): The ID of the user to be updated.
        username (str): The new username for the user.
        birth_date (datetime.date): The new birth date for the user.
        email (str): The new email for the user.

        Returns:
        st.success: If the user is successfully updated, a success message is returned.
        st.error: If an error occurs during the user update process, an error message is returned.
        """
        try:
            iso_date = birth_date.isoformat()

            requests.put(
                url=f"{self.api_url}/users/{user_id}",
                json={
                    "id": user_id,
                    "username": username,
                    "birth_date": iso_date,
                    "email": email,
                },
            )
            return st.success("Successfully updated user!")

        except requests.exceptions.RequestException as e:
            st.error(f"Could not update user: {e}")

    def delete_user(self, user_id: int) -> Union[st.success, st.error]:
        """
        Deletes a user from the system using the provided user ID.

        Parameters:
        user_id (int): The ID of the user to be deleted.

        Returns:
        st.success: If the user is successfully deleted, a success message is returned.
        st.error: If an error occurs during the user deletion process, an error message is returned.
        """
        try:
            requests.delete(url=f"{self.api_url}/users/{user_id}")
            return st.success("User deleted!")

        except requests.exceptions.RequestException as e:
            return st.error(f"Error to delete user: {e}")

    def read_users(self, offset=0, limit=100):
        """
        Retrieves a list of users from the system.

        This function sends a GET request to the API endpoint "/users/" with optional query parameters
        for pagination (offset and limit). It returns the JSON response containing the list of users.

        Parameters:
        offset (int): The starting index for pagination. Default is 0.
        limit (int): The maximum number of users to retrieve per request. Default is 100.

        Returns:
        dict: A dictionary containing the JSON response from the API.
        st.error: If an error occurs during the API request, an error message is returned using Streamlit's st.error function.
        """
        try:
            response = self.session.get(
                url=f"{self.api_url}/users/?offset={offset}&limit={limit}"
            )
            return response.json()

        except requests.exceptions.RequestException as e:
            return st.error(f"Error reading users: {e}")

    def read_user(self, user_id: int) -> Union[dict, bool]:
        """
        Retrieves a single user from the system using the provided user ID.

        This function sends a GET request to the API endpoint "/users/{user_id}".
        It returns the JSON response containing the user's details.

        Parameters:
        user_id (int): The ID of the user to retrieve.

        Returns:
        dict: A dictionary containing the JSON response from the API.
        bool: False if an error occurs during the API request.

        Raises:
        requests.exceptions.RequestException: If an error occurs during the API request.
        """
        try:
            response = self.session.get(url=f"{self.api_url}/users/{user_id}")
            return response.json()

        except requests.exceptions.RequestException as e:
            st.error(f"Error reading user: {e}")
            return False
