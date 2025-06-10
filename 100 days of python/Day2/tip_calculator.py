print("Welcome to tip calculator!")
total_bill = float(input("What was the total bill?: $"))
tip = int(input("How much tip would you like to give ? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))
result =  tip /100 * total_bill + total_bill
bill_per_person = result / split
final_amt = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amt}")








