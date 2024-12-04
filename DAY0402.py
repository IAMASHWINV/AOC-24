from DAY0401 import fetch_ip, str_list


def get_daigonal_count(ip_arr):
    count = 0
    x_len = len(ip_arr)
    y_len = len(ip_arr[0])
    for indx in range(1, x_len - 1):
        for indy in range(1, y_len - 1):
            if ip_arr[indx][indy] == 'A':
                if (ip_arr[indx-1][indy-1] + ip_arr[indx+1][indy+1] == 'MS' or ip_arr[indx-1][indy-1] + ip_arr[indx+1][indy+1] == 'SM') and \
                   (ip_arr[indx-1][indy+1] + ip_arr[indx+1][indy-1] == 'MS' or ip_arr[indx-1][indy+1] + ip_arr[indx+1][indy-1] == 'SM'):
                    count += 1

    return count


ip = fetch_ip()
ip_arr = str_list(ip)
print(f" part b : {get_daigonal_count(ip_arr)}")