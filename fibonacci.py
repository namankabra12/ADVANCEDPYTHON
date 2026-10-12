import re

EMAIL_PATTERN = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+'


def find_emails(text):
    return re.findall(EMAIL_PATTERN, text)


def is_valid_email(candidate):
    if re.fullmatch(EMAIL_PATTERN, candidate):
        return True
    else:
        return False


sample_text = """Hello team,
For help write to support@examplecorp.com or sales.team@business-hub.co.in
You can also contact rahul_23@gmail.com
Our newsletter is newsletter+promo@my-site.org
Wrong ones are @missing-local.com and plain.text@
"""

emails = find_emails(sample_text)
print("Emails found:")
for email in emails:
    print(email)
print("Total emails found:", len(emails))

print()
test_list = [
    "support@examplecorp.com",
    "sales.team@business-hub.co.in",
    "rahul_23@gmail.com",
    "@missing-local.com",
    "plain.text@",
    "newsletter+promo@my-site.org",
    "info@123.com",
]

for item in test_list:
    if is_valid_email(item):
        print(item, "-> VALID")
    else:
        print(item, "-> INVALID")