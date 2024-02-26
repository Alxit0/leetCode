class Solution(object):
    def generateParenthesis(self, n):
        r = []
        
        def foo(s, left, right):
            if len(s) == n*2:
                r.append(s)
                return
            
            if left < n:
                foo(s + '(', left + 1, right)
            
            if right < left:
                foo(s + ')', left, right + 1)
            
        foo('', 0, 0)
        return r
            
        
        
        

def main():
    s = Solution()
    
    print(s.generateParenthesis(3))
    # ["((()))","(()())","(())()","()(())","()()()"]
    
    print(s.generateParenthesis(1))
    # ["()"]

if __name__ == '__main__':
    main()
