# add code below ...

def palindrome(word):
    """
    Docstring for palindrome
    
    :param word: the word to check
    """    

    # Make the word lowercase
    word = word.lower()

    # Ignore any non-alphabetical characters
    cleanWord = ''

    for letter in word:
        if letter.isalpha():
            cleanWord += letter

    # Return if the word matches its reverse
    return cleanWord == cleanWord[::-1]



def parentheses(sequence):

  """
  Docstring for parentheses
    
  :param sequence: a sequence containing parentheses to check
  """

  # Count open parentheses that need to be resolved
  openCounter = 0
  for character in sequence:
      # If we find an open parenthesis, the number of open parentheses 
      # will be increased and decreased for closed parentheses
      if character == '(':    
        openCounter += 1
      elif character == ')':
        openCounter -= 1

  # If the openCounter is 0, then all parentheses have been matched
  return openCounter == 0
