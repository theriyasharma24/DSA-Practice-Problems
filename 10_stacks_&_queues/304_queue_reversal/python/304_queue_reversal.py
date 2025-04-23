class Solution:
    def reverseQueue(self, q):
        stack = []
        while not q.empty():
            stack.append(q.get())
        for item in reversed(stack):
            q.put(item)
        return q



#{ 
 # Driver Code Starts
# Initial Template for Python 3

from queue import Queue

if __name__ == '__main__':
    t = int(input())  # Number of test cases
    for _ in range(t):  # Iterate over each test case
        a = list(map(int,
                     input().split()))  # Read input for the current test case
        n = len(a)  # Get the number of elements
        q = Queue(maxsize=n)  # Create a queue with maxsize n

        for j in a:
            q.put(j)  # Add elements to the queue

        ob = Solution()
        q = ob.reverseQueue(q)  # Call the reverseQueue method

        # Print the elements of the reversed queue
        for i in range(n):
            print(q.get(), end=" ")
        print()

# } Driver Code Ends
#Time Complexity: O(n)
#Space Complexity: O(n)