def funkcja1 (imie, wiek=20):

    '''Funkcja wypisuje imię oraz wiek.

    :param imie:
    :param wiek:
    :return:
    '''
    print(imie, wiek)

funkcja1("Jakub",20)
funkcja1("ASDAD",83)
funkcja1(wiek=16,imie="ADA")
funkcja1("asdasdasd")

print(funkcja1.__doc__)
print(help(funkcja1))
