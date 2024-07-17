# Find the triplets that adds up to a zero

nums = [-1,0,1,2,-1,-4]
result = []
for i in range(len(nums)):
    for j in range(i+1, len(nums)-1):
        requireEle = (-1) * (nums[i] + nums[j])
        if requireEle in nums[j+1:]:
            triplets = sorted([nums[i], nums[j], requireEle]) # Just to assure if not already exist
            if triplets not in result:
                result.append(triplets)
    

print(result)
