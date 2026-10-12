import re

text = input("Enter some text: ")

pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

emails = re.findall(pattern, text)

if len(emails) == 0:
    print("No emails found")
else:
    print("Emails found:")
    for email in emails:
        print(email)
