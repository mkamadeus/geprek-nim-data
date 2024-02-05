#!python3

import json

with open("./kode_jurusan.json", "r") as f:
    codes = json.load(f)

with open("./list_jurusan.json", "r") as f:
    majors = json.load(f)

reversed_codes = {v: k for k, v in codes.items()}

for major_id, code in reversed_codes.items():
    data = {
        "id": str(major_id),
        "faculty": None,
        "short_name": code,
        "name": majors[major_id],
        "locales": {"en": {"name": None}},
    }

    print(major_id)
    print(data)

    with open(f"./majors/{major_id}.json", "w") as f:
        json.dump(data, f, indent=2)
