def calculate_area(shape,base,height):
    if shape == "tringle":
        area = (1 / 2) * base * height
    elif shape == "rectangle":
        area = base*height
    else:
        area = (1 / 2) * base * height

    return area

c = calculate_area("recta",20,2)
print(c)
