from DAY0101 import fetch_loc_list

lst1, lst2 = fetch_loc_list()



def calc_sim_score(lst1, lst2):
    sim_score = 0
    for i in lst1:
        for j in lst2:
            if i==j:
                sim_score+=i
            elif i<j:
                break
    return sim_score

print(calc_sim_score(lst1, lst2))