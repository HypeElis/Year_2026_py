# Validate user input exercise


error1 = "username is no longer than 12 character."
error2 = "username must not contain spaces."
error3 = "username must not contain digits."
user = input("Enter your username: ")


if len(user) > 12:
    print(error1)
elif " " in user:
    print(error2)
elif not user.isalpha():
    print(error3)   
else:
    print(f"Hello {user}")


