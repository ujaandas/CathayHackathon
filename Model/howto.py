import requests
import json

# This is the URL of the server running the Flask app
# Replace this with your own URL
url = "http://localhost:5000/call"

# This is the name of the function you want to call
function_name = "recommend"

# These are the parameters you want to pass to the function
params = {
    "user_id": "510892B00001637F",
    "fruit_name": "Pineapple",
    "top_n": 5,
}

# Call the API
response = requests.post(
    f"{url}/{function_name}",
    data=json.dumps(params),
    headers={"Content-Type": "application/json"},
)


# Print the response
print(response.json())
