# You are creating a simple profile page that fetches user data from an API (https://jsonplaceholder.typicode.com/users/1).
# Explain or show code for:
# Fetching and displaying the user’s name and email.
# Handling the loading and error states.

import requests

def fetch_user():
    url = "https://jsonplaceholder.typicode.com/users/1"
    try:
        print("Loading...")
        response = requests.get(url)
        response.raise_for_status()  # raises error if any
        user = response.json()
        print(f"Name: {user['name']}")
        print(f"Email: {user['email']}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

fetch_user()

# requests.get() → sends a GET request to the API.

# .json() → converts the response to a Python dictionary.

# try...except → handles network or request errors.

# print("Loading...") shows that data is being fetched.