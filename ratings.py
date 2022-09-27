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
        #print(f"{restaurant} is rated at {rating}.") 

def add_restaurant():

    new_restaurant = input("Please enter a restaurant name: ")
    new_score = input(f"Please rate {new_restaurant}: ")
    restaurants[new_restaurant] = new_score

def see_restaurants():
    for restaurant, rating in sorted(restaurants.items()):
      print(f"{restaurant} is rated at {rating}.")


def user_choices():

    restaurant_ratings(input_file)

    while True:
        print("\nWhat would you like to do?")
        print(f"1. See restaurants rating")
        print(f"2. Add a new restaurant and rating.")
        print(f"3. Update a restaurant's rating")
        print(f"4. Quit")
        options = input("Select option from list: ")
        options = int(options)

        if options == 1: 
            see_restaurants()

        elif options == 2:
            add_restaurant()

        elif options == 3:
            #restaurant_ratings(input_file)
            restaurant = input("Which restaurant's rating would you like to change? ")
            if restaurant in restaurants:
                new_rating = input(f"{restaurant}'s current rating is {restaurants[restaurant]}, what should the new rating be? ")
                new_rating = int(new_rating)
                restaurants[restaurant] = new_rating

        else:
           break
        
print()

with open("scores.txt") as input_file:
    #add_restaurant()
    user_choices()
    #restaurant_ratings(input_file)

# input_file.close() # close file here