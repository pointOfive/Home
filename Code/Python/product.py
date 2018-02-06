# same, more clever

nums = list(range(10,1,-1))
nums = [6,7,8,1,2,3,9,10]

left_max = [-1] * len(nums)
cur_left_max = left_max[0]
for i in range(1, len(nums)):
    if cur_left_max < nums[i-1]:
        left_max[i] = nums[i-1]
        cur_left_max = nums[i-1]
    else:
        left_max[i] = left_max[i-1]

right_max = [-1] * len(nums)
cur_right_max = right_max[-1]
for i in range(-2, -len(nums)-1,-1):
    if cur_right_max < nums[i+1]:
        right_max[i] = nums[i+1]
        cur_right_max = nums[i+1]
    else:
        right_max[i] = right_max[i+1]

print(nums)
print(left_max)
print(right_max)


# largest three incresing multiplication

nums = [6,7,8,1,2,3,9,10]
# find largest number with a larger number to the right
maxs=(-1,-1,-1,-1)
for i in range(0, len(nums)):
    for j in range(i+1, len(nums)):
        for k in range(j+1, len(nums)):
            if nums[i] < nums[j] and nums[j] < nums[k]:
                if maxs[0] < nums[i]*nums[j]*nums[k]:
                    maxs = (nums[i]*nums[j]*nums[k],nums[i],nums[j],nums[k])
                    
maxs
