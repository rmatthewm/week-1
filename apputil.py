def palindrome(word):
    
    word = word.lower()

    cleanWord = ''

    for letter in word:
        if letter.isalpha():
            cleanWord += letter


    return cleanWord == cleanWord[::-1]

    

# add code below ...
