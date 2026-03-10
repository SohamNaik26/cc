import requests

# Enter your API details here
API_KEY = "YOUR_API_KEY"
SEARCH_ENGINE_ID = "YOUR_SEARCH_ENGINE_ID"

# Search keyword
search_query = "cat"

# Google Custom Search API URL
url = "https://www.googleapis.com/customsearch/v1"

# Parameters
params = {
    "q": search_query,
    "key": API_KEY,
    "cx": SEARCH_ENGINE_ID,
    "searchType": "image"
}

# Send request
response = requests.get(url, params=params)

# Convert response to JSON
results = response.json()

# Print image links
if "items" in results:
    for item in results["items"]:
        print(item["link"])
else:
    print("No results found")