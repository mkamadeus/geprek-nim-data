#!python3

import os
import json
import pathlib

MERGED_DIRECTORY = pathlib.Path("./.merged")

# merge students
students = []
for filename in os.listdir("./students"):
    with open(f"./students/{filename}", "r") as f:
        students.append(json.load(f))

with open(MERGED_DIRECTORY / "students.json", "w") as f:
    json.dump(students, f)

# merge faculties
faculties = {}
for filename in sorted(os.listdir("./faculties")):
    with open(f"./faculties/{filename}", "r") as f:
        faculty = json.load(f)
    faculties[faculty["id"]] = faculty

with open(MERGED_DIRECTORY / "faculties.json", "w") as f:
    json.dump(faculties, f, indent=2)

# merge majors
majors = {}
for filename in sorted(os.listdir("./majors")):
    with open(f"./majors/{filename}", "r") as f:
        major = json.load(f)
    majors[major["id"]] = major

with open(MERGED_DIRECTORY / "majors.json", "w") as f:
    json.dump(majors, f, indent=2)

# create mappings
mappings = {faculty: [] for faculty in faculties.keys()}
for major_id, major in majors.items():
    if major["faculty"] is not None:
        mappings[major["faculty"]].append(
            {"major_id": major["id"], "major_name": major["name"]}
        )

print(json.dumps(mappings, indent=2))
