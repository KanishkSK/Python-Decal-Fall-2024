'''
1 Oski Stole Your Power 
Oski hacked your computer and you can no longer use x**y or pow(x, y). Find a different way (by writing a function) that can compute x raised to the power of y. 
'''
def computePower(x,y):

    ans = 0;

    for i in range(y):
      ans *= x


    return ans

'''
2 What Should I Wear? 
You are trying to decide what to wear to the Python DeCal lecture, but you are only concerned about the day’s lowest and highest temperatures. Write a function that takes in a list as input and returns a tuple with the min and max as two values. 
>>> readings = [15, 14, 17, 20, 23, 28, 20] 
>>> temperatureRange(readings) 
(14, 28) 
'''
def temperatureRange (readings):
    return (min(readings), max(readings)) 

readings = [15, 14, 17, 20, 23, 28, 20] 
print("2: ",temperatureRange(readings))

'''
3 Check if its the Weekend 
All your classes have assigned problem sets due next week, and you want to check if it’s the weekend so you have time to work on them. Write a function that takes a day of the week (represented as an integer, where 1 = Monday, 2 = Tuesday, etc) and returns True if its a weekend and False if otherwise. 
>>> day = 6 # Saturday 
>>> isWeekend(day) 
True 
'''

def isWeekend(day):
    return (day == 6 or day ==7)

day = 6 # Saturday 
print("3: ",isWeekend(day))

'''
4 Fuel Efficiency Calculator 
The Python DeCal wants to take a trip to the Lick Observatory ( San Jose, CA) and they want to pick the best car. Write a function that takes the distance traveled (in miles) and the amount of fuel consumed (in gallons) as input and returns the fuel efficiency. 
>>> distance = 70 # miles 
>>> fuel = 21.5 # gallons 
>>> fuel_efficiency(distance, fuel) 
3.26 
'''

def fuel_efficiency(distance,fuel): 
    return distance/fuel

distance = 70 # miles 
fuel = 21.5 # gallons 
print("4: ",fuel_efficiency(distance, fuel))

'''
5 Secret Code 
Write a function that takes an integer as input and moves its last digit to the front of the number. You may NOT convert the input to a string. Hint: Try modulus (%) and floor division. (\\) to solve this problem. 
>>> n = 12345 
>>> decodeNumbers(n) 
51234 
'''

def decodeNumbers(n): 

    numofdigits = 0
    loop = n

    while loop > 0: 
        numofdigits +=1
        loop = loop // 10

    return n // 10 + ((n %10) * (10 ** (numofdigits-1)))

n = 12345 
print("5: ", decodeNumbers(n))

'''
6 Min & Max but with Loops! 
Oh no! Oski hacked you computer again... now you have lost the ability to use min() and max(). 
6.1 For Loops 
Write two functions to manually find the minimum and maximum values in a list of numbers with for loops. 
>>> nums = [2024, 98, 131, 2, 3, 72] 
>>> find_min_with_for_loop(nums) 
2 
>>> find_max_with_for_loops(nums) 
2024 
'''


def find_min_with_for_loop(nums): 
    a = nums[0]
    for i in range(len(nums)): 
        
        if nums[i] < a:
            a = nums[i]

    return a

def find_max_with_for_loop(nums): 
    a = nums[1]
    for i in range(len(nums)):
        
        if nums[i] > a:
         a = nums[i]

    return a

nums = [2024, 98, 131, 2, 3, 72] 
print("6.1: min - ", find_min_with_for_loop(nums)) 

print("6.1: max - ", find_max_with_for_loop(nums)) 
 
'''
6.2 While Loops 
Write two functions to manually find the minimum and maximum values in a list of numbers with while loops. 
>>> nums = [2024, 98, 131, 2, 3, 72] 
>>> find_min_with_while_loop(nums) 
2 
'''

def find_min_with_while_loop(nums):
    index = 0
    a = nums[0]

    while index < len(nums): 
        if a > nums[index]: 
            a = nums[index]
        index+=1
    return a


def find_max_with_while_loop(nums):
    index = 0
    a = nums[0]

    while index < len(nums): 
        if a < nums[index]: 
            a = nums[index]
        index+=1
    return a

nums = [2024, 98, 131, 2, 3, 72] 
print("6.2: min - ", find_min_with_while_loop(nums))

'''
7 Counting Vowels 
Write a function that takes a string as an input and returns the number of vowels in the string and the number of consonants in the string as tuple. Don’t forget about capital letters! Hint: You can use .isalpha() to check if a character is a letter. 
>>> text = "UC Berkeley, founded in 1868!" 
>>> vowel_and_consonant_count(text) 
(4, 11) 
'''
# shouldn't it be (8,11)
def vowel_and_consonant_count(text): 
    vowel_count = 0 
    consonant_count = 0
    
    for i in range(len(text)):  
        if text[i:i+1].isalpha() == False: 
            continue
        if text[i:i+1].lower() == 'a' or text[i:i+1].lower() == 'e' or text[i:i+1].lower() == 'i' or text[i:i+1].lower() == 'o' or text[i:i+1].lower() == 'u':
          vowel_count +=1

        else: 
          consonant_count += 1 

    return (vowel_count, consonant_count)

text = "UC Berkeley, founded in 1868!" 

print("7: ", vowel_and_consonant_count(text))


'''
8 Calculate Digital Root 
Write a function that takes an integer as an input and returns the sum of its digits. 
>>> num = 2468 
>>> digital_root(num) 
20 
'''
def digital_root(num): 

    limit = num
    sum = 0
    while limit > 0: 
        sum += limit % 10
        limit = limit // 10

    return sum

num = 2468 
print("8: ", digital_root(num))
