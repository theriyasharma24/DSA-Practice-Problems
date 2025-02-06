# Problem Statement: [Check if Strings are Rotations of Each Other](https://www.geeksforgeeks.org/problems/check-if-strings-are-rotations-of-each-other-or-not-1587115620/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card)

## Difficulty: Easy

### Problem Description:

You are given two strings of **equal lengths**, `s1` and `s2`. The task is to check if `s2` is a **rotated version** of the string `s1`.

> **Note**: The characters in the strings are in **lowercase**.

---

### **Example 1:**

**Input**:  
```
s1 = "abcd", s2 = "cdab"
```
**Output**:  
```
true
```
**Explanation**:  
After **2 right rotations**, `s1` will become equal to `s2`.

---

### **Example 2:**

**Input**:  
```
s1 = "aab", s2 = "aba"
```
**Output**:  
```
true
```
**Explanation**:  
After **1 left rotation**, `s1` will become equal to `s2`.

---

### **Example 3:**

**Input**:  
```
s1 = "abcd", s2 = "acbd"
```
**Output**:  
```
false
```
**Explanation**:  
The strings are **not rotations** of each other.

---

### **Constraints:**
- `1 <= s1.length, s2.length <= 10^5`
- `s1` and `s2` contain only **lowercase** English letters.
