# Function to swap two characters in a character array
def swap(ch, i, j):
    temp = ch[i]
    ch[i] = ch[j]
    ch[j] = temp


# Recursive function to generate all permutations of a string
def permutations(ch, curr_index=0):
    """
    :param ch: Characters of the string
    :param curr_index: Index value assigned as zero
    :return: Permutations of the given string
    """
    if curr_index == len(ch) - 1:
        print(''.join(ch))

    for i in range(curr_index, len(ch)):
        swap(ch, curr_index, i)
        permutations(ch, curr_index + 1)
        swap(ch, curr_index, i)


if __name__ == '__main__':
    s = 'ABC'
    permutations(list(s))
