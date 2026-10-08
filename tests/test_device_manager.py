import os
import tempfile
import unittest

import sys

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../src")
    )
)

from device_manager import DeviceManager
from storage import Storage


class TestDeviceManager(unittest.TestCase):

    def setUp(self):

        self.temp_file = tempfile.NamedTemporaryFile(
            delete=False
        )

        self.temp_file.close()

        with open(self.temp_file.name, "w") as file:
            file.write('{"devices": []}')

        storage = Storage(self.temp_file.name)

        self.manager = DeviceManager(storage)

    def tearDown(self):

        os.remove(self.temp_file.name)

    def create_test_device(self):

        return {
            "id": "dev001",
            "hostname": "Router-1",
            "management-ip": "192.168.1.10",
            "vendor": "Cisco",
            "device-type": "router"
        }

    def test_create_device(self):

        device = self.create_test_device()

        success, message = self.manager.create_device(
            device
        )

        self.assertTrue(success)
        self.assertIn("created successfully", message)

    def test_get_device(self):

        device = self.create_test_device()

        self.manager.create_device(device)

        result = self.manager.get_device("dev001")

        self.assertIsNotNone(result)
        self.assertEqual(
            result["hostname"],
            "Router-1"
        )

    def test_update_device(self):

        device = self.create_test_device()

        self.manager.create_device(device)

        success, message = self.manager.update_device(
            "dev001",
            {
                "hostname": "Main-Router"
            }
        )

        self.assertTrue(success)

        result = self.manager.get_device("dev001")

        self.assertEqual(
            result["hostname"],
            "Main-Router"
        )

    def test_delete_device(self):

        device = self.create_test_device()

        self.manager.create_device(device)

        success, message = self.manager.delete_device(
            "dev001"
        )

        self.assertTrue(success)

        result = self.manager.get_device("dev001")

        self.assertIsNone(result)

    def test_duplicate_device(self):

        device = self.create_test_device()

        self.manager.create_device(device)

        success, message = self.manager.create_device(
            device
        )

        self.assertFalse(success)
        self.assertIn("already exists", message)

    def test_invalid_ip(self):

        device = self.create_test_device()

        device["management-ip"] = "invalid-ip"

        success, message = self.manager.create_device(
            device
        )

        self.assertFalse(success)
        self.assertIn("Invalid management IP", message)

    def test_nonexistent_device(self):

        result = self.manager.get_device("dev999")

        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()