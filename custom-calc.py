 # Homework: Your job is to make a custom calculator. 
# Your calculator should accept at least three values. 

# For example height, width, length

# It should print a prompt that makes it clear what 
# is being calculated. 

# For example: 
# Enter height, width, and length to calculate the area of a cube
# Height: 3
# Width: 4
# Length: 2

# After accepting input the calculator should perform 
# an accurate calculation and display the results in 
# a clear and well formatted message. 

# For example: A cube with a height of 3, width of 4, and length of 2 has an area of 24

# You can accept string input that becomes part of the description. 
# For example: Input units: inches

# Be sure to convert your numeric values to numbers before performing math operations!

#First, make a list of the variables
#Use "float" to convert the string inputs to floats (numbers)
# user_height = float(input("Enter height in inches: "))
# user_width = float(input("Enter width in inches: "))
# user_length = float(input("Enter length in inches: "))

#Variable that will create the inches squared
# area_cube = user_height * user_width * user_length

# #Use "str" to convert the floats back to strings so they display properly in the terminal
# #Looked up the way to display a smaller "2" to represent squared = "\u00b2"
# print("A cube with a height of " + str(user_height) + " inches" + ", width of " + str(user_width) + " inches" 
#       + ", and length of " + str(user_length) + " inches" + " has an area of " + str(area_cube)+ " inches" + "\u00b2" + ".")

# Turned my more "manual" approach into a proper "function" approach!

def area_cube(height, width, length):
    cube_area = height * width * length
    return cube_area

height = float(input("Enter height in inches: "))
width = float(input("Enter height in inches: "))
length = float(input("Enter height in inches: "))

cube_area_result = area_cube(height, width, length)
print(f"A cube with a height of {height}, a width of {width}, and a length of {length}, has an area of {cube_area_result}\u00b2 inches.")