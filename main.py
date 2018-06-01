def read_pi():
    with open("pi.txt") as pi_txt:
        pi = "".join(pi_txt.readlines()).replace("\n", "")
    return pi[2:]


def get_pi(shift):
    pi = read_pi()
    offset = 0
    try:
        while True:
            if shift > 1:
                yield "{}{}".format(pi[offset], pi[offset + 1])
            else:
                yield str(pi[offset])
            offset += shift
    except IndexError:
        pass


def formater(value, expected_lenght):
    value = str(bin(int(value))).replace("0b", "")
    diff = expected_lenght - len(value)
    for el in range(diff):
        value = "0" + value
    return value


def average(octets, lenght):
    weights = range(lenght)
    for index, octet in enumerate(octets):
        for position, bit in enumerate(octet):
            if bit == "1":
                print("------------------------")
                print("index", index)
                print("octet", octet)
                print("position", position)
                print("weights", weights)
                print("len", len(octets))
                weights[position] += 1
           
    print("average: {}".format(weights))


def compute(lenght, shift):
    octets = [formater(el, lenght) for el in get_pi(shift)]
    average(octets, lenght)


def main():
    compute(8, 2)
    compute(4, 1)
    

if __name__ == "__main__":
    main()
