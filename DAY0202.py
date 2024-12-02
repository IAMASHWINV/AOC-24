from DAY0201 import fetch_ip_list, val_const
input = fetch_ip_list()

#299

def val_const(input):
    nlst = [input[i+1] - input[i] for i in range(len(input) - 1)]
    signs = {x > 0 for x in nlst if x != 0}
    mag = [abs(x) > 0 and abs(x)<=3 for x in nlst]
    return len(signs)==1 and mag.count(False)==0

def pb_dampner(lsts):
    safe_c = 0
    for i in lsts:
        if val_const(i):
            safe_c+=1
        elif rem_level(i):
            safe_c+=1
    return safe_c

def rem_level(lst):
    is_safe = False
    for i in range(len(lst)):
        if val_const(lst[:i]+lst[i+1:]):
            return True
    return is_safe


print(pb_dampner(input))
        

        








    







