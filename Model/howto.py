import requests

# This is the URL of the server running the FastAPI app
# Replace this with your own URL
url = "http://localhost:8000/engine"

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
    json=params,
)

params2 = {"ID": "510812B00000C8DD", "FruitID": 83, "Rating": "5"}

response2 = requests.post(
    f"http://localhost:8000/postRating",
    json=params2,
)

print(response2.json())

# Print the response
# print(response.json())
# print(requests.get("http://localhost:8000/getUser").json())
