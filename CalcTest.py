from Calculator import Calculator
def calcTest():
    number1 = int((input("Please enter your  number1")))
    number2 = int((input("Please enter your  number2")))

    operation =input("Select your choice 1.Add 2.Subtract 3.Multiply 4.Divide")
    mycalc = Calculator(number1, number2)
    if operation == "Add":

        print(mycalc)

        print(mycalc.add())
    if operation == "Subtract":
        print(mycalc.sub())
    if operation == "Multiply":
        print(mycalc.multiply())
    if operation == "Divide":
        print(mycalc.divide())


calcTest()

