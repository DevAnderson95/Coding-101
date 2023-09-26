nums_one = [1,2,3,17]
nums_two = [2,3,4,5,1]

prompt = "Find the unique numbers between the two list"

new_list = set(nums_one + nums_two)
for i in new_list:
    print(i)