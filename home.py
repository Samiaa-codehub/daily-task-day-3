# daily-task-3
num1=int(input("Enter your first number:"))
num2=int(input("Eter your second number:"))
operation= input("Enter your operation( add , subtract , multiply , division)")
if operation == "add":
    print("Result:",num1 + num2),
elif operation == "subtract":
    print("Result:",num1-num2),
elif operation == "multiply":
    print("Result:",num1*num2),
elif operation =="division":
    print("Result:" ,num1/num2 ),
else:
    print("not valid")