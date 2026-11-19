
import math
from datetime import datetime


def main():
    width = int(input("Enter the width of the tire in mm (ex 205): "))
    aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

    volume = (
        math.pi
        * width**2
        * aspect_ratio
        * (width * aspect_ratio + 2540 * diameter)
        / 10_000_000_000
    )

    print(f"The approximate volume is {volume:.2f} liters")

    
    current_date = f"{datetime.now():%Y-%m-%d}"

    
    with open("volumes.txt", "at") as volumes_file:
        print(
            f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}",
            file=volumes_file,
        )

        
        buy = input("Would you like to buy tires with these dimensions? (yes/no): ")
        if buy.strip().lower() == "yes":
            phone = input("Enter your phone number: ")
            print(f"Phone number: {phone}", file=volumes_file)
            print("Thank you! We will contact you soon.")


if __name__ == "__main__":
    main()