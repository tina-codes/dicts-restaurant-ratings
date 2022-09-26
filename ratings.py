"""Restaurant rating lister."""


# put your code here
restaurants = {}

def restaurant_ratings(input_file):
    
    for line in sorted(input_file):
      restaurant_rating = line.rstrip().split(":")
      restaurant, rating = restaurant_rating
      restaurants[restaurant] = rating
      print(f"{restaurant} is rated at {rating}.") 

def add_restaurant():
    new_restaurant = input("Please enter a restaurant name: ")
    new_score = input(f"Please rate {new_restaurant}: ")
    restaurants[new_restaurant] = new_score
    restaurant_ratings(input_file)

    for restaurant, rating in sorted(restaurants.items()):
      print(f"{restaurant} is rated at {rating}.")

with open("scores.txt") as input_file:
    restaurant_ratings(input_file)
    add_restaurant()
