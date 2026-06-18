# Phishing Detector

def check_phishing(msg):

    msg = msg.lower()
    warnings = []

    # simple keyword list
    keywords = ["urgent", "otp", "verify", "click", "bank", "login"]

    for word in keywords:
        if word in msg:
            warnings.append(f"⚠ Found keyword: {word}")

    # link check
    if "http" in msg:
        warnings.append("⚠ Link detected")

    # email check
    if "@" in msg:
        warnings.append("⚠ Email detected (verify sender)")

    return warnings


# MAIN
print("🔍 Simple Phishing Checker")

text = input("Enter message: ")

result = check_phishing(text)

print("\nResult:")

if len(result) == 0:
    print("Safe ✅")
else:
    print("Suspicious ❌")
    for r in result:
        print(r)