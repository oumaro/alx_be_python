# This script provides clothing recommendations based on the weather.

# Prompt the user for the current weather condition.
# The .lower() method is used to make the input case-insensitive.
weather = input("What's the weather like today? (sunny/rainy/cold): ")

# Check the weather condition and provide a recommendation.
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
