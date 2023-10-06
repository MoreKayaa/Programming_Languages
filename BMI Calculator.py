# Favian Mokaya Imbera SCT211-0022/2021


#Enter your weight(in kg) and height(in metres) respectively
weight = float(input ())
height = float(input())
bmi = weight/(height**2)
print ("Your bmi is "+str(bmi))
if bmi < 18.5:
	print ("""According to WHO,your nutritional status is:
Underweight""")
elif 18.5 <= bmi < 25:
	print ("""According to WHO,your nutritional status is:
Normal""")
elif 24.9 <= bmi < 29.9:
	print ("""According to WHO,your nutritional status is:
Overweight""")
else:
	print ("""According to WHO,your nutritional status is:
Obesity""")