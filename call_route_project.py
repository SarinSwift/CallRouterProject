
# 1. looping through array
# array = [+1512, +1415, ...]
# dict = [+1512: 0.04, +1415: 0.02, ...]

# -loop through carrier routes
# -create empty string
#   - if it is a substring of the number,
        # check if it's longer than our current string variable:
            # replace the variable string with that number that matched
            # else: we can skip
#   - if it's not, continue
# then use this string variable we created to map to the correct value in the dictionary

def firstSolution(number):
    '''use the cmd+f in our file to find the prefix the number's prefix'''






# ------------------------------------------------------------------------------------------------------------------

def read_words(filename):
    '''takes in a text file and returns an array of strings'''
    return [line.strip() for line in open(filename)]

def create_dict(word_list):
    '''takes in an array of strings, and returns a dictionary of
    key - router number
    value - price
    runtime: O(n) where n is the number of the router_price in the word_list'''
    dict = {}

    for str in word_list:
        number = str[:-5]          # '+8130'
        price = str[-4:]           # '0.32'
        dict[number] = price

    return dict

def secondSolution(number):
    '''
    runtime: O(n) where n is the number of key-value pairs in the dictionary'''

    # arrayRoutes = read_words('route-costs-106000.txt')
    arrayRoutes = read_words('route-costs-106000.txt')
    dictRoutes = create_dict(arrayRoutes)

    lowest_price = 100.00
    longNumber = number
    for router in dictRoutes.keys():
        if longNumber.startswith(router):
            if float(dictRoutes[router]) < lowest_price:
                lowest_price = float(dictRoutes[router])
    if lowest_price == 100.00:
        return None
    return lowest_price







# ------------------------------------------------------------------------------------------------------------------

def turn_to_array_tuple(file_name):
    '''turns a file into the number and price tuple
    ex. [(8130, '0.68'), (86153, '0.32')]
    '''
    router_price = []
    f = open(file_name)
    for line in f:
        line = line.strip().split(',')      # '[[+3330027], [0.39]]'
        number = line[0]
        price = line[1]
        router_price.append((int(number), price))
    f.close()

    router_price.sort()

    return router_price

def turn_to_numbers(filename):
    '''takes in a text file and returns an array of strings
    ex. [15124156620, 14152345678, ...]
    '''
    numbers_list = []
    f = open(filename)
    for line in f:
        line = line.strip()
        numbers_list.append(int(line))
    f.close()
    return numbers_list

def binary_search_recursive(array, item, left=None, right=None):
    '''returns the price in the router array of tuples, if the router number is the prefix of our number
    ex. returns either None, or 0.05 which is the price of the found router number
    '''
    if right == None:
        left = 0
        right = len(array) - 1
    elif left > right:
        return None
    middleIndex = (left + right) // 2
    middleVal = array[middleIndex][0]       # middleVal is the firdst item in the tuple (router number)
    if middleVal == item:
        return array[middleIndex][1]        # returning the price of the matched router number
    if middleVal < item:                    # need to search in the right side of array
        left = middleIndex + 1
    elif middleVal > item:                  # need to search in the left side of array
        right = middleIndex - 1

    return binary_search_recursive(array, item, left, right)


def third_solution():
    '''Implementing binary search
    currently returns an array of [number, costToCall]
    ex. [['+14237515032', '0.05'], ['+14815535238', 0], ['+14235244135', '0.05']]
    '''
    # Create an array of tuples from the router costs
    list_numbers = turn_to_numbers('phone-numbers-100.txt')
    array_tuples = turn_to_array_tuple('route-costs-106000.txt')        # [(86153, '0.84'), ...]

    # todo: create text file as follows: +8615345522316,0.84
    #                                   +8130345522316,0.68
    #                                   +4491878473600,0.48
    #                                   +4452312234601, 0

    final_array = []

    for num in list_numbers:
        curr_number = num
        while str(curr_number) != '':
            searched_num = binary_search_recursive(array_tuples, curr_number)
            print(searched_num)
            if searched_num == None:
                cut_int = str(curr_number)[:-1]
                if cut_int == '':
                    final_array.append([('+'+str(num)), 0])
                    break
                curr_number = int(cut_int)
            else:
                final_array.append([('+'+str(num)), searched_num])
                break

    return final_array


def main():
    # print(secondSolution('+449275049'))      # 0.49
    # print(secondSolution('+861532344'))      # 0.84
    # print(secondSolution('+1718428566'))     # None

    print(third_solution())


if __name__ == '__main__':
    main()
