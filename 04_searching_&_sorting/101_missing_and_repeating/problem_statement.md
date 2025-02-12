# Problem Statement: [Missing And Repeating](https://www.geeksforgeeks.org/problems/find-missing-and-repeating2512/1)

## Difficulty: Easy  
---

### **Problem Description**

Given an unsorted array `arr` of positive integers. One number `a` from the set `[1, 2, ..., n]` is missing and one number `b` occurs twice in the array. Find numbers `a` and `b`.

**Note**:  
The test cases are generated such that there always exists one missing and one repeating number within the range `[1, n]`.

---

### **Examples**

#### **Example 1**

**Input**:  
`arr = [2, 2]`

**Output**:  
`[2, 1]`

**Explanation**:  
Repeating number is `2` and the smallest positive missing number is `1`.

---

#### **Example 2**

**Input**:  
`arr = [1, 3, 3]`

**Output**:  
`[3, 2]`

**Explanation**:  
Repeating number is `3` and the missing number is `2`.

---

#### **Example 3**

**Input**:  
`arr = [4, 3, 6, 2, 1, 1]`

**Output**:  
`[1, 5]`

**Explanation**:  
Repeating number is `1` and the missing number is `5`.

---

### **Constraints**

- `2 ≤ arr.size() ≤ 10^6`
- `1 ≤ arr[i] ≤ arr.size()`
