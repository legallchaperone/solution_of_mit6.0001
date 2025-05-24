import string
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    all_letters = string.ascii_lowercase
    available_letters = ""
    for letter in all_letters:
        if letter not in letters_guessed:
            available_letters += letter
    return available_letters;

letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']

print (get_available_letters(letters_guessed))