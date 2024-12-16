sum_odd = int(input("Enter number: "))
sum_even = int(input("Enter number: "))

while(True):
    number = int(input("Enter number: "))
    if number == 0:
        break
    if number % 2 == 0 :
        sum_odd += number
    else:
        sum_even += number
print (f"sum of odd number: {sum_even}")
print (f"sum of even number: {sum_odd}")

        
    
    