# Problem Statement: [Reverse an Array](https://www.geeksforgeeks.org/problems/reverse-an-array/1?itm_source=geeksforgeeks)

## Difficulty: Easy

### Problem Description:

You are given an array of integers `arr[]`. Your task is to reverse the given array.

### Input:

- An array of integers `arr[]`.

### Output:

- Return the array after reversing it.

### Example 1:

**Input**:  
`arr = [1, 4, 3, 2, 6, 5]`

**Output**:  
`[5, 6, 2, 3, 4, 1]`

**Explanation**:  
The elements of the array are 1, 4, 3, 2, 6, 5. After reversing the array, the first element goes to the last position, the second element goes to the second last position, and so on. Hence, the reversed array is `[5, 6, 2, 3, 4, 1]`.

---

### Example 2:

**Input**:  
`arr = [4, 5, 2]`

**Output**:  
`[2, 5, 4]`

**Explanation**:  
The elements of the array are 4, 5, 2. The reversed array will be `[2, 5, 4]`.

---

### Example 3:

**Input**:  
`arr = [1]`

**Output**:  
`[1]`

**Explanation**:  
The array has only one element, hence the reversed array is the same as the original array.

---

### Constraints:

- `1 <= arr.size() <= 10^5`
- `0 <= arr[i] <= 10^5`
