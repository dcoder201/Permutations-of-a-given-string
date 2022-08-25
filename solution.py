#User function Template for python3
from itertools import permutations

class Solution:
    def find_permutation(self, S):
        # Code here
        result_ls=[]
        ans_li=permutations(list(S))
        for val in ans_li:
            for item in val:
                single_val="".join(val)
            result_ls.append(single_val)
        final_val=sorted(list(set(result_ls)))
        return final_val
        
            
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        S=input()
        ob = Solution()
        ans = ob.find_permutation(S)
        for i in ans:
            print(i,end=" ")
        print()
# } Driver Code Ends
