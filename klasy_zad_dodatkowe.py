"""zad_1 Utwórz klasę Konwerter a w niej metody: int_to_roman -  zamienia int na liczby rzymskie (do 3999)
	roman_to_int - zamienia liczbę rzymska na int """


class Konwerter:
    dict_val = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9,
                'V': 5, 'IV': 4, 'I': 1}

    @classmethod
    def int_to_roman(cls, num):
        if not (0 < num <= 3999):
            return "Liczba poza przedziałem"
        elif isinstance(num, int):
            result = ''
            for k, v in Konwerter.dict_val.items():
                while num >= v:
                    result += k
                    num -= v
            return result

    @staticmethod
    def roman_to_int(rom):
        result = 0
        for i in range(len(rom)):
            if i > 0 and Konwerter.dict_val[rom[i]] > Konwerter.dict_val[rom[i - 1]]:
                result += Konwerter.dict_val[rom[i]] - 2 * Konwerter.dict_val[rom[i - 1]]
            else:
                result += Konwerter.dict_val[rom[i]]
        return result

    def cel_to_farh(self, cel):
        result = cel * 9 / 5 + 32
        return result

    def farh_to_cel(self, farh):
        result = round((farh - 32) / 1.8, 2)
        return result


k = Konwerter()
print(k.int_to_roman(5))
print(k.int_to_roman(2580))
print(k.int_to_roman(60))
print(k.int_to_roman(4000))

print(k.roman_to_int('IV'))
print(k.roman_to_int('XXII'))
print(k.roman_to_int('CIX'))

print(k.farh_to_cel(0))
print(k.farh_to_cel(17))
print(k.farh_to_cel(52))

print(k.cel_to_farh(44))
print(k.cel_to_farh(14))
print(k.cel_to_farh(3))

print("Z @classmethod:")
print(Konwerter.int_to_roman(1))
print(Konwerter.int_to_roman(4))
print(Konwerter.roman_to_int("IV"))
print(Konwerter.roman_to_int("XXI"))

assert Konwerter().int_to_roman(1) == "I"
assert Konwerter().int_to_roman(4) == "IV"
assert Konwerter().int_to_roman(3999) == "MMMCMXCIX"
assert Konwerter().roman_to_int("MMMCMXCIX") == 3999
assert Konwerter().roman_to_int("IV") == 4
assert Konwerter().roman_to_int("II") == 2

assert Konwerter().farh_to_cel(0) == -17.78
assert Konwerter().farh_to_cel(52) == 11.11
assert Konwerter().cel_to_farh(44) == 111.2
assert Konwerter().cel_to_farh(3) == 37.4

assert Konwerter.int_to_roman(1) == "I"
assert Konwerter.int_to_roman(4) == "IV"
assert Konwerter.roman_to_int("IV") == 4
assert Konwerter.roman_to_int("II") == 2


### NOTATNIK

class Osoba:
    def __init__(self, imie, email):
        if "@" not in email:
            raise Exception("Nie właściwy format emaila. Prawidłowy format --> nazwa@domena.pl")
        self.imie = imie
        self.email = email

    # @property
    # def email(self):
    #     return self._email
    #
    # @email.setter
    # def email(self, a):
    #     if "@" not in a: raise Exception("Podaj wlasciwy format maila: nazwa@blabla.pl")
    #     self._email = a

    def show(self):
        return(f"{self.imie}, email: {self.email}")


class Adres:
    def __init__(self, ulica, miasto):
        self.ulica = ulica
        self.miasto = miasto

    def show(self):
        return(f"adres: {self.ulica}, {self.miasto}")


class Kontakt():
    def __init__(self, osoba, adres):
        self.os = osoba
        self.ad = adres

    def show(self):
        print("Wynik klasy Kontakt: ")
        print(Osoba.show(os))  # print(f"{self.os.imie}, email: {self.os.email}")
        print(Adres.show(ad))  # print(f"adres: {self.ad.ulica}, {self.ad.miasto}")


class Notebook:
    def __init__(self):
        self.slownik_danych = {}

    def add(self, imie, email, ulica, miasto):
        self.slownik_danych[imie] = [email, ulica, miasto]

    def show(self, imie):
        if imie in self.slownik_danych.keys():
            print(f"{imie}, {self.slownik_danych[imie][0]}' \n"
                  f"adres: {self.slownik_danych[imie][1]}, {self.slownik_danych[imie][2]}")
        else:
            print(f"Brak wpisu dla osoby: {imie}")


os = Osoba('Zenek', 'zenek@zenek.pl')
os2 = Osoba('Zenek', 'zenek@zenek.pl')
os.show()
os2.show()
ad = Adres("Polna", "Warszawa")
ad.show()
print()
contact = Kontakt(os, ad)
contact.show()
notes = Notebook()
notes.add("Franek", "franio@franio.pl", "Polna", "Wyszków")
notes.add('Robert', 'robert@gmail.com>', 'Królewska 27', 'Warszawa')
notes.add('Ala', 'ala@wp.pl', 'Dziwna 15', 'Pacanów')
notes.show('Ala')
notes.show("Krzyś")