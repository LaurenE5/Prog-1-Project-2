from console_gfx import ConsoleGfx

# Project 2B
# First class method


def to_hex_string(data):
    # empty string to return hex string
    final_data = str()
    # dictionary to convert from RLE to hex
    hex_ = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
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
    # labels beginning comparison value
    previous_element = flat_data[0]
    # creates empty list
    encode = []
    element_times = 0

    for element in flat_data:

        # if element is listed 15 times
        if element_times == 15:
            encode.append(15)
            encode.append(element)
            element_times = 0

        # if element is the same as the previous element
        if element == previous_element:
            element_times += 1

        # if element is different from previous element
        else:
            encode.append(element_times)
            encode.append(previous_element)
            element_times = 1
            previous_element = element
    # adds to empty list
    encode.append(element_times)
    encode.append(previous_element)

    # returns condensed list
    return encode


def get_decoded_length(rle_data):
    # only looks at odd index values
    new_data = rle_data[0:len(rle_data):2]
    sum = 0

    for element in range(0, len(new_data)):
        # adds together the odd index values
        sum += new_data[element]

    # returns the total number of values in list
    return sum


def decode_rle(rle_data):
    # empty list
    decode = []
    # extracts the number of times elements are repeated
    element_times = rle_data[0:len(rle_data):2]
    # extracts elements
    element = rle_data[1:len(rle_data):2]

    for i in range(len(element_times)):
        # multiplies the elements by the number of times that they are listed
        sum = element_times[i] * [element[i]]
        # puts the values in a list
        decode.extend(sum)

    return decode


def string_to_data(data_string):
    # empty list to return data
    final_data = []
    # dictionary converting string to data
    hex_ = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
            '9': 9, 'a': 10, 'A': 10, 'b': 11, 'B': 11, 'c': 12, 'C': 12,
            'd': 13, 'D': 13, 'e': 14, 'E': 14, 'f': 15, 'F': 15}

    # adds converted string character to list
    for character in data_string:
        final_data.append(hex_[character])

    # returns list
    return final_data


# Project 2C Functions
def to_rle_string(rle_data):
    rle_string = str()
    hex_ = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
            9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}

    num_of_elements = 0
    for character in rle_data:
        num_of_elements += 1

        # adds a colon after every even element
        if num_of_elements % 2 == 0:
            rle_string += hex_[character]
            rle_string += ':'
        else:
            rle_string += str(character)

    # removes it if there are colons at the end of the string
    if rle_string[-1] == ':':
        rle_string = rle_string.rstrip(rle_string[-1])

    return rle_string


def string_to_rle(rle_string):
    final_data = []
    hex_ = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
            '9': 9, 'a': 10, 'A': 10, 'b': 11, 'B': 11, 'c': 12, 'C': 12,
            'd': 13, 'D': 13, 'e': 14, 'E': 14, 'f': 15, 'F': 15}
    # creates elements in a list, one element from each side of the colon
    rle_data = rle_string.split(':')

    for character in rle_data:
        # if element is 3 things long (ex: 15f)
        if len(character) == 3:
            # then the first two are added as they are
            final_data.append(int(character[0:2]))
            # the last element is converted, and then added to the list
            final_data.append(hex_[character[2]])
        else:
            # for each element in the string within the list
            for element in character:
                # converts each element into hex
                final_data.append(hex_[element])

    return final_data


# main project
def main():
    # Display welcome message
    print('Welcome to the RLE image encoder!')
    print('\n')
    print('Displaying Spectrum Image: ')

    # display spectrum message
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)

    image_data = None

    while True:
        # print all the menu options
        print('\n'),
        print('RLE Menu'),
        print('--------'),
        print('0. Exit'),
        print('1. Load File'),
        print('2. Load Test Image'),
        print('3. Read RLE String'),
        print('4. Read RLE Hex String'),
        print('5. Read Data Hex String'),
        print('6. Display Image'),
        print('7. Display RLE String'),
        print('8. Display Hex RLE Data'),
        print('9. Display Hex Flat Data'),
        print('\n')

        # prompt the user for menu option
        option = int(input('Select a Menu Option: '))

        if option == 0:
            break

        elif option == 1:

            # prompt the file name entered by user
            filename = input('Enter name of file to load: ')

            # store ConsoleGfx.load_file(filename) in image_data variable
            image_data = ConsoleGfx.load_file(filename)

        elif option == 2:

            # store the ConsoleGfx.test_image into image_data variable
            image_data = ConsoleGfx.test_image
            print('Test image data loaded.')

        # RLE String
        elif option == 3:
            string = input('Enter an RLE string to be decoded: ')

            # Read input and convert to list
            final_data = string_to_rle(string)
            decode = decode_rle(final_data)

        elif option == 4:
            hex_string = input('Enter the hex string holding RLE data: ')

            # Reads hex string input and convert to a list
            final_data = string_to_data(hex_string)
            decode = decode_rle(final_data)

        elif option == 5:
            flat_data = input('Enter the hex string holding flat data: ')

            # translates a string to hex format
            final_data = string_to_data(flat_data)
            # saves hex string and decompresses rle data
            decode = decode_rle(final_data)

        elif option == 6:

            print('Displaying image...')
            # display the image_data using ConsoleGfx.display_image(image_data)
            print(ConsoleGfx.display_image(image_data))

        elif option == 7:
            # compresses rle data
            encode = encode_rle(decode)
            # prints hex string w colon in between
            rle_string = to_rle_string(encode)
            print('RLE representation: ', rle_string)

        elif option == 8:
            # compresses rle data
            encode = encode_rle(decode)
            # prints hex string without colons
            final_data = to_hex_string(encode)

            print('RLE hex values: ', final_data)

        elif option == 9:
            # prints decompressed rle data with hex values
            string = to_hex_string(decode)
            print('Flat hex values: ', string)
    return


if __name__ == "__main__":
    main()
