# UK Restaurant Finder
This Streamlit application allows users to search for restaurants by UK postcode, providing details such as name, cuisines, ratings, and addresses. The app fetches restaurant data from a Just Eat API and displays it in a user-friendly card layout.

## Prerequisites
Before running this application, you will need:

Python 3.8+
pip (Python package installer)

Installation
Clone the repository and install the required Python packages.

```console
# Clone the repository
git clone https://github.com/CIA41998/restaurant_dashboard.git
cd restaurant_dashboard

# Install required packages
pip install -r requirements.txt
```

## Setting Up
Ensure you have the following files in your project directory:

styles.css: Contains the CSS for styling the restaurant cards.
restaurant_card.html: HTML template for displaying each restaurant.

## How to Run the App
To run the app, navigate to the project directory in your terminal and execute the following command:
```console
streamlit run dashboard.py
```

## Features
Search for restaurants by UK postcode.
Displays a list of restaurants with detailed information.
Interactive UI to fetch and display restaurant data.
