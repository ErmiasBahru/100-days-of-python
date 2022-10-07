print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
tip = int(input("What perentage tip would you like to give? 10, 12 or 15? "))
split = int(input("How many people to split the bill? "))

total = "{:.2f}".format((((bill * (tip / 100)) + bill) / split))

print(f"Each person should pay: ${total}")