import string

def passwordStrengthCheck(password: str):
    lengthMeasure = 0
    hasLower = 0
    hasUpper = 0
    hasDigit = 0
    hasSymbol = 0

    if len(password) >= 8:
        lengthMeasure += 1
    if len(password) >= 12:
        lengthMeasure += 1

    for char in password:
        if char.islower():
            hasLower = 1
            continue
        elif char.isupper():
            hasUpper = 1
            continue
        elif char.isdigit():
            hasDigit = 1
            continue
        elif char in string.punctuation:
            hasSymbol = 1
    
    total = lengthMeasure + hasLower + hasUpper + hasDigit + hasSymbol

    if total < 3:
        strength = "Weak"
    elif total < 5:
        strength = "Moderate"
    else:
        strength = "Strong"

    suggestions = []
    if lengthMeasure < 2:
        suggestions.append("Increase length")
    if hasLower == 0:
        suggestions.append("Add lowercase characters")
    if hasUpper == 0:
        suggestions.append("Add uppercase characters")
    if hasDigit == 0:
        suggestions.append("Add numbers")
    if hasSymbol == 0:
        suggestions.append("Add symbols")
    
    return strength, suggestions

print("Enter a password to assess its strength: ", end="")
password = input()
strength, suggestions = passwordStrengthCheck(password)
print("\nThe given password's strength is: " + strength + "\n")
if len(suggestions) > 0:
    print("Suggestions to improve password strength: ")
    for suggestion in suggestions:
        print("- " + suggestion + " ")