
## problem (nice one)
remainder given 4k+3 = x , (2020+ x)^2020  mod 8
![](Assets/Binomial/questions/1771654198.png)
## problem (made blunder)
didnt include ncr
![](Assets/Binomial/questions/1771655961.png)
## problem (consecutive terms to be divided)
the question is easy need to think
![](Assets/Binomial/questions/1771656534.png)
## problem (alternate approach for trinomaial without multinomial expansion)
The constant term in the expansion of $\left(2x + \frac{1}{x^7} + 3x^2\right)^5$ is ________.

Constant term in the expansion of
$$\left(2x + \frac{1}{x^7} + 3x^2\right)^5$$
$$= \frac{1}{x^{35}} \left(2x^8 + 1 + 3x^9\right)^5$$
$$= \frac{1}{x^{35}} \left(1 + x^8(3x + 2)\right)^5$$

Term independent of $x$ = coefficient of $x^{35}$ in 

* important step:

expanding the binomial inside : $(x^8(3x + 2))^t$ ,  $0 < t < 5$ 
$\frac{8t+r}{35}$ , $0 < r < t$

$${^5C_4} \left(x^8(3x + 2)\right)^4$$
$$= {^5C_4} \times \text{coefficient of } x^3 \text{ in } (2 + 3x)^4$$
$$= {^5C_4} \times {^4C_3}(2)^1(3)^3$$
$$= 5 \times 4 \times 2 \times 27$$
$$= 1080$$
## problem (made bullshit blunder)
![](Assets/Binomial/questions/1771762665.png)
## problem (standar one )
Let $\alpha$ be the constant term in the binomial expansion of $\left(\sqrt{x} - \frac{6}{x^{\frac{3}{2}}}\right)^n, n \le 15$.
If the sum of the coefficients of the remaining terms in the expansion is $649$ 
and the coefficient of $x^{-n}$ is $\lambda\alpha$, then $\lambda$ is equal to 
## problem (coprime to 5)
[2022  ·  hard]

If the coefficient of x10 in the binomial expansion of $${\left( {{{\sqrt x } \over {{5^{{1 \over 4}}}}} + {{\sqrt 5 } \over {{x^{{1 \over 3}}}}}} \right)^{60}}$$
is $${5^k}\,.\,l$$, where l, k $$\in$$ N and l is co-prime to 5, 
then k is equal to _____________.

$$ \Rightarrow r = 24$$

$$\therefore$$ Coefficient $$ = {}^{60}{C_{24}}\,.\,{5^3}$$

$$ = {{60!} \over {24!\,\,36!}}\,.\,{5^3}$$


Also given that, l is coprime to 5 means l can't be multiple of 5.
So we have to find all the factors of 5 in 60!, 24! and 36!


$$\therefore$$ Exponent of 5 in 60!

$$= \left\lceil {{{60} \over 5}} \right\rceil  + \left\lceil {{{60} \over {{5^2}}}} \right\rceil  + \left\lceil {{{60} \over {{5^3}}}} \right\rceil  + $$ .....

Exponent of 5 in 24!


$${{{5^{14}}} \over {{5^4}\,.\,{5^8}}}\,.\,{5^3} = {5^k}$$


---
## problem (number of integers k , based on n <= r
The number of positive integers k such that the constant term in
the binomial expansion of $${\left( {2{x^3} + {3 \over {{x^k}}}} \right)^{12}}$$,
x $$\ne$$ 0 is $2^8$ . l, where l is an odd integer, is ______________.

$${T_{r + 1}} = {}^{12}{C_r}{(2{x^{3}})^{12-r}}\,.\,{\left( {{3 \over {{x^k}}}} \right)^{r}}$$
For constant term,

$3(12-r) - kr = 0$

or r = $\frac{36}{3+k}$

$0 >= r >= 12$

get k with this inequality 
## problem (wrong assumption greatest num tm)
i assumed m is integer
q.) To find the greatest term in $(3+6x)^n$ , given $T_9$ is the greatest term,
Using the formula $m = \frac{(n+1)|X|}{|X|+1}$
$$m = \frac{3(n+1)}{3+1} = \frac{3n+3}{4}$$
Since $T_9$ is the greatest term 
$[m]+1 =9$
the integer part of $m$ must satisfy $[m] = 8$:
$$8 < \frac{3n+3}{4} < 9$$
$$32 < 3n+3 < 36$$
$$29 < 3n < 33$$
$$9.66 < n < 11$$
The least integer value is **$n_0 = 10$**.
## problem (blunder)
If n is the number of irrational terms in the
expansion of $${\left( {{3^{1/4}} + {5^{1/8}}} \right)^{60}}$$, then (n $$-$$ 1) is divisible by :
i did everything correct but at alast found the terms that are irrational
instead of finding the number of irrational terms 
## problem (blunder)
Let the coefficients of third, fourth and fifth terms in the
expansion of $${\left( {x + {a \over {{x^2}}}} \right)^n},x \ne 0$$, 
be in the ratio 12 : 8 : 3. Then the term independent of x in the
expansion, is equal to ___________.

in thia step i forgot to write a.

 $${{coefficient\,of\,{T_3}} \over {coefficient\,of\,{T_4}}} = {{{}^n{C_4}.{a^2}} \over {{}^n{C_3}.{a^3}}} = {3 \over {a(n - 2)}} = {3 \over 2}$$
## problem
![](Assets/Binomial/questions/1771348694.png)
The least value of **n** for which the number of integral terms in the Binomial expansion of $(\sqrt[3]{7} + \sqrt[12]{11})^n$ is 183, is :

---
General term $= {}^nC_r \left(7^{1/3}\right)^{n-r} \left(11^{1/12}\right)^r$
$= {}^nC_r (7)^{\frac{n-r}{3}} (11)^{r/12}$

For integral terms, $r$ must be multiple of 12

$\therefore r = 12k, k \in \text{W}$

Total values of $r = 183$

Hence $\max r = 12(182)$

$= 2184$

Min value of $n = 2184$
## problem term from ending / begining
![](Assets/Binomial/questions/1771430899.png)
they solved the problem gracefully 
but i made a mess while solving 
i didnt think of writing the end term w.r.t to b , instead made mess by writing it from begining
## problem (blunder multiple times)
If the coefficients of three consecutive terms in the expansion of $$(1+x)^{n}$$ are in 
the ratio $$1: 5: 20$$, then the coefficient of the fourth term is

when give to find coeff of 4th term , i directly take ${}^{n}C_{4}$
instead of ${}^{n}C_{3}$ 
