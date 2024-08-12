# Define function for addition
def add(numbers):
    count = 0
    for i in numbers:
        count = i + count
    return count
# Define function for subtraction
def sub(numbers):
    count = 0
    for i in numbers:
        count = i - abs(count)
    return abs(count)
# Define function for multiplication
def multiply(numbers):
    r_count = 1
    for i in numbers:
        r_count = i*r_count
    return r_count
# Define function for division
def div(numbers):
    result = float(numbers[0]) 
    for number in numbers[1:]:
        if int(number) == 0:
            return "Error: Division by zero is not allowed."
        result /= float(number)
    return result
        
numbers = [int(x) for x in input("Enter the numbers: ").split()] # Take input many numbers from users 
# Calculator operation rule
print("Please select operation -\n" \
        "1. Add\n" \
        "2. Sub\n" \
        "3. Multiply\n" \
        "4. Div\n")
select = int(input("Choose an option: "))
if select==1:
    res = add(numbers)
elif select==2:
    res = sub(numbers)
elif select==3:
    res = multiply(numbers)
elif select==4:
    res = div(numbers)
# Output of the result
print(res)