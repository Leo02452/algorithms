def sort_word(word):
    word_array = list(word)
    for i in range(len(word_array)):
        current_value = word_array[i].lower()
        current_position = i
        while (current_position > 0) and (
            word_array[current_position - 1] > current_value
        ):
            word_array[current_position] = word_array[current_position - 1]
            current_position = current_position - 1
        word_array[current_position] = current_value
    return ''.join(word_array)


def is_anagram(first_string, second_string):
    first_sorted_word = sort_word(first_string)
    second_sorted_word = sort_word(second_string)
    if first_string == '' or second_string == '':
        return (first_sorted_word, second_sorted_word, False)
    return (
        first_sorted_word,
        second_sorted_word,
        first_sorted_word == second_sorted_word
    )
