first = float(input("Enter the first number ==> " ))
sec = float(input("Enter the second number ==> "))
opr = input("Enter operation(+, -, *, /) => ").strip ()

if opr == "+":
    total = first + sec
elif opr == "-":
    total = first - sec
elif opr == "*":
    total = first * sec
elif opr == "/":
   if sec != 0:
       total = first / sec
   else:
       total = "Error! Division by zero is not allowed."
else:
    total = "Please Enter a Valid Operation"

print (total)   
