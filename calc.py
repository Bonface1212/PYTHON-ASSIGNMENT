first = float(input("Enter the first number ==> " ))
sec = float(input("Enter the second number ==> "))
opr = str(input("Enter operation(+, -, *, /) => "))

if opr == "+":
    total = first + sec
elif opr == "-":
    total = first - sec
elif opr == "*":
    total = first * sec
elif opr == "/" and sec == 0:
    total = "Error! Division by zero is not allowed."
    total = first / sec
else:
    total = str("Please Enter a Valid Operation")

print (total)   
