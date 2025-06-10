print("Welcome to Python Pizza Deliveries!")
rate = 0
size = input("What size pizza do you want? S, M or L: ")
if size == "S":
    rate += 15
    print("You have order Small Size Pizza for $15")
elif size == "M":
    rate += 20
    print("You have ordered MEDIUM  size pizza for $20")
elif size == "L":
    rate =+ 25
    print("You have ordered Large Size pizza for $25")
else:
    print("You have typed wrong inputs.")
pepperoni = input("Do you want peppereoni on your pizza? Y or N: ")
if pepperoni == "Y":
    if size=="S":
        rate +=2
    else:
        rate +=3

exatra_cheese = input("Do you want extra cheese? Y or N: ")
if exatra_cheese == "Y":
    rate +=1

print(f"Your final bill is {rate}")
























