
## problem (remainder by modulus)
Find remainder when $7^{103}$ is divided by 23.


Given:
$$7^{110} \equiv 1 \pmod{23}$$

We can write $7^{110}$ as:
$$7^{103} \cdot 7^7 \equiv 1 \pmod{23}$$

This implies that $7^{103}$ is the modular multiplicative inverse of $7^7$ modulo 23.

### 1. Calculate $7^7 \pmod{23}$
* $7^1 \equiv 7 \pmod{23}$
* $7^2 = 49 \equiv 3 \pmod{23}$
* $7^3 \equiv 3 \cdot 7 = 21 \equiv -2 \pmod{23}$
* $7^6 \equiv (-2)^2 =4 \pmod{23}$
* $7^7 = 7^6 \cdot 7^1 \equiv 4 \cdot 7 = 28 \equiv 5 \pmod{23}$

### 2. Solve for $7^{103}$
$$7^{103} \cdot 5 \equiv 1 \pmod{23}$$

We need to find the inverse of $5$ modulo 23. Since $5 \times 14 = 70$ and $70 = (3 \times 23) + 1$:
$$5 \times 14 \equiv 1 \pmod{23}$$

Therefore:
$$7^{103} \equiv 14 \pmod{23}$$
## problem (for numbers closer to each other remainder can be found by this)
![](Assets/Binomial/questions/1771605822.png)
## problem (remainder for $f(n)$) 
 **Statement (S2): $13(13)^n - 12n - 13$ is divisible by 144**

1. **Rewrite $13^n$ using Binomial Expansion:**
   * $13^n = (1 + 12)^n$
   * $(1 + 12)^n = 1 + n(12) + \frac{n(n-1)}{2}(12^2) + \dots$
   * $13^n \equiv 1 + 12n \pmod{144}$ (since all subsequent terms contain $12^2 = 144$)

2. **Substitute back into the expression:**
   * $13(1 + 12n + 144K) - 12n - 13$
   * $13 + 156n + (13 \cdot 144K) - 12n - 13$
   * $144n + 13(144K)$

3. **Conclusion:**
   * The expression simplifies to $144(n + 13K)$, which is a multiple of 144 for all $n \in \mathbb{N}$.
   * Therefore, (S2) is **correct**.
## problem (made blunder) 
 **Question **

Let the number $(22)^{2022} + (2022)^{22}$ leave the remainder $\alpha$ when divided by $3$ and $\beta$ when divided by $7$. Then $(\alpha^2 + \beta^2)$ is equal to:
made mistake applying fermat theorem on 2022 with mod 3 
fermat theorem not applicable when a is divisible by p    a,p should be coprime .
## proble (made blunder )
at the end , i didnt devide by 2 , i just took the remainder of $3^{2022} - 1$    
The remainder on dividing $1 + 3 + 3^2 + 3^3 + \dots + 3^{2021}$ by $50$ is __________.

Given series:
$S = 1 + 3 + 3^2 + 3^3 + \dots + 3^{2021}$

The sum of a G.P. is given by $S = \frac{a(r^n - 1)}{r - 1}$

$$S = \frac{1(3^{2022} - 1)}{3 - 1}$$
$$S = \frac{3^{2022} - 1}{2}$$
## problem ( remainder when div by 6 , using by 2 and 3 , CRT )  
To find the remainder of $3^{10} - 2^{10}$ divided by $6$

### 1. Modulo 2
* $3 \equiv 1 \pmod 2$
* $2 \equiv 0 \pmod 2$
* $3^{10} - 2^{10} \equiv 1^{10} - 0^{10} \equiv \mathbf{1 \pmod 2}$

### 2. Modulo 3
* $3 \equiv 0 \pmod 3$
* $2 \equiv -1 \pmod 3$
* $3^{10} - 2^{10} \equiv 0^{10} - (-1)^{10} \equiv 0 - 1 \equiv -1 \equiv \mathbf{2 \pmod 3}$

### 3. Combining results (Chinese Remainder Theorem)
We are looking for a number $x \in \{0, 1, 2, 3, 4, 5\}$ such that:
* $x$ is odd (from $x \equiv 1 \pmod 2$)
* $x$ divided by $3$ leaves a remainder of $2$ (from $x \equiv 2 \pmod 3$)

Checking the odd numbers:
* $1 \pmod 3 = 1$
* $3 \pmod 3 = 0$
* $5 \pmod 3 = 2$ (Matches!)

**Remainder = 5**
## problem (tricky)
To find the greatest integer $k$ such that $(49^k + 1)$ divides $S = \sum_{i=0}^{125} 49^i$:
1. **GP Sum:** $S = \frac{49^{126} - 1}{48}$
2. **Factorize:** $49^{126} - 1 = (49^{63} + 1)(49^{63} - 1)$
3. **Compare:** $S = \frac{(49^{63} + 1)(49^{63} - 1)}{48} \implies k = 63$
## problem (made blunder)
$(2021)^{3762} \equiv \text{mod } 17$

$(2021)^{16} \equiv 1 \text{ mod } 17$

$(2021)^{3762} \equiv (2021)^{10} \text{ mod } 17$

$\equiv (-2)^{10} \text{ mod } 17$

$\equiv (- 1024) \text{ mod } 17$ (made blunder)
