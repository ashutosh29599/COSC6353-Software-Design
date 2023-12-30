import os
import shutil
import sys
import unittest

sys.path.append("src")
from discover_vendors import discover_vendors


class DiscoverVendorsFinderTest(unittest.TestCase):
    def test_discover_vendors(self, expected_vendor_modules=["avis", "budget", "dollar"]):
        actual_vendor_modules = [vendor.__module__ for vendor in discover_vendors()]

        assert all(item in actual_vendor_modules for item in expected_vendor_modules)

    def test_add_a_vendor_and_check_and_then_remove_a_vendor_and_check(self):
        def add_a_vendor(vendor_name):
            shutil.copy("src/vendors/avis.py", f"src/vendors/{vendor_name}.py")

        def remove_a_vendor(vendor_name):
            try:
                os.remove(f"src/vendors/{vendor_name}.py")
            except:
                pass

        add_a_vendor("shinchan")
        self.test_discover_vendors(expected_vendor_modules=["avis", "budget", "dollar", "shinchan"])

        remove_a_vendor("shinchan")
        self.test_discover_vendors(expected_vendor_modules=["avis", "budget", "dollar"])
