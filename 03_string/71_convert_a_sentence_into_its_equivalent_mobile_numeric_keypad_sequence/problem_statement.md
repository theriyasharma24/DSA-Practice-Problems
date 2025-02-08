# Problem Statement: [Convert a Sentence into its Equivalent Mobile Numeric Keypad Sequence](https://www.geeksforgeeks.org/problems/convert-a-sentence-into-its-equivalent-mobile-numeric-keypad-sequence0547/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card)

## Difficulty: Easy  

### **Problem Description:**
Given a sentence in the form of an **uppercase string**, convert it into its equivalent **mobile numeric keypad sequence**.  
Please note there might be **spaces** in between the words, and we can print spaces by pressing `0`.  

---

### **Example 1:**

**Input:**  
```
S = "GFG"
```
**Output:**  
```
43334
```
**Explanation:**  
- For **'G'**, press **'4'** one time.  
- For **'F'**, press **'3'** three times.  
- For **'G'**, press **'4'** one time.

---

### **Example 2:**

**Input:**  
```
S = "HEY U"
```
**Output:**  
```
4433999088
```
**Explanation:**  
- For **'H'**, press **'4'** two times.  
- For **'E'**, press **'3'** two times.  
- For **'Y'**, press **'9'** three times.  
- For **space (' ')**, press **'0'** one time.  
- For **'U'**, press **'8'** two times.

---

### **Your Task:**  
You do **not** need to read input or print anything.  
Complete the function **`printSequence(S)`**, which takes a **string** as input and returns its equivalent **mobile numeric keypad sequence** as a **string**.

---

### **Expected Complexity:**
- **Time Complexity:** `O(N)`, where `N` is the length of `S`
- **Auxiliary Space:** `O(N)`

---

### **Constraints:**
- `1 ≤ Length of String ≤ 10^5`
- `S` contains only **uppercase English letters** (`A-Z`) and **spaces** (`' '`).
