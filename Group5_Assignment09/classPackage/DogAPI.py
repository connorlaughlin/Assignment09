# Name: Connor Laughlin, Elizabeth Piper
# email: laughlcd@mail.uc.edu, piperec@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 04/04/2024
# Course/Section: IS4010 Section 001
# Semester/Year: Spring 2024
# Brief Description of the assignment: This assignment involves building a Python application to interact with the Dog API, fetching random dog images and lists of dog breeds. The project is organized into a main package and a class package as per the assignment requirements.
# Brief Description of what this module does: This module, dog_api.py, defines the DogAPI class, which facilitates interaction with the Dog API endpoints. It provides methods to fetch a random dog image and a list of dog breeds from the API.
# Anything else that's relevant: put the link here API Documentation: https://dog.ceo/dog-api/

#DogAPI.py

import requests
import json

class DogAPI:
    def __init__(self):
        self.base_url = "https://dog.ceo/api/"

    def get_random_dog_image(self):
        endpoint = "breeds/image/random"
        url = self.base_url + endpoint
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return data.get('message')
            else:
                print("Error fetching data:", response.status_code)
                return None
        except requests.exceptions.RequestException as e:
            print("Error fetching data:", e)
            return None

    def get_dog_breeds(self):
        endpoint = "breeds/list/all"
        url = self.base_url + endpoint
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return list(data.get('message').keys())
            else:
                print("Error fetching data:", response.status_code)
                return None
        except requests.exceptions.RequestException as e:
            print("Error fetching data:", e)
            return None
