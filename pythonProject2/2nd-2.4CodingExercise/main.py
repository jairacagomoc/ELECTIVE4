flavors = ["boots", "chocolates", "straberry", "cookies n cream", "bubblegum"]
toppings = ["almonds", "banana slices", "chocolate syrup", "caramel", "white chocolate chips"]
ice_cream = dict (zip(flavors, toppings))
print(ice_cream)

ice_cream["chocolate"] = "blueberries"
ice_cream.update ({"macha": "picatchios", "ube": "mange slices"})
print(ice_cream)