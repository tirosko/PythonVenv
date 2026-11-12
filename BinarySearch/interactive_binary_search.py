
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Interaktívna verzia
def interactive_binary_search():
    # Získanie vstupu od používateľa
    sorted_list = list(map(int, input("Zadaj zoradený zoznam čísel (oddelené medzerou): ").split()))
    target = int(input("Zadaj cieľový prvok: "))
    
    result = binary_search(sorted_list, target)
    
    if result != -1:
        print(f"Prvok sa nachádza na indexe {result}")
    else:
        print("Prvok sa v zozname nenachádza")

# Spustenie interaktívnej verzie
interactive_binary_search()
