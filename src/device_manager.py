import ipaddress

from storage import Storage
from validator import ConfigValidator


class DeviceManager:

    def __init__(self, storage):

        self.storage = storage
        self.validator = ConfigValidator()

        data = self.storage.load_data()

        self.devices = {
            device["id"]: device
            for device in data["devices"]
        }

    def _save(self):

        data = {
            "devices": list(self.devices.values())
        }

        self.storage.save_data(data)

    def _validate_ip(self, ip_address):

        try:
            ipaddress.ip_address(ip_address)
            return True

        except ValueError:
            return False

    def _validate_device_id(self, device_id):

        return bool(device_id.strip())

    def _validate_hostname(self, hostname):

        return bool(hostname.strip())

    # -------------------------
    # CREATE
    # -------------------------

    def create_device(self, device):

        device_id = device["id"]

        if not self._validate_device_id(device_id):
            return False, "Device ID cannot be empty."

        if not self._validate_hostname(device["hostname"]):
            return False, "Hostname cannot be empty."

        if not self._validate_ip(device["management-ip"]):
            return False, "Invalid management IP address."

        if device_id in self.devices:
            return False, f"Device '{device_id}' already exists."

        configuration = {
            "network-device:devices": {
                "device": [device]
            }
        }

        valid, message = self.validator.validate(
            configuration
        )

        if not valid:
            return False, message

        self.devices[device_id] = device

        self._save()

        return True, f"Device '{device_id}' created successfully."

    # -------------------------
    # READ
    # -------------------------

    def get_device(self, device_id):

        return self.devices.get(device_id)

    def list_devices(self):

        return list(self.devices.values())

    # -------------------------
    # UPDATE
    # -------------------------

    def update_device(self, device_id, updated_data):

        if device_id not in self.devices:
            return False, f"Device '{device_id}' not found."

        updated_device = self.devices[device_id].copy()

        updated_device.update(updated_data)

        if not self._validate_hostname(
            updated_device["hostname"]
        ):
            return False, "Hostname cannot be empty."

        if not self._validate_ip(
            updated_device["management-ip"]
        ):
            return False, "Invalid management IP address."

        configuration = {
            "network-device:devices": {
                "device": [updated_device]
            }
        }

        valid, message = self.validator.validate(
            configuration
        )

        if not valid:
            return False, message

        self.devices[device_id] = updated_device

        self._save()

        return True, f"Device '{device_id}' updated successfully."

    # -------------------------
    # DELETE
    # -------------------------

    def delete_device(self, device_id):

        if device_id not in self.devices:
            return False, f"Device '{device_id}' not found."

        del self.devices[device_id]

        self._save()

        return True, f"Device '{device_id}' deleted successfully."