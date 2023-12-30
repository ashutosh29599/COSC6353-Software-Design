from random import random

from vendor_response import vendor_response


def get_price_response():
    random_number = int(random() * 100)

    if random_number % 2 == 0:
        return vendor_response(vendor_name="Dollar", price_per_day=10000)

    raise Exception("Failure")
