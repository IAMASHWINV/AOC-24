import re
pattern = r"mul\((\d+,\d+)\)"
test_Str = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

def get_input():
    with open("03-01.txt", "r") as f:
        ip_string = f.read()
    return ip_string


def get_relevant_ops(ip_string):
    matches = re.findall(pattern, ip_string)
    return matches

def get_sumr(matches):
    total = 0
    for match in matches:
        n1, n2 = match.split(",")
        total+= int(n1)*int(n2)
    return total

ip_str = get_input()
matches = get_relevant_ops(ip_str)
print(f"part a : {get_sumr(matches)}")
