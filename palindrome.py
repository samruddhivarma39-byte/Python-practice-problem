user_input = input("Enter a string: ") 
clean_text = user_input.lower() 
reversed_text = "" 
for char in clean_text: 
    reversed_text = char + reversed_text 
if clean_text == reversed_text: 
    print("Yes, its a palindrome!") 
else: 
    print("No, its not a palindrome.")