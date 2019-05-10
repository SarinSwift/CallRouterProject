# Routing project challenge 2

# crappy solution

# def read_file(filename):
#     return [line.strip() for line in open(filename)]

# def create_route_dict(routers):
#     dict = {}
#
#     for string in routers:
#
#         substr_price = string[(len(string) - 4): len(string)]
#         substr_router = string[0: len(string) - 5]
#         dict[substr_router] = substr_price
#
#     return dict
#
# def find_longest_prefix(number, dict):
#     longest_prefix = ""
#
    # for router in dict.keys():
    #     if router == number[0: len(router)]:
    #         if len(longest_prefix) < len(router):
    #             longest_prefix = router
    # return longest_prefix
#
# def return_price(string, dict):
#     if string == '':
#         return None
#     return dict[string]
#
# result_arr = []
# routers = read_file('route-costs-106000.txt')
# numbers = read_file('phone-numbers-1000.txt')
# router_dict = create_route_dict(routers)
#
# for number in numbers:
#     router = find_longest_prefix(number, router_dict)
#     price = return_price(router, router_dict)
#     result = (router, price)
#     result_arr.append(result)

# good solution
class Router(object):

    def __init__(self):

        self.shortest_router = 100
        self.longest_router = 0

    def read_router_file(self, filename):
        router_dict = {}
        f = open(filename)
        for line in f:
            line = line.strip().split(',')
            router_dict[line[0]] = line[1]
            if self.shortest_router > len(line[0]):
                self.shortest_router = len(line[0])
            if self.longest_router < len(line[0]):
                self.longest_router = len(line[0])

        f.close()
        return router_dict

    def read_phone_file(self, filename):
        return [line.strip() for line in open(filename)]

    def get_longest_prefix(self, dict, number):
        if len(number) > self.longest_router:
            chop = len(number) - self.longest_router
            number = number[:-chop]

        while True:
            if len(number) < self.shortest_router:
                break

            if number in dict:
                return dict[number]
            else:
                number = number[:-1]

# recursion
# set initial phone # length to longest router
# chop off phone # digits until length < shortest_router
def main():

    router = Router()
    router_dict = router.read_router_file('route-costs-1000000.txt')
    phone_list = router.read_phone_file('phone-numbers-3.txt')
    price = router.get_longest_prefix(router_dict, '+4444349844894896754')
    print(price)


if __name__ == '__main__':
    main()
