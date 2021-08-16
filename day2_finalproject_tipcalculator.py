print("******************************")
print("Welcome to the tip calculator.")

total_bill = input("What was the total bill? ")
tip_amount = input("How much would you like to tip? 10, 12, 15 or 18? ")


#some bounds on tipping 
if(int(tip_amount)<0):
    print("Come on you have to tip something")
elif(int(tip_amount)>total_bill):
    print("That is more than the bill itself!")

ppl_splitting = input("How many people are you splitting the bill with? ")

tip = float(tip_amount) / 100
tip_amount_sum = 1 + tip

#print(type(tip_amount))

#print(tip_amount_sum)
indvl_amount = float(total_bill) * float(tip_amount_sum) / int(ppl_splitting)
#final_amount = "{:.2f}".format(indvl_amount)
print(f"Each person should pay: $ {indvl_amount:.2f}")

#to clean it up, you can remove another line of "final_amount" and input it like
#it is shown above. :.#f 
