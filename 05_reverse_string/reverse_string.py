def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    word = list(phrase)
    word.reverse()
    word = "".join(word)
    # print(word)
    return word
    #or word = phrase[::-1]
    
print(reverse_string("hello"))