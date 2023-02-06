def sequentialSearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first <= last and not found:
        midpoint = (first + last)//2
        if alist[midpoint]:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint
            else:
                first = midpoint

    return found

testlist = [1, 2, 8, 12, 17, 19, 32, 42]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 13))