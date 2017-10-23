while True:
    name = input("Name please: ")
    if name != 'joe':
        continue
    password = input("Hello Joe.. Enter your Password: ")
    if password.islower() == "swordfish":
        break
print("Access Granted")