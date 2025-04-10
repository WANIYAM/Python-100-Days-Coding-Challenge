# 15.Sort a list in ascending and descending order (without built-in methods).
def bubble_sort(lst, ascending=True):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (ascending and lst[j] > lst[j + 1]) or (not ascending and lst[j] < lst[j + 1]):
                # Swap
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
# Get list from user
user_input = input("Enter a list of numbers separated by spaces: ")
num_list = [int(x) for x in user_input.split()]

# Sort in ascending and descending order
asc_sorted = bubble_sort(num_list.copy(), ascending=True)
desc_sorted = bubble_sort(num_list.copy(), ascending=False)

print("Ascending order:", asc_sorted)
print("Descending order:", desc_sorted)
