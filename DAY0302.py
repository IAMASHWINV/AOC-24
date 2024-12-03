from DAY0301 import get_input 
import re

test_string = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
pattern = r"do\(\)|don't\(\)|mul\(\d+,\d+\)"
mul_p = r"mul\((\d+),(\d+)\)"


def get_relevant_ops(ip_string):
    matches = re.findall(pattern, ip_string)
    return matches


def get_sum_from_processed(ip_list):
    add, total = True, 0
    for ele in ip_list:
        if "mul" in ele and add:
            numbers = re.findall(mul_p, ele)[0]
            total += int(numbers[0])*int(numbers[1])
        elif "do()" in ele:
            add = True
        elif "don't" in ele:
            add = False
    return total


ip = get_input()

matched_strs = get_relevant_ops(ip)

print(f"part b : {get_sum_from_processed(matched_strs)}")