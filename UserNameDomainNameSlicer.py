emailAddress = input("Enter your email address?: ").strip()

userName = emailAddress[:emailAddress.index("@")]

domainAddress = emailAddress[emailAddress.index("@") + 1:]

print("Your username is {} and your domain name is {}".format(userName, domainAddress))
