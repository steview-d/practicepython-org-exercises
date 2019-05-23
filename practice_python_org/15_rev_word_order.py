def reverse_string_words(str):
    return ' '.join(str.split(' ')[::-1])


print(reverse_string_words("This is a string that needs reversing"))