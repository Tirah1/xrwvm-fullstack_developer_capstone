# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv


load_dotenv()

backend_url = os.getenv(
    "backend_url", default="http://localhost:3030"
)
sentiment_analyzer_url = os.getenv(
    "sentiment_analyzer_url",
    default="http://localhost:5050/",
)


def get_request(endpoint, **kwargs):
    """Make a GET request to the backend server."""
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params = params + key + "=" + value + "&"

    request_url = backend_url + endpoint + "?" + params

    print(f"GET from {request_url}")
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        # If any error occurs, handle it explicitly
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")


def analyze_review_sentiments(text):
    """Analyze the sentiment of a given text."""
    request_url = sentiment_analyzer_url + "analyze/" + text
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        # Handle errors explicitly
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")


def post_review(data_dict):
    """Post a review to the backend server."""
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except Exception as err:
        # Handle errors explicitly
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
