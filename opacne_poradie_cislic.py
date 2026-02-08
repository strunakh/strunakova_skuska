class ObracacCisla:
    def __init__(self, Cislo: int):
        self.Cislo = Cislo

    def spracuj(self):
        n = abs(self.Cislo)  # pracuje s absolútnou hodnotou
        otocene = 0

        # špeciálny prípad: ak je číslo 0
        if n == 0:
            return 0, 0

        while n > 0:
            # Obrátenie pomocou celočíselného delenia a zvyškom po delení
            cifra = n % 10
            otocene = otocene * 10 + cifra
            n //= 10

        # vrátenie znamienka
        if self.Cislo < 0:
            otocene = -otocene

        # Ciferný súčin otočeného čísla
        sucin = 1
        m = abs(otocene)
        while m > 0:
            sucin *= m % 10
            m //= 10

        return otocene, sucin


def main():
    try:
        cislo = int(input("Napíšte celé číslo: "))
    except ValueError:
        print("Nesprávny vstup")
        return

    obracac = ObracacCisla(cislo)
    otocene, sucin = obracac.spracuj()

    print(f"Otočené číslo: {otocene}")
    print(f"Ciferný súčin: {sucin}")


main()