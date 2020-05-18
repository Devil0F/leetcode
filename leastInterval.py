#第一次提交

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if len(tasks) <= 1:	#第16行从1开始遍历，所以长度小于1的tasks会使程序报错
            return 1
        dic = {}
        for task in tasks:	#计算各个任务的数量	
            dic[task] = dic.get(task,0) + 1	
        dic_sort = sorted(dic.items(),key = lambda x:x[1],reverse = True)

        max_task = dic_sort[0][1]
        equal_max = 1

        for i in range(1,len(dic_sort)):	#计算与数量最大值任务相同的任务数量	
            if max_task ==  dic_sort[i][1]:
                equal_max += 1
        
        ans = (max_task - 1) * (n+1) + equal_max	#关键点，利用贪心算法得到公式

        return ans if ans > len(tasks) else len(tasks)	#判断特殊情况，比如["A","A","B","B","C","C","D","D"]
