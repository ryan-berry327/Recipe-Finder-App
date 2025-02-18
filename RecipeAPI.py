class RecipeAPI:

   def __init__(self, api_key,base_url,num_recipe):
        self.api_key = '1e4bbc6925e14291bd42452b5a7da089'
        self.base_url = 'https://api.spoonacular.com'
        self.endpoint_url  = '/recipes/findByIngredients'
        self.num_recipe = num_recipe

    # Build the request URL by adding the URL with parameters
    def build_url(self, ingredients):
        ingredients_str = ",".join(ingredients)
        url = f"{self.base_url}{self.endpoint_url}?ingredients={ingredients_str}&apiKey={self.api_key}&number={self.num_recipe}"
        return url # return the specific url to find the recipe

    # This method sends a GET request to the Spoonacular API and returns the response
    def search_recipes(ingredients):
        url = self.build_url(ingredients) # Build the URL
        response = requests.get(url) # Send the GET request
        if respons.status_code == 200: # if request was successful
            return response.json() # Return the JSON response
        else:
            print(f"ErrorL {response.status_code}")
            return None # None if theres an error

    # Puts the API response and returns a list of the recipes
    def parse_recipes(response):
        recipes = []

        if response: 
            for recipe in response:
                recipe_data = {
                    "name": name["title"], # Recipe title
                    "ingredients": recipe["userIngredients"] # Ingredients used
                    "missing_ingredients": recipe["missedIngredients"], # Missing ingredients
                    "instructions": recipe.get("instructions","Instructions not available") # Gets instructions if they are available
                    "link": f"https://spoonacular.com/recipes/{recipe['title'].replace(' ', '-')}-{recipe['id']}"  # Recipe link
                }
                recipes.append(recipe_data)
        
        return recipes
        

    

    
