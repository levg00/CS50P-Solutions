import validators

def main():
    email = input("What's your email address? ").strip()
    if validators.email(email):
        print("Valid")
    else:
        print("Invalid")

main()
