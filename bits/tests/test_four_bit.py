from pytest import mark


from bits.four_bit import FourBit


class TestFourBit:
    def test_four_bit(self):
        pass

    @mark.parametrize(
        "test_input, expected_decimal",
        [
            ((0, 0, 0, 0), 0),
            ((1, 1, 1, 1), 15),
        ],
    )
    def test_four_bit_decimal(self, test_input, expected_decimal):
        test_four_bit = FourBit(test_input)

        assert expected_decimal == test_four_bit.decimal()
