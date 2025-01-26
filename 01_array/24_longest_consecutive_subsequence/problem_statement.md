# \Problem Statement: [Longest Consecutive Subsequence](https://www.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/1)

## **Difficulty**: Medium

---

## **Problem Description**

Given an array `arr[]` of non-negative integers, find the **length** of the longest subsequence such that the elements in the subsequence are **consecutive integers**. The consecutive numbers can appear in any order in the array.

---

### **Input**

- `arr[]`: An array of non-negative integers.

---

### **Output**

- Return an integer representing the length of the longest subsequence of consecutive numbers.

---

### **Examples**

#### Example 1:

**Input**:  
`arr[] = [2, 6, 1, 9, 4, 5, 3]`  
**Output**:  
`6`  
**Explanation**:  
The consecutive numbers here are **1, 2, 3, 4, 5, 6**. These 6 numbers form the longest consecutive subsequence.

---

#### Example 2:

**Input**:  
`arr[] = [1, 9, 3, 10, 4, 20, 2]`  
**Output**:  
`4`  
**Explanation**:  
The longest consecutive subsequence is **1, 2, 3, 4**.

---

#### Example 3:

**Input**:  
`arr[] = [15, 13, 12, 14, 11, 10, 9]`  
**Output**:  
`7`  
**Explanation**:  
The consecutive numbers are **9, 10, 11, 12, 13, 14, 15**, which has a length of 7.

---

### **Constraints**

- \( 1 \leq \text{arr.size()} \leq 10^5 \)
- \( 0 \leq \text{arr}[i] \leq 10^5 \)
