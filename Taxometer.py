start_price = 4.50
km = int(input("Bitte Kilometer eingeben: "))
if km < 9:
   costs = 2.70
else:
    costs =2.00
total_expenses = start_price + costs * km
print("Deine Kosten sind:", total_expenses)