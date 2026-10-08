# YANG Network Device Configuration Manager

A beginner-level **Network Device Configuration Manager** implemented in Python using a **YANG data model**.

The project demonstrates how YANG can be used to define the structure and constraints of network device configuration, while Python provides CRUD operations, local JSON storage, validation, and a command-line interface.

---

## 1. Project Overview

Network devices such as routers, switches, and firewalls contain structured configuration information.

This project models that configuration using **YANG** and provides a simple Python application to manage it.

The application supports:

- Create network devices
- Read network device configuration
- Update network devices
- Delete network devices
- Store configuration in JSON
- Validate configuration using a YANG model
- Validate management IP addresses
- Restrict device types using YANG enumeration
- Handle invalid and duplicate devices
- Run automated unit tests

This project is intentionally designed as a **first YANG implementation** and therefore does not communicate with real network devices.

---

## 2. Project Goals

The main goals are to understand:

1. What YANG is
2. How YANG models network configuration
3. How `module`, `container`, `list`, `key`, and `leaf` work
4. How Python can implement CRUD operations over a YANG-modeled configuration
5. How configuration can be stored locally
6. How configuration can be validated against a YANG schema
7. How to structure a small configuration-management application

---

## 3. Architecture

```text
                         User
                          |
                          v
                  +---------------+
                  |    main.py    |
                  |   CLI Layer   |
                  +-------+-------+
                          |
                          v
                 +-------------------+
                 |  DeviceManager    |
                 |                   |
                 | CRUD Operations   |
                 +---------+---------+
                           |
                 +---------+---------+
                 |                   |
                 v                   v
        +----------------+   +---------------+
        | ConfigValidator|   |    Storage    |
        |                |   |               |
        | YANG Validation|   | JSON Storage  |
        +-------+--------+   +-------+-------+
                |                    |
                v                    v
       network-device.yang      devices.json
```

---

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| YANG | Network configuration modeling |
| pyang | YANG model validation |
| Yangson | YANG data validation |
| JSON | Local configuration persistence |
| unittest | Automated testing |
| Git | Version control |

---

## 5. Features

### Device Management

The application supports complete CRUD operations.

#### Create

Add a new network device:

- Device ID
- Hostname
- Management IP
- Vendor
- Device Type

#### Read

View:

- All devices
- Individual device information

#### Update

Modify existing device configuration.

#### Delete

Remove a device from the configuration.

---

## 6. YANG Model

The project uses the following YANG model:

```text
module: network-device
  +--rw devices
     +--rw device* [id]
        +--rw id               string
        +--rw hostname         string
        +--rw management-ip    ip-address
        +--rw vendor           string
        +--rw device-type      enumeration
```

The model defines:

```text
devices
└── device
    ├── id
    ├── hostname
    ├── management-ip
    ├── vendor
    └── device-type
```

---

## 7. YANG Concepts Used

### Module

The complete model is contained inside:

```yang
module network-device {
```

The module represents the YANG model for our application.

### Namespace

```yang
namespace "urn:example:network-device";
```

The namespace uniquely identifies the YANG model.

### Prefix

```yang
prefix "nd";
```

Provides a short identifier for the module.

### Container

```yang
container devices {
```

Groups related configuration.

### List

```yang
list device {
```

Allows multiple network devices to exist.

### Key

```yang
key "id";
```

Makes the device ID the unique identifier for each device.

### Leaf

For example:

```yang
leaf hostname {
    type string;
    mandatory true;
}
```

A leaf represents an individual configuration value.

### Enumeration

The device type is restricted to:

```yang
type enumeration {
    enum router;
    enum switch;
    enum firewall;
}
```

Therefore:

```text
router     ✓
switch     ✓
firewall   ✓
laptop     ✗
server     ✗
```

---

## 8. Example YANG Model

The current model is:

```yang
module network-device {

    namespace "urn:example:network-device";
    prefix "nd";

    organization
        "Beginner YANG Network Device Manager";

    description
        "A simple YANG model for managing network devices.";

    container devices {

        list device {

            key "id";

            leaf id {
                type string;
                mandatory true;
            }

            leaf hostname {
                type string;
                mandatory true;
            }

            leaf management-ip {
                type string;
                mandatory true;
            }

            leaf vendor {
                type string;
                mandatory true;
            }

            leaf device-type {
                type enumeration {
                    enum router;
                    enum switch;
                    enum firewall;
                }

                mandatory true;
            }
        }
    }
}
```

> Note: If the model is extended to use `ietf-inet-types`, `management-ip` can instead use the YANG `inet:ip-address` type.

---

## 9. Example Configuration

A valid device configuration looks like:

```json
{
    "id": "dev001",
    "hostname": "Router-1",
    "management-ip": "192.168.1.10",
    "vendor": "Cisco",
    "device-type": "router"
}
```

Multiple devices can be stored:

```json
{
    "devices": [
        {
            "id": "dev001",
            "hostname": "Router-1",
            "management-ip": "192.168.1.10",
            "vendor": "Cisco",
            "device-type": "router"
        },
        {
            "id": "dev002",
            "hostname": "Switch-1",
            "management-ip": "192.168.1.20",
            "vendor": "Cisco",
            "device-type": "switch"
        }
    ]
}
```

---

## 10. Project Structure

```text
YangConfigManager/
│
├── yang/
│   ├── network-device.yang
│   └── yang-library.json
│
├── src/
│   ├── main.py
│   ├── device_manager.py
│   ├── storage.py
│   └── validator.py
│
├── data/
│   └── devices.json
│
├── tests/
│   └── test_device_manager.py
│
├── venv/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 11. File Responsibilities

### `main.py`

Provides the command-line interface.

Responsibilities:

- Display menu
- Read user input
- Call CRUD operations
- Display results

### `device_manager.py`

Contains the main device-management logic.

Responsibilities:

- Create device
- Read device
- Update device
- Delete device
- Validate input
- Call YANG validator
- Save configuration

### `storage.py`

Handles JSON persistence.

Responsibilities:

- Load configuration from JSON
- Save configuration to JSON

### `validator.py`

Handles YANG-based validation.

Responsibilities:

- Load the YANG data model
- Convert configuration into a YANG data tree
- Validate configuration

### `network-device.yang`

Defines the network device configuration schema.

### `yang-library.json`

Describes the YANG module used by the validation system.

### `devices.json`

Stores the locally persisted network-device configuration.

### `test_device_manager.py`

Contains automated unit tests for the device-management functionality.

---

## 12. Installation

### Step 1: Clone or create the project

```bash
git clone <repository-url>
cd YangConfigManager
```

Or create the project manually.

### Step 2: Create a virtual environment

```bash
python3 -m venv venv
```

### Step 3: Activate the virtual environment

macOS/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Step 4: Install dependencies

```bash
pip install -r requirements.txt
```

---

## 13. Dependencies

`requirements.txt`:

```text
pyang
yangson
```

Python's built-in modules are also used:

```text
json
os
ipaddress
unittest
tempfile
```

These do not need to be installed separately.

---

## 14. Validate the YANG Model

From the project root:

```bash
pyang yang/network-device.yang
```

If there are no errors, the YANG model is syntactically valid.

To view the model as a tree:

```bash
pyang -f tree yang/network-device.yang
```

Example:

```text
module: network-device
  +--rw devices
     +--rw device* [id]
        +--rw id               string
        +--rw hostname         string
        +--rw management-ip    string
        +--rw vendor           string
        +--rw device-type      enumeration
```

---

## 15. Running the Application

Run:

```bash
python src/main.py
```

The application displays:

```text
==================================================
 YANG Network Device Configuration Manager
==================================================
1. Create Device
2. List Devices
3. Get Device
4. Update Device
5. Delete Device
6. Exit

Enter your choice:
```

---

## 16. CRUD Examples

### Create

Select:

```text
1
```

Enter:

```text
Enter device ID: dev001
Enter hostname: Router-1
Enter management IP: 192.168.1.10
Enter vendor: Cisco
Enter device type: router
```

Output:

```text
Device 'dev001' created successfully.
```

### Read

Select:

```text
2
```

Output:

```text
--- Device List ---

ID: dev001 | Hostname: Router-1 | IP: 192.168.1.10 | Vendor: Cisco | Type: router
```

To retrieve a specific device, select:

```text
3
```

Then:

```text
Enter device ID: dev001
```

### Update

Select:

```text
4
```

Enter:

```text
Enter device ID: dev001
```

Then provide the new value:

```text
Hostname [Router-1]: Main-Router
```

Press Enter on other fields to keep their existing values.

### Delete

Select:

```text
5
```

Then:

```text
Enter device ID: dev001
```

Output:

```text
Device 'dev001' deleted successfully.
```

---

## 17. Validation

The application performs validation at multiple levels.

### Device ID

Cannot be empty.

```text
""       → Invalid
"dev001" → Valid
```

### Hostname

Cannot be empty.

```text
""          → Invalid
"Router-1"  → Valid
```

### Management IP

Python's `ipaddress` module is used to check the IP address.

```text
192.168.1.10 → Valid
10.0.0.1     → Valid
invalid-ip   → Invalid
```

### Device Type

The YANG enumeration allows:

```text
router
switch
firewall
```

Other values are rejected by YANG validation.

---

## 18. JSON Persistence

Configuration is stored in:

```text
data/devices.json
```

This means configuration remains available after the application exits.

The flow is:

```text
Application starts
       |
       v
Read devices.json
       |
       v
Load configuration
       |
       v
Perform CRUD operation
       |
       v
Save devices.json
```

Without JSON persistence, all configuration would disappear when the Python program terminates.

---

## 19. YANG Validation Flow

When a device is created or updated:

```text
User Input
    |
    v
Python Dictionary
    |
    v
Build YANG-compatible structure
    |
    v
Yangson
    |
    v
YANG Schema
    |
    +---- Valid ------> Save Configuration
    |
    +---- Invalid -----> Reject Configuration
```

This ensures that configuration isn't simply stored blindly.

---

## 20. Unit Testing

The project uses Python's built-in `unittest` framework.

Run all tests:

```bash
python -m unittest discover -s tests -v
```

The tests cover:

- Create device
- Get device
- Update device
- Delete device
- Duplicate device
- Invalid IP address
- Nonexistent device

Example:

```text
test_create_device ... ok
test_delete_device ... ok
test_duplicate_device ... ok
test_get_device ... ok
test_invalid_ip ... ok
test_nonexistent_device ... ok
test_update_device ... ok

----------------------------------------------------------------------
Ran 7 tests

OK
```

---

## 21. Design Principles

The project follows a simple separation of responsibilities.

### CLI Layer

```text
main.py
```

Handles user interaction.

### Business Logic Layer

```text
device_manager.py
```

Handles CRUD and configuration logic.

### Validation Layer

```text
validator.py
```

Handles YANG-based validation.

### Storage Layer

```text
storage.py
```

Handles JSON persistence.

### Data Model

```text
network-device.yang
```

Defines the configuration schema.

This separation makes the project easier to understand and extend.

---

## 22. Development Phases

The project was developed incrementally.

### Phase 1 — Project Setup

Created:

- Python project
- Virtual environment
- CLI skeleton
- Basic project structure

### Phase 2 — YANG Model

Created the `network-device.yang` model and learned:

- Module
- Namespace
- Prefix
- Container
- List
- Key
- Leaf
- Type
- Mandatory fields

### Phase 3 — CRUD

Implemented:

- Create
- Read
- Update
- Delete

using Python dictionaries.

### Phase 4 — JSON Persistence

Added:

```text
storage.py
devices.json
```

so configuration survives application restarts.

### Phase 5 — YANG Validation

Integrated YANG-aware validation using Yangson.

Also added:

- Device-type enumeration
- Configuration validation
- Validation before create/update

### Phase 6 — Testing & Error Handling

Added:

- Input validation
- IP validation
- Duplicate detection
- Missing-device handling
- Unit tests
- Final documentation

---

## 23. Why YANG?

YANG provides a structured way to model network configuration.

Instead of defining all configuration rules directly inside Python, the schema can be described using YANG.

For example:

```yang
leaf device-type {
    type enumeration {
        enum router;
        enum switch;
        enum firewall;
    }
}
```

The Python application can then validate configuration against this model.

This separates:

```text
Configuration Schema
        |
        v
      YANG
```

from:

```text
Application Logic
        |
        v
      Python
```

---

## 24. Why JSON?

JSON is used only for **local persistence** in this project.

It allows the application to save configuration without requiring a database.

JSON was selected because it is:

- Simple
- Human-readable
- Easy to manipulate with Python
- Suitable for a beginner-level project

---

## 25. Why NETCONF Is Not Used

NETCONF is intentionally **not included**.

The purpose of this project is to understand the fundamentals of YANG modeling and configuration management without introducing the additional complexity of:

- SSH
- NETCONF sessions
- NETCONF RPCs
- Real network devices
- Candidate/running datastores
- Commit operations

A future version could use NETCONF to send validated configuration to actual network devices.

---

## 26. Limitations

This is an educational project and has several limitations.

- It does not communicate with real network devices.
- It does not use NETCONF or RESTCONF.
- JSON is used instead of a production datastore.
- Authentication is not implemented.
- Multiple users are not supported.
- There is no network-device synchronization.
- There is no configuration rollback mechanism.
- The YANG model is intentionally small.
- The CLI is designed for learning rather than production use.

---

## 27. Possible Future Improvements

The project can be extended later with:

```text
NETCONF
   ↓
RESTCONF
   ↓
Real network devices
   ↓
SSH authentication
   ↓
Multiple YANG modules
   ↓
Interface configuration
   ↓
Routing configuration
   ↓
Configuration rollback
   ↓
Web interface
   ↓
Database
```

Possible future YANG modules could model:

- Interfaces
- VLANs
- Routing
- DNS
- System configuration
- Firewall rules

---

## 28. Interview Explanation

A concise explanation of the project:

> I developed a beginner-level Network Device Configuration Manager using Python and YANG. I created a YANG model defining the structure of network devices, including device ID, hostname, management IP, vendor, and device type. The Python application provides CRUD operations and stores the configuration locally in JSON. Before creating or updating a device, the configuration is validated against the YANG model. I also implemented Python-level validation and unit tests. I intentionally excluded NETCONF because the main objective was to understand YANG modeling and configuration management fundamentals.

### Why YANG?

> YANG provides a standardized way to define the structure and constraints of network configuration. It separates the configuration schema from the application logic.

### Why Python?

> Python provides a simple environment for implementing the CRUD operations, storage, validation, and CLI.

### Why JSON?

> JSON provides simple local persistence without introducing the complexity of a database.

### Why no NETCONF?

> This is my first YANG project, so I focused on understanding YANG modeling and configuration validation first. NETCONF can be added later for communicating with actual network devices.

---

## 29. License

This project is intended for educational and learning purposes.
