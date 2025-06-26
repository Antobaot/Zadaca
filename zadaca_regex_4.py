import re

email = input("Unesi e-mail: ").lower()
eduid = input("Unesi eduID: ").lower()


regex_email = r'^[a-zčćžšđ]+\.{1}[a-zčćžšđ]+@fpmoz\.sum\.ba$'

regex_eduid = r'^[a-zčćžšđ]{1}[a-zčćžšđ]+[0-9]*@sum\.ba$'

if re.fullmatch(regex_email, email):
    print("E-mail je ispravan")
else:
    print("E-mail NIJE ispravan")

if re.fullmatch(regex_eduid, eduid):
    print("eduID je ispravan")
else:
    print("eduID NIJE ispravan")
