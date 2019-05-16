# Routing project challenge 2


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
    middleVal = array[middleIndex][0]       # middleVal is the first item in the tuple (router number)
    if middleVal == item:
        return array[middleIndex][1]        # returning the price of the matched router number
    if middleVal < item:                    # need to search in the right side of array
        left = middleIndex + 1
    elif middleVal > item:                  # need to search in the left side of array
        right = middleIndex - 1

    return binary_search_recursive(array, item, left, right)


def second_solution():
    '''Implementing binary search
    currently returns an array of [number, costToCall]
    ex. [['+14237515032', '0.05'], ['+14815535238', 0], ['+14235244135', '0.05']]
    '''

    # Create an array of all our phone numbers
    # Create an array of tuples from the router costs
    list_numbers = turn_to_numbers('phone-numbers-1000.txt')            # [15124156620, ...]
    array_tuples = turn_to_array_tuple('route-costs-106000.txt')        # [(86153, '0.84'), ...]

    # todo: create text file as follows: +8615345522316,0.84
    #                                   +8130345522316,0.68
    #                                   +4491878473600,0.48
    #                                   +4452312234601, 0

    final_array = []

    # Loop throuhg all the numbers we want to find and search for the price using the binary method
    for num in list_numbers:
        curr_number = num                # 15124156620
        while str(curr_number) != '':
            searched_num = binary_search_recursive(array_tuples, curr_number)

            if searched_num == None:
                # remove the last digit in the number and search on it as the new number
                cut_int = str(curr_number)[:-1]
                if cut_int == '':
                    final_array.append([('+'+str(num)), 0])
                    break
                curr_number = int(cut_int)
            else:
                final_array.append([('+'+str(num)), searched_num])
                break

    return final_array



if __name__ == '__main__':
    print(second_solution())
