class BitValueError(ValueError):
    def __init__(self, bit):
        self.message = f"{bit=} is not a 1 or 0"


class FourBit:
    def __init__(self, bits: tuple):

        self.p3 = self.validate_bit(bits[0])
        self.p2 = self.validate_bit(bits[1])
        self.p1 = self.validate_bit(bits[2])
        self.p0 = self.validate_bit(bits[3])

    @staticmethod
    def validate_bit(bit: int):

        if 0 <= bit <= 1:
            return bit
        else:
            raise BitValueError(bit)

    def decimal(self) -> int:

        eights = self.p3 * 8
        fours = self.p3 * 4
        twos = self.p3 * 2
        ones = self.p0 * 1

        return eights + fours + twos + ones

    def binary(self) -> str:

        return bin(self.decimal())

    def __repr__(self):
        return f"4bit: {self.binary()}"
