"""
Find maximum sum of triplets in an array such than i < j < k and a[i] < a[j] < a[k]

"""
from bisect import bisect_left

def get_suffix_array(arr):
    new_arr = [0]*len(arr)
    for i in range(len(arr)-2, -1, -1):
        new_arr[i] = max(new_arr[i+1], arr[i+1])
    return new_arr

def max_triplet_sum(arr):
    suffix = get_suffix_array(arr)
    sorted_arr = [arr[0]]
    max_triplet = 0
    for i, val in enumerate(arr[1:]):
        index = bisect_left(sorted_arr, val)

        if suffix[i]>val  and max_triplet < val+sorted_arr[index-1]+suffix[i]:
            max_triplet = val+sorted_arr[index-1]+suffix[i]
    return max_triplet

arr = [2,202, 2, 3, 204, 4, 5]
print(max_triplet_sum(arr))