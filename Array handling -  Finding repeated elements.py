'''Given an unsorted array of size n. Array elements are in the range of 1 to n.
One number from set {1, 2, …n} is missing and one number occurs twice in the array. 
Find these two numbers.'''

def find_missing(arr):
  n = len(arr)
  seen_set = set()
  repeating = 0
  missing = 0

  for num in arr:
      if num in seen_set:
          repeating = num
      seen_set.add(num)

  for i in range(1, n + 1):
      if i not in seen_set:
          missing = i

  return missing, repeating

arr1 = [3, 1, 3]
result1 = find_missing(arr1)
print("Output 1:", result1)  # Output: (2, 3)

arr2 = [4, 3, 6, 2, 1, 1]
result2 = find_missing(arr2)
print("Output 2:", result2)  # Output: (5, 1)
