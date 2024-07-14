dicti = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

dictiMinus = {
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900,
}

def romanToInt(s: str) -> int:
    kek = 0
    i = 0
    fed = False
    while i < len(s):
        if i != len(s) - 1:
            if s[i] + s[i+1] not in dictiMinus.keys():
                kek += dicti[s[i]]
                fed = False
                i += 1
            else:
                fed = True
                kek += dictiMinus[s[i] + s[i+1]]
                i += 2
        elif i == len(s) - 1 and not fed:
            kek += dicti[s[i]]
            i += 1
    return kek

val = input("Enter a Roman Numeral: ").upper()
print(f"{romanToInt(val)}")