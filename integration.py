import requests
import time
import csv

# GraphQL API Endpoint
GRAPHQL_URL = "https://countries.trevorblades.com/"
GRAPHQL_QUERY = """
query {
    countries {
        name
        capital
        currency
    }
}
"""

# REST API Endpoint
REST_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_countries():
    """Fetches country data from the GraphQL API."""
    response = requests.post(GRAPHQL_URL, json={"query": GRAPHQL_QUERY})
    
    if response.status_code == 200:
        data = response.json()
        return data["data"]["countries"]
    else:
        print(f"Error fetching data: {response.status_code}")
        return []

def post_country_details(country):
    """Posts country details to the REST API with error handling."""
    payload = {
        "title": f"Country: {country['name']}",
        "body": f"Capital: {country['capital']}, Currency: {country['currency']}",
        "userId": 1
    }
    
    attempt = 0
    while attempt < 5:
        response = requests.post(REST_URL, json=payload)

        if response.status_code == 201:
            print(f"Successfully posted: {response.json()}")
            return response.json()
        elif response.status_code == 403:
            print("Error 403: Forbidden. Skipping request.")
            return None
        elif response.status_code == 500:
            attempt += 1
            wait_time = 2 ** attempt  # Exponential backoff/retry strategy define
            print(f"Error 500: Internal Server Error. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
        else:
            print(f"Unexpected error: {response.status_code}")
            return None

def save_to_csv(countries):
    """Saves all fetched countries to a CSV file."""
    with open("countries.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Country Name", "Capital", "Currency"])
        
        for country in countries:
            writer.writerow([country["name"], country["capital"], country["currency"]])
    
    print("Data saved to countries.csv")

def main():
    """Automates the entire workflow."""
    countries = fetch_countries()
    if countries:
        save_to_csv(countries)
        selected_country = countries[0]  # Pick the first country
        post_country_details(selected_country)
    else:
        print("No data fetched.")

if __name__ == "__main__":
    main()
