#!python3

import os
import json
import pathlib

MERGED_DIRECTORY = pathlib.Path("./.merged")

# merge students
students = []
for filename in reversed(sorted(os.listdir("./students"))):
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
mappings = {
    faculty_id: {"faculty_name": faculties[faculty_id]["name"], "faculty_majors": {}}
    for faculty_id in faculties.keys()
}
mappings["unassigned"] = {"faculty_name": "N/A", "faculty_majors": {}}

for major_id, major in majors.items():
    if major["faculty"] is not None:
        mappings[major["faculty"]]["faculty_majors"].update(
            {major["id"]: major["name"]}
        )
    else:
        mappings["unassigned"]["faculty_majors"].update({major["id"]: major["name"]})

with open(MERGED_DIRECTORY / "directory.json", "w") as f:
    json.dump(mappings, f, indent=2)
