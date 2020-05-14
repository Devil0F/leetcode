#第一次提交
#顺序遍历num，将字符压入栈(ans)中
#如果k>0,ans不为空,i小于栈中新进来的值，即满足while循环条件，将栈中此数弹出，同时k-1，因为已经移除了一位数字
#退出for循环之后会有两种情况
#一种是k=0时，此时ans里的结果的位数符合条件
#当k!=0时，代表ans中有多余的数字，此时根据K值删除ans末尾数据即可
#最后用join()将final_ans转化为字符串，再用lstrip删除头部的'0'
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        ans = []
        for i in num:
            while k and ans and i < ans[-1]:
                ans.pop()
                k -= 1
            ans.append(i)
        final_ans = ans[:-k] if k else ans

        return "".join(final_ans).lstrip('0') or '0'
