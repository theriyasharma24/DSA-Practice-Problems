# Problem Statement: [Row with Maximum 1s](https://www.geeksforgeeks.org/problems/row-with-max-1s0023/1)

## Difficulty: Medium

### Problem Description:

You are given a **2D binary array** `arr[][]` consisting of only `1s` and `0s`. Each row of the array is **sorted in non-decreasing order**. Your task is to **find and return the index of the first row that contains the maximum number of `1s`**.

If no such row exists, return `-1`.

**Note:**

- The array follows **0-based indexing**.
- The number of **rows** and **columns** in the array are denoted by `n` and `m` respectively.

---

### Example 1:

**Input**:

```plaintext
arr = [[0,1,1,1],
       [0,0,1,1],
       [1,1,1,1],
       [0,0,0,0]]
```

**Output**:

```plaintext
2
```

**Explanation**:  
Row `2` contains the most number of `1s` (**4** `1s`). Hence, the output is `2`.

---

### Example 2:

**Input**:

```plaintext
arr = [[0,0],
       [1,1]]
```

**Output**:

```plaintext
1
```

**Explanation**:  
Row `1` contains the most number of `1s` (**2** `1s`). Hence, the output is `1`.

---

### Example 3:

**Input**:

```plaintext
arr = [[0,0],
       [0,0]]
```

**Output**:

```plaintext
-1
```

**Explanation**:  
No row contains any `1s`, so the output is `-1`.

---

### Constraints:

- `1 ≤ arr.size(), arr[i].size() ≤ 10^3`
- `0 ≤ arr[i][j] ≤ 1` (Each element is either `0` or `1`)
