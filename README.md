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

styles.css: Contains the CSS for styling the restaurant cards. <br />
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

## Assumptions
- assumed that the maximum rating for the restaurants is 5 stars <br />
- assumed to be a quick tool, where more information is not needed to be seen <br />
- assumed that the API is always available and can be called

## Improvements
One of the main improvements is the visual of the dashboard. Even though it is easily readable and the user can navigate it in a simple way, different improvements could be made to increase the user interaction. Currently, it is a pretty simple dashboard with no visuals for every restaurant. An added logo for each restaurant and some pictures/icons could improve the engagement of the user. Moreover, even though teh color of JET was used for the header, the logo of the company and other company fonts could have been included. Last, the dashboard was tested on mobile and bigger screens, but it is not certain that the layout would hold in all cases, meaning that it would not be the best experience in all cases. 
