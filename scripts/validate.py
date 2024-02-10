import os
import json
import jsonschema

with open("./schemas/faculty.json", "r") as f:
    faculty_schema = json.load(f)

with open("./schemas/major.json", "r") as f:
    major_schema = json.load(f)

for filename in sorted(os.listdir("./faculties")):
    with open(f"./faculties/{filename}", "r") as f:
        faculty = json.load(f)
    try:
        jsonschema.validate(faculty, faculty_schema)
    except:
        print(f"Error validating {filename}")

print("Faculties validation complete")

for filename in sorted(os.listdir("./majors")):
    with open(f"./majors/{filename}", "r") as f:
        major = json.load(f)
    try:
        jsonschema.validate(major, major_schema)
    except:
        print(f"Error validating {filename}")

print("Majors validation complete")
