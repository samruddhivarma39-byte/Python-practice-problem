num = int(input("Enter a number: ")) 
sum = 0 
num = abs(num) 
while num>0: 
    digit = num % 10 
    sum += digit 
    num = num // 10 
print("Sum of digit: ",sum)