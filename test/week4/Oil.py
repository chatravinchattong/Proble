k = float(input("Enter km: "))
ch = int(input("Enter car type: "))
if ch == "ev":
    total = k * 1
else:
    total = k * 4
print("Total cost: ", total)
    