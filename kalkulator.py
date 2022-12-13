def dodawanie(s1,s2):
    wynik = s1+s2
    return wynik

def odejmowanie(s1,s2):
    wynik = s1-s2
    return wynik
def dzielenie(s1,s2):
    if s2!=0:
        wynik = s1/s2
    else: wynik="Nie dzielimy przez zero"
    return wynik
def mnozenie(s1,s2):
    wynik = s1*s2
    return wynik

print(dodawanie(2,5))
print(odejmowanie(4,5))
print(dzielenie(4,0))
print(mnozenie(3,5))
slownik={'+':dodawanie,'-':odejmowanie,'/':dzielenie,'*':mnozenie}
s1=int(input("Podaj pierwsza wartosc: "))
s2=int(input("Podaj druga wartosc: "))
znak=input("Podaj znak działania jakie chcesz wykonać: ")
print(slownik[znak](s1,s2))