# Problem Statement: [More than n/k Occurrences](https://www.geeksforgeeks.org/problems/count-element-occurences/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card)

**Difficulty**: Easy

---

## Problem Description:

Given an array `arr` of size `n` and an integer `k`, find the count of elements in the array that appear more than \( \frac{n}{k} \) times.

---

## Examples:

### Example 1:

**Input**:  
`arr = [3, 1, 2, 2, 1, 2, 3, 3], k = 4`  
**Output**:  
`2`  
**Explanation**:  
In the given array, `3` and `2` are the only elements that appear more than \( \frac{n}{k} = \frac{8}{4} = 2 \) times.

---

### Example 2:

**Input**:  
`arr = [2, 3, 3, 2], k = 3`  
**Output**:  
`2`  
**Explanation**:  
In the given array, `3` and `2` are the only elements that appear more than \( \frac{n}{k} = \frac{4}{3} \approx 1.33 \) times.

---

### Example 3:

**Input**:  
`arr = [1, 4, 7, 7], k = 2`  
**Output**:  
`0`  
**Explanation**:  
In the given array, no element appears more than \( \frac{n}{k} = \frac{4}{2} = 2 \) times.

---

## Constraints:

- \( 1 \leq arr.size() \leq 10^6 \)
- \( 0 \leq arr[i] \leq 10^8 \)
- \( 1 \leq k \leq arr.size() \)
