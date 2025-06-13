# Problem Statement: [Division without using multiplication, division and mod operator](https://www.geeksforgeeks.org/problems/division-without-using-multiplication-division-and-mod-operator/1)

**Difficulty:** Medium  

---

## **Problem Description**

Given two integers `dividend` and `divisor`. Find the **quotient** after dividing the `dividend` by `divisor` **without using** multiplication (`*`), division (`/`), and mod (`%`) operators.

### Note:
- If the quotient is strictly greater than `2^31 - 1`, return `2^31 - 1`.
- If the quotient is strictly less than `-2^31`, return `-2^31`.

---

## **Examples**

### **Example 1**

**Input:**
```

dividend = 10, divisor = 3

```

**Output:**
```

3

```

**Explanation:**
10 divided by 3 gives quotient as 3 and remainder as 1.

---

### **Example 2**

**Input:**
```

dividend = 43, divisor = -8

```

**Output:**
```

-5

```

**Explanation:**
43 divided by -8 gives quotient as -5 and remainder as 3.

---

## **Constraints**

- -10⁹ ≤ `dividend`, `divisor` ≤ 10⁹

---

## **Expected Time Complexity**

- **O(log n)** (Efficient implementation using bit manipulation)

---

## **Expected Auxiliary Space**

- **O(1)** (Constant space)
