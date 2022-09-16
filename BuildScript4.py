# Script to execute GET from API resource and save results in a csv file format.

import requests
import json
import pandas as pd

# URL for Hyrule Compendium API, treasure category.
url = "https://botw-compendium.herokuapp.com/api/v2/category/treasure"

# Get request for data in format of a json.
response = requests.request("GET", url).json()

# Convert and save data to csv file format.
df = pd.DataFrame(response['data'])
df.to_csv('TheLegendofZelda_BOTW_treasures.csv')