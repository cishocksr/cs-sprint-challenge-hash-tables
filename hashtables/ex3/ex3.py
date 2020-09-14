def intersection(arrays):
    arr_of_dicts = []
    result = []

    for arr in arrays:
        numsMap = {}

        for num in arr:
            numsMap[num] = True
        
        arr_of_dicts.append(numsMap)

    for key in arr_of_dicts[0]:
        i = 1
        while i < (len(arr_of_dicts)):
            if key in arr_of_dicts[i]:
                i += 1
            else:
                break
        if i == len(arr_of_dicts):
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
