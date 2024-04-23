import json


records = []

with open("data.json", "r") as my_data:
    records = json.load(my_data)

new_entry = {
        "first_name": "Jerome",
        "last_name": "Morales"
}

records.append(new_entry)


for record in records:
    print(f"{record['first_name']} {record['last_name']}")



