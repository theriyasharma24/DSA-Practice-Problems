# Problem Statement: [Kth Smallest](https://www.geeksforgeeks.org/problems/kth-smallest-element5635/1)

## Difficulty: Medium

### Problem Description:

Given an array `arr[]` and an integer `k` where `k` is smaller than the size of the array, the task is to find the kth smallest element in the given array.

### Follow up:

Don't solve it using the inbuilt sort function.

### Input:

- An array of integers `arr[]`.
- An integer `k`, where `1 <= k <= arr.size()`.

### Output:

- Return the kth smallest element in the array.

### Example 1:

**Input**:  
`arr[] = [7, 10, 4, 3, 20, 15], k = 3`

**Output**:  
`7`

**Explanation**:  
The 3rd smallest element in the given array is 7.

---

### Example 2:

**Input**:  
`arr[] = [2, 3, 1, 20, 15], k = 4`

**Output**:  
`15`

**Explanation**:  
The 4th smallest element in the given array is 15.

---

### Expected Time and Space Complexity:

- **Time Complexity**: O(n + (max_element))
- **Auxiliary Space**: O(max_element)

### Constraints:

- `1 <= arr.size() <= 10^6`
- `1 <= arr[i] <= 10^6`
- `1 <= k <= n`
