with open("DataFiles/21.txt") as f:
    data = f.read().replace("contains ", "").replace(")", "").splitlines()
    data = [d.split(" (") for d in data]

allIngredients = set()
allergensToPotentialIngredients = {}
for d in data:
    ingredients = set(d[0].split(" "))
    allIngredients = allIngredients.union(ingredients)
    allergens = d[1].split(", ")
    for allergen in allergens:
        if allergen in allergensToPotentialIngredients:
            allergensToPotentialIngredients[allergen] = allergensToPotentialIngredients[
                allergen] & ingredients
        else:
            allergensToPotentialIngredients[allergen] = ingredients

print(allergensToPotentialIngredients)

allIngredientsThatCantContainsAllergens = allIngredients
for ingredients in allergensToPotentialIngredients.values():
    allIngredientsThatCantContainsAllergens = allIngredientsThatCantContainsAllergens - ingredients

retval = 0
for d in data:
    ingredients = set(d[0].split(" "))
    retval += len([i for i in ingredients if i in allIngredientsThatCantContainsAllergens])
print(retval)
