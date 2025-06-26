import re

# Store credentials in a dictionary
vault = {}

# Function to check password strength using lambda and filter
def is_strong(password):
    checks = [
        lambda s: len(s) > 8,
        lambda s: any(c.islower() for c in s),
        lambda s: any(c.isupper() for c in s),
        lambda s: any(c.isdigit() for c in s),
        lambda s: any(c in "!@#$%^&*()-_+=" for c in s)
    ]
    passed = list(filter(lambda f: f(password), checks))
    return len(passed) == len(checks)

# Classify password strength
def classify_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()-_+=" for c in password)

    score = sum([has_upper, has_lower, has_digit, has_special])

    if length >= 12 and score == 4:
        return "Strong"
    elif length >= 8 and score >= 3:
        return "Medium"
    else:
        return "Weak"

# Main menu loop
while True:
    print("\n--- Password Vault Menu ---")
    print("1. Add New Credential")
    print("2. View Credentials")
    print("3. Delete a Credential")
    print("4. Analyze Password Strength")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        user = input("Enter username: ")
        password = input("Enter password: ")
        vault[user] = password
        print("Credential added successfully!")

    elif choice == '2':
        if vault:
            print("\nStored Credentials:")
            for user, pwd in vault.items():
                print(f"{user}: {pwd}")
        else:
            print("No credentials stored.")

    elif choice == '3':
        user = input("Enter the username to delete: ")
        if user in vault:
            del vault[user]
            print("Credential deleted.")
        else:
            print("Username not found.")

    elif choice == '4':
        print("\nPassword Strength Analysis:")
        for user, pwd in vault.items():
            strength = classify_strength(pwd)
            status = "Strong" if is_strong(pwd) else "Not Strong (by filter)"
            print(f"{user}: {strength} | {status}")

    elif choice == '5':
        print("Exiting Password Vault. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
