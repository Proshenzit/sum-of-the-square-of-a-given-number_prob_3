num = int(input("Enter your number: "))
a = num%10
num = num//10
b = num%10
c =num//10
add = (a**2)+(b**2)+(c**2)
print("your required sum is:",add)