from device_manager import DeviceManager
from storage import Storage


def display_menu():
    print("\n" + "=" * 50)
    print(" YANG Network Device Configuration Manager")
    print("=" * 50)

    print("1. Create Device")
    print("2. List Devices")
    print("3. Get Device")
    print("4. Update Device")
    print("5. Delete Device")
    print("6. Exit")


def create_device(manager):

    print("\n--- Create Device ---")

    device_id = input("Enter device ID: ")
    hostname = input("Enter hostname: ")
    management_ip = input("Enter management IP: ")
    vendor = input("Enter vendor: ")
    device_type = input("Enter device type: ")

    device = {
        "id": device_id,
        "hostname": hostname,
        "management-ip": management_ip,
        "vendor": vendor,
        "device-type": device_type
    }

    success, message = manager.create_device(device)

    print(message)


def list_devices(manager):

    print("\n--- Device List ---")

    devices = manager.list_devices()

    if not devices:
        print("No devices found.")
        return

    for device in devices:
        print(
            f"ID: {device['id']} | "
            f"Hostname: {device['hostname']} | "
            f"IP: {device['management-ip']} | "
            f"Vendor: {device['vendor']} | "
            f"Type: {device['device-type']}"
        )


def get_device(manager):

    print("\n--- Get Device ---")

    device_id = input("Enter device ID: ")

    device = manager.get_device(device_id)

    if device is None:
        print(f"Device '{device_id}' not found.")
        return

    print("\nDevice Information")
    print("------------------")
    print(f"ID:             {device['id']}")
    print(f"Hostname:       {device['hostname']}")
    print(f"Management IP:  {device['management-ip']}")
    print(f"Vendor:         {device['vendor']}")
    print(f"Device Type:    {device['device-type']}")


def update_device(manager):

    print("\n--- Update Device ---")

    device_id = input("Enter device ID: ")

    device = manager.get_device(device_id)

    if device is None:
        print(f"Device '{device_id}' not found.")
        return

    print("\nCurrent configuration:")
    print(f"Hostname: {device['hostname']}")
    print(f"IP:       {device['management-ip']}")
    print(f"Vendor:   {device['vendor']}")
    print(f"Type:     {device['device-type']}")

    print("\nEnter new values.")
    print("Press Enter to keep the current value.")

    hostname = input(f"Hostname [{device['hostname']}]: ")

    management_ip = input(
        f"Management IP [{device['management-ip']}]: "
    )

    vendor = input(f"Vendor [{device['vendor']}]: ")

    device_type = input(
        f"Device Type [{device['device-type']}]: "
    )

    updated_data = {}

    if hostname:
        updated_data["hostname"] = hostname

    if management_ip:
        updated_data["management-ip"] = management_ip

    if vendor:
        updated_data["vendor"] = vendor

    if device_type:
        updated_data["device-type"] = device_type

    success, message = manager.update_device(
        device_id,
        updated_data
    )

    print(message)


def delete_device(manager):

    print("\n--- Delete Device ---")

    device_id = input("Enter device ID: ")

    success, message = manager.delete_device(device_id)

    print(message)


def main():

    storage = Storage("data/devices.json")

    manager = DeviceManager(storage)

    while True:

        display_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":
            create_device(manager)

        elif choice == "2":
            list_devices(manager)

        elif choice == "3":
            get_device(manager)

        elif choice == "4":
            update_device(manager)

        elif choice == "5":
            delete_device(manager)

        elif choice == "6":
            print("\nExiting application...")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()