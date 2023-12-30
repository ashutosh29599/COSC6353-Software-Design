from discover_vendors import discover_vendors
from rental_price_finder import get_lowest_price


def display_vendors(vendors):
    print("\nThe following vendor(s) offer the best rates for you.")

    for vendor in vendors["vendors"]:
        print(
            f"{vendor}: ${vendors['total_price'] / 100:.2f} at the rate of ${vendors['price_per_day'] / 100:.2f} per day.")


if __name__ == "__main__":
    number_of_days = int(input("For how many days do you need a vehicle?\n"))

    try:
        vendors = get_lowest_price(number_of_days, discover_vendors())

        display_vendors(vendors)

    except Exception as exception:
        print(exception)
