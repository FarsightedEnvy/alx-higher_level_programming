def find_peak(list_of_integers):
    # Edge case: empty list
    if not list_of_integers:
        return None
    
    # Binary search approach to find peak
    left, right = 0, len(list_of_integers) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        # Check if mid is a peak
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]
        
        # Move towards the direction of the larger neighbor
        if mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            right = mid - 1
        else:
            left = mid + 1
    
    # If we reach here, list_of_integers[left] should be a peak
    return list_of_integers[left]

# Example usage:
# list_of_integers = [1, 3, 20, 4, 1, 0]
# print(find_peak(list_of_integers))
