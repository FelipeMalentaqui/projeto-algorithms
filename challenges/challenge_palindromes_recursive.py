def is_palindrome_recursive(word, low_index, high_index, nome=''):
    # print(high_index)
    if word == '':
        return False

    nome += word[high_index]

    if word == nome:
        return True

    if high_index == low_index:
        return False

    else:
        return is_palindrome_recursive(word, low_index, high_index - 1, nome)


# word = "ANA"
# a = len(word - 1)
# saída: True

# word = "SOCOS"
# saída: True

# word = "REVIVER"
# saída: True

# word = "COXINHA"
# saída: False

# word = "AGUA"
# saída: False

# Em Python, None equivale ao valor nulo (null).
# Podemos iniciar as variáveis com o valor None .
# print(is_palindrome_recursive(word, 0, a))
# is_palindrome_recursive((word, 0, len(word - 1)))
