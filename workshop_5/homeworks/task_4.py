# ==============================
# Task 4: Contact manager
# ==============================
# Build a small contact manager where each contact is a dictionary
# with keys: name, phone, email.
# Store them all in a list called `contacts`. Write these functions:
#   - add_contact(contacts, name, phone, email)
#   - find_by_name(contacts, name) -> returns the contact dict or None
#   - all_emails(contacts) -> returns a list of every email address
#
# Add 3 contacts and test each function.

contacts = []




def add_contact(contacts, name, phone, email):
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })

def find_by_name(contacts, name):
    for contact in contacts:
        if contact["name"] == name:
            return contact
    return None


def all_emails(contacts):
    emails = []
    for contact in contacts:
        emails.append(contact["email"])

    return emails



add_contact(contacts, "Nick", 100, "nick@gmail.com")
add_contact(contacts, "Valery", 200, "Valery@gmail.com")

print(contacts)
print(find_by_name(contacts, "Nick"))
print(find_by_name(contacts, "Mike"))

print(all_emails(contacts))
