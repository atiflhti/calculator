print("To exit , enter q")
while True:
    num1 = input("Enter first number: ")
    if num1 == "q":
        break

    num2 = input("Enter second number: ")
    if num2 == "q":
        break
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
      print("Error: Please enter numbers only")
  
    while True:
        operation = input("Enter operation (+,-,*,/): ").strip()
        if operation.lower() == "q" or operation in ("+", "-", "*", "/"):
            break
        print("Warning: Invalid operation. Only + - * / are allowed (no numbers or letters).")

    if operation=="+":
        result=num1+num2
        print("Result:",result)
    
    elif operation =="-":
        result=num1-num2
        print("Result:",result)
    
    elif operation =="*":
        result=num1*num2
        print("Result:",result)
    
    elif operation =="/":
        if num2!=0:
           result=num1/num2
           print("Result:",result)
        else:
           print("Eroor: Division by ziro is not allowed.")