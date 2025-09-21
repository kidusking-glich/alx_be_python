we = input("What's the weather like today? (sunny/rainy/cold):").lower()

"""sun = "sunny" 
rain = "rainy"
cold = "cold"""

if we == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif we == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif we == "cold" :
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Wrong Selection")