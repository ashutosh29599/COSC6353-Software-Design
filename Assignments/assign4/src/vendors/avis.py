from random import random

from vendor_response import vendor_response


def get_price_response():
    return vendor_response(vendor_name="Avis", price_per_day=int(random() * 100000))
