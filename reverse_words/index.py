'''
https://www.interviewcake.com/question/python/reverse-words
'''

def reverse_chars(chars, start, end):
    distance = int((end - start) / 2)
    for j in range(0, distance):
        back_index = (end - j - 1)
        front_index = start + j
        front_value = chars[front_index]
        back_value = chars[back_index]
        chars[front_index] = back_value
        chars[back_index] = front_value

def reverse_words(string):
    chars = list(string)

    reverse_chars(chars, 0, len(chars))

    word_start = 0
    for i, char in enumerate(chars):
        if char == ' ':
            reverse_chars(chars, word_start, i)
            word_start = i + 1

    reverse_chars(chars, word_start, len(chars))

    return ''.join(chars)

message = 'find you will pain only go you recordings security the into if'

print(reverse_words(message))
# returns: 'if into the security recordings you go only pain will you find'
