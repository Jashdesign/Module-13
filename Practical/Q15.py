list1 = ['apple', 'banana', 'mango', 'orange']

search_item = input("Enter the fruit name to search: ")

for fruit in list1:
    if fruit == search_item:
        print(search_item, "is found in the list!")
        break
else:
    print(search_item, "is not found in the list.")