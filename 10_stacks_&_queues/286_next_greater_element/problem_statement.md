# Problem Statement: [Next Greater Element](https://www.geeksforgeeks.org/problems/next-larger-element-1587115620/1)

**Difficulty:** Medium  
---

## **Problem Description**  
You are given an array `arr[]` of integers. The task is to find the **next greater element** for each element of the array in order of their appearance in the array.  
The **next greater element** of an element in the array is the nearest element on the **right** which is **greater than the current element**.

If no such element exists, the next greater element for that position is `-1`. For example, the next greater element of the last element is always `-1`.

---

## **Example 1**  
**Input:**  
```
arr[] = [1, 3, 2, 4]
```
**Output:**  
```
[3, 4, 4, -1]
```
**Explanation:**  
The next greater element to `1` is `3`,  
for `3` it's `4`,  
for `2` it's also `4`,  
and `4` has no greater element to the right, so it's `-1`.

---

## **Example 2**  
**Input:**  
```
arr[] = [6, 8, 0, 1, 3]
```
**Output:**  
```
[8, -1, 1, 3, -1]
```

---

## **Example 3**  
**Input:**  
```
arr[] = [10, 20, 30, 50]
```
**Output:**  
```
[20, 30, 50, -1]
```

---

## **Example 4**  
**Input:**  
```
arr[] = [50, 40, 30, 10]
```
**Output:**  
```
[-1, -1, -1, -1]
```

---

## **Your Task:**  
You don't need to read input or print anything.  
Your task is to complete the function **`nextLargerElement(arr)`**, which takes the array `arr[]` as input and **returns a list of next greater elements** in order of appearance.

---

## **Expected Time Complexity:**  
- **O(N)**

## **Expected Auxiliary Space:**  
- **O(N)**

---

## **Constraints:**  
- **1 ≤ arr.size() ≤ 10⁶**  
- **0 ≤ arr[i] ≤ 10⁹**
