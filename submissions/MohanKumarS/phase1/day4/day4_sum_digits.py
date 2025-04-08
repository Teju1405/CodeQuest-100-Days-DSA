n = int(input("Enter a number: ")) # n = variable -> to store a entered number
result = 0 # result = 0 -> Initially the sum result is '0'
while(n > 0): # while loop -> to iterate the block of statement
    m = n % 10 # to get the unit digit
    result = result + m # result gets sum up with the previous result
    n = n // 10 # floor division (//) -> returns only the integer value -> to eliminate the unit digit
print("Sum of digits: ",result) # display the sum result