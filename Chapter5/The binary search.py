def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    i = 1
    while first <= last and not found:
        print(i)
        i += 1
        midpoint = (first + last)//2
        if alist[midpoint]:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint
            else:
                first = midpoint

    return found

testlist = [17, 20, 26, 31, 44, 54, 55, 65, 77, 93]
print(binarySearch(testlist, 71))
