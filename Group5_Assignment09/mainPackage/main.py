# Name: Connor Laughlin, Elizabeth Piper
# email: laughlcd@mail.uc.edu, piperec@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 04/04/2024
# Course/Section: IS4010 Section 001
# Semester/Year: Spring 2024
# Brief Description of the assignment: This assignment involves building a Python application to interact with the Dog API, fetching random dog images and lists of dog breeds. The project is organized into a main package and a class package as per the assignment requirements.
# Brief Description of what this module does: This module, dog_api.py, defines the DogAPI class, which facilitates interaction with the Dog API endpoints. It provides methods to fetch a random dog image and a list of dog breeds from the API.
# Anything else that's relevant: put the link here API Documentation: https://dog.ceo/dog-api/

#main.py

from classPackage.DogAPI import DogAPI

def main():
    """
    Entry point of the application.
    """
    dog_api = DogAPI()

    # Get a random dog image
    print("Random Dog Image:")
    random_dog_image = dog_api.get_random_dog_image()
    if random_dog_image:
        print(random_dog_image)
    else:
        print("Failed to fetch random dog image.")

    # Get list of dog breeds
    print("\nKnown Dog Breeds:")
    dog_breeds = dog_api.get_dog_breeds()
    if dog_breeds:
        for breed in dog_breeds:
            print(breed)
        print(f"\nThe total number of represented dog breeds: {len(dog_breeds)}")
    else:
        print("Failed to fetch dog breeds.")
        
    #Get list of dog sub breeds
    print("\nSub Dog Breeds:")
    dog_subbreeds = dog_api.get_dog_subbreeds()
    if dog_subbreeds:
        for subbreed in dog_subbreeds:
            print(subbreed)
        print(f"\n The total amount of dog breeds represented is: {len(dog_subbreeds)}")
    else:
        print("Failed to fetch dog sub-breeds.")

if __name__ == "__main__":
    main()
