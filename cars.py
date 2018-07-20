# Create a single class that implements all functionality.
class MakeAndModel():

    def create_dictionary(self):
# Create a method for reading the car makes file.
        car_makes = [line for line in open("car_makes.txt", "r")]
        print(car_makes)
# Create a method for reading the car models file.
# Create a method that invokes the previous two methods and generates a dictionary.
# The dictionary keys will be the make names.
# The value for each key will be a list of model names.
MakeAndModel().create_dictionary()