#Input the marks in Mathematics and find the grade.(Marks>=90 (A, Marks>=80 (B,  Marks>=70 (C, Marks>=60 (D, Marks>=50 (E, Marks <50-> F)

m=(int(input("Enter your marks: ")))
if(m<=100 and m>=90):
    print("Your grade is 'O'")
elif (m<=89 and m>=80):
    print("Your grade is 'E'")
elif (m<=79 and m>=70):
    print("Your grade is 'A'")
elif (m<=69 and m>=60):
    print("Your grade is 'B'")
elif (m<=59 and m>=50):
    print("Your grade is 'C'")
else:
    print("Your grade is 'F'")
