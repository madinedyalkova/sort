def merge_sort(list):
    length = len(list)

    if length == 1:
        return list

    mid = length // 2

    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])

    return merge(left, right)


def merge(left, right):
    op = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            op.append(left[i])
            i += 1
        else:
            op.append(right[j])
            j += 1

    op.extend(left[i:])
    op.extend(right[j:])

    return op


def main():
    us = [22,75,32,4,49,44,28,70]
    sorted = merge_sort(us)
    print(sorted)


main()



                    
  
