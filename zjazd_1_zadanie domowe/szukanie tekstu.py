#znalezienie koncówki adresu email
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

a_data = data.find("@")   #znalezienie znaku
print(a_data)
s = data.find(" ", a_data)
print(s)

address_email = data[a_data + 1 : s]

print(f"Address emial is {address_email}")