class calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    

    def calculate(self,operator):
        if operator == '+':
            return self.a+self.b
        elif operator == '-':
            return self.a-self.b
        elif operator == '*':
            return self.a*self.b
        else:
            return self.a/self.b

cal = calculator(4,5)
print(cal.calculate('+'))
print(cal.calculate('-'))
print(cal.calculate('*'))
print(cal.calculate('/'))
