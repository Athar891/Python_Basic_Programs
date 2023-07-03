# 1. pi needs money between Rs.7000 to 10000.
# 2. if his sis gives him less than 7000 then show message " Ahem, can you rethink the number please.
# 3. if his sis gives him between Rs. 7000 to 10000 then show message " Cool, thanks sis , x rupees will certainly help.
# 4. if his sis gives him more than 10000 then show message " Wow sis!, You are the queen"
def checkmoney(sis):
    if sis < 7000:
        print("Ahem, Can you rethink the number please?")
    elif 7000 <= sis <= 10000:
        print("Cool, thanks sis,", sis, "rupees will certainly help")
    elif sis > 10000:
        print("Wow sis!, you are the queen.")
    return


sis = int(input("Enter the amount money:\n"))
checkmoney(sis)
