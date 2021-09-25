def count_inversions(my_array):
    # create output variable

    res = 0
    size = len(my_array)
    for i in range(size-1):
        for j in range(i+1, size):
            # print(i, end=',')
            # print(j)
            if (my_array[i] > my_array[j]):
                res+=1

    return res


if __name__ == '__main__':
    
    a = [1, 3, 5, 2, 4, 6]
    print(count_inversions(a))