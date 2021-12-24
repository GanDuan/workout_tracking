import requests
from datetime import datetime
import os

GENDER = os.environ.get("YOUR_GENDER")
AGE = os.environ.get("YOUR_AGE")
WEIGHT= os.environ.get("YOUR_WEIGHT")
HEIGHT= os.environ.get("YOUR_HEIGHT")
NUTRI_APP_ID = os.environ.get("APP_ID")
NUTRI_API_KEY = os.environ.get("API_KEY")
EXERCISE_ENDPOINT= "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")
BEARER_TOKEN = os.environ.get("TOKEN")

#TODO post exercise to nutrition
exercise_params = {
    "query": input("What did you do today? "),
    "gender": GENDER,
    "height_cm": HEIGHT,
    "weight_kg": WEIGHT,
    "age": AGE
}

header = {
    "x-app-id": NUTRI_APP_ID,
    "x-app-key": NUTRI_API_KEY,
}

response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_params, headers=header)
result = response.json()
print(result)
#TODO save results to google sheets
today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%X")
exercise = result["exercises"][0]["name"]
duration = result["exercises"][0]["duration_min"]
calories = result["exercises"][0]["nf_calories"]

add_paramas = {
    "workout": {
        "date":date,
        "time":time,
        "exercise":exercise.title(),
        "duration":duration,
        "calories":calories
    }
}

token = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

add_data = requests.post(url=SHEET_ENDPOINT, json=add_paramas, headers= token)
sheet_response = add_data.json()
