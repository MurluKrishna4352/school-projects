#wap to check that you are allowed to vote or not

name = input("Enter your name: ")
age = int(input("Enter your age: "))
out = " %s you can vote"%name
out_1 = " %s you can't vote"%name
if (age>=18):
    print(out)
else:
    print(out_1)
