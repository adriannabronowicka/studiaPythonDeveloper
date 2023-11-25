"""
Mamy konta 3 osób:
Asi, Basi, i Pawła.
Każdy początkowo ma 100 PLN.
Napisz program obsługujący przelewy między tymi kontami.
Wykonaj 4 'przelewy', po czym wyprintuj stan konta każdej osoby:

asia has transferred 20 PLN to pawel
basia has transferred 50 PLN to pawel
pawel has transferred 60 PLN to asia
basia has transferred 30 PLN to asia
asia has 170 PLN
basia has 20 PLN
pawel has 110 PLN

(Można uprościć, że stan konta to int, olewamy istnienie groszy)
"""

account_asia = 100
account_basia = 100
account_pawel = 100

transaction_a_p = 20
transaction_b_p = 50
transaction_p_a = 60
transaction_b_a = 30

account_asia = account_asia - transaction_a_p + transaction_p_a + transaction_b_a
account_basia = account_basia - transaction_b_p - transaction_b_a
account_pawel = account_pawel + transaction_a_p + transaction_b_p - transaction_p_a

print(f"Asia has {account_asia}")
print(f"Basia has {account_basia}")
print(f"Paweł has {account_pawel}")

