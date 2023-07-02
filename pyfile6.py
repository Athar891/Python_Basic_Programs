# The store cost and capacity of an item
Store_capacity = 20000
Store_cost = 3400
# Requirement of the customer
customer_req = 10000
customer_budget = 3500
# Condition to check store and customer equality
if Store_capacity >= customer_req and Store_cost <= customer_budget:
    print("Yes,this power bank is for you:")
else:
    print("No, this power bank not for you:")
print("Thank you for visiting:")
