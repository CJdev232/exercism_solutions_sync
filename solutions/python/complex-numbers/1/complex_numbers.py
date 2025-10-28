import math

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other, 0)
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other, 0)
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __radd__(self, other):  
        return self.__add__(other)  

    def __mul__(self, other):
        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other, 0)
        return ComplexNumber(
            self.real * other.real - self.imaginary * other.imaginary,
            self.imaginary * other.real + self.real * other.imaginary
        )

    def __rmul__(self, other):  
        return self.__mul__(other)  

    def __sub__(self, other):
        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other, 0)
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __rsub__(self, other):  
        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other, 0)
        return other.__sub__(self)

    def __truediv__(self, other):
        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other, 0)
        
        if other.real == 0 and other.imaginary == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        
        denominator = other.real**2 + other.imaginary**2
        real_part = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imag_part = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        
        return ComplexNumber(real_part, imag_part)

    def __rtruediv__(self, other):  
        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other, 0)
        return other.__truediv__(self)

    def __abs__(self):
        return math.sqrt(self.real**2 + self.imaginary**2)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        return ComplexNumber(
            math.exp(self.real) * math.cos(self.imaginary),
            math.exp(self.real) * math.sin(self.imaginary)
        )