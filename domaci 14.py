import re

email = "toma@gmail.com"

email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.match(email_pattern, email):
    print("Jeste email")
else:
    print("Nije email")

