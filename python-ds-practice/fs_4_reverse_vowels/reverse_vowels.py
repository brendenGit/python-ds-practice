def reverse_vowels(string):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    >>> reverse_vowels("aeiou")
    'uoiea'

    >>> reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = []
    for char in string:
        if char in 'aeiouAEIOU':
            vowels.append(char)
    vowels.reverse()
    string_lst = list(string)
    for index in range(0, len(string_lst)):
        if string_lst[index] in 'aeiouAEIOU':
            string_lst[index] = vowels[0]
            vowels.pop(0)
    return ''.join(string_lst)