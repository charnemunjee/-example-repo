import math

# print statement to explain the
# difference between 'investment' and 'bond'
print("Investment - to calculate the amount "
      "of interest you'll earn on your investment.\n"
      "Bond - to calculate the amount you'll "
      "have to pay on a home loan."
      )

# ask user whether they would like to
# calculate their bond repayments or
# value of their investment
calc_choice = input("Enter either “investment” "
                    "or “bond” from the menu above "
                    "to proceed: ").lower()

# calculate investment amount
if calc_choice == "investment":
    # ask user for deposit amount, interest rate,
    # investment term and whether to use simple
    # or compound interest
    deposit = float(input("Enter deposit amount: "))
    interest_rate = float(input("Enter interest rate (only enter the number): "))
    investment_term = float(input("Enter the number of years "
                                  "that you are planning "
                                  "on investing: "))
    interest = input("Would you like simple or compound interest? ")

    # carry out investment calculation
    if interest == "simple":
        amount = deposit * (1 + investment_term * interest_rate / 100)
    elif interest == "compound":
        amount = deposit * math.pow((1 + interest_rate / 100), investment_term)

    # print result
    print(f"Your investment of {deposit} at {interest_rate} "
          f"percent will be {amount} after {investment_term} years.")

# calculate bond repayments
elif calc_choice == "bond":
    # ask user for house price, interest
    # rate and repayment term
    house_value = float(input("Enter house_value: "))
    interest_rate = float(input("Enter interest rate (only enter the number): "))
    repay_term = float(input("Enter the number of months "
                             "that you will pay on your home loan "))

    # carry out loan repayment amount
    repayment = ((interest_rate / 12 / 100 * house_value) /
                 (1 - (1 + interest_rate / 12 / 100)**-repay_term))
    print(f"You will pay {repayment} on home loan of "
          f"{house_value} for {repay_term} months.")
else:
    print("Please enter either 'investment' or 'bond'")
