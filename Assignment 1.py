year = float(input("Please enter the years: "))
office = input("Please enter the office name: ")

if office.upper() == "IT":
    if year >= 10:
        print("10000")
    else:
        print("5000")
elif office.upper() == "HR":
    if year >= 10:
        print("12000")
    else:
        print("6000")
elif office.upper() == "ACCT":
    if year >= 10:
        print("15000")
    else:
        print("7500")
else:
    print("The wrong office name entered")