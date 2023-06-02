def is_palindrome_recursive(word, low_index, high_index):
    print(high_index)

    nome = word[high_index]

    if word == nome:
        return True

    if high_index == low_index:
        return False

    else:
        nome += word[high_index]
        is_palindrome_recursive(word, low_index, high_index - 1)


word = "ANA"
a = len(word - 1)
# saída: True

# word = "SOCOS"
# saída: True

# word = "REVIVER"
# saída: True

# word = "COXINHA"
# saída: False

# word = "AGUA"
# saída: False

print(is_palindrome_recursive(word, 0, a))
# is_palindrome_recursive((word, 0, len(word - 1)))
