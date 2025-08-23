def convert(amount, rate):
    return amount * rate

usd_to_inr = 83.2
inr_to_usd = 1/83.2

choice = input("1. USD→INR  2. INR→USD: ")
amt = float(input("Enter amount: "))

if choice == "1":
    print("INR:", convert(amt, usd_to_inr))
else:
    print("USD:", convert(amt, inr_to_usd))