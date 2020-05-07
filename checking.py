def check(word, guesses, guess):
    status = ""
    matches = 0

    for letter in word:
        if letter in guesses:
            status += letter
        else:
            status += "_ "

        if letter == guess:
            matches += 1

    if matches > 1:
        print('''
Yes ! The word contains''', matches, '"' + guess + '"' + "s")

    elif matches == 1:
        print('''
Yes ! The word contains the one letter "''' + guess + '"')

    else:
        print('''
Sorry. The word does not contains the letter "''' + guess + '"')

    return status
