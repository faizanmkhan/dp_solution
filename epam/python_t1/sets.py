def set_inter():
    input_a = input()
    input_b = input()
    list1 = list(map(int, input_a.split()))
    list2 = list(map(int, input_b.split()))
    set1 = set(list1)
    set2 = set(list2)
    common_value = set1.intersection(set2)
    final_list = list(common_value)
    final_list.sort()
    print(final_list)

set_inter()