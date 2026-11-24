"""
Inkom Emporium receipt program

Exceeding the requirements:
  1. Prints how many days remain until the New Year's Sale (Jan 1).
  2. Prints a "return by" date that is 9:00 PM, 30 days from today.
"""

import csv
import time
from datetime import datetime, timedelta


PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2


REQUEST_NUMBER_INDEX = 0
REQUEST_QUANTITY_INDEX = 1

SALES_TAX_RATE = 0.06


def read_dictionary(filename, key_column_index):
    """Read a CSV file into a compound dictionary.

    The key is the value in column key_column_index of each row.
    The value is the whole row as a list.
    The first line (column headings) is skipped.
    """
    dictionary = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  
        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                dictionary[key] = row_list
    return dictionary


def main():
    try:
        products_dict = read_dictionary("products.csv", 0)

        print("Inkom Emporium")

        number_of_items = 0
        subtotal = 0.0

        with open("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)  
            for row_list in reader:
                if len(row_list) != 0:
                    product_number = row_list[REQUEST_NUMBER_INDEX]
                    quantity = int(row_list[REQUEST_QUANTITY_INDEX])

                    
                    product = products_dict[product_number]
                    name = product[PRODUCT_NAME_INDEX]
                    price = float(product[PRODUCT_PRICE_INDEX])

                    print(f"{name}: {quantity} @ {price:.2f}")

                    number_of_items += quantity
                    subtotal += quantity * price

        sales_tax = subtotal * SALES_TAX_RATE
        total = subtotal + sales_tax

        print(f"Number of Items: {number_of_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")
        print("Thank you for shopping at the Inkom Emporium.")

        
        print(time.ctime())

        
        now = datetime.now()

        new_year = datetime(now.year + 1, 1, 1)
        days_until_sale = (new_year.date() - now.date()).days
        print(f"Only {days_until_sale} days until our New Year's Sale begins on Jan 1!")

        return_by = (now + timedelta(days=30)).replace(
            hour=21, minute=0, second=0, microsecond=0)
        print("Return by: " + return_by.strftime("%a %b %d %Y at %I:%M %p"))

    except FileNotFoundError as not_found_err:
        print("Error: missing file")
        print(not_found_err)

    except PermissionError as perm_err:
        print("Error: cannot read file, permission denied")
        print(perm_err)

    except KeyError as key_err:
        print("Error: unknown product ID in the request.csv file")
        print(key_err)


if __name__ == "__main__":
    main()
