print('Welcome to the Tip Calculator')

total_bill = input('How much is the total bill? $')
split_group = input('How many people are splitting the bill? ')
share_tip = input('Are you all sharing the tip amount? ')

if share_tip == "no" or share_tip == "No":
  split_amount = float(total_bill) / int(split_group)
elif share_tip == "yes" or share_tip == "Yes":
  tip_amount = input('What should to tip percentage be? ')
  tip_amount = (float(tip_amount) / 100) + 1
  split_amount = (float(total_bill) * float(tip_amount)) / int(split_group)

split_amount = "{:.2f}".format(split_amount)

print(f'Everyone should pay: ${split_amount}')
