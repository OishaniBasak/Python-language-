#Write a program that can tell you your BMI Category.
#Ask user to enter height in Meter
#Ask user to enter weight in KG
#Calculate the BMI (Body Mass Index) = weight /(height)**2 and store it in a variable
#If the BMI is 30 or greater, print “Obesity”
#If the BMI is in between 25 and 29, print “Overweight”
#If the BMI is in between 18.5 and 25, print “Normal”
#If the BMI is less than 18.5, print “Underweight”


height=(float(input("Enter your height in meter : ")))
weight=(float(input("Enter your weight in kg : ")))
BMI=weight/(height)**2
print("Body Mass Index : ",BMI)
if(BMI>=30):
    print("Obesity")
elif(BMI>25 and BMI<=29):
    print("Overweight")
elif(BMI>18.5 and BMI<=25):
    print("Normal")
else:
    print("Underweight")
