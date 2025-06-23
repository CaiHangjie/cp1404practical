"""
Email and Name Collector
"""

def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirm = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirm != "" and confirm != "y":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} <{email}>")


def get_name_from_email(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(part.capitalize() for part in parts)
    return name


if __name__ == '__main__':
    main()
