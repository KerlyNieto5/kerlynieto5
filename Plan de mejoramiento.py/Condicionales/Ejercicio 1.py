#Escriba un programa en Python que acepte 3 números y calcule el mínimo
num1 = 7
num2 = 4
num3 = 9

if num1 < num2:
    if num1 < num3:
        min_num = num1
    else:
        min_num = num3
elif num2 < num3:
    min_num = num2
else:
    min_num = num3

print(min_num)