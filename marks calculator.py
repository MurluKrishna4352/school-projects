#Write a Python script to accept marks in three subjects (out of 100) and display its total
#marks and percentage.
sub_1 = float(input("Enter the marks of first subject out of 100:   "))
sub_2 = float(input("Enter the marks of second subject out of 100:   "))
sub_3 = float(input("Enter the marks of third subject out of 100:   "))

print("Total marks: ", sub_1+sub_2+sub_3,"/300")#total marks
print("Percentage marks: ", round((sub_1+sub_2+sub_3)/3),"%")#percentage of given marks
