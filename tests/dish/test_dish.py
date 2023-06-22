from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    item1 = Ingredient("bacon")

    pizza = Dish("pizza", 20.0)
    assert pizza.name == "pizza"

    hamburguer = Dish("hamburguer", 15.0)
    assert hamburguer.name == "hamburguer"

    pizza.add_ingredient_dependency(item1, 4)

    pizza2 = Dish("pizza", 20.0)
    assert pizza2.name == "pizza"

    assert hash(pizza) == hash(pizza2)
    assert hash(pizza2) != hash(hamburguer)

    assert repr(pizza) == "Dish('pizza', R$20.00)"
    assert repr(hamburguer) != "Dish('queijo', R$15.00)"

    assert pizza == pizza2

    assert pizza.get_restrictions() == {
        Restriction.ANIMAL_DERIVED, Restriction.ANIMAL_MEAT}

    with pytest.raises(TypeError):
        Dish("test", "00.0")

    with pytest.raises(ValueError):
        Dish("test1", -0001.0)

    with pytest.raises(ValueError):
        Dish("test2", -01.0)

    assert pizza.recipe.get(item1) == 4
    assert pizza.recipe.get(item1) != 3
    assert pizza.get_ingredients() == {item1}
    assert pizza2.get_ingredients() == set()
