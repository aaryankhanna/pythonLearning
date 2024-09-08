def twoSum(nums, target):
    d = {}
    ans = set()
    
    # Store the index and value in the dictionary
    for i in range(len(nums)):
        d[i] = nums[i]
    
    # Iterate through the dictionary to find pairs
    for key, value in d.items():
        rem = target - value
        
        # Find the key corresponding to rem
        rem_key = None
        for k, v in d.items():
            if v == rem and k != key:
                rem_key = k
                break
        
        if rem_key is not None:
            ans.add(key)
            ans.add(rem_key)
    
    # Convert the set to a list and return it
    ans = list(ans)
    return ans

print(twoSum([3, 2, 4], 6))  # Output: [1, 2]
