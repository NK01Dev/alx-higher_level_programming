def no_c(my_string):
    result = ""
    for char in my_string:
        if char != 'C' and char != 'c':
            result += char
    new_string = result
    return new_string
