# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    check = False
    count = 0
    for l in secret_word:
        for i in letters_guessed:
          if (i == l):
            count += 1
            if(count == len(secret_word)):
                check = True       
    return check  



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    str=''
    letters = []
    for i in secret_word:
        if (i in letters_guessed):  
            letters.append(i)
        else:  
            letters.append("_ ")  

    for k in letters:
        str += k
    return f"{str}"           



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters = string.ascii_lowercase
    for l in letters :
        if l in letters_guessed:
            letters = letters.replace(l, ' ')
    return letters
                

def unique_letters (secret_word):
    unique = []
    count = 0
    for l in secret_word:
       if l not in unique:
           count += 1
       unique.append(l)    
    return count


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed = []
    
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long. \n -------------")
    gusses_left = 6
    Warnings_left = 3
    vowels = ['a', 'o', 'e', 'u', 'i']
    

    while(gusses_left > 0):
         if (gusses_left != 1):
            print(f"You have {gusses_left} guesses left. ")
            print(f"Available letters: {get_available_letters(letters_guessed)}")
         else:
             print(f"You have {gusses_left} guess left.")
             print(f"Available letters: {get_available_letters(letters_guessed)}")
         
         letter = input("Please guess a letter: ").lower()
         isAlpha = letter.isalpha()
         if letter == '*':
             show_possible_matches(get_guessed_word(secret_word, letters_guessed))
             continue
         if not isAlpha :
            if Warnings_left > 0:     
             Warnings_left -= 1
             print(f"Oops! That is not a valid letter. you'have {Warnings_left} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
            else:
             gusses_left -= 1
             print(f"Oops! That is not a valid letter. you'have {Warnings_left} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
         if letter in letters_guessed and Warnings_left > 0: 
                 Warnings_left -= 1
                 print(f"Oops! You've already guessed that letter. You now have {Warnings_left} warnings {get_guessed_word(secret_word, letters_guessed)}")
                 continue
         elif letter in letters_guessed and Warnings_left < 1:
                 print(f"Oops! You've already guessed that letter. You now have {Warnings_left} warnings {get_guessed_word(secret_word, letters_guessed)}")
                 gusses_left -= 1
                 continue
         letters_guessed.append(letter)
         if all (letter in letters_guessed for letter in secret_word):             
              print(f"good guess: {get_guessed_word(secret_word, letters_guessed)}")
              print("-------------")
              print(f'Congratulations, you won! \nYour total score for this game is: {gusses_left * unique_letters(secret_word)}')
              break 
         if letter in secret_word:
             print(f"good guess: {get_guessed_word(secret_word, letters_guessed)}")
             print("-------------")
         elif letter not in secret_word:
             print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
             print("-------------")
             if letter in vowels:
                 gusses_left -= 2       
             elif isAlpha and letter not in vowels:
                 gusses_left -= 1         
    if (gusses_left <= 0):
        print(f'Sorry, you ran out of guesses. The word was {secret_word}. ')
    
             
                 











# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = str(my_word).replace(" ","")

    if len(my_word) != len (other_word):
      return False              
    
    for i in range (len(other_word)):
        
        if my_word [i] == '_':
            if other_word [i] in my_word:
              return False  
        else: 
          if other_word [i] != my_word[i]:
              return False
          
    return True

        

      
            
   



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    for word in wordlist:
        if match_with_gaps(my_word, word):
            print (word)


                
        
        
        



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    hangman(secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    
    # ---------------------------------------------
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)
    # ---------------------------------------------


    # test to each faunction 
    # ----------------------------------------------
    # l2 = ['e', 'i', 'k', 'p', 'r', 's']
    # print(is_word_guessed('apple', l2))
    # print (get_guessed_word('apple', l2))
    # print (get_available_letters(l2))
    # print(match_with_gaps("te_ t", "tact"))
    # print(match_with_gaps("a_ _ le", "banana"))
    # print(match_with_gaps("a_ _ le", "apple"))
    # print(match_with_gaps("a_ ple", "apple"))
    #-----------------------------------------------
    
    

    # show_possible_matches('_ a_ _ _ t')     
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
