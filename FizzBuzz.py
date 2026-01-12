value=0
while value<30:
    value=value+1
    output= str(value) + ' '
    if value % 3 == 0: 
        output = output + "fizz"
    if value % 5 == 0:
        output = output + "Buzz"
    print(output)