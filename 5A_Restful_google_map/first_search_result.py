import requests
import webbrowser

# Enter your API details here
API_KEY = "YOUR_API_KEY"
SEARCH_ENGINE_ID = "YOUR_SEARCH_ENGINE_ID"

# Take input from user
search_query = input("Enter something for searching: ")

# Google Custom Search API URL
url = "https://www.googleapis.com/customsearch/v1"

# Parameters
params = {
    "q": search_query,
    "key": API_KEY,
    "cx": SEARCH_ENGINE_ID
}

# Send request
response = requests.get(url, params=params)

# Check response
if response.status_code == 200:

    results = response.json()

    if "items" in results and len(results["items"]) > 0:
        first_link = results["items"][0]["link"]

        print("Successfully Found:", first_link)

        # Open the first result in browser
        webbrowser.open(first_link)

    else:
        print("No results found")

elif response.status_code == 400:
    print("Bad Request Error (400)", response.json())

else:
    print(f"HTTP Error {response.status_code}: {response.text}")