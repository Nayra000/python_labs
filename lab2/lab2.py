#Reverse a String 
print("nayra"[::-1])

print("="*20)

# Check if a String is a Palindrome 
print("tot" == "tot"[::-1])

print("="*20)

#Remove Duplicates from a String 
print("".join(set("nayra")))

print("="*20)

#Find the Longest Word in a String 
text = "Python is a great programming language" 
print(max(text.split(" "),key=len))

print("="*20)


#Find Common Elements Between Two Tuples
tuple1 = (1, 2, 3) 

tuple2 = (2, 3, 4) 

print(set(tuple1) & set(tuple2)) 
# & => intersection between two sets
# | => union between two sets
# - => difference between two sets

print("="*20)

#Write a Python program to find the maximum and minimum value in a dictionary. 

my_dict = {"a": 10, "b": 20, "c": 5}  
print(f"max = {max(my_dict.values())} ,min = {min(my_dict.values())}")
print(f"max = {my_dict[max(my_dict ,key=my_dict.get)]} ,min = {my_dict[min(my_dict ,key=my_dict.get)]}")

print("="*20)

#Merge Two Dictionaries 
dict1 = {"a": 1, "b": 2} 

dict2 = {"c": 3, "d": 4} 

dict1.update(dict2)
print(dict1)

print("="*20)
#Find Common Keys in Two Dictionaries 
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(set(dict1) & set(dict2))


#The longest alphabetical ordered substring
string = input("Enter a string: ")
currStr = longestStr = string[0]
for i in range(1, len(string)):
    if(string[i] >= string[i-1]):
        currStr += string[i]
    else:
        longestStr = max(longestStr, currStr, key=len)
        currStr = string[i]

longestStr = max(longestStr, currStr, key=len)
print("Longest substring in alphabetical order is: ", longestStr)

