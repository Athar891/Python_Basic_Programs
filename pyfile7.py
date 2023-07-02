# This is a program to check the proper use of if and elif functions
price = int(input("Enter the desired price:"))
qty = int(input("Enter the quantity:"))
amount = price*qty
if amount > 10000:  # if total amount is between 5000 and 10000
    print("10% discount applicable")
    discount = amount*10/100
    amount = amount-discount
elif amount > 5000:  # if total amount is between 2000 and 5000
    print("5% discount is applicable:")
    discount = amount*5/100
    amount = amount-discount
elif amount > 2000:  # if total amount is between 1000 and 2000
    print("2% discount is applicable:")
    discount = amount*2/100
    amount = amount-discount
elif amount > 1000:  # if the total amount is less than 1000
    print("1% discount is applicable:")
    discount = amount*1/100
    amount = amount-discount

print("amount payable:", amount)
