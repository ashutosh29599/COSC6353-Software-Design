import sys
import unittest

from parameterized import parameterized

sys.path.append("src")

from rental_price_finder import get_lowest_price
from vendor_response import vendor_response


def create_mock_service(vendor, price_per_day):
    return lambda: vendor_response(vendor, price_per_day)


def rental_service_raises_exception():
    raise Exception("Failure!")


class RentalPriceFinderTest(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

    def test_get_lowest_price_when_there_is_no_vendors(self):
        self.assertRaisesRegex(Exception, "No vendors available.", get_lowest_price, 5)

    @parameterized.expand([
        (1, 10000, 10000),
        (5, 10000, 50000),
    ])
    def test_get_lowest_price_for_rental_when_there_is_one_vendor(self, number_of_days, price_per_day, total_price):
        vendor1_service_mock = create_mock_service("Vendor1", price_per_day)

        lowest_price_result = get_lowest_price(number_of_days, [vendor1_service_mock])
        self.assertEqual(lowest_price_result, {
            "vendors": ["Vendor1"],
            "price_per_day": price_per_day,
            "total_price": total_price,
        })

    @parameterized.expand([
        (1, [("Vendor1", 10000), ("Vendor2", 5000)], 5000, "Vendor2"),
        (1, [("Vendor1", 10000), ("Vendor2", 20000)], 10000, "Vendor1"),
        (1, [("Vendor1", 10000), ("Vendor2", 20000), ("Vendor3", 30000)], 10000, "Vendor1"),
        (1, [("Vendor1", 10000), ("Vendor2", 5000), ("Vendor3", 30000)], 5000, "Vendor2"),
        (1, [("Vendor1", 10000), ("Vendor2", 20000), ("Vendor3", 5000)], 5000, "Vendor3"),
    ])
    def test_get_lowest_price_when_there_are_multiple_vendors(self, number_of_days, vendor_mock_responses,
                                                              expected_lowest_price, expected_vendor):
        rental_service_mocks = [create_mock_service(vendor_mock_response[0], vendor_mock_response[1]) for
                                vendor_mock_response in vendor_mock_responses]

        lowest_price_result = get_lowest_price(number_of_days, rental_service_mocks)
        self.assertEqual(lowest_price_result, {
            "vendors": [expected_vendor],
            "price_per_day": expected_lowest_price,
            "total_price": expected_lowest_price,
        })

    def test_get_lowest_price_for_one_day_when_three_vendors_are_available_first_one_fails_request(self):
        vendor2_mock_service = create_mock_service("Vendor2", 20000)
        vendor3_mock_service = create_mock_service("Vendor3", 30000)
        rental_service_mocks = [rental_service_raises_exception, vendor2_mock_service, vendor3_mock_service]

        lowest_price_result = get_lowest_price(1, rental_service_mocks)
        self.assertEqual(lowest_price_result, {
            "vendors": ["Vendor2"],
            "price_per_day": 20000,
            "total_price": 20000,
        })

    def test_get_lowest_price_for_one_day_when_three_vendors_are_available_all_failing_request(self):
        rental_service_mocks = [rental_service_raises_exception] * 3

        self.assertRaisesRegex(Exception, "No vendors available.", get_lowest_price, 5, rental_service_mocks)

    def test_get_lowest_price_when_there_are_multiple_lowest_price_vendors(self):
        vendor1_mock_service = create_mock_service("Vendor1", 5000)
        vendor2_mock_service = create_mock_service("Vendor2", 20000)
        vendor3_mock_service = create_mock_service("Vendor3", 5000)

        rental_service_mocks = [vendor1_mock_service, vendor2_mock_service, vendor3_mock_service]

        lowest_price_result = get_lowest_price(1, rental_service_mocks)

        self.assertEqual(lowest_price_result, {
            "price_per_day": 5000,
            "total_price": 5000,
            "vendors": ["Vendor1", "Vendor3"],
        })
