from pprint import pprint


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
    price_list = []
    router_dict = router.read_router_file('route-costs-10000000.txt')
    phone_list = router.read_phone_file('phone-numbers-1000.txt')
    for number in phone_list:
        price_list.append([number, router.get_longest_prefix(router_dict, number)])
    print(price_list)


if __name__ == '__main__':
    main()
