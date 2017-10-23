while True:
    name = input("Name please: ")
    if name != 'joe':
        continue
    password = input("Hello Joe.. Enter your Password: ")
    if password.islower() != "swordfish":
        continue   # Back to input of name
print("Access Granted")