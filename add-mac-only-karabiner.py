import json


INPUT_FILE = "colemak-dh.json"
OUTPUT_FILE = "colemak-dh-mac.json"

with open(INPUT_FILE, "r") as f:
    data = json.load(f)

    CONDITIONS_KEY = "conditions"
    CONDITIONS_VALUE = [
                    {
                        "type": "device_if",
                        "identifiers": [
                            { "vendor_id": 1452 },
                            { "vendor_id": 76 },
                            { "is_built_in_keyboard": True }
                        ]
                    }
                ]

    for manipulator in data["manipulators"]:
        manipulator[CONDITIONS_KEY] = CONDITIONS_VALUE

    with open(OUTPUT_FILE, "w") as f:
        json.dump(data, f, indent=4)