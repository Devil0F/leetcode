# 第一次成功提交
# 根据最终得到的数组可知，数组里面数据满足大小大小，或小大小大关系，这里的大小指的是数组数据与前一个数据相比
# 故设立变量up,down用于记录数据与前一个数据比较结果，根据题意max(|up - down|) = 1
# 找出该数组变量是先增还是先减，如果先增，则up始终>=down，相反亦然
# 由于最后结果要求返回数组长度，而up和down记录的是增长和减少的次数，根据题意up+down+1即为数组长度
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up = 0
        down = 0
        sign = 0
        if len(nums) < 2:
            return len(nums)
        if len(nums) == 2:
            if nums[0] == nums[1]:
                return 1
            else:
                return 2
        for i in range(1,len(nums)):
            if  nums[i] > nums[i-1]:
                sign = 1
                break
            if  nums[i] < nums[i-1]:
                sign = -1
                break
        if sign == 1:
            for i in range(1,len(nums)):
                if nums[i] > nums[i-1] and up <= down:
                    up += 1
                if nums[i] < nums[i-1] and up > down:
                    down += 1
        else:
            for i in range(1,len(nums)):
                if nums[i] > nums[i-1] and up < down:
                    up += 1
                if nums[i] < nums[i-1] and up >= down:
                    down += 1
        return up + down + 1

# 第二次成功提交
# 核心思想没变，简化了判断数组里数据增长减少的方法
# 即满足条件时，up的每次增加受另一个变量down影响，down不变，up永远不变，每次进入上升段，up只+1，反之亦然
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up = 1
        down = 1
        if len(nums) < 2:
            return len(nums)
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                up = down+1
            if nums[i] < nums[i-1]:
                down = up + 1
        return max(up,down)
