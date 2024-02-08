def multiply_by_index(nums):
    total = [0, 2]

    for i in range(len(nums)):#5 0 1 
        total.append(i * nums[i])
    print(total)

multiply_by_index([1, 2, 3, 4, 5])