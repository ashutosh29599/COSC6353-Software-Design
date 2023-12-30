from vendor_response import vendor_response


def get_price_response():
    return vendor_response(vendor_name="Budget", price_per_day=10000)
