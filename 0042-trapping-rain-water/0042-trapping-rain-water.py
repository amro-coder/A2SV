class Solution:
    def trap(self, arr: List[int]) -> int:
        n = len(arr)

        prefix_sum = [0]
        acc = 0
        for ele in arr:
            acc += ele
            prefix_sum.append(acc)


        stack = []
        mapper = {}
        for i in range(n):

            while stack:
                value,idx = stack[-1]
                if arr[i] >= value: # pop
                    popped_value,popped_idx = stack.pop()
                    mapper[popped_idx] = i
                else:
                    break
            stack.append((arr[i],i))

        for i in range(len(stack)-1):
            _,curr_idx = stack[i]
            _,next_idx = stack[i+1]
            mapper[curr_idx] = next_idx
        mapper[n-1] = None

        ans = 0
        curr_idx = 0
        while mapper[curr_idx] is not None:
            next_idx = mapper[curr_idx]
            #
            length = min(arr[curr_idx],arr[next_idx])
            interval = next_idx-curr_idx-1
            range_sum = prefix_sum[next_idx]-prefix_sum[curr_idx+1]
            ans += length  * interval - range_sum

            curr_idx = next_idx

        return ans