

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

def third_solution(number, dictRoutes):
    '''
    runtime: O(n) where n is the number of key-value pairs in the dictionary'''
    
    # - start with the longest number
    # - create while loop while the lenght of the longestNumber is more than 0
    # - check if that key is in dict.keys()
    # - if it is, then we return the value in that dictionary
    # - if it is'nt, we cut the last digit
    #   - and then run it again on the same number until we find a value
    longNumber = number
    while len(longNumber) > 0:
        if longNumber in dictRoutes.keys():
            return dictRoutes[longNumber]
        else:
            longNumber = longNumber[:-1]
    return None



def main():

    # arrayRoutes = read_words('route-costs-106000.txt')
    arrayRoutes = read_words('route-costs-106000.txt')
    dictRoutes = create_dict(arrayRoutes)

    arrayTup = []
    for num in read_words('phone-numbers-1000.txt'):
        arrayTup.append((num, third_solution(num, dictRoutes)))
    print(arrayTup)

if __name__ == '__main__':
    main()
