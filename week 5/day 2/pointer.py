list1 = [1,9,2, 8,3,7]
#       12,19,13,18
list = [10,20,30,40,50,60,70,80,90,100]
p_list = []
for l in list:
    if list.index(l) < list.index(list[-2]):
        r = list[list.index(l)] + list[list.index(l) + 1] + list[list.index(l) + 2]
        p_list.append(r)
print("p_list", p_list)
print("max", max(p_list))








# p_list = []
# for l in list:
#     r += l
#     if (list.index(l)+1) % 3 == 0:
#         p_list.append(r)
#         r = 0
# print(p_list)