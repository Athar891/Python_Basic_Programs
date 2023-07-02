# In this program we will learn using of while loop.
sweets = 0
days = 0
total = 0
print("No of sweets you eat each day:\n")
while days <= 6:
    days = days + 1
    sweets = int(input("Enter no of sweets eaten each day {}\n".format(days)))
    total = total + sweets
    print(total)
Avg = total / 6
print(Avg)
