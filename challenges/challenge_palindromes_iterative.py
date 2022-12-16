def is_palindrome_iterative(word):
    if word == "":
        return False
    last_index = (len(word) - 1)
    for index in range(len(word)):
        first_letter = word[index]
        last_letter = word[last_index]

        if first_letter == last_letter:
            if index >= last_index:
                return True
            last_index -= 1
        else:
            return False
