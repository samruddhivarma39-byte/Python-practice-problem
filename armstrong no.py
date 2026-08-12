n = int(input("Enter a number: ")) 
temp = n 
sum = 0 
digits = len(str(n)) 
while temp >0: 
    digits = temp % 10 
    sum += digits ** digits 
    temp //= 10 
if sum == n: 
    print(n,"is an armstrong number") 
else: 
    print(n, "is not strong armstrong")