# In this program we will learn to check leap year.
Your_year = int(input("Enter the desire year:"))
if Your_year % 100 == 0:  # First check condition.
    print("This is Not a leap year:")
elif Your_year % 4 == 0:  # Second check condition.
    print("This is leap year:")
elif Your_year % 400 == 0:  # Third check condition.
    print("This is leap year:")
else:
    print("This is not a leap year:")
