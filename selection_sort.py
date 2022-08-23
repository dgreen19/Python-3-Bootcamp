def selectionSort(arr: list) -> list:
  for i in range(len(arr)):
    # Initially, assume the first element of the unsorted part is the minimum.
    minimum = i

    for j in range(i+1, len(arr)):
      if (arr[j] < arr[minimum]):
        # Update position of minimum element if a smaller element is found.
        minimum = j

    # Swap the minimum element with the first element of the unsorted part. 
    if i is not minimum:     
      print(arr)
      print("Swapping to: ")
      temp = arr[i]
      arr[i] = arr[minimum]
      arr[minimum] = temp
      print(arr)
    
  return arr

# Driver code

print(selectionSort([13, 4, 9, 5, 3, 16, 12]))