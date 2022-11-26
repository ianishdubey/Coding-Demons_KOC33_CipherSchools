# EMAIL SLICER Project

#to use this email slicer for infinite times
while True:
    #Get user email address
    Email = input("Enter your Email: ").strip()

    #Slice out the user name
    Username = Email[:Email.index("@")]

    #Slice out the Domain Name
    domain_name = Email[Email.index("@")+1:]
    #to get Domain name in upper case
    Domain = domain_name.upper()

    #Format massage
    Main = (f"Username:{Username} and your domain:{Domain}")

    #Display output massage
    print(Main)
