# Create dictionary
d = {"name": "Saanvi", "age": 18}
print("Dictionary:", d)

# Access
print("Name:", d["name"])

# Update
d["age"] = 19
print("Updated:", d)

# Remove element
d.pop("age")
print("After removal:", d)

# Merge dictionaries
d2 = {"city": "Pune"}
d.update(d2)
print("Merged:", d)
