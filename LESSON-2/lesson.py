# First problem to solve – Count the occurrence of each vowel in the sentence given as input by the user. 

vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}

string = (input("Enter a sentence")).lower()

for letter in string:
    if letter in vowels:
        
        vowels[letter]+=1

print(f"Your string has {vowels['a']} A, {vowels['e']} E, {vowels['i']}, I, {vowels['o']} O and {vowels['u']} U")
print(f"Total number of vowels = {sum(list(vowels.values()))}")


# Slight modification to the previous problem – 
# Count the occurrence of each alphabet that occurs in the sentence given as input by the user.

alphabets = {}

for letter in string:
    if letter == " ": continue
    if letter in alphabets:
        alphabets[letter]+=1
    else:
        alphabets[letter]=1

print(alphabets)


# Problem – 2 Find if a given number entered by the user is a pangram or not ? 
# A pangram number is a number which contains at least once occurrence of each number.
number = input("Enter a number: ")

if len(number)<10:
    print("Not a panagram")
else:
    digits = {}
    for i in range(len(number)):
        if number[i] not in digits:
            digits[number[i]]=1
    
    if len(digits)>=10: print("Its a panagam")
    else: print("Its not a panagram")


# Problem 3: make a student register by taking the user input.