nums=[3,2,2,3]        
nums.sort()
count=1
for i in nums:
    if i==3:
        nums.remove(i)
        nums.remove(i)
    else:
        count+=1
print(count)
print(nums)
/Users/Souvagya-Mac/Library/Jupyter/runtime/jpserver-3319-open.html
