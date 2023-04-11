#Name: Final Project
#Author: Isabella Oliveira Castro
#Student ID: 8865024
#Date: April 10, 2023

""""
This program will help the user to organize their recipes.
"""
import random

class Recipe:
    ##This function will initialize a new recipe instance with the provided name, ingredients, instructions, and category.
    #It will also assign a random id to the recipe provided.
    def __init__(self, name, ingredients, instructions, category):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.category = category
        self.id = random.randint(1, 1000000)
        
    #It will return a string representation of the recipe instance.
    def __repr__(self):
        return f"<Recipe name={self.name} id={self.id}>"

class RecipeOrganizer:
    #It will initialize a new recipe organizer instance with an empty list of recipes.
    def __init__(self):
        self.recipes = []

    #It will add a new recipe instance to the list of recipes.
    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    #It will remove the provided recipe instance from the list of recipes.
    def remove_recipe(self, recipe):
        self.recipes.remove(recipe)

    #It will search for recipes that match the provided search query (case-insensitive) by name, ingredients, or category.
    #Will return a list of matching recipe instances.
    def search_recipe(self, search_query):
        results = []
        for recipe in self.recipes:
            if search_query.lower() in recipe.name.lower():
                results.append(recipe)
            elif search_query.lower() in recipe.ingredients.lower():
                results.append(recipe)
            elif search_query.lower() in recipe.category.lower(): 
                results.append(recipe)
        if not results:
            print("No matching recipe found.")
        else:
            print("Matching recipes:")
            for recipe in results:
                print(f"{recipe.name} (id={recipe.id})")
        return results

    #Display all recipes in the list of recipes.
    def display_all(self):
        for recipe in self.recipes:
            print(f"{recipe.name} (id={recipe.id})")

    #Edit the provided recipe instance with the provided new values for name, ingredients, instructions, and/or category.
    def edit_recipe(self, recipe, name=None, ingredients=None, instructions=None, category=None):
        if name:
            recipe.name = name
        if ingredients:
            recipe.ingredients = ingredients
        if instructions:
            recipe.instructions = instructions
        if category:
            recipe.category = category
""""
Create a new instance of the RecipeOrganizer class and start a while loop that prompts the user 
for input and executes the appropriate method based on the user's selection. 
"""
def main():
    organizer = RecipeOrganizer()
    while True:
        print("\nWelcome to your personal recipe organizer! \n")
        print("Please, make a selection!")
        print("\nRecipe Organizer")
        print("1. Add Recipe")
        print("2. Remove Recipe")
        print("3. Search Recipe")
        print("4. Display All Recipes")
        print("5. Edit Recipe")
        print("6. Exit")

        choice = input("Enter your choice: ")
        
        #The user will create a new recipe.
        if choice == "1":
            name = input("Enter recipe name: ")
            ingredients = input("Enter recipe ingredients: ")
            instructions = input("Enter recipe instructions: ")
            category = input("Enter recipe category: ")
            recipe = Recipe(name, ingredients, instructions, category)
            organizer.add_recipe(recipe)
            print("Recipe added successfully. Recipe id is", recipe.id)
        
        #The user will delete an existing recipe.
        elif choice == "2":
            search_query = input("Enter recipe name or id to delete: ")
            try:
                search_id = int(search_query)
                results = [recipe for recipe in organizer.recipes if recipe.id == search_id]
            except ValueError:
                results = organizer.search_recipe(search_query)
            if not results:
                print("No matching recipe found.")
            elif len(results) == 1:
                organizer.remove_recipe(results[0])
                print("Recipe removed successfully.")
            else:
                print("Multiple recipes found:")
                for recipe in results:
                    print(f"{recipe.name} (id={recipe.id})")
                search_id = input("Enter recipe id to delete: ")
                for recipe in results:
                    if recipe.id == int(search_id):
                        organizer.remove_recipe(recipe)
                        print("Recipe removed successfully.")
                        break

        #The user will search an existing recipe
        elif choice == "3":
            search_query = input("Enter search query: ")
            organizer.search_recipe(search_query)

        #It will display all the recipes
        elif choice == "4":
            organizer.display_all()

        #The user will edit a recipe
        elif choice == "5":
            search_query = input("Enter recipe name or id to edit: ")
            try:
                search_id = int(search_query)
                results = [recipe for recipe in organizer.recipes if recipe.id == search_id]
                if not results:
                    print("No matching recipe found.")
                elif len(results) == 1:
                    recipe = results[0]
                    name = input(f"Enter new name for recipe '{recipe.name}': ") if input("Do you want to change the name? (y/n): ").lower() == "y" else None
                    ingredients = input(f"Enter new ingredients for recipe '{recipe.name}': ") if input("Do you want to change the ingredients? (y/n): ").lower() == "y" else None
                    instructions = input(f"Enter new instructions for recipe '{recipe.name}': ") if input("Do you want to change the instructions? (y/n): ").lower() == "y" else None
                    category = input(f"Enter new category for recipe '{recipe.name}': ") if input("Do you want to change the category? (y/n): ").lower() == "y" else None
                    organizer.edit_recipe(recipe, name=name, ingredients=ingredients, instructions=instructions, category=category)
                    print("Recipe edited successfully.")
                else:
                    print("Multiple recipes found:")
                    for recipe in results:
                        print(f"{recipe.name} (id={recipe.id})")
                    search_id = input("Enter recipe id to edit: ")
                    for recipe in results:
                        if recipe.id == int(search_id):
                            name = input(f"Enter new name for recipe '{recipe.name}': ") if input("Do you want to change the name? (y/n): ").lower() == "y" else None
                            ingredients = input(f"Enter new ingredients for recipe '{recipe.name}': ") if input("Do you want to change the ingredients? (y/n): ").lower() == "y" else None
                            instructions = input(f"Enter new instructions for recipe '{recipe.name}': ") if input("Do you want to change the instructions? (y/n): ").lower() == "y" else None
                            category = input(f"Enter new category for recipe '{recipe.name}': ") if input("Do you want to change the category? (y/n): ").lower() == "y" else None
                            organizer.edit_recipe(recipe, name=name, ingredients=ingredients, instructions=instructions, category=category)
                            print("Recipe edited successfully.")
                            break
            except ValueError:
                results = organizer.search_recipe(search_query)
                if not results:
                    print("No matching recipe found.")
                elif len(results) == 1:
                    recipe = results[0]
                    name = input(f"Enter new name for recipe '{recipe.name}': ") if input("Do you want to change the name? (y/n): ").lower() == "y" else None
                    ingredients = input(f"Enter new ingredients for recipe '{recipe.name}': ") if input("Do you want to change the ingredients? (y/n): ").lower() == "y" else None
                    instructions = input(f"Enter new instructions for recipe '{recipe.name}': ") if input("Do you want to change the instructions? (y/n): ").lower() == "y" else None
                    category = input(f"Enter new category for recipe '{recipe.name}': ") if input("Do you want to change the category? (y/n): ").lower() == "y" else None
                    organizer.edit_recipe(recipe, name=name, ingredients=ingredients, instructions=instructions, category=category)
                    print("Recipe edited successfully.")
                else:
                    print("Multiple recipes found:")
                    for recipe in results:
                        print(f"{recipe.name} (id={recipe.id})")
                        search_id = input("Enter recipe id to edit: ")
                    for recipe in results:
                        if recipe.id == int(search_id):
                            name = input(f"Enter new name for recipe '{recipe.name}': ") if input("Do you want to change the name? (y/n): ").lower() == "y" else None
                            ingredients = input(f"Enter new ingredients for recipe '{recipe.name}': ") if input("Do you want to change the ingredients? (y/n): ").lower() == "y" else None
                            instructions = input(f"Enter new instructions for recipe '{recipe.name}': ") if input("Do you want to change the instructions? (y/n): ").lower() == "y" else None
                            category = input(f"Enter new category for recipe '{recipe.name}': ") if input("Do you want to change the category? (y/n): ").lower() == "y" else None
                            organizer.edit_recipe(recipe, name=name, ingredients=ingredients, instructions=instructions, category=category)
                            print("Recipe edited successfully.")
                            break
        
        #The loop ends here
        elif choice == "6":
            print("Goodbye!")
            break
    else:
        print("Invalid choice. Please try again.")

"""
This script runs the main() function if the script is being run as the main program.
"""
if __name__ == "__main__":
    main()