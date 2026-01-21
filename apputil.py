# add code below ...

def palindrome(word):
    
    word = word.lower()

    cleanWord = ''

    for letter in word:
        if letter.isalpha():
            cleanWord += letter


    return cleanWord == cleanWord[::-1]

    
def parentheses(sequence):
  openCounter = 0
  for character in sequence:
      if character == '(':    
        openCounter += 1
      elif character == ')':
        openCounter -= 1

  return openCounter == 0
