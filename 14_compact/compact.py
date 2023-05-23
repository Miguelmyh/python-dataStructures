def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    return [element for element in lst if element]
#for element in lst:
#if element:
#   lst.append(element)
#return lst
    
print(compact([0, 1, 2, '', [], False, (), None, 'All done']))