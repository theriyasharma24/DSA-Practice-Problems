# Problem Statement: [Remove All Duplicates from a Given String](https://www.geeksforgeeks.org/problems/remove-all-duplicates-from-a-given-string4321/1)

## Difficulty: Easy  
---

### **Problem Description**

Given a string `s` which may contain **lowercase and uppercase** characters, the task is to **remove all duplicate characters** from the string and return the resultant string.  

The order of remaining characters in the output should be **the same as in the original string**.

---

### **Examples**

#### **Example 1**
**Input**:  
```python
s = "geEksforGEeks"
```
**Output**:  
```python
"geEksforG"
```
**Explanation**:  
After removing duplicate characters such as `E, e, k, s`, we get the string **"geEksforG"**.

---

#### **Example 2**
**Input**:  
```python
s = "HaPpyNewYear"
```
**Output**:  
```python
"HaPpyNewYr"
```
**Explanation**:  
After removing duplicate characters such as `e, a`, we get the string **"HaPpyNewYr"**.

---

### **Constraints**
- `1 ≤ N ≤ 10^6`
- The string contains **uppercase and lowercase English letters**.
