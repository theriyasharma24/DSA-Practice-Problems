# Problem Statement: [First and Last Occurrences](https://www.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/1)

## Difficulty: Medium  

---

### **Problem Description**  

Given a sorted array `arr` with possibly some duplicates, the task is to find the first and last occurrences of an element `x` in the given array.  

**Note**: If the number `x` is not found in the array, return both indices as `-1`.  

---

### **Examples**  

#### **Example 1**  

**Input**:  
`arr = [1, 3, 5, 5, 5, 5, 67, 123, 125], x = 5`  

**Output**:  
`[2, 5]`  

**Explanation**:  
The first occurrence of `5` is at index `2`, and the last occurrence is at index `5`.  

---

#### **Example 2**  

**Input**:  
`arr = [1, 3, 5, 5, 5, 5, 7, 123, 125], x = 7`  

**Output**:  
`[6, 6]`  

**Explanation**:  
The first and last occurrence of `7` is at index `6`.  

---

#### **Example 3**  

**Input**:  
`arr = [1, 2, 3], x = 4`  

**Output**:  
`[-1, -1]`  

**Explanation**:  
There is no occurrence of `4` in the array, so the output is `[-1, -1]`.  

---

### **Constraints**  

- `1 ≤ arr.size() ≤ 10^6`  
- `1 ≤ arr[i], x ≤ 10^9`  
