
#  Email Slicer

email = input("Enter your Email: ").strip()

username=email[:email.index("@")]

domain_name=email[email.index("@")+1:]

prop1=domain_name.upper()

main=(f"Username:{username} and your domain:{prop1}")

print(main)
