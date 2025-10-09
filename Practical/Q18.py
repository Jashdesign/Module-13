numbers_list = [10, 20, 30, 40, 50]

def my_iterator(lst):
    index = 0
    while index < len(lst):
        yield lst[index] 
        index += 1

iterator = my_iterator(numbers_list)

for num in iterator:
    print(num)