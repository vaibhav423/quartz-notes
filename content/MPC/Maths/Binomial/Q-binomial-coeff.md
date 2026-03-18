## problem (find range for k [nice one])

${ }^{n-1} C_r=\left(k^2-8\right){ }^n C_{r+1}$ if and only if  (i.e find range for k)

$\Rightarrow k^2-8= \frac{r+1}{n}$

we need to find the range of $\frac{r+1}{n}$

so the minimum inequality it should satisfy is:

$0 \ge  r \ge  n-1$ , $0 \ge  r+1 \ge  n$   
$1 \ge  r+1 \ge  n$ , $0 \ge  r+1 \ge  n$   

⇒ $1 \ge  r+1 \ge  n$ 

⇒ $\frac{1}{n} \ge  \frac{r+1}{n} \ge  1$  

we need to think logically from here ,the question is to 
find the **maximum possible range for k** ,for all valid (r,n)

now increasing n will increase the size of range , hence 1/n → 0  

⇒ $0 \ge  k^2-8 \ge  1$ 
### misc thoughts:
the valid range of r for all pairs (k,n)
is $0 \le r \le n-1$ 
## problem (sum using vandermonde or integration)

Let 
$$
\alpha=\sum_\limits{k=0}^n\left(\frac{\left({ }^n C_k\right)^2}{k+1}\right)
$$ 
and 
$\beta=\sum_\limits{k=0}^{n-1}\left(\frac{{ }^n C_k{ }^n C_{k+1}}{k+2}\right)$ 

If $5 \alpha=6 \beta$, then $n$ equals _______.

[[Binomial#5 Vandermonde Identity (imp)]]
use vandermonde identity or

integerate $(1+x)^n$ multiply by $(1+x)^n$ . and find suitable coeff  
## problem (invovles pattern finding )

In the expansion of $$(1+x)\left(1-x^2\right)\left(1+\frac{3}{x}+\frac{3}{x^2}+\frac{1}{x^3}\right)^5, x \neq 0$$, the sum of the coefficients of $x^3$ and $$x^{-13}$$ is equal to __________.

**Answer:** 118

**Explanation:**

$$
\begin{aligned}
& (1+x)\left(1-x^2\right)\left(1+\frac{3}{x}+\frac{3}{x^2}+\frac{1}{x^3}\right)^5 \\
& =(1+x)\left(1-x^2\right)\left(\left(1+\frac{1}{x}\right)^3\right)^5 \\
& =\frac{(1+x)^2(1-x)(1+x)^{15}}{x^{15}} \\
& =\frac{(1+x)^{17}-x(1+x)^{17}}{x^{15}}
\end{aligned}
$$

$$=\operatorname{coeff}\left(\mathrm{x}^3\right)$$ in the expansion $$\approx \operatorname{coeff}\left(\mathrm{x}^{18}\right)$$ in

$$\begin{aligned}
& (1+x)^{17}-x(1+x)^{17} \\
& =0-1 \\
& =-1
\end{aligned}$$

$$\operatorname{coeff}\left(\mathrm{x}^{-13}\right)$$ in the expansion $$\approx \operatorname{coeff}\left(\mathrm{x}^2\right)$$ in

$$\begin{aligned}
& (1+x)^{17}-x(1+x)^{17} \\
& =\left(\begin{array}{c}
17 \\
2
\end{array}\right)-\left(\begin{array}{c}
17 \\
1
\end{array}\right) \\
& =17 \times 8-17 \\
& =17 \times 7 \\
& =119
\end{aligned}$$
## problem (taylor expansion , tough)

Let $$a=1+\frac{{ }^2 \mathrm{C}_2}{3 !}+\frac{{ }^3 \mathrm{C}_2}{4 !}+\frac{{ }^4 \mathrm{C}_2}{5 !}+...., \mathrm{b}=1+\frac{{ }^1 \mathrm{C}_0+{ }^1 \mathrm{C}_1}{1 !}+\frac{{ }^2 \mathrm{C}_0+{ }^2 \mathrm{C}_1+{ }^2 \mathrm{C}_2}{2 !}+\frac{{ }^3 \mathrm{C}_0+{ }^3 \mathrm{C}_1+{ }^3 \mathrm{C}_2+{ }^3 \mathrm{C}_3}{3 !}+....$$ Then $$\frac{2 b}{a^2}$$ is equal to _________.

**Answer:** 8

**Explanation:**

$$\begin{aligned}
& a=1+\frac{{ }^2 C_2}{3!}+\frac{{ }^3 C_2}{4!}+\frac{{ }^4 C_2}{5!}+\ldots \\
& b=1+\frac{{ }^1 C_0+{ }^1 C_1}{1!}+\frac{{ }^2 C_0+{ }^2 C_1+{ }^2 C_2}{2!}+\ldots \\
& b=1+\frac{2}{1!}+\frac{2^2}{2!}+\frac{2}{3!}+\ldots=e^2
\end{aligned}$$

Using $$e^x=1+\frac{x}{1!}+\frac{x^2}{2!}+\frac{x}{3!}+\ldots$$

$$\begin{aligned}
a= & 1+\sum_{r=2}^{\infty} \frac{{ }^r C_2}{(r+1)!}=1+\sum_{r=2} \frac{r(r-1)}{2(r+1)!} \\
& =1+\frac{1}{2} \sum_{r=2}^{\infty} \frac{(r+1) r-2 r}{(r+1)!} \\
& =1+\frac{1}{2} \sum_{r=2}^{\infty} \frac{1}{(r-1)!}-\frac{1}{2} \sum_{r=2} \frac{2 r}{(r+1)!} \\
& =1+\frac{1}{2}\left(\frac{1}{1!}+\frac{1}{2!}+\ldots\right)-\sum_{r=2}^{\infty} \frac{(r+1)-1}{(r+1)!} \\
& =1+\frac{1}{2}(e-1)-\sum_{r=2}^{\infty} \frac{1}{r!}+\sum_{r=2} \frac{1}{(r+1)!} \\
& =1+\frac{1}{2}(e-1)-\left(e-\frac{1}{1!}-\frac{1}{0!}\right)+\left(e-\frac{1}{1!}-\frac{1}{0!}-\frac{1}{2!}\right) \\
& =1+\frac{e}{2}-\frac{1}{2}-e+2+e-2-\frac{1}{2}=\frac{e}{2} \\
\Rightarrow & \frac{2 b}{a^2}=\frac{2}{\frac{e^2}{4}} 8
\end{aligned}$$
## problem (2nd time blunder on$r^2.ncr$)

Suppose$\sum\limits_{r = 0}^{2023} {{r^2}{}~^{2023}{C_r} = 2023 \times \alpha  \times {2^{2022}}}$. Then the value of$\alpha$is ___________

did$f^{\prime} - f^{\prime\prime}$instead of$f^{\prime} + f^{\prime\prime}$
## problem (hockey stick based)
[[Binomial#7 Hockey-stick Identity (Version 1)]]
If$\left( {{}^{40}{C_0}} \right) + \left( {{}^{41}{C_1}} \right) + \left( {{}^{42}{C_2}} \right) + \,\,.....\,\, + \,\,\left( {{}^{60}{C_{20}}} \right) = {m \over n}{}^{60}{C_{20}}$m and n 
are coprime, then m + n is equal to ___________.

$\sum_{i=0}^{20}{}^{40+i}C_{40} = {}^{40+20+1}C_{40+1}$
## problem (inequality based, v tough)

If the sum of the coefficients of all the positive powers of x,
in the Binomial expansion of${\left( {{x^n} + {2 \over {{x^5}}}} \right)^7}$is 939, 
then the sum of all the possible integral values of n is _________.
![](Assets/Binomial/questions/1772319990.png)
![](Assets/Binomial/questions/1772319990.png)
## problem (vandermode based) 

$\sum\limits_{k = 1}^{31} {\left( {{}^{31}{C_k}} \right)\left( {{}^{31}{C_{k - 1}}} \right) - \sum\limits_{k = 1}^{30} {\left( {{}^{30}{C_k}} \right)\left( {{}^{30}{C_{k - 1}}} \right) = {{\alpha (60!)} \over {(30!)(31!)}}} }$,

${}^{31}{C_k} {}^{31}{C_{31 -k + 1}}$-${}^{30}{C_k} {}^{30}{C_{30 -k + 1}}$

${}^{62}C_{32}$-${}^{60}C_{31}$
## problem (lengthy p , q)
If the coefficients of$x$and$x^{2}$in the expansion of$(1+x)^{\mathrm{p}}(1-x)^{\mathrm{q}}, \mathrm{p}, \mathrm{q} \leq 15$, are$-3$and$-5$respectively, then the coefficient of$x^{3}$is equal to _____________.
## problem (imp double summation)

find$\sum\limits_{i,\,j = 0\,\,i \ne j}^n {{}^n{C_i}\,{}^n{C_j}}$

$\sum\limits_{i,\,j = 0\,\,i \ne j}^n {{}^n{C_i}\,{}^n{C_j} = \sum\limits_{i,\,j = 0}^n {{}^n{C_i}\,{}^n{C_j} - \sum\limits_{i = j}^n {{}^n{C_i}\,{}^n{C_j}} } }$

$= \sum\limits_{j = 0}^n {{}^n{C_i}\,\sum\limits_{j = 0}^n {{}^n{C_j} - \sum\limits_{i = 0}^n {{}^n{C_i}\,{C_i}} } }$

$= {2^n}\,.\,{2^n} - {}^{2n}{C_n}$

$= {2^{2n}} - {}^{2n}{C_n}$
## problem (sum for r!)

$\sum\limits_{r=1}^{20}\left(r^{2}+1\right)(r !)$is equal to

$((r+1)^2 - 2r)r!$
$(r+1)(r+1)! - 2rr!$
$(r+1+1-1)(r+1)! - 2( (r+1-1)r! )$
$(r+2)! - (r+1)! - 2((r+1)! - r!)$
## problem (a0+a1+a2+.. type , substitue 1 ,-1)

Let (1 + x + 2x2)20 = a0 + a1x + a2x2 + .... + a40x40. 
Then a1 + a3 + a5 + ..... + a37 is equal to

${(1 + x + 2{x^2})^{20}} = {a_0} + {a_1}x + {a_2}{x^2} + .... + {a_{40}}{x^{40}}$

Put x = 1

$\Rightarrow {4^{20}} = {a_0} + {a_1} + ....... + {a_{40}}$..... (i)

Put x =$-$1

$\Rightarrow {2^{20}} = {a_0} - {a_1} + ....... +  - {a_{39}} + {a_{40}}$..... (ii)

by (i)$-$(ii) we get,

${4^{20}} - {2^{20}} = 2({a_1} + {a_3} + ...... + {a_{37}} + {a_{39}})$

$\Rightarrow {a_1} + {a_3} + ...... + {a_{37}} = {2^{39}} - {2^{19}} - {a_{39}}$..... (iii)
## problem (nice inequality)

The number of elements in the set {n$\in${1, 2, 3, ......., 100} | (11)n > (10)n + (9)n} is ______________.

${11^n} > {10^n} + {9^n}$

$\Rightarrow {11^n} - {9^n} > {10^n}$

$\Rightarrow {(10 + 1)^n} - {(10 - 1)^n} > {10^n}$

$\Rightarrow 2\{ {}^n{C_1}{.10^{n - 1}} + {}^n{C_3}{10^{n - 10}} + {}^n{C_5}{10^{n - 5}} + .....\}  > {10^n}$

$\Rightarrow$ ${1 \over 5}\left[ {{}^n{C_1}{{10}^n} + {}^n{C_3}{{10}^{n - 2}} + {}^n{C_5}{{10}^{n - 4}} + .....} \right] > {10^n}$

$\Rightarrow$ ${1 \over 5}\left[ {{}^n{C_1} + {}^n{C_3}{{10}^{ - 2}} + {}^n{C_5}{{10}^{ - 4}} + .....} \right] > 1$

Clearly the above inequality is true for n$\ge$5

For n = 4, we have${1 \over 5}\left[ {4 + {4 \over {{{10}^2}}}} \right] = {4 \over 5}\left( {{{101} \over {100}}} \right) < 1$

$\Rightarrow$Inequality does not hold good for n = 1, 2, 3, 4

So, required number of elements ={5, 6, 7, ......., 100} = 96
## problem (2) a0+a1+.. type, substitue 1, -1)

If the sum of the coefficients of all even powers of x in the product
 (1 + x + x2 + ....+ x2n)(1 - x + x2 - x3 + ...... + x2n) is 61, then n is equal to _______.


(1 + x + x2 + ....+ x2n)(1 - x + x2 - x3 + ...... + x2n)

= a0 + a1x + a2x2 + …..
put x = 1

 (2n + 1) $\times$ 1 = a0 + a1 + a2 + …… (1)

put x = –1

 1$\times$(2n + 1) = a0 – a1 + a2+  …….. (2)

Adding (1) and (2)

4n + 2 = 2(a0 + a2 + ….. )

$\Rightarrow$4n + 2 = 2 $\times$ 61

$\Rightarrow$n = 30
## problem

