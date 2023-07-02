# In this program we will learn more about function use:
# function are the module which help to automate the work
def buy_book(b1, b2, b3):
    total = b1 + b2 + b3
    if total > 1400:
        print("You are eligible to purchase the book:")
    else:
        print("You are not eligible to purchase the book:")
    return


Pocket_money = int(input("Pocket money saved:\n"))
Internship_money = int(input("Money earned during internship:\n"))
Credit_money = int(input("Credit money saved:\n"))

# Use of call function
buy_book(Pocket_money, Internship_money, Credit_money)
