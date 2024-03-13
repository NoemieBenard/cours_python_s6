def longest_word(word_list) :
    current = word_list[0]
    max_length = len(current)
    for word in word_list[1:] :
        length = len(word)
        if  length > max_length :
            max_length = length
            current = word
    return current