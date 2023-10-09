first = int(input("Input first number: "))
second = int(input("Input second number: "))
if first < second:
    #swap the two numbers
    temp = first
    first = second
    second = temp
answer = first - second
print("The answer of "+str(first)+"-"+str(second)+" is " + str(answer))