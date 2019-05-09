
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


# 2.

def firstSolution(carrierRoutes, number):
    arrayRoutes = carrierRoutes.keys()
    dict = carrierRoutes

    for routeNum in arrayRoutes:
        mathingString = ""
        # ...
