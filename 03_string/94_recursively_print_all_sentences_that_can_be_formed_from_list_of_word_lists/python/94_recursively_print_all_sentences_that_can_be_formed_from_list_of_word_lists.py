from typing import List

class Solution:
    def sentences(self, L: List[List[str]]) -> List[List[str]]:
        result = []
        self.generate_sentences(L, 0, [], result)
        return result

    def generate_sentences(self, L, row, sentence, result):
        if row == len(L): 
            result.append([" ".join(sentence)])
        
        for word in L[row]:
            self.generate_sentences(L, row + 1, sentence + [word], result)




#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


class StringMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([str(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":

    a = IntArray().Input(2)

    list = StringMatrix().Input(a[0], a[1])

    obj = Solution()
    res = obj.sentences(list)

    StringMatrix().Print(res)

# } Driver Code Ends

#Time Complexity: O(N^M)
#Space Complexity: O(M*N^M)