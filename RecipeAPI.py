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

    def search_recipes(ingredients):
        pass

    def parse_recipes(response):
        pass

    

    
