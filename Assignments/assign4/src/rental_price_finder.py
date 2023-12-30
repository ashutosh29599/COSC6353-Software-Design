def fetch_data_from_a_service(rental_service):
    try:
        return rental_service()
    except:
        pass


def get_lowest_price(number_of_days, car_rental_services=[]):
    vendor_detail_from_services = list(filter(lambda detail: detail,
                                              ([fetch_data_from_a_service(car_rental_service) for car_rental_service in
                                                car_rental_services])))

    if not vendor_detail_from_services:
        raise Exception("No vendors available.")

    lowest_price = min(vendor_detail_from_services, key=lambda vendor_detail: vendor_detail["price_per_day"])[
        "price_per_day"]

    lowest_priced_vendors = [vendor_detail["vendor"] for vendor_detail in vendor_detail_from_services
                             if vendor_detail["price_per_day"] == lowest_price]

    return {"price_per_day": lowest_price, "total_price": lowest_price * number_of_days,
            "vendors": lowest_priced_vendors}
