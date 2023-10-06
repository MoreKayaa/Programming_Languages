#Favian Mokaya Imbera SCT211-0022/2021


#Tip Calculator
#Enter the bill,no of people and tip percantage

#Tip Percentage must be either 10,12 or 15

def person_pay(a,b):
	return a/b
	
def tip_payment(a,b):
	return a*(b/100)

while True:
	try:
		bill = float(input())
		break
	except:
		print("Must be a number")
		
while True:
	try:
		people = float(input())
		break
	except:
		print("Must be a number value!")
		
while True:
	try:
		tip = float(input())
		break
	except:
		print("Must be a number value!")
if tip == 10 or tip == 12 or tip ==15:		
	each_pays = person_pay(bill,people)
	each_tips = tip_payment(each_pays,tip)
	print ("Each person pays Ksh{0:.2f} for the 	    bill".format(each_pays))
	print ("Each person pays Ksh{0:.2f} for the 	tip".format(each_tips))
	print ("Which means each person will pay a 	total of Ksh{0:.2f}".format(each_pays + 		each_tips))
else:
	print("Percentage of tip must be 10,12 or 15")