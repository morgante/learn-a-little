'''
https://www.interviewcake.com/question/merge-sorted-arrays
'''

def merge_arrays(list1, list2):
    merged_list = []

    twochecked = 0
    for value1 in list1:
        for value2 in list2[twochecked:]:
            if (value2 >= value1):
                break
            merged_list.append(value2)
            twochecked += 1
        merged_list.append(value1)

    return merged_list


my_array = [3, 4, 6, 10, 11, 15]
alices_array = [1, 5, 8, 12, 14, 19]

print merge_arrays(my_array, alices_array)
