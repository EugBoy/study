with open("1.txt") as file:
    arr1 = [int(row.strip()) for row in file]
    
with open("2.txt") as file:
    arr2 = [int(row.strip()) for row in file]
    
set1 = set(arr1);
set2 = set(arr2);

# print(set1);
# print(set2);


#arr_union - объединение
arr_union = list(set(set1 | set2));

#arr_difference - разность
arr_difference = list(set(set1 - set2));

#arr - перечисление
arr = arr1 + arr2;

#set - симетричная разность
arr_s_difference = list(set(set1 ^ set2)); 

def bubble(array):
    N = len(array);
    for i in range(N-1):
        for j in range(N-i-1):
            if array[j] > array[j+1]:
                buff = array[j]
                array[j] = array[j+1]
                array[j+1] = buff
                
bubble(arr);
print(arr);























MIN_MERGE = 32


def calcMinRun(n):
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r
def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
def merge(arr, l, m, r):
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])
    i, j, k = 0, 0, l
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1
def timSort(arr):
    n = len(arr)
    minRun = calcMinRun(n)
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSort(arr, start, end)
    size = minRun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            if mid < right:
                merge(arr, left, mid, right)
        size = 2 * size
if __name__ == "__main__":
    arr = [-2, 7, 15, -14, 0, 15, 0,
           7, -7, -4, -13, 5, 8, -14, 12]
    print("Given Array is")
    print(arr)
    timSort(arr)
    print("After Sorting Array is")
    print(arr)
