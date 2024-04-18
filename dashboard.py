import streamlit as st
import requests

# Constants
API_URL = "https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"

def fetch_restaurants(postcode):
    url = API_URL.format(postcode=postcode.replace(" ", ""))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    return response.json()

def extract_restaurant_data(data):
    restaurants = []
    for item in data.get('restaurants', []):
        if len(restaurants) >= 10:
            break
        restaurant_info = {
            'Name': item.get('name'),
            'Cuisines': ', '.join([cuisine['name'] for cuisine in item.get('cuisines', [])]),
            'Rating': item.get('rating', {}).get('starRating'),
            'Address': f"{item['address']['firstLine']}, {item['address']['city']}, {item['address']['postalCode']}"
        }
        restaurants.append(restaurant_info)
    return restaurants

def display_restaurants(restaurants):
    for restaurant in restaurants:
        st.subheader(restaurant['Name'])
        st.text(f"Cuisines: {restaurant['Cuisines']}")
        st.text(f"Rating: {restaurant['Rating']}")
        st.text(f"Address: {restaurant['Address']}")
        st.write("---")

def main():
    st.title("UK Restaurant Finder")
    postcode = st.text_input("Enter a UK postcode (e.g., EC4M 7RF):", "EC4M 7RF")
    if st.button("Fetch Restaurants"):
        try:
            data = fetch_restaurants(postcode)
            restaurants = extract_restaurant_data(data)
            display_restaurants(restaurants)
        except requests.HTTPError as e:
            st.error(f"Failed to fetch data: {e.response.status_code} {e.response.reason}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
