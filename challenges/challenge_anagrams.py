def is_anagram(first_string, second_string):
    if first_string == '' or second_string == '':
        return False

    first_frase = frase_arr(first_string)
    second_frase = frase_arr(second_string)

    merge_sort(first_frase, 0, len(first_frase))  # aqui ele guarda a alteração
    # na propria variavel, não precisando retornar mesma coisa no de baixo
    merge_sort(second_frase, 0, len(second_frase))

    first_okay = ''.join(first_frase)
    second_okay = ''.join(second_frase)

    if first_okay == second_okay:
        return True

    if first_okay.lower() == second_okay.lower():
        return True

    if first_okay != second_okay:
        return False


def merge_sort(palavras, start=0, end=None):

    if end is None:
        end = len(palavras)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(palavras, start, mid)
        merge_sort(palavras, mid, end)
        merge(palavras, start, mid, end)

# função auxiliar que realiza a mistura dos dois arrays


def merge(palavras, start, mid, end):
    left = palavras[start:mid]
    right = palavras[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            palavras[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            palavras[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            palavras[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            palavras[general_index] = right[right_index]
            right_index = right_index + 1


def frase_arr(frase):
    nova_frase = list(frase)
    return nova_frase


# palavras = frase_arr('camelo')

# merge_sort(palavras, 0, len(palavras))
# print(palavras)
# print(is_anagram('camelo', 'meloca'))
