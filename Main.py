import math

choice = 1


def calcCube():
    a = input("Please enter the height of the side in cm:")
    return round(float(a) ** 3, 2)


def calcTetrahedron():
    side = input("Please enter the height of the side in cm:")
    return round(float(side) ** 3 / (6 * math.sqrt(2)), 2)


def main():
    global choice
    while choice > 0:
        print("Choose one of the folowing choices: ")
        choice = input(
            """
                1- Calculate the volume of an equilateral cube
                2- Calculate an equilateral tetrahedron
                0- Exit
            """
        )
        choice = int(choice)
        if choice > 0:
            print(choice)
        if choice is 1:
            print(f"The volume of the cube is: {calcCube()} cm.")
            choice = 0
        elif choice is 2:
            print(f"The volume of the tetrahedron is: {calcTetrahedron()} cm.")
            choice = 0
        else:
            if choice is not 0:
                print("OBS!Your choice is not one of the possible choices!")


main()
