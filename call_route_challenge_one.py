# Routing project challenge 1

def read_file(filename):
    return [line.strip() for line in open(filename)]

def create_route_dict(routers):
    dict = {}

    for string in routers:
        substr_price = string[(len(string) - 4): len(string)]
        substr_router = string[0: len(string) - 5]
        dict[substr_router] = substr_price

    return dict

# def find_lowest_price(number, dict):
#     lowest_price = 9999
#     for router in dict.keys():
#         if router in number:
#             if lowest_price > float(dict[router]):
#                 lowest_price = float(dict[router])
#     return lowest_price

def find_longest_prefix(number, dict):

    longest_prefix = ""
    start = 0
    end = 3

    for router in dict.keys():
        router_pref = router[start: end]
        if router_pref == number[start: end]:

            while True:
                if router_pref != number[start: end]:
                    break
                end += 1
                router_pref = router[start: end]
                longest_prefix = router_pref
                router_to_return = router

    return router_to_return


routers = read_file('route-costs-106000.txt')
numbers = read_file('phone-numbers-3.txt')
router_dict = create_route_dict(routers)
sample_number = numbers[0]

router = find_longest_prefix(sample_number, router_dict)
price = router_dict[router]
print(price)
