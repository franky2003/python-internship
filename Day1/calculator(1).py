class Calc:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def evaluate(self, expression):
            result = eval(expression)
            print(f"The result is {result}")

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

calc = Calc(num1, num2)

print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")

while True:
    choice = input("Enter choice:")
    if choice == "1":
        calc.evaluate(f'{calc.num1} + {calc.num2}')
    elif choice == "2":
        calc.evaluate(f'{calc.num1} - {calc.num2}')
    elif choice == "3":
        calc.evaluate(f'{calc.num1} * {calc.num2}')
    elif choice == "4":
        calc.evaluate(f'{calc.num1} / {calc.num2}')
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice")

#Output
'''
Enter num1: 1
Enter num2: 2

1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
Enter choice:1
The result is 3
Enter choice:2
The result is -1
Enter choice:3
The result is 2
Enter choice:4
The result is 0.5
Enter choice:5
Exiting...
'''        