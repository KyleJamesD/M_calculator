
client_name= input("Enter client name:")
address = input("Enter Address of Property:")
purchase_price = int(input("Enter purchase price of property (IE: 500000):"))

if purchase_price <= 500000:
    minimum_down_percent = ((purchase_price * 5/100) / purchase_price) * 100
elif  500000 < purchase_price <= 1000000:
    minimum_down_percent =((((purchase_price - 500000)* 10/100) + (500000 * 5/100)) / purchase_price) * 100
elif purchase_price > 1000000: 
    minimum_down_percent = 20

down_payment_check = False
while not down_payment_check:
    down_payment_percent = float(input(f"Enter down payment percentage (minimum {minimum_down_percent:.3f}):"))
    if down_payment_percent >= minimum_down_percent:
        if down_payment_percent < 100:
            down_payment_check = True
        else: print ("Please Enter the Value between the minimum and 100.")
    else: print ("Please Enter the Value between the minimum and 100.")



down_payment_amount = purchase_price * down_payment_percent / 100

if 5 <= down_payment_percent < 10:
    mortgage_insurance_prem = (purchase_price-down_payment_amount) * 4 / 100
elif 10 <= down_payment_percent < 15:
    mortgage_insurance_prem = (purchase_price-down_payment_amount) * 3.1 / 100
elif 15 <= down_payment_percent < 20:
    mortgage_insurance_prem = (purchase_price-down_payment_amount) * 2.8 / 100
elif down_payment_percent >= 20:
    mortgage_insurance_prem = 0


principal_amount = purchase_price - down_payment_amount + mortgage_insurance_prem

print (f"Down payment is amount is ${down_payment_amount:.0f}")
print (f"Mortgage Insurance price is ${mortgage_insurance_prem:.0f} ")
print (f"Total mortgage amount is ${principal_amount:.0f}")


mortgage_term_check = False
while not mortgage_term_check:
    mortgage_term = int(input("Enter mortgage Term (1, 2, 3, 5, 10):"))
    if mortgage_term == 1 or mortgage_term == 2 or mortgage_term == 3 or mortgage_term == 5 or mortgage_term == 10:
        mortgage_term_check = True
    else: print ("Please Enter a valid term number (1, 2, 3, 5, 10):")




amoritization_term_check = False
while not amoritization_term_check:
    amoritization = int(input("Enter mortgage amortization period (5, 10, 15, 20, 25):"))
    if amoritization == 5 or amoritization == 10 or amoritization == 15 or amoritization == 20 or amoritization == 25:
        amoritization_term_check = True
    else: print ("Please Enter a valid choice (5, 10, 15, 20, 25):")

if mortgage_term == 1:
    mortgage_interest_rate = 5.95
elif mortgage_term == 2:
    mortgage_interest_rate = 5.9
elif mortgage_term == 3:
    mortgage_interest_rate = 5.6
elif mortgage_term == 5:
    mortgage_interest_rate = 5.29
elif mortgage_term == 10:
    mortgage_interest_rate = 6

monthly_payment = amoritization * 12 # find the amount of payments for the total amortization

monthly_interest_rate = ((1 + (mortgage_interest_rate/100)/2)**2)**(1/12)-1 #EMR
# print (f"monthly_interest_rate={monthly_interest_rate:.8f}")
monthly_payment_amount = principal_amount*(monthly_interest_rate*(1 + monthly_interest_rate)**monthly_payment) / ((1 + monthly_interest_rate)**monthly_payment - 1) #M
# print (f"monthly_payment_amount={monthly_payment_amount:.2f}")

print (f"Interest rate for the term will be {mortgage_interest_rate:.2F}%")
print (f"Monthly payment amount is : ${monthly_payment_amount:.0F}")
show_schedule = input("Would you like to see the amortization Scedule? (Y/N):").lower()





monthly_pay_ments = mortgage_term * 12 # = find the amount of monthly payments in the term
closing_balance = principal_amount



if show_schedule == "y":
    print (f"{'Monthly Amortization Schedule':>51} \n")
    print(f"{'Month':<9}{'Opening Bal':<19}{'Payment':<13}{'Principal':<16}{'Interest':<12}{'Closing Bal':<11}")
    i = 0
    total_interest = 0
    total_principal = 0
    while i < monthly_pay_ments:
        i += 1
        opening_balance = closing_balance
        monthly_interest_amount = opening_balance * monthly_interest_rate  # this = MI = interest
        monthly_principle = monthly_payment_amount - monthly_interest_amount # this = MP = principal
        closing_balance = opening_balance - monthly_principle # this is = CB = Closing Balance
        total_principal += monthly_principle
        total_interest += monthly_interest_amount
        print(f"{i:>5} {opening_balance:>14.2f} {monthly_payment_amount:>14.2f} {monthly_principle:>14.2f} {monthly_interest_amount:>14.2f} {closing_balance:>14.2f}")
    print ("================================================================================")
    print (f"Total{total_principal:>45.2f} {total_interest:>14.2f}")

    







