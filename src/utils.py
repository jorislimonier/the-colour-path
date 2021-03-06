import unidecode


def digit_from_number(date: str) -> int:
    """Convert a number to the iterative sum of its digits"""
    # convert `date` to a string if it isn't already one
    if not isinstance(date, str):
        date = str(date)

    summed_date = 0

    # iterate over digits in `date`
    for digit in date:
        summed_date += int(digit)

    # recursively sum digits until only one is left
    if len(str(summed_date)) > 1:
        return digit_from_number(str(summed_date))
    else:
        return summed_date


def plain_upper(letter: str) -> str:
    """Converts a letter to its uppercase plain equivalent"""
    letter = unidecode.unidecode(letter)  # remove accent

    # convert to uppercase if necessary
    if not letter.isupper():
        letter = letter.upper()

    return letter


def letter_rank(letter: str) -> int:
    """Gets the number associated to a letter.
    It is simply computed by taking the count of the letter
    in the alphabet modulo 9, then adding 1"""
    base_rank = ord("A")
    letter = plain_upper(letter)
    return (ord(letter) - base_rank) % 9 + 1


def digit_from_str(name: str) -> int:
    """Takes a name, converts it to the rank of its letters,
    then reduces by iteratively summing the obtained digits"""
    number_name = ""

    for letter in name:
        letter_rk = letter_rank(letter)
        number_name += str(letter_rk)
    return digit_from_number(number_name)
