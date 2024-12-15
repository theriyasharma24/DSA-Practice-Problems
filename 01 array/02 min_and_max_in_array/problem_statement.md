# Problem Statement: [Min and Max in Array](https://www.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card)

## Difficulty: Basic

### Problem Description:

Given an array `arr[]`, your task is to find the minimum and maximum elements in the array. Return an array that contains two elements: the first one will be the minimum element and the second will be the maximum element of the array.

### Input:

- An array of integers `arr[]`.

### Output:

- Return an array of two integers, where:
  - The first integer is the minimum element of the array.
  - The second integer is the maximum element of the array.

### Example 1:

**Input**:  
`arr = [3, 2, 1, 56, 10000, 167]`

**Output**:  
`1 10000`

**Explanation**:  
The minimum element is 1 and the maximum element is 10000.

---

### Example 2:

**Input**:  
`arr = [1, 345, 234, 21, 56789]`

**Output**:  
`1 56789`

**Explanation**:  
The minimum element is 1 and the maximum element is 56789.

---

### Example 3:

**Input**:  
`arr = [56789]`

**Output**:  
`56789 56789`

**Explanation**:  
Since the array contains only one element, both the minimum and maximum elements are the same.

---

### Expected Time and Space Complexity:

- **Time Complexity**: O(n)
- **Auxiliary Space**: O(1)

### Constraints:

- `1 <= arr.size() <= 10^5`
- `1 <= arr[i] <= 10^12`
