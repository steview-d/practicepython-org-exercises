def remove_dupes_set(arg1):
    return set(arg1)


def remove_dupes_loop(arg1):
    
    new_list = []
    for i in arg1:
        if i not in new_list:
            new_list.append(i)
    
    return new_list


my_list = ['apple', 'banana', 'pear', 'apple', 'orange', 'pear', 'lemon', 'kiwi']

print(remove_dupes_set(my_list))
print(remove_dupes_loop(my_list))