def to_rle_string(rle_data):
    rle_string = str()
    hex_ = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
            9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}

    num_of_elements = 0
    for character in rle_data:
        num_of_elements += 1
        if num_of_elements % 2 == 0:
            rle_string += hex_[character]
            rle_string += ':'
        else:
            rle_string += str(character)

    if rle_string[-1] == ':':
        rle_string = rle_string.rstrip(rle_string[-1])

    return rle_string


def string_to_rle(rle_string):
    final_data = []
    hex_ = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
            '9': 9, 'a': 10, 'A': 10, 'b': 11, 'B': 11, 'c': 12, 'C': 12,
            'd': 13, 'D': 13, 'e': 14, 'E': 14, 'f': 15, 'F': 15}
    rle_data = rle_string.split(':')

    for character in rle_data:
        if len(character) == 3:
            final_data.append(int(character[0:2]))
            final_data.append(hex_[character[2]])
        else:
            for element in character:
                final_data.append(hex_[element])

    return final_data


if __name__ == "__main__":
    final_data = string_to_rle("13d:7f")
    print(final_data)
