import requests


def get_geolocation(api_key, search_string):

    # Base URL for LocationIQ API
    base_url = "https://us1.locationiq.com/v1/search.php"

    # Parameters for request
    params = {
        "key": api_key,
        "q": search_string,
        "format": "json"
    }

    # Send GET request
    response = requests.get(base_url, params=params)

    # Convert response to JSON
    data = response.json()

    if response.status_code == 200 and data:

        result = {
            "place_id": data[0].get("place_id"),
            "lat": data[0].get("lat"),
            "lon": data[0].get("lon"),
            "display_name": data[0].get("display_name")
        }

        return result

    else:
        print(f"Error: {response.status_code} - {data.get('error','No error message')}")
        return None


# Paste your LocationIQ API key here
api_key = "YOUR_LOCATIONIQ_API_KEY"

# Take location input
search_string = input("Enter the location: ")

# Call function
result = get_geolocation(api_key, search_string)

# Display result
if result:
    print("\nOutput:")
    for key, value in result.items():
        print(f"{key} : {value}")