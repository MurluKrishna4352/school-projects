#Write a Python script to accept two numbers and display their addition, difference, product,
#division, integer division, remainder and exponent (raise to power).

user_input = float(input("Enter a number: "))
user_input_2 = float(input("Enter another number: "))
print(user_input,"+",user_input_2," = ", user_input + user_input_2,"\n ")# ADDITION
print(user_input,"*",user_input_2," = ", user_input * user_input_2,"\n")# MULTIPLICATION
print(user_input,"/",user_input_2," = ", user_input / user_input_2,"\n")# DIVISION
print(user_input,"-",user_input_2," = ", user_input - user_input_2,"\n")# sUBTRACTION
print(user_input_2,"-",user_input," = ", user_input_2 - user_input,"\n")# SUBTRACTION
print(user_input,"%",user_input_2," = ", user_input % user_input_2,"\n")#REMAINDER
print(user_input,"^",user_input_2," = ", user_input ** user_input_2,"\n")# POWER
print(user_input,"//",user_input_2," = ", user_input // user_input_2,"\n")#FLOOR
