class Calculator:
# Write methods to add(), subtract(), multiply() and divide()
    def add(self, _num1, _num2):
        self.num1 = _num1
        self.num2 = _num2
        final = self.num1 + self.num2
        return final
    def substract(self, _num1, _num2):
        self.num1 = _num1
        self.num2 = _num2
        final = self.num1 - self.num2
        return final
    def multiply(self, _num1, _num2):
        self.num1 = _num1
        self.num2 = _num2
        final = self.num1 * self.num2
        return final
    def divide(self, _num1, _num2):
        self.num1 = _num1
        self.num2 = _num2
        final = self.num1 // self.num2
        return final

calculator = Calculator()
print(calculator.add(10,5))
print(calculator.substract(10,5))
print(calculator.multiply(10,5))
print(calculator.divide(10,5))