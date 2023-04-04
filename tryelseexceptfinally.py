def div(num1,num2):
    try:
         num1/num2
    except ZeroDivisionError:
         print('division by zero not allowed')
    else:
         print(f'the result is {num1/num2}')
    finally:
         print('This is always executed')

div(3,2)
div(3,0)


