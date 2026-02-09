class NumberReverser:
    def __init__(self, number: int):
        self.number = number

    def process(self):
        n = abs(self.number)  # uses absolute value
        reversed = 0

        # input value 0
        if n == 0:
            return 0, 0

        while n > 0:
            # Reversing using integer division and modulo
            figure = n % 10
            reversed = reversed * 10 + figure
            n //= 10

        if self.number < 0:
            reversed = -reversed

        # Digit product of the reversed number
        product = 1
        m = abs(reversed)
        while m > 0:
            product *= m % 10
            m //= 10

        return reversed, product


def main():
    try:
        number = int(input("Enter integer: "))
    except ValueError:
        print("Invalid input value")
        return

    reverser = NumberReverser(number)
    reversed, product = reverser.process()

    print(f"Reversed number: {reversed}")
    print(f"Digit product: {product}")


main()