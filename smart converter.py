print("SMART UNIT CONVERTER")
print("--------------------")

while True:
    print("\nChoose Conversion Type")
    print("1. Length")
    print("2. Temperature")
    print("3. Weight")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nLength Conversion")
        meters = float(input("Enter value in meters: "))
        km = meters / 1000
        print("Kilometers:", km)

    elif choice == 2:
        print("\nTemperature Conversion")
        c = float(input("Enter temperature in Celsius: "))
        f = (c * 9/5) + 32
        print("Fahrenheit:", f)

    elif choice == 3:
        print("\nWeight Conversion")
        kg = float(input("Enter weight in kilograms: "))
        grams = kg * 1000
        print("Grams:", grams)

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice, try again!")