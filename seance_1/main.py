points = {"a":1,"e":1,"i":1,"l":1,"n":1,"o":1,"r":1,"s":1,"t":1,"u":1,"d":2,"g":2,"m":2,"b":3,"c":3,"p":3,"f":4,"h":4,"v":4,"j":8,"q":8,"k":10,"w":10,"x":10,"y":10,"z":10,"?":0}

def longest_word(words) :
    """Return the longest word of words"""
    current = words[0]
    max_length = len(current)
    for word in words[1:] :
        length = len(word)
        if  length > max_length :
            max_length = length
            current = word
    return current

def possible(word, letters) :
    """Test if word can be written with letters"""
    letters_copy = letters.copy()
    for letter in word :
        if not(letter in letters_copy) :
            return False
        letters_copy.remove(letter)
    return True

def possible_with_joker(word, letters) :
    """Test if word can be written with letters, joker version"""
    letters_copy = letters.copy()
    for letter in word :
        if letter in letters_copy :
            letters_copy.remove(letter)
        else :
            if "?" in letters_copy :
                letters_copy.remove("?")
            else :
                return False
    return True

def possible_words(letters) :
    """Return the list of possible words with letters"""
    words = []
    file = open("frenchssaccent.dic", 'r')
    for line in file :
        word = line[0:len(line)-1]
        if possible_with_joker(word, letters) :
            words.append(word)
    file.close()
    return words


def best(letters) :
    """Return the longest word that can be written with letters"""
    words = possible_words(letters)
    return longest_word(words)


def score(word,letters) :
    """Return the score obtained with word and the possible letters"""
    res = 0
    for letter in word :
        if letter in letters :
            #if letter is not in letters, then the joker is used, with score 0
            res += points[letter]
    return res

def max_score(words,letters) :
    """Return the word with the highest score within words and its score"""
    current = words[0]
    max_score = score(current,letters)
    for word in words[1:] :
        word_score = score(word,letters)
        if word_score > max_score :
            max_score = word_score
            current = word
    return current, max_score


def best_score(letters) :
    """Return the word with the highest score that can be written with letters
    and its score
    """
    words = possible_words(letters)
    return max_score(words,letters)



