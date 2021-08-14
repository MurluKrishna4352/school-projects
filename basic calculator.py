#Write a Python script to accept two numbers and display their addition, difference, product,
#division, integer division, remainder and exponent (raise to power).

user_input = float(input("Enter a number: "))
user_input_2 = float(input("Enter another number: "))
print(user_input,"+",user_input_2," = ", user_input + user_input_2,"\n ")
print(user_input,"*",user_input_2," = ", user_input * user_input_2,"\n")
print(user_input,"/",user_input_2," = ", user_input / user_input_2,"\n")
print(user_input,"-",user_input_2," = ", user_input - user_input_2,"\n")
print(user_input_2,"-",user_input," = ", user_input_2 - user_input,"\n")
print(user_input,"%",user_input_2," = ", user_input % user_input_2,"\n")
print(user_input,"^",user_input_2," = ", user_input ** user_input_2,"\n")
print(user_input,"//",user_input_2," = ", user_input // user_input_2,"\n")
