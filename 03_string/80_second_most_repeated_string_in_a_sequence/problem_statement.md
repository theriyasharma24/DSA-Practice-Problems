# Problem Statement: [Second Most Repeated String in a Sequence](https://www.geeksforgeeks.org/problems/second-most-repeated-string-in-a-sequence0534/1)

## Difficulty: Easy

---

### **Problem Description**

Given a sequence of strings, the task is to find out the second most repeated (or frequent) string in the given sequence.

**Note:** There will always be a unique second most repeated string.

---

### **Examples**

#### **Example 1**

**Input**:  
```
N = 6  
arr[] = {aaa, bbb, ccc, bbb, aaa, aaa}
```
**Output**:  
```
bbb
```
**Explanation**:  
- "aaa" appears 3 times (most frequent).  
- "bbb" appears 2 times (second most frequent).  
- "ccc" appears 1 time.  
- The second most frequent string is `"bbb"`.

---

#### **Example 2**

**Input**:  
```
N = 6  
arr[] = {geek, for, geek, for, geek, aaa}
```
**Output**:  
```
for
```
**Explanation**:  
- "geek" appears 3 times (most frequent).  
- "for" appears 2 times (second most frequent).  
- "aaa" appears 1 time.  
- The second most frequent string is `"for"`.

---

### **Function Signature**
```python
def secFrequent(arr: List[str], N: int) -> str:
```

### **Your Task**
You don't need to read input or print anything.  
Your task is to implement the function `secFrequent(arr, N)`, which takes a list of strings `arr[]` and an integer `N` as inputs, and returns the second most frequent string in the array.  

If no such string exists, return an empty string.

---

### **Expected Time and Space Complexity**
- **Expected Time Complexity:** `O(N * max(|Si|))`
- **Expected Auxiliary Space:** `O(N * max(|Si|))`

---

### **Constraints**
- `1 ≤ N ≤ 10^3`
- Each string in `arr` consists of lowercase English letters (`a-z`).
