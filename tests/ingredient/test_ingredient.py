from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient1 = Ingredient("salmão")
    assert ingredient1.name == "salmão"

    assert repr(ingredient1) == "Ingredient('salmão')"

    ingredient2 = Ingredient("carne")
    assert ingredient2.name == "carne"
    assert repr(ingredient2) == "Ingredient('carne')"

    assert ingredient1 != ingredient2

    ingredient3 = Ingredient("salmão")
    assert ingredient3.name == "salmão"
    assert repr(ingredient3) == "Ingredient('salmão')"

    assert ingredient1 == ingredient3
    assert ingredient2 != ingredient3

    assert ingredient1.name != ingredient2.name

    assert hash(ingredient1) == hash(ingredient3)
    assert hash(ingredient2) != hash(ingredient3)

    assert ingredient1.restrictions == { 
        Restriction.ANIMAL_MEAT,
        Restriction.SEAFOOD,
        Restriction.ANIMAL_DERIVED
        }
