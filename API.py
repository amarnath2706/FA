def math_operation(num1, num2, operation):
    if (operation == 'add'):
        r = num1 + num2
        result = 'The sum of '  +str(num1)  +' and '  +str(num2)  +' is : '  +str(r)
    if (operation == 'subtract'):
        r = num1-num2
        result = 'The Differecce of' +str(num1) +'and' +str(num2) +'is' +str(r)
    if (operation == 'multiply'):
        r = num1*num2
        result = 'The Product of' +str(num1) +'and' +str(num2) +'is' +str(r)
    if (operation == 'divide'):
        r = num1/num2
        result = 'The division of' +str(num1) +'and' +str(num2) +'is' +str(r)
    return result

Output = math_operation(20,6,'add')
print(Output)