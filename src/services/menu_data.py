# Req 3
import csv

from src.models.dish import Dish
from src.models.ingredient import Ingredient
from collections import defaultdict


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.ingredients = set()
        self.source_path = source_path
        self.read_file()

    def read_file(self):
        dish_dict = defaultdict(lambda: None)
        ingredient_set = set()

        with open(self.source_path, "r") as new_file:
            reader = csv.reader(new_file)
            next(reader)

            for line in reader:
                dish_name = line[0]
                dish_price = float(line[1])
                ingredient_name = line[2]
                ingredient_quantity = int(line[3])

                dish = dish_dict[dish_name]
                if dish is None:
                    dish = Dish(dish_name, dish_price)
                    dish_dict[dish_name] = dish
                    self.dishes.add(dish)

                ingredient = Ingredient(ingredient_name)
                ingredient_set.add(ingredient)
                dish.add_ingredient_dependency(ingredient, ingredient_quantity)

        self.ingredients = ingredient_set
