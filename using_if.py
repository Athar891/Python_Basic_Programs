# understanding how to use if statement in a program
price_donut = int(input("The price of each donut is:"))
No_donut = int(input("No of donut:"))
Amount_donut = price_donut*No_donut

if Amount_donut >= 1000:
    print('10% discount is applicable in your purchase:')
    discounted_price = Amount_donut*10/100
    Amount_donut = Amount_donut-discounted_price

print("Your total amount of purchase is:\n", Amount_donut)
