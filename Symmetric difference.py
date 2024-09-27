print("\033c")
def def_set(set1, set2):
    return set1.symmetric_difference(set2)


set1 = {"Blue", "Green","Red"}
set2 = {"Blue", "Yellow","Red"}


symmetric_diff_a = def_set(set1, set2)

print("Symmetric difference of sets", symmetric_diff_a)

