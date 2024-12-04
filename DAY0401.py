def fetch_ip():
    with open("04-01.txt") as f:
        op = f.read().split()
    return op


def str_list(ip_lst):
    ip_arr = list(map(list,ip_lst))
    return ip_arr


def vertical_count(ip_arr):
    count = 0
    for indx, elex in enumerate(ip_arr):
        for indy, eley in enumerate(elex):
            if eley == "X":
                #horizontal L
                if indy>=3 and "".join(elex[indy-3:indy+1])=="SAMX":
                    count+=1
            #horizontal R
                if indy<=136 and "".join(elex[indy:indy+4]) == "XMAS":
                    count+=1
    return count

def get_daigonal_count(ip_arr):
    count = 0
    for indx, elex in enumerate(ip_arr):
        for indy, eley in enumerate(elex):
            #Upper R
            if eley == "X" and indx>=3 and indy<=136:
                tword = eley + ip_arr[indx-1][indy+1]+ip_arr[indx-2][indy+2]+ip_arr[indx-3][indy+3]
                if tword == "XMAS":
                    count+=1
            #Lower R
            if eley == "X" and indx<=136 and indy<=136:
                tword = eley + ip_arr[indx+1][indy+1]+ip_arr[indx+2][indy+2]+ip_arr[indx+3][indy+3]
                if tword == "XMAS":
                    count+=1
            
            #upper L
            if eley == "X" and indx>=3 and indy>=3:
                tword = eley + ip_arr[indx+-1][indy-1]+ip_arr[indx-2][indy-2]+ip_arr[indx-3][indy-3]
                if tword == "XMAS":
                    count+=1
            #lower L
            if eley == "X" and indx<=136 and indy>=3:
                tword = eley + ip_arr[indx+1][indy-1]+ip_arr[indx+2][indy-2]+ip_arr[indx+3][indy-3]
                if tword == "XMAS":
                    count+=1

    return count

ip = fetch_ip()
ip_arr = str_list(ip)
#transpose for vertical
transposed_ip = list(map(list, zip(*ip_arr)))
count = 0
count+=vertical_count(ip_arr)
count+= vertical_count(transposed_ip)
count+=get_daigonal_count(ip)





print(count)