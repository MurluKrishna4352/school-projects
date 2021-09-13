# wap to take percentage and display the grade
#> 90    A
#> 80 nd <=90 B
#>=60 nd <=80 C
#<60    D

percent = float(input("Enter your percent: "))

if(percent>90):
    print("Your grade is : A")

elif(percent <= 90 and percent >80):
    print("Your grade is : B")

elif(percent <= 80 and percent >60):
    print("Your grade is : C")

elif(percent < 60):
    print("Your grade is : D")
