# First class method
def to_hex_string(data):
    # empty string to return hex string
    final_data = str()
    # dictionary to convert from RLE to hex
    hex_ = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
            9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    for element in data:
        # adds hex character to empty string
        final_data += hex_[element]
    return final_data


def count_runs(flat_data):
    # number of items in input
    num_element = 0
    # stores element to compare
    previous_element = flat_data[0]
    # number of runs
    num_runs = 1

    for element in flat_data:

        # restarts count if there are more than 15 items in the list
        if num_element == 15:
            num_runs += 1
            num_element = 0

        # compares element to previous element, if same, nothing happens
        if element == previous_element:
            num_element += 1
            num_runs += 0

        # compares element to previous element, if different, adds one to number of runs
        else:
            previous_element = element
            num_element = 1
            num_runs += 1

    return num_runs


def encode_rle(flat_data):
    previous_element = flat_data[0]
    encode = []
    element_times = 0
    for element in flat_data:
        if element_times == 15:
            encode.append(15)
            encode.append(element)
            element_times = 0
        if element == previous_element:
            element_times += 1
        else:
            encode.append(element_times)
            encode.append(previous_element)
            element_times = 1
            previous_element = element
    encode.append(element_times)
    encode.append(previous_element)
    return encode


def get_decoded_length(rle_data):
    new_data = rle_data[0:len(rle_data):2]
    sum = 0
    for element in range(0, len(new_data)):
        sum += new_data[element]
    return sum


def decode_rle(rle_data):
    decode = []
    element_times = rle_data[0:len(rle_data):2]
    element = rle_data[1:len(rle_data):2]
    for i in range(len(element_times)):
        sum = element_times[i] * [element[i]]
        decode.extend(sum)
    return decode


def string_to_data(data_string):
    final_data = []
    hex_ = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
            '9': 9, 'a': 10, 'A': 10, 'b': 11, 'B': 11, 'c': 12, 'C': 12,
            'd': 13, 'D': 13, 'e': 14, 'E': 14, 'f': 15, 'F': 15}
    for character in data_string:
        final_data.append(hex_[character])

    return final_data


if __name__ == "__main__":
    pass
