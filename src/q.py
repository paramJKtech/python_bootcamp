nums = [1,2,3,4,1]
num_map = {}
for i in range(len(nums)):
    if(num_map.get(nums[i]) is None):
        num_map[nums[i]] = nums[i]
    else:
        print("true")
print("false")

