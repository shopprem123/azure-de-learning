# day01_variables.py
# Python equivalent of SQL : SELECT 'Priya' AS name, 15 AS years_exp

name = "Priya"
years_exp = 15
is_manager = True

print("----- EXAMINING COMPONENT TYPES -----")
print(name)
print(years_exp)
print(f"Data type of yers_exp variable: {type(years_exp)}")
print(f"Data type of name variable: {type(name)}")
print(f"Data type of is_manager variable: {type(is_manager)}")

print("\n------ RUNNING CONDITIONAL BRANCH (CASE WHEN) -----")

#SQL : CASE WHEN years_exp > 10 THEN 'Senior' ELSE 'Junior' END
if years_exp > 10:
    print(name + " is a senior professional")
else:
    print(name + " is building expertise")

print("\n------ MULTI BRANCH CONDITION LOGIC -----")

#SQL : CASE WHEN years_exp > 10 THEN 'Senior' WHEN years_exp > 5 THEN 'Mid-level' ELSE 'Junior' END
if years_exp > 10:
    level = "Senior"
elif years_exp > 5:
    level = "Mid-level"
else:
    level = "Junior"

print(f"Result mapping assignment: {name} is classified as a {level}.")
