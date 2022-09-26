"""Restaurant rating lister."""


# put your code here

def restaurant_ratings(input_file):

    # sorted(animals.items())
    restaurants = {}
    # words = line.rstrip().split()
    for line in sorted(input_file):
        
        restaurant_rating = line.rstrip().split(":")
        restaurant, rating = restaurant_rating
        restaurants[restaurant] = rating
        print(f"{restaurant} is rated at {rating}.") 

    #for restaurant in sorted(restaurants.items()):
        #print(f"{restaurant} is rated at {restaurants[restaurant]}.")   


with open("scores.txt") as input_file:
    restaurant_ratings(input_file)