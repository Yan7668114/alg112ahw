def min_edit_distance(str1, str2):
    if len(str1) == 0:
        return len(str2)
    elif len(str2) == 0:
        return len(str1)
    
    if str1[-1] == str2[-1]:
        return min_edit_distance(str1[:-1], str2[:-1])
    else:
        insert_dist = min_edit_distance(str1, str2[:-1])
        delete_dist = min_edit_distance(str1[:-1], str2)
        replace_dist = min_edit_distance(str1[:-1], str2[:-1])

        return 1 + min(insert_dist, delete_dist, replace_dist)

str1 = "willson"
str2 = "Yan"
result = min_edit_distance(str1, str2)
print(f"最小编辑距离 between '{str1}' 和 '{str2}': {result}")
