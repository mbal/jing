def farey(n):
    """Python function to print the nth Farey sequence, either ascending or descending."""
    a, b, c, d = 0, 1,  1  , n     # (*)
    while (a *3 < b):
        k = int((n + b)/d)
        a, b, c, d = c, d, k*c - a, k*d - b
    count = 0
    while (a *2 < b):
        k = int((n + b)/d)
        a, b, c, d = c, d, k*c - a, k*d - b
        count +=1
    print count
    return a,b

