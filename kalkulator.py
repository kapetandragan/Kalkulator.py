import math

def sabiranje(a, b):
    return a + b

def oduzimanje(a, b):
    return a - b

def mnozenje(a, b):
    return a * b

def deljenje(a, b):
    if b != 0:
        return a / b
    else:
        return "Greška: deljenje sa nulom!"

def stepenovanje(a, b):
    return a ** b

def kvadratni_koren(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Greška: kvadratni koren negativnog broja!"

# Glavna funkcija kalkulatora
def kalkulator():
    print("Dobrodošli u kalkulator sa složenim funkcijama!")
    while True:
        print("Izaberite operaciju:")
        print("1. Sabiranje")
        print("2. Oduzimanje")
        print("3. Množenje")
        print("4. Deljenje")
        print("5. Stepenovanje")
        print("6. Kvadratni koren")
        print("7. Izlaz")
        opcija = input("Unesite opciju (1-7): ")

        if opcija == "7":
            print("Hvala što ste koristili kalkulator!")
            break

        try:
            a = float(input("Unesite prvi broj: "))
            if opcija != "6":
                b = float(input("Unesite drugi broj: "))
        except ValueError:
            print("Greška: Unesite validan broj!")
            continue

        if opcija == "1":
            rezultat = sabiranje(a, b)
        elif opcija == "2":
            rezultat = oduzimanje(a, b)
        elif opcija == "3":
            rezultat = mnozenje(a, b)
        elif opcija == "4":
            rezultat = deljenje(a, b)
        elif opcija == "5":
            rezultat = stepenovanje(a, b)
        elif opcija == "6":
            rezultat = kvadratni_koren(a)
        else:
            print("Greška: Unesite validnu opciju!")
            continue

        print("Rezultat: ", rezultat)
        print()

# Pokretanje kalkulatora
kalkulator()