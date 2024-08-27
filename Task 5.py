#1 -Number of Vovwels and count of each Vowel in a string

word = "Guvi Geeks Network Private Limited"
vowels = 0
list1 = ["a", "e", "i", "o", "u"]
for char in word:
    if char in list1:
        vowels = vowels+1

# For loop used to count total number of Vowels in  the string

print("The Number of vowels are:", vowels)

# Assigned individual variable to count each individual number of Vowels

a_count = word.count("a")
e_count = word.count("e")
i_count = word.count("i")
o_count = word.count("o")
u_count = word.count("u")
print("The Number of a is:", a_count)
print("The Number of e are:", e_count)
print("The Number of i are:", i_count)
print("The Number of 0 is:", o_count)
print("The Number of u is:", u_count)



#2 Creating pyramid from numbers 1 to 20

for i in range(0, 20):
    for j in range(20 - i):
        print(" ", end = " ")
    for j in range (1, i):
        print(j, end = " ")
    for i in range(i, 0, -1):
        print(i, end = " ")
    print("\n")






#3 Removing vowels in a string

word = "Guvi Geeks Network Private Limited"
list1 = ["a", "e", "i", "o", "u"]
for char in list1:
    word = word.replace(char, "")
print("New Word - ", word)




#4 Returning number of unique charcters in a string

ord = "Guvi Geeks Network Private Limited"
for char in word:
    if word.count(char) == 1:
        print(char)





#5 Plaindrome

# True case
word = "malayalam"
a = word[::-1]
if word == a:
    print("True")
else:
    print("False")

# False case
word = "Selvakumar"
a = word[::-1]
if word == a:
    print("True")
else:
    print("False")





#6  Returning longest common substring

s1 = ("selvakumar")
s2 = ("ashokselvan")
def longest_common_substring_naive(s1, s2):
    max_len = 0
    end_index = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            k = 0
            while (i + k < len(s1) and j + k < len(s2) and s1[i + k] == s2[j + k]):
                k += 1
            if k > max_len:
                max_len = k
                end_index = i
    return s1[end_index:end_index + max_len]
print("Longest Common Substring:", longest_common_substring_naive(s1, s2))





#7 Returning most frequent character in a given string

word = "Guvi Geeks Network Private Limited"
temp = 0
ans = ""
for i in word:
    count = word.count(i)
    if count>temp:
        temp = count
        ans = i
print(ans)




#8 Anagram


# False Case
string1 = ("ABC")
string2 = ("DEF")
if (len(string1) == len(string2)):

#Sorting the strings and assigning it to a variables to compare them

    sorted_string1 = sorted(string1)
    sorted_string2 = sorted(string2)
    if (sorted_string1 == sorted_string2):
       print("The given strings are Anagram")
    else:
        print("The given strings are not Anagram")


# True Case
s1 = ("silent")
s2 = ("litsen")
if (len(s1) == len(s2)):

#Sorting the strings and assigning it to a variables to compare them

    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)
    if (sorted_s1 == sorted_s2):
       print("The given strings are Anagram")
    else:
        print("The given strings are not Anagram")






#9 Returning number of words in string

word = "Guvi Geeks Network Private Limited Task Completed"

#Split function is used here to exclude the count of spaces in the given string

string = word.split()
print(len(string))
    