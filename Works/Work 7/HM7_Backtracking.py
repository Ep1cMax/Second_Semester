def form_sum(candidates, target, curr_sum=0, pos=0, used=None):
    if used is None:
        used = []

    if curr_sum == target:
        return True

    if curr_sum > target or pos >= len(candidates):
        return False

    if form_sum(candidates, target, curr_sum + candidates[pos],
                pos + 1, used + [candidates[pos]]):
        return True

    return form_sum(candidates, target, curr_sum, pos + 1, used)

n, k = map(int, input().split())
candidates = list(map(int, input().split()))
result = form_sum(candidates, k)
print("YES" if result else "NO")



'''
Ввод:
4 10
1 2 3 4
YES
'''