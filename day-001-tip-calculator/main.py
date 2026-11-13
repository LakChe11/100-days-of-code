"""Tip calculator"""


def main():
    print("Day 1: Tip calculator")
    bill_amount = int(input("What was the total bill? $"))
    tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
    tip_amount = bill_amount * (1+ (tip_percentage / 100))
    print (f"The total amount to pay is: ${tip_amount: .2f}")



    


if __name__ == "__main__":
    main()
