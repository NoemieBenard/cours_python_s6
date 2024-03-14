def longest_word(words) :
    current = words[0]
    max_length = len(current)
    for word in words[1:] :
        length = len(word)
        if  length > max_length :
            max_length = length
            current = word
    return current

def possible(word, letters) :
    letters_copy = letters.copy()
    for letter in word :
        if not(letter in letters_copy) :
            return False
        letters_copy.remove(letter)
    return True

def possible_words(letters) :
    words = []
    file = open("frenchssaccent.dic", 'r')
    for line in file :
        word = line[0:len(line)-1]
        if possible(word, letters) :
            words.append(word)
    file.close()
    return words