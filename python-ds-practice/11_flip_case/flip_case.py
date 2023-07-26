def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    flipped_phrase = []
    for char in phrase:
        if to_swap.islower():
            if char == to_swap:
                flipped_phrase.append(char.upper())
            elif char.lower() == to_swap:
                flipped_phrase.append(char.lower())
            else:
                flipped_phrase.append(char)
        elif to_swap.isupper():
            if char == to_swap:
                flipped_phrase.append(char.lower())
            elif char.upper() == to_swap:
                flipped_phrase.append(char.upper())
            else:
                flipped_phrase.append(char)
    return ''.join(flipped_phrase)