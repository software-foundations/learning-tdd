"""
1 -> Receive an integer number

2 -> know if the humber is multiple of 3 and 5:
    Bacon and eggs

3 -> Know if the number is multiple of 3:
    Bacon

4 -> Know if the number is multiple of 5:
    Eggs

5 -> Know if the number is not multiple of 3 and 5:
    Pass Hungry
"""

def bacon_with_eggs(n: int):
    assert isinstance(n, int), 'n should be int'

    if n % 3 == 0:
        if n % 5 == 0:
            return "Bacon with eggs"
        else:
            return "Bacon"

    elif n % 5 == 0:
        return "Eggs"
    else:
        return "Pass hungry"
