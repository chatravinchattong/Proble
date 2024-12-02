number = int(input("Enter the multiplication table number: "))
print(f"multiplication table for: {number}")
for i in range(1,13):
    resul = number * i
    print(f"{number} x {i} = {resul} ")