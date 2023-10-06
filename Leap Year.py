#Favian Mokaya Imbera SCT211-0022/2021

#Enter the year 
year=int(input())
if year%4==0 and year%100!=0:
	print(year,"is a leap year")
elif year%400==0:
	print(year,"is a leap year")
else:
	print(year,"is not a leap year")