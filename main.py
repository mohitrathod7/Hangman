from checking import check
from wordfile import get_word
# ----------------------------------------------------------------------------------------------------------------------


def main1():

    word = get_word()
    guesses = []
    guessed = False
    print()
    print("The word contains", len(word), "letters.")
    print("_ " * len(word))

    while not guessed:

        print()
        text = "Please enter one letter or a word of " + str(len(word)) + " letters : "

        guess = input(text).upper()

        if guess.isalpha() == True:
            if guess in guesses:
                print('''
You have already guessed "''' + guess + '".')

            elif len(guess) == len(word):
                guesses.append(guess)
                if guess == word:
                    guessed = True
                else:
                    print('''
Sorry,that is incorrect word.''')
            elif len(guess) == 1:
                guesses.append(guess)
                result = check(word, guesses, guess)
                if result == word:
                    guessed = True
                else:
                    print(result)
            else:
                print("Invalid Entry.")
            
            print()
            print('''You had guessed following letters : ''', guesses[0:len(guesses)])
            
        else:
            print("Please enter only alphabets, not numbers or any other special characters !!!")
             
    print('''
Yes,the word is''', word + "! You got it in", len(guesses), "tries.")


# ----------------------------------------------------------------------------------------------------------------------


def main2():
    word = input('Enter a word : ').upper()
    guesses = []
    guessed = False
    print()
    print("The word contains", len(word), "letters.")
    print("_ " * len(word))
    
    while not guessed:

        print()
        text = "Please enter one letter or a word of " + str(len(word)) + " letters : "
        guess = input(text)
        guess = guess.upper()

        if guess.isalpha() == True:
            if guess in guesses:
                print('''
You have already guessed "''' + guess + '"')

            elif len(guess) == len(word):
                guesses.append(guess)
                if guess == word:
                    guessed = True
                else:
                    print('''
Sorry,that is incorrect''')
            elif len(guess) == 1:
                guesses.append(guess)
                result = check(word, guesses, guess)
                if result == word:
                    guessed = True
                else:
                    print(result)
            else:
                print("Invalid Entry.")
    
            print()
            print('''You had guessed following letters : ''', guesses[0:len(guesses)])
            
        else:
            print("Please enter only alphabets, not numbers or any other special characters !!!")

    print('''
Yes,the word is''', word + "! You got it in", len(guesses), "tries.")
# ----------------------------------------------------------------------------------------------------------------------
