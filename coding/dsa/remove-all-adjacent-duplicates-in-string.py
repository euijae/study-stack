class Solution:
    def removeAllDuplicates(self, s: str) -> str:
        stack = [] # [ch, freq]

        # abbbacxdd
        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
            else:
                if stack and stack[-1][1] > 1:
                    stack.pop()
                    if stack and stack[-1][0] == ch:
                        stack[-1][1] += 1
                    else:
                        stack.append([ch, 1])
                else:
                    stack.append([ch, 1])
            
        # end of iteration, 
        if stack and stack[-1][1] > 1:
            stack.pop()
        
        return ''.join(ch for ch, _ in stack)

solution = Solution()
s = "abbbacxdd"
print(solution.removeAllDuplicates(s))
