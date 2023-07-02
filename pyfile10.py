# This is program is revision of while loop.
hour = 0
day = 0
total = 0
print("Total run hours in each day:\n")
while day <= 6:
    day = day + 1
    hour = int(input("Run hours day {}\n".format(day)))
    total = total + hour
Avg_hour = total / day
print(Avg_hour)
