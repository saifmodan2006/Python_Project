# 1) Count Vowels in a String

# Task: Take a string input from the user and count how many vowels (a, e, i, o, u) it contains.

text = input("Enter your value:")
vowels = 'aeiou'
count = 0

for working in text.lower():
    if working in vowels:
        count += 1
print(f"Vowel Count {count}")

print("******----------------------------------******")


a =[1,2,3]
b =[4,5,6]

result = []

for i in a:
    if i not in b:
        result.append(i)
for i in b:
    if i not in a:
        result.append(i)

print(result)


print("******------------------------******")

# 2) Unique Elements from Two Lists

# Task: Given two lists, create a new list containing only elements that appear in either list but not both.
# exp:
# a = [1,2,3]
# b= [1,456,2]
# output = [456, 3]


a = [4, 5, 6]
b = [5, 7, 8]

result = []

for i in a:
    if i not in b:
        result.append(i)

for i in b:
    if i not in a:
        result.append(i)

print(result)


print("****----------------------****")

# 3) Word Frequency Counter
# Task: Take a sentence from user input and create a dictionary where keys are words and values are the number of times the word appears.


line = input("Enter a sentence: ")

count = {}
for word in line.split():
    count[word] = count.get(word, 0) + 1

print(count)
