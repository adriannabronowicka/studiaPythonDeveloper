a = 5
b = 7.4
c = "mama"
d_lista = [1, 2, 3, 3.5, "mama", "54"]

if c == "tata":
    print("Cześć tata")
elif c == "mama" and d_lista[2] > 0:
    print(f"Nasze słowo to {c}")
else:
    print("No nic nie pasuje")

for i in range(2, 15, 4):
    print(i)

for i in range(100, -1, -10):
    print(i)

while (a < 10):
    print(f"a wynosi {a}")
    a += 3

while True:
    wiek = int(input("ile masz lat?"))
    if wiek >= 18:
        break
    else:
        print("Zły wiek")