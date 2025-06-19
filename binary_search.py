# binary_search.py

# Binary search implementation in Python

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = [2, 5, 8, 12, 16, 23]
key = 16
result = binary_search(arr, key)
print("Key found at index:" if result != -1 else "Key not found", result)
