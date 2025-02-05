# Problem Statement: [Sorted Matrix](https://www.geeksforgeeks.org/problems/sorted-matrix2333/1)

## Difficulty: Basic

### Problem Description:

You are given an **N × N matrix** `Mat`. Your task is to **sort all elements of the matrix** in non-decreasing order and return the sorted matrix.

---

### Example 1:

**Input**:

```plaintext
N = 4
Mat = [[10, 20, 30, 40],
       [15, 25, 35, 45],
       [27, 29, 37, 48],
       [32, 33, 39, 50]]
```

**Output**:

```plaintext
10 15 20 25
27 29 30 32
33 35 37 39
40 45 48 50
```

**Explanation**:  
Sorting all elements in the matrix and rearranging them row-wise gives the above result.

---

### Example 2:

**Input**:

```plaintext
N = 3
Mat = [[1, 5, 3], 
       [2, 8, 7], 
       [4, 6, 9]]
```

**Output**:

```plaintext
1 2 3
4 5 6
7 8 9
```

**Explanation**:  
Sorting all elements in the matrix and rearranging them row-wise gives the above result.

---

### Your Task:

You don't need to read input or print anything. Your task is to complete the function:

```python
def sortedMatrix(N: int, Mat: List[List[int]]) -> List[List[int]]:
```

This function takes:
- An integer `N` (size of the matrix),
- A `N × N` matrix `Mat` (list of lists).

It **returns the sorted matrix** as a `N × N` list.

---

### Expected Complexity:

- **Time Complexity:** `O(N² log N²) ≈ O(N² log N)`
- **Auxiliary Space:** `O(N²)`

---

### Constraints:

- `1 ≤ N ≤ 1000`
- `1 ≤ Mat[i][j] ≤ 10⁵`
