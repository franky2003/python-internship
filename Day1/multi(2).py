def multiplication_table(number):
    print(f"Multiplication table for {number}:")
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

number=int(input("Enter the number:"))
multiplication_table(number)

'''
Enter the number:5
Multiplication table for 5:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
'''