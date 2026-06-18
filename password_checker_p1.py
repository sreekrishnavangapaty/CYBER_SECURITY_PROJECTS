# Password Strength Checker

def check_strength(pw):

    length = len(pw)

    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for char in pw:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        else:
            has_symbol = True

    score = 0

    if length >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1

    if score <= 2:
        return "Weak ❌"
    elif score <= 4:
        return "Moderate 👍"
    else:
        return "Strong ✅"


# MAIN
print("🔐 Password Analyzer")

pw = input("Enter password: ")

print("Result:", check_strength(pw))