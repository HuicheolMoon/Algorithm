# Problem : https://www.acmicpc.net/problem/2941
# Date : 2020-02-25

s = input()

cro_alphas = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
for char in cro_alphas:
    s = s.replace(char, " ")
cro_len = len(s)
print(cro_len)
