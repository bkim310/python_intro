def print_upper_words(list, letter):
    """changes all strings in a list that start with a certain letter to all uppercase"""
    for let in letter:
        for str in list:
            for char in str:
                if char[0].lower() == let.lower():
                    return str.upper()

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], ["h", "y"])