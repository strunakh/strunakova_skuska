from string import ascii_letters, digits

class AnalyzerTextu:
    ZNAKY = "ÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ" + "áčďéěíňóřšťúůýž" + ascii_letters + digits + " ,.?!;"

    def __init__(self, text: str):
        self.Text = text

    def _je_povoleny_znak(self, znak: str) -> bool:
        return znak in self.ZNAKY

    def spracuj(self)-> list[str]:
        filtrovane = []
        # Prázdny zoznam, do ktorého sa ukladajú ponechané znaky

        for z in self.Text:
            if self._je_povoleny_znak(z):
                filtrovane.append(z)

        # Rozdelenie na slová (zvládne aj viac medzier)
        return "".join(filtrovane).split()


def main():
    text = input("Vložte text:")

    analyzator = AnalyzerTextu(text)   
    slova = analyzator.spracuj()
    
    print(f"\nPočet slov je: {len(slova)}")
    print("Slová v opačnom poradí:")
    print(" ".join(reversed(slova)))   


main()