def check_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.islower() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in "!@#$%^&*()-_=+[{]}|;:'\",<.>/?`~" for c in password):
        strength += 1
    if strength == 5:git in
        return "Strong Password"
    elif strength >= 3:
        return "Medium Password"
    else:
        return "Weak Password"
password = input("Enter your password: ")
print(check_password_strength(password))
