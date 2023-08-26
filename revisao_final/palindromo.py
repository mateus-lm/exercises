def palindromo(palavra):
    final_string = len(palavra)
    for i in range(final_string):
        if not(palavra[i] == palavra[-i-1]):
            return False
    return True
