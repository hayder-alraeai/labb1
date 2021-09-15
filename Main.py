import math


def calcCube():
    a = input("Please enter the height of the side in cm:")
    return round(float(a) ** 3, 2)


def calcTetrahedron():
    side = input("Please enter the height of the side in cm:")
    return round(float(side) ** 3 / (6 * math.sqrt(2)), 2)


def main():
    while True:
        print("Choose one of the folowing choices: ")
        choice = input(
            """
                1- Calculate the volume of an equilateral cube
                2- Calculate an equilateral tetrahedron
                0- Exit
            """
        )

        choice = int(choice)

        if choice is 1:
            print(f"The volume of the cube is: {calcCube()} cm.")
            con = input("Do you like to close the app? y/n: ")
            if con is "y":
                break
        elif choice is 2:
            print(f"The volume of the tetrahedron is: {calcTetrahedron()} cm.")
            con = input("Do you like to close the app? y/n: ")
            if con is "y":
                break
        elif choice is 0:
            break
        else:
            print("OBS!Your choice is not one of the possible choices!")


main()
