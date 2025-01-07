# Problem Statement: [Common in 3 Sorted Arrays](https://www.geeksforgeeks.org/problems/common-elements1132/1)

**Difficulty**: Easy

## Problem Description:

You are given three arrays sorted in increasing order. Find the elements that are common in all three arrays.  
If there are no such elements, return an empty array. In this case, the output will be `[-1]`.

**Note**: Can you handle the duplicates without using any additional Data Structure?

---

## Examples:

### Example 1:

**Input**:  
`arr1 = [1, 5, 10, 20, 40, 80]`  
`arr2 = [6, 7, 20, 80, 100]`  
`arr3 = [3, 4, 15, 20, 30, 70, 80, 120]`  
**Output**: `[20, 80]`  
**Explanation**: 20 and 80 are the only common elements in `arr1`, `arr2`, and `arr3`.

---

### Example 2:

**Input**:  
`arr1 = [1, 2, 3, 4, 5]`  
`arr2 = [6, 7]`  
`arr3 = [8, 9, 10]`  
**Output**: `[-1]`  
**Explanation**: There are no common elements in `arr1`, `arr2`, and `arr3`.

---

### Example 3:

**Input**:  
`arr1 = [1, 1, 1, 2, 2, 2]`  
`arr2 = [1, 1, 2, 2, 2]`  
`arr3 = [1, 1, 1, 1, 2, 2, 2, 2]`  
**Output**: `[1, 2]`  
**Explanation**: We do not need to consider duplicates.

---

## Constraints:

- \(1 \leq arr1.size(), arr2.size(), arr3.size() \leq 10^5\)
- \(-10^5 \leq arr1[i], arr2[i], arr3[i] \leq 10^5\)

---

## Expected Time Complexity:

- **O(n)** where \(n = arr1.size() + arr2.size() + arr3.size()\)

## Expected Auxiliary Space:

- **O(1)** (in-place comparison without extra data structures)
