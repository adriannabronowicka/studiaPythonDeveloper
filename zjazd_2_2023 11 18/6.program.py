# dana jest baza użytkowników z hasłami
# program pozwala na dodanie uzytkownika oraz zmianę hasła
# program sprawdza, czy nazwa uzytkownika dostępna
# program wymaga dwukrotnego wprowadzenia hasła przy dodawaniu nowego uzytkownika
# program pyta, czy zakończyć, czy kontynuować dodawanie uzytkowników

# w przypadku niedostepnej nazwy uzytkownika, program proponuje nazwę
# program sprawdza poziom skomplikowania hasła


"""user_name = input("Enter the user name: ")

if user_name not in user_dict.keys():
    print(f"The name is available")
    user_password = input("Enter the password: ")
    user_password1 = input("Enter the password: ")
    if user_password == user_password1:
        user_dict[user_name] = user_password
    else:
        print("Passwords are not the same")
else:
    print("User name is not available ")

print(user_dict)"""


from funckcje_do_programu import *

username = input("Enter the username: ")
while True:
    if is_user_available(username): # taki zapis oznacza to samo co if is_user_avilable(user_name) == True:
        add_user(username)
        print("The username has been added.")
        break
    else:
        print(f"I suggest the username: {suggest_username(username)}")
        decision = input("Do you want to enter the new username? (N) or do you want to use the suggested username (S): ")
        if decision == "S":
            username = suggest_username(username)
        else:
            username = input("Enter the username: ")

















