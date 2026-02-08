from string import ascii_letters, digits

class TextAnalyzer:
    CHARACTERS = "ÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ" + "áčďéěíňóřšťúůýž" + ascii_letters + digits + " ,.?!;"

    def __init__(self, text: str):
        self.Text = text
        self.words = []

    def _char_ok(self, c: str) -> bool:
        return c in self.CHARACTERS

    def process(self)-> list[str]:
        # kept characters in list
        filtered = []
        for z in self.Text:
            if self._char_ok(z):
                filtered.append(z)
  
        # spliting to words
        words = []
        word = ""
        for c in filtered:
            if c == " ":
                if len(word) > 0:
                    words.append(word)
                    word = ""
            else: 
                word = word + c

        if len(word) > 0:
            words.append(word)

        # reversing
        reversed_words = []
        
        n = len(words) - 1
        while n >= 0:
            reversed_words.append(words[n])
            n -= 1

        self.words = reversed_words
        return len(words)
    
    def print_words(self):
        text = ""
        for word in self.words:
            if text == "":
                text = text + word
            else:
                text = text + " " + word
        print(text)

def main():
    text = input("Vložte text:")

    analyzer = TextAnalyzer(text)   
    count = analyzer.process()
    
    print(f"\nPočet slov je: {count}")
    print("Slová v opačnom poradí:")
    analyzer.print_words()    

main()