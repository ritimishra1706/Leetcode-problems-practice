class Solution:
    def findSum(self,A,N): 
        min_ele=A[0]
        max_ele=A[0]
        for i in range(2,N):
            if A[i]<min_ele:
                min_ele=A[i]
            if A[i]>max_ele:
                max_ele=A[i]
        return min_ele+max_ele        
        #code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    ob = Solution()
    print(ob.findSum(a,n))
# } Driver Code Ends