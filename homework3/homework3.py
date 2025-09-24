def say_goodbye(name):
    return(print("Goodbye,", name))

def circle_area(radius):
    area = 3.14 * (radius ** 2)
    return(print(area))

def subtract(a, b):
    return(print(a - b))

def multiply(a, b):
    return(print(a * b))

def divide(a, b):
    return(print(a / b))

def temperatures(*readings):
   lowest = min(readings)
   highest = max(readings)
   return(print((lowest, highest)))

#temperatures(14, 26, 86, 3)

def is_weekend(num):
    if num == 6 or num == 7:
        return(print("Its the Weekend!"))
    else:
        return(print("Its not the weekend"))

#is_weekend(7)

def fuel_efficiency(miles, gallons):
    return(print(miles / gallons))

def secret_number(num1):
    length = (len(str(num1)))
    last_digit = num1 % 10
    rest = num1 // 10
    return(print(last_digit * (10 ** (length - 1)) + rest))
    
#secret_number(12345)

def power(x, y):
    start = 1
    for i in range(y):
        start *= x
    return(print(start))
    
def find_min(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return print(minimum)

find_min([12, 5, 6, 99])

def find_max(numbers1):
    maximum = numbers1[0]
    for num1 in numbers1:
        if num1 > maximum:
            maximum = num1
    return(print(maximum))
    
def find_min_while(value):
    i = 0
    minimum = value[0]
    while i < len(value):
        if value[i] < minimum:
            minimum = value[i]
        i += 1
    return(print(minimum))

def find_max_while(value1):
    i = 0
    maximum = value1[0]
    while i < len(value1):
        if value1[i] > maximum:
            maximum = value1[i]
        i += 1
    return(print(maximum))



def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10   
        n //= 10          
    return(print(total))
sum_of_digits(12345)
# My favotite function I made was the secret number one (5.4)
secret_number(123456)
