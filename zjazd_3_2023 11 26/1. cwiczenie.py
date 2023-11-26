"""
Napisz funkcję przyjmującą użytkownika (np. remigiusz) i zwracającą
stan konta.
"""

NAMES = {
    2356354: "eugeniusz",
    8936743: "tymoteusz",
    2389654: "remigiusz"
}

BALANCE = {
    2356354: 3200,
    8936743: 5100,
    2389654: 60
}
"""
def accounts(names, balance):
    for number, name in names.items():
        if number in balance:
            print(f"{name} has {balance[number]}")

accounts(NAMES, BALANCE)"""
def get_username_balance(searched_username: str) -> int:
    for user_id, username in NAMES.items():
        if username == searched_username:
            return BALANCE[user_id]


user_name = input("Enter the name: ")
balance = get_username_balance(user_name)
print(f"The user {user_name} has {balance}.")
