def break_word(stuff):
    words = stuff.split(' ')
    return words
    #thids will help you to break up the phrases

def sort_word(words):
    return sorted(words)

def print_first_words(words):
    word = words.pop(0)
    print(word)

def print_last_words(words):
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    words = break_word(sentence)
    return sort_word(words)

def print_first_and_last(sentence):
    words =break_word(sentence)
    print_first_words(words)
    print_last_words(words)

def print_first_and_last_sorted(sentence):
    words =sort_sentence(sentence)
    print_first_words(words)
    print_last_words(words)
