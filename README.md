# Recipe Finder App

This is a simple Python application that allows users to input ingredients they have on hand and get recipe suggestions using the Spoonacular API. The application takes a list of ingredients as input, sends the data to the Spoonacular API, and retrieves a list of recipes based on those ingredients.

## Features

- **Ingredient Input**: The user provides a list of ingredients (comma-separated).
- **Recipe Fetching**: Using the Spoonacular API, the app fetches recipes that include the provided ingredients.
- **Results Display**: Displays the title of the found recipes.

## Requirements

- Python 3.x
- `requests` library (can be installed using `pip install requests`)
- An API key from Spoonacular (sign up on [Spoonacular](https://spoonacular.com/food-api) to get your free API key).
