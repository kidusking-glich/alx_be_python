we = input("What's the weather like today? (sunny/rainy/cold):").lower()

sun = "sunny" 
rain = "rainy"
cold = "cold"

if we == sun:
    print("Wear a t-shirt and sunglasses.")
elif we == rain:
    print("Don't forget your umbrella and a raincoat.")
else:
    print("Make sure to wear a warm coat and a scarf.")