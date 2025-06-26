import re

string = input("Unesite neki string: ")

pattern = r'^[Zz][\w\s]*[0-5]+[\s\w]*[bB]$'

rezultat = re.search(pattern, string)

if rezultat:
    print('Podudara')
else:
    print('Ne podudara')
