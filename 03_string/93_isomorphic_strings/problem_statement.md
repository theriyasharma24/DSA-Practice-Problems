# Problem Statement: [Isomorphic Strings](https://www.geeksforgeeks.org/problems/isomorphic-strings-1587115620/1)

## Difficulty: Easy

---

### **Problem Description**

Given two strings `s1` and `s2`, check if these two strings are **isomorphic** to each other.

Two strings are **isomorphic** if the characters in `s1` can be replaced to get `s2`, while maintaining the order of characters.

- A character may map to itself.
- No two characters may map to the same character.

---

### **Examples**

#### **Example 1**

**Input**:  
`s1 = "aab"`  
`s2 = "xxy"`

**Output**:  
`true`

**Explanation**:

- There are two different characters in `"aab"` (`a` and `b`), and `"xxy"` (`x` and `y`).
- The frequency of `a` is `2`, and `b` is `1`, which matches the frequency of `x` (`2`) and `y` (`1`).
- Hence, `"aab"` and `"xxy"` are isomorphic.

---

#### **Example 2**

**Input**:  
`s1 = "aab"`  
`s2 = "xyz"`

**Output**:  
`false`

**Explanation**:

- `"aab"` has two distinct characters (`a`, `b`), whereas `"xyz"` has three (`x`, `y`, `z`).
- Since there is no one-to-one mapping between the characters, they are not isomorphic.

---

#### **Example 3**

**Input**:  
`s1 = "aac"`  
`s2 = "xyz"`

**Output**:  
`false`

**Explanation**:

- `"aac"` has two distinct characters (`a`, `c`), whereas `"xyz"` has three (`x`, `y`, `z`).
- No one-to-one mapping is possible.

---

### **Constraints**

- `1 ≤ |s1|, |s2| ≤ 10^5`
- `s1` and `s2` contain only lowercase English letters (`a-z`).

---
