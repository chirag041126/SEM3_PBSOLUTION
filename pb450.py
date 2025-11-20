
d = {
    "student0": 'Student@0',
    "student1": 'Student@11',
    "student2": 'Student@121',
    "student3": 'Student@052',
    "student4": 'Student@01278',
    "student5": 'Student@0125',
    "student6": 'Student@042',
    "student7": 'Student@07800',
    "student8": 'Student@012'
}
def check_password(p):
    if len(p) < 8 or len(p) > 15:
        return False

    upper = lower = digit = special = 0

    for ch in p:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
        elif ch.isdigit():
            digit += 1
        elif ch in "@$_":   
            special += 1
        else:
            return False   
        
    if upper >= 1 and lower >= 1 and digit >= 1 and special >= 1:
        return True
    return False

for i in range(3):
    uname = input("Enter username: ")
    pwd = input("Enter password: ")

    if uname in d and d[uname] == pwd:
        print("Login successful!")
        break
    else:
        print("Enter correct password and username")
else:
    print("Try after 24h")
    exit()

for i in range(3):
    new_pwd = input("Set new password: ")

    if check_password(new_pwd):
        d[uname] = new_pwd
        print("Password updated successfully!")
        break
    else:
        print("Follow the password format")

else:
    print("Follow the password format")
    print("Try after 24h")
    exit()

print("\nUpdated Dictionary:")
print(d)

sorted_items = sorted(d.items(), key=lambda x: len(x[1]))

print("\nUsername and password sorted by password length:")
for user, pwd in sorted_items:
    print(user, ":", pwd)
