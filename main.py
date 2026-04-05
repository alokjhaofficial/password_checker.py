password = input("Enter your password: ")

length = len(password) >= 8
upper = any(c.isupper() for c in password)
lower = any(c.islower() for c in password)
digit = any(c.isdigit() for c in password)
special = any(not c.isalnum() for c in password)

score = sum([length, upper, lower, digit, special])

if score == 5:
    print("Strong Password ✅")
elif score >= 3:
    print("Medium Password ⚠️")
else:
    print("Weak Password ❌")