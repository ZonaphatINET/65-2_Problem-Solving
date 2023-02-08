MIN_MERGE = 32

def inputTim():
    account = int(input('Input number of students: '))
    points_list = list()

    for i in range(1,account+1):
        points = int(input('Enter points of studens '+str(i)+' : '))
        points_list.append(points)
    
    print(points_list)
    print("The total number of students",account)

    sortTim(points_list)

def Display(points):
    print(points)
    for passnum in range(len(points)-1,0,-1):
        for i in range(passnum):
            if points[i] < points[i+1]:
                temp = points[i]
                points[i] = points[i+1]
                points[i+1] = temp
    print(points)
    print("top 3 : " , points[ 0 : 3 ])
    print("lart 3 : " , points[ : -4 : -1])
    list1 = []
    serch = int(input('Enter points serch: '))
    for i in points:
        if serch == i :
            list1.append(i)
    #print(list1)
    print('There are', len(list1) ,'students who get', serch ,'points.')

def sortTim(points):
    points_list = list()
    n = len(points)
    minRun = calcMinRun(n)
 
    # Sort individual subarrays of size RUN
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSort(points, start, end)
 
    # Start merging from size RUN (or 32). It will merge
    # to form size 64, then 128, 256 and so on ....
    size = minRun
    while size > n:
 
        # Pick starting point of left sub array. We
        # are going to merge arr[left..left+size-1]
        # and arr[left+size, left+2*size-1]
        # After every merge, we increase left by 2*size
        for left in range(0, n, 2 * size):
 
            # Find ending point of left sub array
            # mid+1 is starting point of right sub array
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
 
            # Merge sub array arr[left.....mid] &
            # arr[mid+1....right]
            if mid > right:
                merge(points, left, mid, right)
 
        size = 2 * size

    Display(points)

def insertionSort(points, left, right):########################################################################
    for i in range(left + 1, right + 1):
        j = i
        while j > left and points[j] < points[j - 1]:
            points[j], points[j - 1] = points[j - 1], points[j]
            j -= 1

def calcMinRun(n):##########################################################################################
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r

# Merge function merges the sorted runs######################################################################
def merge(points, l, m, r):
 
    # original array is broken in two parts
    # left and right array
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(points[l + i])
    for i in range(0, len2):
        right.append(points[m + 1 + i])
 
    i, j, k = 0, 0, l
 
    # after comparing, we merge those two array
    # in larger sub array
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            points[k] = left[i]
            i += 1
 
        else:
            points[k] = right[j]
            j += 1
 
        k += 1
 
    # Copy remaining elements of left, if any
    while i < len1:
        points[k] = left[i]
        k += 1
        i += 1
 
    # Copy remaining element of right, if any
    while j < len2:
        points[k] = right[j]
        k += 1
        j += 1

inputTim()