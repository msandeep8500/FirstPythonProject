class Calculator:
    def __init__(self,x,y):
        self.x=x
        self.y =y

    def __str__(self):
        return f'{str(self.x)} {str(self.y)}'
    def add(self):
        print("Method invoked")
        sum = self.x +self.y
        print("Sum is "+ str(sum))

        return sum
    def sub(self):
        return self.x- self.y
    def multiply(self):
        return self.x * self.y
    def divide(self):
        return self.x/self.y
