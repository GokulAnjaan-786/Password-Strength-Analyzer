from checker import check_strength
from hash_generator import generate_hash

password = input("Enter your password: ")

score, feedback = check_strength(password)

print("\nPassword Score:", score, "/10")

if score <= 4:
    print("Strength: Weak")

elif score <= 8:
    print("Strength: Strong")

else:
    print("Strength: Very Strong")

print("\nSuggestions:")

for item in feedback:
    print("-", item)

hashed_password = generate_hash(password)

print("\nSHA-256 Hash:")
print(hashed_password)