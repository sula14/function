#Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

def degree_nums(a,b):
    num = a
    for i in range(b-1):
        num = num * a
    return num

a = degree_nums(2, 3)
print(a)