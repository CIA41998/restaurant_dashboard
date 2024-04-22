import streamlit as st
import requests
import html
import re

# Constants
API_URL = "https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"
JUST_EAT_COLOR = "#ff8100" 
STAR_FILLED = "★"
STAR_EMPTY = "☆"
MAX_RATING = 5

st.set_page_config(layout="wide")

# Read the CSS file
def load_css(css_file):
    with open(css_file, "r") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Read the HTML file
def load_html(html_file, **kwargs):
    with open(html_file, "r") as f:
        html_content = f.read()
        html_content = html_content.format(**kwargs)
        return html_content


def fetch_restaurants(postcode):
    url = API_URL.format(postcode=postcode.replace(" ", ""))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    # Raises an HTTPError for bad responses
    response.raise_for_status()  
    return response.json()

def extract_restaurant_data(data):
    restaurants = []
    for item in data.get('restaurants', []):
        if len(restaurants) >= 10:
            break
        numeric_rating = float(item.get('rating', {}).get('starRating', 0))  # Convert rating to float
        rounded_rating = round(numeric_rating)  # Round the rating to the nearest whole number
        stars_filled = "★" * rounded_rating + "☆" * (MAX_RATING - rounded_rating)
        rating_display = f"{numeric_rating} ({stars_filled})"  # Display both numeric and star rating
        restaurant_info = {
            'Name': item.get('name'),
            'Cuisines': ', '.join([cuisine['name'] for cuisine in item.get('cuisines', [])]),
            'Rating': rating_display,
            'Address': f"{item['address']['firstLine']}, {item['address']['city']}, {item['address']['postalCode']}"
        }
        restaurants.append(restaurant_info)
    return restaurants

# Display the restaurant data as cards in a grid layout
def display_restaurants(restaurants):
    load_css("styles.css")
    num_cols = 4
    rows = [st.container() for _ in range((len(restaurants) + num_cols - 1) // num_cols)]
    cols_per_row = [r.columns(num_cols) for r in rows]

    for index, restaurant in enumerate(restaurants):
        col_index = index % num_cols
        row_index = index // num_cols
        col = cols_per_row[row_index][col_index]
        map_url = f"https://www.google.com/maps/search/?api=1&query={html.escape(restaurant['Address'])}"
        restaurant_html = load_html("restaurant_card.html",
                                    name=restaurant['Name'],
                                    cuisines=restaurant['Cuisines'],
                                    rating=restaurant['Rating'],
                                    address=restaurant['Address'],
                                    map_url=map_url)
        
        with col:
            st.markdown(restaurant_html, unsafe_allow_html=True)

def valid_postcode(postcode):
    # Basic UK postcode regex
    pattern = r"^[A-Z]{1,2}[0-9R][0-9A-Z]? ?[0-9][A-Z]{2}$"
    return re.match(pattern, postcode.upper())

# Main function to run the Streamlit app
def main():
    # Load and apply the CSS styles
    load_css("styles.css")

    st.markdown("""
        <div style='background-color:#ff8100;color:white;padding:10px;text-align:center;'>
            <span style='font-size:24px;vertical-align:middle;'>UK Restaurant Finder</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
        <style>
            div.stTextInput > label {font-size: 18px;}
        </style>
        """, unsafe_allow_html=True)
    postcode = st.text_input("Enter a UK postcode (e.g., EC4M 7RF):", "EC4M 7RF")

    if st.button("Fetch Restaurants"):
        if not valid_postcode(postcode):
            st.error("Please enter a valid UK postcode.")
        else:
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