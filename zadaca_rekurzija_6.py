def obrni(s):
    if s == "":
        return ""
    return obrni(s[1:]) + s[0]

tekst = input("Unesi neki tekst: ")
print("Obrnuto:", obrni(tekst))
