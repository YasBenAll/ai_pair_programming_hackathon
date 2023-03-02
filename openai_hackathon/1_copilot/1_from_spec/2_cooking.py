"""
Add type hints to all your functionality and use mypi to test for correctness.

Pick a favorite recipe.
Ingredients and spices are required with quantities or weights.

"""

"""
1. Store the ingredients and spices in a data structure.
2. Make map for the associated quantities and weights.
3. Create a recipe class.
4. Create a generator to yield the ingredients and spices for each step.
5. Wrap the generator to enrich it with the quantities and weights.
6. Create a method to render the recipe as html. 
"""


# 1. Store the ingredients and spices in a data structure.
ingredients = {
                "step 1": ["flour", "sugar", "butter"],
                "step 2": ["eggs", "milk", "vanilla essence"],
                "step 3": ["baking powder"]
            }
spices = {
                "step 1": ["cinnamon", "nutmeg"],
                "step 2": [],
                "step 3": []
            }
# 2. Make map for the associated quantities and weights.
quantities = {
    "flour": "3 cups",
    "sugar": "1 1/2 cup",
    "butter": "1 cup",
    "eggs": "4",
    "milk": "1 cup",
    "vanilla essence": "2 teaspoon",
    "baking powder": "1 teaspoon",
}

def flatten_list(_2d_list):
    flat_list = []
    # Iterate through the outer list
    for element in _2d_list:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list

# add spices to quantities map
for spice in flatten_list([i[1] for i in spices.items()]):
    quantities[spice] = "1 teaspoon"

# 3. Create a recipe class.
class Recipe:
    def __init__(self, ingredients, spices, quantities, steps):
        self.ingredients = ingredients
        self.spices = spices
        self.quantities = quantities
        self.steps = steps

# 4. Create a generator to yield the ingredients and spices for each step.
    def ingredients_generator(self, spices=False):
        # ingredients per step
        if not spices:
            for step in range(1, self.steps+1): 
                for ingredient in self.ingredients[f"step {step}"]:
                    yield step, ingredient
        else:
            for step in range(1, self.steps+1): 
                for spice in self.spices[f"step {step}"]:
                    yield step, spice

# 5. Wrap the generator to enrich it with the quantities and weights.
    def ingredients_enriched(self, spices=False):
        for step, ingredient in self.ingredients_generator(spices):
            yield step, ingredient, self.quantities[ingredient]

# 6. Create a method to render the recipe as html.
    def render(self):
        """
        Render the recipe as html.
        """
        print("Ingredients:")
        step_prev = 0
        for step, ingredient, quantity in self.ingredients_enriched():
            if step != step_prev:
                print(f"\nStep {step}")
            print(f"\t {ingredient}: {quantity}")
            step_prev = step
        print("Spices:")
        for step, ingredient, quantity in self.ingredients_enriched(spices):
            if step != step_prev:
                print(f"\nStep {step}")
            print(f"\t {ingredient}: {quantity}")
            step_prev = step
        

if __name__ == "__main__":
    recipe = Recipe(ingredients, spices, quantities,3)
    recipe.render()