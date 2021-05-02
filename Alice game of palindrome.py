def utility_fun_for_del(Str, i, j):     
    if (i >= j):
        return 0
    if (Str[i] == Str[j]):
        return utility_fun_for_del(Str, i + 1,j - 1)
    return (1 + min(utility_fun_for_del(Str, i + 1, j),utility_fun_for_del(Str, i, j - 1)))

def min_ele_del(n,instances):
    alice=0
    for i in instances:
        a=utility_fun_for_del(i, 0, len(i) - 1)
        if a%2==0:
            alice+=1
    return alice

