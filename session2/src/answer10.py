n = int(input("Input a number: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print("") # next line