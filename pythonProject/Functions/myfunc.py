def get_sep(sep, sep_len):
    return sep * sep_len

word = '~'
print(get_sep('=', 50))
print(get_sep('+', 100))
print(get_sep(word, 5))

result = get_sep(word, 35)
text = 'Hello {} Func {}'.format(result, result)
text2 = f'Here {result} and here {result}'
print(text)
print(text2)