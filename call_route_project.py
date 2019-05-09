
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

def firstSolution(number):
    '''
    runtime: O(n) where n is the number of key-value pairs in the dictionary'''

    # arrayRoutes = read_words('route-costs-106000.txt')
    arrayRoutes = read_words('route-costs-10.txt')
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

def main():
    print(firstSolution('+449275049'))      # 0.49
    print(firstSolution('+861532344'))      # 0.84
    print(firstSolution('+1718428566'))     # None

if __name__ == '__main__':
    main()
