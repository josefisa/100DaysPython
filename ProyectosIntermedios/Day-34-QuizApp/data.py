import requests
import json

parameters = {
    "amount":  10,
    "type":"boolean",
}

def get_questions():
    response = requests.get(url="https://opentdb.com/api.php", params=parameters )
    response.raise_for_status()
    response.json()
    data = response.json()["results"]
    return data

question_data = get_questions()