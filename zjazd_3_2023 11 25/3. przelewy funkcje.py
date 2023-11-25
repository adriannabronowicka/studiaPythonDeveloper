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

Asia ma konto w banku "GlupiBank" i za każde otrzymane srodki traci 1zł
Basia i Pawel maja konto w "SpokoBank"
"""
ACCOUNTS = {
    "asia": 100,
    "basia": 100,
    "pawel": 100
}

ACCOUNTS_BANK = {
    "asia": "GlupiBank",
    "basia": "SpokoBank",
    "pawel": "SpokoBank"
}
def transfers(giver, receiver, amount):
    ACCOUNTS[giver] -= amount
    ACCOUNTS[receiver] += amount
    if ACCOUNTS_BANK[receiver] == "GlupiBank":
        ACCOUNTS[receiver] -= 1
    print(ACCOUNTS)

transfers("asia", "pawel", 20)
transfers("basia", "pawel", 50)
transfers("pawel", "asia", 60)
transfers("basia", "asia", 30)
