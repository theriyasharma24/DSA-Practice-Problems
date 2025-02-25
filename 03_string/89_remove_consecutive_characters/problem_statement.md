# Problem Statement: [Remove Consecutive Characters](https://www.geeksforgeeks.org/problems/consecutive-elements2306/1)

## Difficulty: Easy  
---

### **Problem Description**

You are given a string `s`, consisting of **lowercase English alphabets**.  
Your task is to **remove consecutive duplicate characters** from the string.

The order of remaining characters in the output should be **the same as in the original string**.

---

### **Examples**

#### **Example 1**
**Input**:  
```python
s = "aabb"
```
**Output**:  
```python
"ab"
```
**Explanation**:  
- The character `'a'` at index `2` is the same as `'a'` at index `1`, so it is removed.  
- The character `'b'` at index `4` is the same as `'b'` at index `3`, so it is removed.  
- The final string is **"ab"**.

---

#### **Example 2**
**Input**:  
```python
s = "aabaa"
```
**Output**:  
```python
"aba"
```
**Explanation**:  
- The character `'a'` at index `2` is the same as `'a'` at index `1`, so it is removed.  
- The character `'a'` at index `5` is the same as `'a'` at index `4`, so it is removed.  
- The final string is **"aba"**.

---

#### **Example 3**
**Input**:  
```python
s = "abcddcba"
```
**Output**:  
```python
"abcdcba"
```
**Explanation**:  
- The character `'d'` at index `5` is the same as `'d'` at index `4`, so it is removed.  
- No other consecutive duplicates exist.  
- The final string is **"abcdcba"**.

---

### **Constraints**
- `1 ≤ n ≤ 10^6`
- The string contains **only lowercase English alphabets**.
