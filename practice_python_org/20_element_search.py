num_list = [1, 4, 8, 11, 12, 14, 16, 18, 20]

def search(my_num, num_list):
    return my_num in num_list
        

def binary_search(my_num, num_list):
    while len(num_list) > 3:
        if my_num < num_list[int(len(num_list)/2)]:
            num_list = num_list[:int(len(num_list)/2)]
        else:
            num_list = num_list[int(len(num_list)/2):]
    
    if my_num in num_list:
        return True
    else:
        return False


if __name__ == "__main__":
    # print(search(8, num_list))
    # print(binary_search(16, num_list))
    
    for x in range(21):
        print(x, binary_search(x, num_list))