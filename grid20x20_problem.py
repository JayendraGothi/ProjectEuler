def pascal(n):
    """Returns nth rowsof Pascal's triangle."""
    row = [1]
    multiple = [0]
    for x in range(n):
        row=[l+r for l,r in zip(row+multiple,multiple+row)]
    return row

def reverse_pascal(row):
    """Returns recursive addition of all the pascal rows"""
    while(len(row)>1):
        row = [l+r for l,r in zip(row[:-1],row[1:])]
    return row

print long(reverse_pascal(pascal(20))[0])
