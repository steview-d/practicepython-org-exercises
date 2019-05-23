# with open('assets/categories.txt', 'r') as f:
#     all_text = (f.read()).splitlines()
    
# new_list = []
# dict = {}

# for item in all_text:
#     cat = item[3:-25]
#     new_list.append(cat)
#     if cat not in dict:
#         dict[cat] = 1
#     else:
#         dict[cat] += 1
        
# print(dict)


dict = {}
with open('assets/categories.txt', 'r') as f:
    line = f.readline()
    
    while line:
        line = line[3:-25]
        if line not in dict:
            dict[line] = 1
        else:
            dict[line] += 1
            
        line = f.readline()
        
print(dict)