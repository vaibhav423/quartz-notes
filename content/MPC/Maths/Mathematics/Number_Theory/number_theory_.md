# gallery

```img-gallery
path: Assets/number_theory_
type: vertical
mobile: 3
columns: 3
gutter: 2
radius: 20
```

# general

https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm

https://math.stackexchange.com/questions/2501253/algebraic-proof-of-the-double-dabble-method-algorithms-binary-numbers-to-deci

https://math.stackexchange.com/questions/3194889/proof-of-equivalence-between-two-methods-of-binary-to-decimal-conversion


https://math.stackexchange.com/questions/44836/gcd-and-lcm-of-fractions#textLCM20of20reduced20fractions203D20LCMnumerators2FLCMdenominators

Wilson theorem proof:

consider a prime 'p'
 -> coprime and less than p are (p-1) numbers each of these number have a inverse of each 

-> 2.3.4...(p-2) = 1 mod p
multiply (p-1)
-> (p-1)! = -1modp

## Modular Inverse via Tabular Method
* logic is that  a and b are coprime then there exist x and y such that ax + by = 1
* we can find x and y by using the quotients obtained from the Euclidean division of a and b    

**Example:** Find $19^{-1} \pmod{49}$

### 1. Setup Quotients
Perform Euclidean Division until the remainder is 1:
- 49 = (**2**) × 19 + 11
- 19 = (**1**) × 11 + 8
- 11 = (**1**) × 8 + 3
- 8  = (**2**) × 3 + 2
- 3  = (**1**) × 2 + 1  <-- Stop here

**Quotients ($q$):** 2, 1, 1, 2, 1

### 2. The Table
**Rule:** $y_{n} = (q \times y_{n-1}) + y_{n-2}$
Start the second row with **0** then **1**.

| $q$ | | 2 | 1 | 1 | 2 | 1 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **$y$** | **0** | **1** | **2** | **3** | **5** | **13** | **18** |

**Calculation Path:**
- $(2 \times 1) + 0 = 2$
- $(1 \times 2) + 1 = 3$
- $(1 \times 3) + 2 = 5$
- $(2 \times 5) + 3 = 13$
- $(1 \times 13) + 5 = 18$

### 3. Determine Sign
Check the product of the original number and the table result:
$19 \times 18 = 342$

Find $342 \pmod{49}$:
$342 \div 49 = 6.97... \rightarrow 6 \times 49 = 294$
$342 - 294 = 48$

Since $48 \equiv -1 \pmod{49}$, the inverse is **$-18$**.

### 4. Final Answer
$-18 + 49 = \mathbf{31}$

# images

![](Assets/number_theory_/191cbecdcdb.88df60bb99320b53.png)
![](Assets/number_theory_/193b50fbf84.b1a28596f083ffe2.png)
![](Assets/number_theory_/193b50fbfa6.a532c065dd7f28a6.png)
![](Assets/number_theory_/193b50fbfc4.a6d916dd8630ad13.png)
![](Assets/number_theory_/193b50fbfde.af149d57b62aa53f.png)
![](Assets/number_theory_/193b50fc002.b62bc057423c3b67.png)
![](Assets/number_theory_/193b50fc025.b627bf198d6949ed.png)
![](Assets/number_theory_/193b5156ca5.9792fc8e13690b9b.jpg)
![](Assets/number_theory_/193b5470222.85931a994602dbd8.jpg)
![](Assets/number_theory_/193b54722cf.a62e2ab2cd4b4f50.jpg)
![](Assets/number_theory_/193b5e2f476.85b532f72a075ade.jpg)
![](Assets/number_theory_/193b66a12cf.9e91459bcef97c3b.jpg)
![](Assets/number_theory_/193b9545052.8860dc1e8880503e.jpg)
