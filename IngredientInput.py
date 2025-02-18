class IngredientInput:

    def __init__(self):
        self.ingredients = set()

    def get_user_input(self):
        while True:
            user_input = input("Please list your ingredients separated by a comma: ")
            if self.validate_input(user_input):  # Keep asking if input is invalid
                break  # Exit the loop when input is valid

    def validate_input(self, user_input):
        if not user_input.strip():  # Check if input is empty
            print("Input cannot be empty.")
            return False  # Invalid input
        
        if any(char.isdigit() for char in user_input):  # Check for numbers
            print("Invalid input. Ingredient names cannot contain numbers.")
            return False  # Invalid input
        
        # Convert input into a cleaned set of ingredients (removes extra spaces and converts to lowercase)
        cleaned_ingredients = {ingredient.strip().lower() for ingredient in user_input.split(',')}
        
        # Update the set with the cleaned ingredients
        self.ingredients.update(cleaned_ingredients)

        print("Ingredients stored:", self.ingredients)  # Show stored ingredients
        return True  # Valid input


# Create an instance and start user input
ob = IngredientInput()
ob.get_user_input()
