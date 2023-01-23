print('Welcome to the Tip Calculator')

total_bill = input('How much is the total bill? ')
split_group = input('How many people are splitting the bill? ')
share_tip = input('Are you all sharing the tip amount? ')
tip_amount = input('How much is the total tip from the group? ')

if share_tip == "no" or share_tip == "No":
  split_amount = float(total_bill) / int(split_group)
elif share_tip == "yes" or share_tip == "Yes":
  split_amount = (float(total_bill) + float(tip_amount)) / int(split_group)  

print('Everyone should pay: $' + str(split_amount))