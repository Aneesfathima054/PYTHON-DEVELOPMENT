def validate_email(email):
    if "@" not in email:
        return False
     parts = email.split("@")
    if len(parts) != 2:
        return False
    local, domain = parts
    if not local or not domain:
        return False
    if "." not in domain:
        return False
    if domain.startswith(".") or domain.endswith("."):
        return False
    return True
# Main program
email = input("Enter an email address: ")
if validate_email(email):
    print(f"{email} is a valid email.")
else:
    print(f"{email} is NOT a valid email.")
