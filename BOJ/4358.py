# 생태학
# Problem : https://www.acmicpc.net/problem/4358
# Date : 2021-10-17

from collections import defaultdict
import sys


trees = defaultdict(int)
tree = sys.stdin.readline().rstrip()
num = 0
while tree:
    trees[tree] += 1
    num += 1
    tree = sys.stdin.readline().rstrip()
species = sorted(trees.keys())
for tree in species:
    share = trees[tree] / num * 100
    print(f"{tree} {share:0.4f}")
