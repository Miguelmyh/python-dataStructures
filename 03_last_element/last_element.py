def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    
    for item in lst:
        if len(lst) == 0:
            return None
            
        return lst[-1] 
    
print(last_element([1, 2, 3]))