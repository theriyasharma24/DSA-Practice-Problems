# Problem Statement: [Median of 2 Sorted Arrays of Different Sizes](https://www.geeksforgeeks.org/problems/median-of-2-sorted-arrays-of-different-sizes/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card)

## **Difficulty**: Hard

## **Problem Description**

Given two sorted arrays `a[]` and `b[]`, find and return the median of the combined array after merging them into a single sorted array.

---

## **Examples**

### **Example 1**

**Input**:  
`a[] = [-5, 3, 6, 12, 15]`  
`b[] = [-12, -10, -6, -3, 4, 10]`

**Output**:  
`3`

**Explanation**:  
The merged array is `[-12, -10, -6, -5, -3, 3, 4, 6, 10, 12, 15]`.  
So the median of the merged array is `3`.

---

### **Example 2**

**Input**:  
`a[] = [2, 3, 5, 8]`  
`b[] = [10, 12, 14, 16, 18, 20]`

**Output**:  
`11`

**Explanation**:  
The merged array is `[2, 3, 5, 8, 10, 12, 14, 16, 18, 20]`.  
So the median of the merged array is `(10 + 12) / 2 = 11`.

---

### **Example 3**

**Input**:  
`a[] = []`  
`b[] = [2, 4, 5, 6]`

**Output**:  
`4.5`

**Explanation**:  
The merged array is `[2, 4, 5, 6]`.  
So the median of the merged array is `(4 + 5) / 2 = 4.5`.

---

## **Your Task**

You need to complete the function **`findMedianSortedArrays()`**, which takes:

- Two integer arrays `a[]` and `b[]` as input,
- Returns the **median** of the combined sorted array.

---

## **Expected Complexity**

- **Time Complexity**: \( O(\log \min(n, m)) \)
- **Space Complexity**: \( O(1) \)

---

## **Constraints**

- \( 0 \leq a.size(), b.size() \leq 10^6 \)
- \( 1 \leq a[i], b[i] \leq 10^9 \)
- \( a.size() + b.size() > 0 \)
