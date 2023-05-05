import math

while True :
    num1 = int(input("Enter your number :"))
    op = input("Enter operation(pick from, radical, sin , cos , tan , cot , factorial) or exit: ")
    if op == "radical":
         result = math.sqrt(num1)
         print(result)
    if op == "sin":
         result = math.sin(num1)
         print(result)
    if op == "cos":
         result = math.cos(num1)
         print(result)
    if op == "tan":
         result = math.tan(num1)
         print(result)
    if op == "cot":
         result1 = math.tan(num1)
         result = (1/result1)
         print(result)
    if op == "factorial":
         result = math.factorial(num1)
         print(result)
    if op == "exit":
         break
         
         print("your Result :",re)
    

         