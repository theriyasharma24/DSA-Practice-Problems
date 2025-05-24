Here is the Markdown (`.md`) version of the **"Sort by Set Bit Count"** problem in the format you requested:

---

````markdown
# Problem Statement: [Sort by Set Bit Count](https://www.geeksforgeeks.org/problems/sort-by-set-bit-count1153/1)

**Difficulty:** Easy  
**Accuracy:** 36.7%  
**Submissions:** 52K+  
**Points:** 2  
**Average Time:** 20m  

---

### **Problem Description**  
Given an array of integers, sort the array **in descending order according to the count of set bits** (1s) in the binary representation of array elements.  

📌 **Note:** For integers having the **same number of set bits**, maintain their original relative order in the array (i.e., use a **stable sort**).

---

### **Examples**

#### **Example 1**  
**Input:**  
```python
arr = [5, 2, 3, 9, 4, 6, 7, 15, 32]
````

**Output:**

```python
15 7 5 3 9 6 2 4 32
```

**Explanation:**
Binary representations and set bit counts:

* 15 → 1111 → 4
* 7  → 0111 → 3
* 5  → 0101 → 2
* 3  → 0011 → 2
* 9  → 1001 → 2
* 6  → 0110 → 2
* 2  → 0010 → 1
* 4  → 0100 → 1
* 32 →100000 → 1

Grouped and sorted in descending order of set bits (while maintaining order within groups):

```python
[15], [7], [5, 3, 9, 6], [2, 4, 32]
```

---

#### **Example 2**

**Input:**

```python
arr = [1, 2, 3, 4, 5, 6]
```

**Output:**

```python
3 5 6 1 2 4
```

**Explanation:**
Binary representations:

* 3 → 0011 → 2
* 5 → 0101 → 2
* 6 → 0110 → 2
* 1 → 0001 → 1
* 2 → 0010 → 1
* 4 → 0100 → 1

Sorted output:

```python
[3, 5, 6], [1, 2, 4]
```

### **Expected Time Complexity:**

* `O(N log N)`

### **Expected Auxiliary Space:**

* `O(1)`


### **Constraints:**
1 ≤ N ≤ 105
1 ≤ A[i] ≤ 106


