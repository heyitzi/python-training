import math

def circle_area(radius):
    area = (math.pi) * (radius ** 2)
    return f"The area of the circle is: {area}"

user_rad = input("Enter the radius of your circle: ")
print(circle_area(int(user_rad)))