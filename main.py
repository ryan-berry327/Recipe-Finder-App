from ingredient_input import IngredientInput
from recipe_api import RecipeAPI

class Main:

    @staticmethod
    def run():
        # Initialize the IngredientInput class to get user input
        ingredient_input = IngredientInput()
        ingredient_input.get_user_input()

        # Get the list of ingredients
        ingredients = ingredient_input.get_ingredients()

        # Initialize the RecipeAPI class with your API key, base URL, and number of recipes
        api_key = "1e4bbc6925e14291bd42452b5a7da089"  # Replace with your actual API key
        base_url = "https://api.spoonacular.com"  # Base URL for Spoonacular API
        num_recipes = 5  # Set the number of recipes you want to fetch
        recipe_api = RecipeAPI(api_key, base_url, num_recipes)  # Now passing num_recipes

        # Search for recipes using the ingredients
        recipes = recipe_api.search_recipes(ingredients)

        # Display the results
        if recipes:
            print("\nFound Recipes:")
            for recipe in recipes:
                # Safely access fields and handle missing keys using .get()
                title = recipe.get("title", "No title available")

                print(f"Title: {title}")
                print("-------------")
        else:
            print("No recipes found.")

# Run the main function
if __name__ == "__main__":
    Main.run()  # Call the run method to execute the program

