def fetch_loc_list():
    lst1,lst2 = [],[]
    with open("01-01.txt") as f:
        for row in f:
            ip = row.split()
            lst1.append(int(ip[0]))
            lst2.append(int(ip[1]))
    lst1.sort()
    lst2.sort()
    return lst1, lst2


def get_diff(lst1,lst2):
    total_diff = sum([abs(a - b) for a, b in zip(lst1, lst2)])
    return total_diff


lst1, lst2 = fetch_loc_list()
get_diff(lst1,lst2)
