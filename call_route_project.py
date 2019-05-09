
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
    return [line.strip() for line in open(filename)]

def create_dict(word_list):
    dict = {}

    for str in word_list:
        number = str[:-5]          # '+8130'
        price = str[-4:]           # '0.32'
        dict[number] = price

    return dict

def firstSolution(number):
    arrayRoutes = read_words('route-costs-10.txt')
    dictRoutes = create_dict(arrayRoutes)

    print("arrayRoutes")
    print(arrayRoutes)
    print("\ndictRoutes")
    print(dictRoutes)

    lowest_price = 100.00
    for router in dictRoutes.keys():
        if router in number:
            if float(dictRoutes[router]) < lowest_price:
                lowest_price = float(dictRoutes[router])
    return lowest_price


if __name__ == '__main__':
    print(firstSolution('+449275049'))
    print(firstSolution('+14105547746'))
