def apply_to_all(map_fn, s):
    return [map_fn(x) for x in s]

def keep_if(filter_fn, s):
    return [x for x in s if filter_fn(x)]

def reduce(reduce_fn, s, initial):
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced, x)
    return reduced

def flatten(lst):
    if not lst:
        return []
    if type(lst[0]) is list:
        return flatten(lst[0]) + flatten(lst[1:])
    return [lst[0]] + flatten(lst[1:])

# Q6
def deep_len(lst):
    """Returns the deep length of the list.

    >>> deep_len([1, 2, 3])     # normal list
    3
    >>> x = [1, [2, 3], 4]      # deep list
    >>> deep_len(x)
    4
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> deep_len(x)
    6
    """
    "*** YOUR CODE HERE ***"
    # combine while loop with recurrsion
    if not lst:
        return 0
    if type(lst[0]) is list:
        return deep_len(lst[0]) + deep_len(lst[1:])
    else:
        return 1 + deep_len(lst[1:])
    # return len(flatten(lst)) ctrl / to comment everything
    # def helper(n):
    # if type(n) != list:
    #     return lst
    # else:
    #    return sum([helper(b) for b in lst],[])

    # return helper(lst)


    
# Q7
def merge(lst1, lst2):
    """Merges two sorted lists recursively.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    "*** YOUR CODE HERE ***"
    if lst2 == []:
        return lst1
    if lst1 == []:
        return lst2
    elif lst2[0] < lst1[0]:
        return [lst2[0]] + merge(lst1,lst2[1:])
    else:
        return [lst1[0]] + merge(lst1[1:], lst2)
# Q11
def coords(fn, seq, lower, upper):
    """
    >>> seq = [-4, -2, 0, 1, 3]
    >>> fn = lambda x: x**2
    >>> coords(fn, seq, 1, 9)
    [[-2, 4], [1, 1], [3, 9]]
    """ 
    "*** YOUR CODE HERE ***"
    return [[x,fn(x)] for x in seq if lower <= fn(x) <= upper]
# Q13
def deck():
    "*** YOUR CODE HERE ***"
    return [[x,s] for x in range(1,14) for s in ['clubs', 'diamonds', 'hearts', 'spades']]

def sort_deck(deck):
    "*** YOUR CODE HERE ***"
    deck.sort(key = lambda x: x[0])
    deck.sort(key = lambda x: x[1])





def get_seven_a(x):
    """
    >>> x = [1, 3, [5, 7], 9]
    >>> get_seven_a(x)
    7
    """
    "*** YOUR CODE HERE ***" 
    return x[2][1]

def get_seven_b(x):
    """
    >>> x = [[7]]
    >>> get_seven_b(x)
    7
    """
    "*** YOUR CODE HERE ***" 
    return x[0][0]

def get_seven_c(x):
    """
    >>> x = [1, [2, [3, [4, [5, [6, [7]]]]]]]
    >>> get_seven_c(x)
    7
    """
    "*** YOUR CODE HERE ***" 
    return x[1][1][1][1][1][1][0]