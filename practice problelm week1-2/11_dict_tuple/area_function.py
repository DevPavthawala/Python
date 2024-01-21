import math

def calc_area(radius):
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    diameter = 2 * radius
    return area,circumference,diameter

if __name__ == '__main__':
    radius = input("Enter the radius :")
    radius = float(radius)
    area,circumfernce,diameter = calc_area(radius)
    print(f'area :{area} , circumference : {circumfernce}, diameter : {diameter}')