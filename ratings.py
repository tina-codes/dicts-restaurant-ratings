"""Restaurant rating lister."""
# put your code here
restaurants = {}

# input_file = open("scores.txt")

def restaurant_ratings(input_file):
    
    # with open("scores.txt") as input_file:

      for line in sorted(input_file):
        restaurant_rating = line.rstrip().split(":")
        restaurant, rating = restaurant_rating
        restaurants[restaurant] = rating
        print(f"{restaurant} is rated at {rating}.") 

def add_restaurant():

    new_restaurant = input("Please enter a restaurant name: ")
    new_score = input(f"Please rate {new_restaurant}: ")
    restaurants[new_restaurant] = new_score

    for restaurant, rating in sorted(restaurants.items()):
      print(f"{restaurant} is rated at {rating}.")


def user_choices():

    while True:
        print("\nWhat would you like to do?")
        print(f"1. See restaurants rating")
        print(f"2. Add a new restaurant and rating.")
        print(f"3. Quit")
        options = input("Select option from list: ")
        options = int(options)

        if options == 1: 
            restaurant_ratings(input_file)

        elif options == 2:
            add_restaurant()

        # elif options == 3:
        else:
           break
        
print()

with open("scores.txt") as input_file:
    #add_restaurant()
    user_choices()
    #restaurant_ratings(input_file)

# input_file.close() # close file here