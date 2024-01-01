def min_chocolate_difference(arr, m):
  n = len(arr)
  if n < m:
      return -1  

  arr.sort()  

  min_diff = float('inf')

  for i in range(n - m + 1):
      diff = arr[i + m - 1] - arr[i]
      min_diff = min(min_diff, diff)

  return min_diff
  
arr1 = [7, 3, 2, 4, 9, 12, 56]
m1 = 5
result1 = min_chocolate_difference(arr1, m1)
print("Output 1:", result1)  

arr2 = [3, 4, 1, 9, 56, 7, 9, 12]
m2 = 5
result2 = min_chocolate_difference(arr2, m2)
print("Output 2:", result2) 
