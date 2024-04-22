class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        for operatoin in logs:
            if operatoin[:-1]=="..":
                if stack:
                    stack.pop()
            elif operatoin[:-1]!='.':
                stack.append(0)
        return len(stack)
                
        