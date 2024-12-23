def main():
    print("This code will calculate the perimeter of a triangle.")
    side1 = float(input("\nWhat is the length of Side 1? "))
    side2 = float(input("\nWhat is the length of Side 2? "))
    side3 = float(input("\nWhat is the length of Side 3? "))
    perimeter = side1 + side2 + side3

    print(f"\nThe perimeter of the triangle is {perimeter}")


if __name__ == '__main__':
    main()