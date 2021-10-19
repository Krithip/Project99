userInput = input("enter a sentence")
#characterCount = 0
wordCount = 1
for i in userInput:
 #   characterCount=characterCount+1
    if(i == ' '):
        wordCount = wordCount + 1
#print("number of characters in the string is", characterCount)
print("number of words in the string is", wordCount)