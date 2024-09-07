score = int(input("Enter score: "))
conduct = input("Enter conduct grade: ")

if score >= 60 and conduct == "A":
    print("Congratulations! You get an award.")
elif score >= 60:
    print("Your conduct grade is not A.")
elif conduct == "A":
    print("Your score is not high enough.")
else:
    print("Your score is not high enough and your conduct grade is not A.")