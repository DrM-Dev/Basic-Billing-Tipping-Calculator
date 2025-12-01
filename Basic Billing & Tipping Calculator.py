#Code by Dr.M-Dev

#Bill Calculator Project:-
print("Welcome to the tip calculator! [PROJECT BY Dr.M_Dev]")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tipe would you like to give? 10, 12, or 15--> %"))
number_of_people = int(input("How many people to split the bill? "))

tip_percentage = tip / 100
bill_with_tip = bill * tip_percentage
total_bill_amount = bill + bill_with_tip   #we did that to get the final payment
                                          #not how much you will get from the TIP xD
bill_after_split = total_bill_amount / number_of_people
final_bill = round(bill_after_split,2)   #just to round the number to get $00.00 form

print(f"each person should pay ${final_bill} ")

#something extra I'd love to add:
print(f"\n\nthe tiping amount from the total cost was: ${bill_with_tip}")

input("the results are here, exit?")
input("cya and take care :)")