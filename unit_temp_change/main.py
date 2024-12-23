def main():
    print("This code will change Fahrenheit into Celsius.")
    degrees_fahrenheit = float(input("\nEnter temperature in Fahrenheit: "))
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0
    print(f"\nTemperature: {degrees_fahrenheit}F = {degrees_celsius}C")
    

if __name__ == '__main__':
    main()