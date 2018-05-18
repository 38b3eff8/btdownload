# 4:
# l  e
# i  e
# d e: d3:agei20ee


def split_array(array):
    if len(array) % 2 != 0:
        return []
    return list(((array[x * 2:(x + 1) * 2]) for x in range(len(array) / 2)))


def array_to_dict(array):
    pairs = split_array(array)
    return dict(pairs)


def find_string(string):
    index = string.find(':')
    length = int(string[0:index])

    s = string[index + 1:index + 1 + length]
    return s, index + length


def find_integer(string):
    index = string.find('e')

    s = string[1:index]

    return int(s), index


def _parse(string):
    result = []

    index = 0
    while index < len(string):
        ch = string[index]
        if ch.isdigit():
            s, sub_index = find_string(string[index:])
            result.append(s)
        elif ch == 'i':
            i, sub_index = find_integer(string[index:])
            result.append(i)
        elif ch == 'l':
            a, sub_index = _parse(string[index + 1:])
            result.append(a)
        elif ch == 'd':
            d, sub_index = _parse(string[index + 1:])

            d = array_to_dict(d)
            result.append(d)
        elif ch == 'e':
            return result, index + 1
        index += sub_index + 1
    return result, -1


def parse(string):
    result, _ = _parse(string)
    return result


def main():
    # string = 'l4:test5:abcdee'
    # string = 'd3:agei20ee'
    # string = 'd4:path3:C:/8:filename8:test.txte'
    # string = '10:testttestt'
    # string = 'i1000e10:testttestt'
    # string = 'l4:testi1000el4:testi1000eee'
    # string = 'd4:testi101000e4:teeti101000e3:arrl4:teste4:ttttd2:tei222eee'
    # string = 'd4:testd4:tttti1000ee2:lili1000eee'
    # string = 'i1000e'
    with open('./test.torrent') as f:
        string = f.read()
        result = parse(string)

        print result[0]['announce']


if __name__ == '__main__':
    main()
