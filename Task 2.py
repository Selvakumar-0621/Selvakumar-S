# Getting 2 list 1 of even and another 1 of odd from a given list

a=[10, 501, 22, 37, 100, 999, 87, 351]  #input
even=[]
odd=[]
for i in a:                             # using for loop 
    if(i % 2==0):                       # Condition to filter even number
        even.append(i)
    else:
        odd.append(i)
print("The even list",even)
print("The odd list",odd)





#Count all prime numbers and create a list of it

a=[10, 501, 22, 37, 100, 999, 87, 351]  #input
num = []
for i in a:
    ans = True
    if i > 2:                           #condition for prime number
        for j in range (2, i):
            if i % j == 0:
                ans = False 
        if ans != False:                #condition for prime number
          num.append(i)
print(num)





# Sum of first and last digit of an Integer

integer = 12345
integer = str(integer)
first_digit = int(integer[0])               #Assigning the 1st digit to a variable
last_digit = int(integer[-1])               #Assigning the last digit to a variable
sum = first_digit + last_digit              #Adding both
print("Sum of first and last digit : ", sum)





# Finding duplicates from 3 lists

list_1 = [1, 2, 3, 4, 5]
list_2 = [2, 4, 6, 7]
list_3 = [1,4, 8, 9]
duplicate = []                            #Variable asigned to store duplicate of list_1 & list_2
duplicate_final = []                      #Variable asigned to store duplicate of found value and list_3
for i in list_1:
    if i in list_2:
        duplicate.append(i)
for i in duplicate:
    if i in list_3:
        duplicate_final.append(i)
print("The duplicate form 3 lists : ", duplicate_final)





# 1st non-repeating elements in a given list of integers

list = [12, 15, 12, 29, 19, 500]
for i in list:
   if list.count(i) < 2:                 #Condition to find non - repeating element
        print("1st Non-Repeating element is : ", i)
        break                            #To stop after finding the 1st non - repeating element






# Triplet from a given list that equals to given value

list = [10, 20, 30, 9]
value = 59
len = len(list)
for i in range (0, len):
    if i < len-2:                            #Condion for getting a triplet
        j = i + 1                            
        k = i + 2                            
        while (k < len):
            if list[i] + list[j] + list[k] == 59:
                print("List of Triplet of which sum eqaul to 59 :", list[i], list[j], list[k])
            j = j + 1
            k = k + 1

    



list_1 = [4, 2, -3, 1, 6]
value = 0
n = len(list_1)
sublist = []
for start in range(n):
     for end in range(start + 1, n + 1):
          sublist.append(list_1[start:end])
for i in sublist:
     if sum(i) == 0:
        print("Sublist of which sum equals to 0 is : ", i)