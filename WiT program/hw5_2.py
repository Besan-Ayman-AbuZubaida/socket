sum=0
for i in range(20):
    sum+=i
print (f'summation of numbers from 0 to 19 --inclusive-- is = {sum}')
print('*'*100)
#=== Edit the code, so that the user can input the number which he wants
#to end with (0 to x) (x is the user input)   
lastNum=int(input('Enter the number you  want to end with (0 to x)'))
sum=0
for i in range(lastNum+1):
    sum+=i
print (f'summation of numbers from 0 to {lastNum} is = {sum}')
print('*'*100)
# 3- Edit the code, so the user can put the first number and the last
# number (from y to x) (y is the first number that the user will input, and
# x is the last number that the user will input).
firstNum=int(input('Enter the number you  want to start with (0 to x)'))
lastNum=int(input('Enter the number you  want to end with (0 to x)'))
sum=0
for i in range(firstNum,lastNum+1):
    sum+=i
print (f'summation of numbers from {firstNum} to {lastNum} is = {sum}')
print('*'*100)
#Write a code that asks the user to input a letter to give the user the
#number of this letter in the Alphabet.
letter = input("Enter a letter to tell you its order: ")
letter = letter.lower() # convert the letter to lowercase to handle uppercase input
if len(letter) > 1: # make sure the user only inputs one letter
    print("Please enter only one letter!")
elif letter < 'a' or letter > 'z': # make sure the input is a valid letter
    print("Please enter a valid letter!")
else:
    number = ord(letter) - 96 # calculate the number of the letter in the alphabet   a small in ascii =97
    print(f"The number of the letter {letter} is {number}")
print ('*'*100)

# 1- count how many letters “z” are there in the sentence.
# sentence="The lazy dog jumps over the hazy maze, and nearly gets stuck in the blizzard"
sentence=input('Enter you sentence to count any character you want: ')
letterCount=sentence.count('z')
print(f'The sentence "{sentence}" has {letterCount} letter z')
# 2- Edit the code, so that the user can input any letter he wants to count.
sentence=input('Enter you sentence to count any character you want: ')
myletter=input('Enter a letter you want to count: ')
letterCount=sentence.count(myletter.lower())
print(f'The sentence "{sentence}" has {letterCount} letter {myletter}')
print('*'*100)
# Write a code that can exclude the vowel from the sentences.
sentence=input('Enter a sentence to exclude the vowels from: ')
vowels="aeiouAEIOU"
newSentence=""
for char in sentence:
    if char not in vowels:
        newSentence+=char
print(f"original sentence is '{sentence}'")
print(f"sentence without vowels  is '{newSentence}'")