def email_slicer_split():
    email = input("enter your email address").split()

    try:
        username,domain = email.split('@')
        print(f"your username is:{username}")
        print(f"your domain is:{domain}")

    except ValueError:
        print("Invalid email format. please ensure it contains one '@' Symbol")
        
email_slicer_split()
