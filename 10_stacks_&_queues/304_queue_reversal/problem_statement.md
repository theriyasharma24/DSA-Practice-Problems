
# Problem Statement: [Queue Reversal](https://www.geeksforgeeks.org/problems/queue-reversal/1)

**Difficulty:** Easy  

---

## Problem Description

You are given a queue `q` containing integer elements. Your task is to **reverse** the queue so that the elements are in the opposite order.

---

## Input

A queue `q` of size `n` containing integer elements.

---

## Output

A queue where the elements appear in reverse order compared to the input.

---

## Examples

### Example 1:
```
Input: q[] = [4, 3, 1, 10, 2, 6]  
Output: [6, 2, 10, 1, 3, 4]  
Explanation: The queue after reversing is 6 2 10 1 3 4
```

### Example 2:
```
Input: q[] = [4, 3, 2, 1]  
Output: [1, 2, 3, 4]  
Explanation: The queue after reversing is 1 2 3 4
```

### Example 3:
```
Input: q[] = [7, 9, 5, 12, 8]  
Output: [8, 12, 5, 9, 7]  
Explanation: The queue after reversing is 8 12 5 9 7
```

---

## Your Task

You don't need to read input or print anything.  
Complete the function `reverseQueue(q)` which takes a `Queue` as input and returns the reversed queue.

---

## Expected Time Complexity

- **O(n)** — where `n` is the number of elements in the queue.

---

## Expected Auxiliary Space

- **O(n)** — due to usage of a stack or recursion.

---

## Constraints

- `1 ≤ q.size() ≤ 10^6`  
- `1 ≤ q[i] ≤ 10^5`  
