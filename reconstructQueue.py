#第一次提交
#将people数组按照第一列升序，第二列降序排列，先确定小个子的位置，相同身高，K越大，越先确定
#通过K值来确定具体位置：新建一个递增数组，长度与people相同，存放位置，每个位置唯一
#每次通过K值确定完位置后，删除该位置，因为先删除后面的不会影响前面，故要第二列降序排列
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ans = [0] * len(people)
        other = [i for i in range(len(people))]
        people.sort(key = lambda x:(x[0],-x[1]))
        for i,k in enumerate(people):
            ans[other[k[1]]] = people[i]
            del other[k[1]]
        return ans

#第二次提交
#将people数组按照第一列降序，第二列升序排列
#先确定大个子位置，同等身高先确定K小的人，先插入k值较小的不会影响后续的操作
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ans = []
        people.sort(key = lambda x:(-x[0],x[1]))
        for i in people:
            ans.insert(i[1],i) 
        return ans       
