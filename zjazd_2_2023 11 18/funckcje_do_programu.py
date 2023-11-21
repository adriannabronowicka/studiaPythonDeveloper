user_dict = {
    'majki': '123',
    'Kamil': '124',
    'Kamil1': '234',
    'Kamil11': '765',
    'Kamil111': 'mama',
    'Kamil001': 'eee',
    'Rafcio': '876',
    'Betty': 'betty'
}

def is_user_available(user):
    if user not in user_dict.keys():
        print(f"The name {user} is available")
        return True
    else:
        print(f"User name {user} is not available ")
        return False

def add_user(user):
    while True:
        user_password = input("Enter the password: ")
        user_password1 = input("Confirm the password: ")
        if user_password == user_password1 and password_has_CAP_small_letter(user_password)\
                and password_has_digit(user_password1) and password_has_special_character(user_password1):
            user_dict[user] = user_password
            break
        else:
            print("Wrong password")

def suggest_username(user):
    return user + "1"

def password_has_CAP_small_letter(user_password):
    if user_password != user_password.lower() and user_password != user_password.upper():
        print("The password has lowercase and uppercase letters ")
        return True
    print("The password has not lowercase and uppercase letters")
    return False

def password_has_special_character(user_password):
    set_of_special_character = set(',./;[]\'\\"')
    if len(set(user_password) & set_of_special_character) > 0:
        return True
    return False

def password_has_digit(user_password):
    for char in user_password:
        return any(char.isdigit() for char in user_password)

