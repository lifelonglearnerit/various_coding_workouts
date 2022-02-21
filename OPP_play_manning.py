"""
Operator overloading for class Fraction
"""
class Fraction(object):
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom

    def __add__(self, other):
        result_top = self.top * other.bottom + other.top * self.bottom
        result_bottom = self.bottom * other.bottom
        return Fraction(result_top, result_bottom)

    def __mul__(self, other):
        result_top = self.top * other.top
        reslut_bottom = self.bottom * other.bottom
        return Fraction(result_top, reslut_bottom)

    def __truediv__(self, other):
        result_top = self.top * other.bottom
        result_bottom = self.bottom * other.top
        return Fraction(result_top, result_bottom)

    def __str__(self):
        return f'{self.top} / {self.bottom}'

first_fraction_top = int(input('Type numerator (top) of the 1st fraction: '))
first_fraction_bottom = int(input('Type denominator (bottom) of the 1st fraction: '))
second_fraction_top = int(input('Type numerator (top) of the 2nd fraction: '))
second_fraction_bottom = int(input('Type denominator (bottom) of the 2nd fraction: '))
first_fraction = Fraction(first_fraction_top, first_fraction_bottom)
second_fraction = Fraction(second_fraction_top, second_fraction_bottom)
sum = first_fraction + second_fraction
mul = first_fraction * second_fraction
div = first_fraction / second_fraction
print(f'sum of the fractions: {sum}')
print(f'multiplication of the fractions: {mul}')
print(f'division of the fractions: {div}')
print('Cheers! t.')

