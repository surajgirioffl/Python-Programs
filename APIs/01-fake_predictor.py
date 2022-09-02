"""
    Python script to get random/fake details of any name entered.
    
    APIs used:
    1) https://api.agify.io?name=Name
       Predict the age of a person based on their name.
    2) https://api.genderize.io?name=Name
       Predict the gender of a person based on their name.
    3) https://api.nationalize.io?name=Name
       Predict the nationality of a person based on their name.
"""

import requests
from functools import lru_cache


@lru_cache(maxsize=10)
def nameDetails(name: str) -> dict:
    """Function to get the details of a name.
    Args:
        name (str):
        Take arguments of any name.
    Returns:
        dict: Return a dictionary of the details of the name.
        dict = {"Name"=..., "Age"=..., "Gender"=..., "Country"=...}
    """
    try:
        ageData = requests.get(f"https://api.agify.io?name={name}")
        genderData = requests.get(f"https://api.genderize.io?name={name}")
        nationalityData = requests.get(f"https://api.nationalize.io?name={name}")
    except requests.exceptions.ConnectionError:
        print("\033[1;31mUnable to connect to internet..\033[0m")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred. ({e})")
        print(f"Response code for ageData: {ageData.status_code}")
        print(f"Response code for genderData: {genderData.status_code}")
        print(f"Response code for nationalityData: {nationalityData.status_code}")
    else:
        # print(ageData.json())
        # print(genderData.json())
        # print(nationalityData.json())
        ageData = ageData.json()
        genderData = genderData.json()
        nationalityData = nationalityData.json()
        requiredData = {
            "Name": name,
            "Age": ageData["age"],
            "Gender": genderData["gender"],
            "Country": nationalityData["country"][0]["country_id"],
        }
        return requiredData


def main():
    name = input("write any name: ")
    if name.isalpha():
        dataDict = nameDetails(name)
        # printing the info
        for key, value in dataDict.items():
            print(f"{key} = {value}")
    else:
        print(f"Invalid Name: {name}")


if __name__ == "__main__":
    main()
