students = {
        "male": ["Ram", "Syam", "Mohan", "Raj"],
        "female": ["Rita", "Sita", "Geeta"]
        }

for key in students.keys():
    for name in students[key]:
        if "S" in name:
            print(name)
