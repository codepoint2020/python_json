import json


my_data = []

# Load existing data
with open("data.json", "r") as my_data:
    records = json.load(my_data)

# New dictionary to be added
new_entry = {
    "first_name": "Jerome",
    "last_name": "Morales"
}

# Append the new dictionary to the records list
records.append(new_entry)

# Save the updated records back to the file
with open("data.json", "w") as my_data:
    json.dump(records, my_data, indent=4)

# Print all records to verify
for record in records:
    print(f"{record['first_name']} {record['last_name']}")
