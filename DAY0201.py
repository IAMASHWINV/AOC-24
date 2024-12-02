def fetch_ip_list():
    lst = []
    with open("02-01.txt") as f:
        for row in f:
            lst.append(list(map(int, row.split())))
    return lst

def fetch_Safe_num():
    input = fetch_ip_list()
    diffs = [[sublist[i+1] - sublist[i] for i in range(len(sublist) - 1)] for sublist in input]
    fin_diff = [val_const(x) for x in diffs]
    print(fin_diff.count(True))
    return fin_diff


def val_const(lst):
    signs = {x > 0 for x in lst if x != 0}
    mag = {abs(x) > 0 and abs(x)<=3 for x in lst}
    return len(signs)==1 and len(mag)==1

fetch_Safe_num()
