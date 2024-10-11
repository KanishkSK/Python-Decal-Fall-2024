'''
1 Debugging 
As you work through this problem set, whenever you encounter an error, please include a comment explaining what the error was and how you later resolved it. You can add these explanations at any relevant place in the file. Example: 
>>> print("Hello, World!") 
>>> """ 
>>> I encountered the following eror: "SyntaxError: unterminated >>> string literal (detected at line 1) when I wrote >>> print("Hello, World!)". So I added the missing " at the end >>> and the code printed it successfully. 
>>> 
2 Practicing Sliding & Striding 
In this problem, you will practice slicing and striding lists! 
2.1 Making a List Variable 
Create a variable (name it anything you want, but make it descriptive!) that is assigned to a list with numbers 0 through 20. You should not write each number manually. 
>>> whateverNameYouWant = # Your code here 
>>> print(whateverNameYouWant) 
[0, 1, 2, ..., 20] # It should print all numbers 1-20 in a list 

'''
list = []
for i in range(21): 
    list.append(i)

print("2.1: ", list)

'''
2.2 Working with List Elements 
Write a function that will take in your list from Part 2.1 and square each element in the list. Assign the result to a new variable. 
1
>>> whateverNameYouWant = # Your code from Part 2.1 >>> 
>>> def squareList(): 
>>> # Your code here 
>>> 
>>> anotherNameYouWant = squareList(list) 
>>> print(anotherNameYouWant) 
[0, 1, 4, ..., 400] 
'''
def squareList(list):
    list2 = []
    for i in range(len(list)): 
        list2.append(list[i] ** 2)

    return list2

listSquared = squareList(list)
print("2.2: ", listSquared)

'''
2.3 Slicing 
Write a function that takes in your new list from Part 2.2 and returns the first 15 elements of the list using slicing. 
>>> anotherNameYouWant = squareList(list) 
>>> first_fifteen_elements(anotherNameYouWant) 
[0, 1, 4, ..., 196] 
'''
def first_fifteen_elements(list):
    short = list[0:15]
    return short

fifteenList = first_fifteen_elements(listSquared)
print("2.3: ", fifteenList)

'''
2.4 Striding 
Write a function that takes in your list from Part 2.2 and returns every 5th element from the list using striding. 
>>> anotherNameYouWant = squareList(list) 
>>> every_fifth_element(anotherNameYouWant) 
[16, 81, 196, 361] 
'''
def every_fifth_element(list):
    fifth = list[4:len(list):5]
    return fifth

everyFifthList = every_fifth_element(listSquared)
print("2.4: ", everyFifthList)

'''
2.5 Slicing & Striding 
Write a function that takes your list from Part 2.2, slices the last 3 elements of the list, and then returns every 3rd element from that list in reverse order. 
>>> anotherNameYouWant = squareList(list) 
>>> fancy_function(anotherNameYouWant) 
[400, 289, 196, 121, 64, 25, 4]
'''

def fancy_function(list):  
    return list[0:len(list) - 3:3]

fancyList = fancy_function(listSquared)
print("2.5: ", fancyList)


'''
3 2D lists 
3.1 Creating a 5x5 2D List 
Write a function that uses nested for loops to create a 5x5 2D list where the numbers 1 through 25 are stored sequentially. Assign the result to a new vari able. 
>>> matrix = create_2d_list() 
>>> print(matrix) 
[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]] 
'''
def create_2d_list():
    list = []
    num = 1
    inter = []
    '''
    for i in range(5):        
        inter.append(num)
        num += 1

    for j in range(len(inter)): 
        list.append(inter)
    '''
    for i in range(5):  
       for j in range(5):        
            inter.append(num)
            num+=1
        
       list.append(inter)
       inter = []      
       

    return list
 

matrix = create_2d_list() 
print("3.1: ", matrix)

'''
3.2 Replacing 2D List with Multiples of 3 
With the 2D list you created in Part 3.1, write a function that will replace all multiples of 3 with the character “?”. 
>>> matrix = create_2d_list() 
>>> modified_2d_list(matrix) 
[[1, 2, ‘?’, 4, 5], 
[‘?’, 7, 8, ‘?’, 10], 
[11, ‘?’, 13, 14, ‘?’], 
[16, 17, ‘?’, 19, 20], 
[‘?’, 22, 23, ‘?’, 25]] 
'''
def modified_2d_list(matrix): 
    list = []
    for i in range(5):
        for j in range(5): 
            if matrix[i][j] % 3 == 0: 
                matrix[i][j] = '?'
    
    return matrix

matrix = create_2d_list() 

print("3.2: ", modified_2d_list(matrix))

'''
3.3 Summing None-’ ?’ Elements 
Assign the result of your function from Part 3.2 to a variable. Write a function that will iterate through the new 2D list variable and return the sum of all the elements that are not “?”. Hint: Try using “!=”. 
>>> matrix = create_2d_list() 
>>> new_matrix = modified_2d_list(matrix) 
>>> sum_non_question_elements(new_matrix) 
217 
'''
def sum_non_question_elements(new_matrix):
    sum = 0
    for i in range(5):
        for j in range(5): 
            if type(new_matrix[i][j]) == int:
                sum += new_matrix[i][j]
    
    return sum

matrix = create_2d_list() 
new_matrix = modified_2d_list(matrix) 

print("3.3: ", sum_non_question_elements(new_matrix))