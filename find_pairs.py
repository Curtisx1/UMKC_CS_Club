def find_pairs(arr1, arr2, n, m, x):
    for i in range(0, n):
        for j in range(0 ,m):
            if (arr1[i] + arr2[j]== x):
                return print(arr1[i], arr2[j])
if __name__ == "__main__":
    arr1 = [1,2,3,4,5]
    arr2 = [2,3,4,5,6]
    n = len(arr1)
    m = len(arr2)
    x = 10
    find_pairs(arr1, arr2, n, m , x)
