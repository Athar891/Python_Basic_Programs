# This program will help to get better grasp of factorial concept
def fact_num(num):
    product = 1  # This is the variable where factorial product will be stored

    for i in range(1, num + 1):  # Here for loop iterate between 1 to num + 1 = 5
        product = product * i   # Here the product will be multiplied with the i ( which is increasing )
    return product


result = fact_num(5)
print("Factorial of 5:", result)
