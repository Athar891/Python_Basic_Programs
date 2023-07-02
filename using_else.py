# In this program we are going to learn about if and else statement
Price_pencil = int(input("The price of each pencil is:"))
No_pencil = int(input("Total no of pencils bought:"))
Final_price = Price_pencil*No_pencil

if Final_price >= 2000:
    print("Your are eligible to get 20% discount:")
    Discounted_price = Final_price*20/100
    Final_price = Final_price-Discounted_price
else:
    print("Your are eligible for 10% discount:")
    Discounted_price = Final_price*10/100
    Final_price = Final_price-Discounted_price

print("The final payable amount is:", Final_price)
