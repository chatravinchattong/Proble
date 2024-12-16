number1 = int(input("Enter numnber: "))
number2 = int(input("Enter number: "))
print("Number between",number1,"and",number2)
for num in range(number1,number2 +1):
    if num % 3 == 0:
        print(num)