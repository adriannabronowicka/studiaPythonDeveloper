"""
Tylko do plikw py
from audi.parts.gearbox.gears import GEARS
print(audi.parts.gearbox.gears.GEARS)

from audi.parts.gearbox.gears import GEARS
"""

from audi import GEARS
print(GEARS)

with open (r'C:\Users\adria\Desktop\studiaPythonDeveloper\zjazd_5_2023 01 13\complicated_tree\audi\shops\warsaw.txt', 'r') as file:
    content = file.read()
print(content)

x = open("audi/shops/warsaw.txt").read()
print(x)

