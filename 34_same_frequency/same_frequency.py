def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    return counter(str(num1)) == counter(str(num2))
    
def counter(toCompare):
    frequency ={}
    
    for item in toCompare:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency
    