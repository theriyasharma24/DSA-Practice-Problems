class TwoStacks:
    def __init__(self):
        self.stack = [None] * 100 
        self.size = 100  
        self.left = -1 
        self.right = 100 

    # Function to push an integer into stack 1
    def push1(self, x):
        if self.left < self.right - 1:
            self.left += 1
            self.stack[self.left] = x 
        else:
            print("Stack Overflow")

    # Function to push an integer into stack 2
    def push2(self, x):
        if self.left < self.right - 1:
            self.right -= 1
            self.stack[self.right] = x 
        else:
            print("Stack Overflow")

    # Function to remove an element from top of stack 1
    def pop1(self):
        if self.left >= 0: 
            popped_element = self.stack[self.left]
            self.left -= 1
            return popped_element
        else:
            return -1  

    # Function to remove an element from top of stack 2
    def pop2(self):
        if self.right < self.size: 
            popped_element = self.stack[self.right]
            self.right += 1
            return popped_element
        else:
            return -1 


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    while T > 0:
        sq = TwoStacks()
        Q = int(input())
        while Q > 0:
            query = list(map(int, input().split()))
            if query[1] == 1:
                if query[0] == 1:
                    sq.push1(query[2])
                elif query[0] == 2:
                    sq.push2(query[2])
            elif query[1] == 2:
                if query[0] == 1:
                    print(sq.pop1(), end=' ')
                elif query[0] == 2:
                    print(sq.pop2(), end=' ')
            Q -= 1
        print()
        T -= 1

        print("~")

# } Driver Code Ends

#Time Complexity: O(1) 
#Space Complexity: O(n)