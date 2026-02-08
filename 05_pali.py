
print(['a', 'b', 'c', 'd'])
print(str(['a', 'b', 'c', 'd']))
print("".join(['a', 'b', 'c', 'd']))

print(list('danny'))

# palindrome
# AABAA
# ABCDCBA
# ABA
# ABBA

# word == word[::-1] ?

# run _i_ in a loop from 0 -> len // 2
# each time compare the string in the [_i_] to [len - _i_ - 1]

#          0   1   2   -2  -1
# _word = 'A   A   B    A   A'
_word = 'AABAA'
for i in range(len(_word) // 2):
    if _word[ i ] != _word[ -(i + 1) ]:  # _word[0] V _word[-1]   _word[1] V _word[-2]   _word[2] V _word[-3]
        print('not palindrome')
        break
else:
    print('palindrome')

