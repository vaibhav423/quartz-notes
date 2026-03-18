# gallery
```img-gallery
path: Assets/Binomial
type: vertical
mobile: 3
columns: 3
gutter: 2
radius: 20
```
# general
![[num_greatest_tm#shortcut]]
![[questions-binomial]]
## identities
### simple identities
pascal identity(always keep one in a selection and not that one in selection):
$$\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$$

group and dot:
$$\binom{n}{r} = \frac{n-r+1}{r}\binom{n}{r-1}$$
the same can be written as:
$$r\binom{n}{r} = \binom{n}{r-1}(n-r+1)$$ = choose not dotted then dotted


$$ r\binom{n}{r} = n\binom{n-1}{r-1} $$ = select dotted then not dotted  

$$ \binom{n}{r} = \frac{n}{n-r}\binom{n-1}{r} $$  = combine the two above

choose group of m with r captains: 
choose r captain from n the choose non captains  from remaining. = 
choos non captains from n then choose remaining .
$$\binom{n}{m}\binom{m}{r} = \binom{n}{r}\binom{n-r}{m-r} = \binom{n}{m-r}\binom{n-m+r}{r}$$

$\sum_{r=0}^{n}(-1)^r \binom{n}{r} = 0$
$\sum_{r=0}^{n}r \binom{n}{r} = n×2^{ n-1 } $
---
### 5 Vandermonde Identity (imp)
$$\sum_{i=0}^{r} \binom{m}{i} \binom{n}{r-i} = \binom{m}{0} \binom{n}{r} + \binom{m}{1} \binom{n}{r-1} + \dots + \binom{m}{r} \binom{n}{0} = \binom{m+n}{r}$$

$\sum_{0}^{27}{}^{27}{C_r}{}^{100}C_{r} = {}^{127}C_{100}$  $∵ {}^{100}C_{r} = {}^{100}C_{100-r}$
### 6 Special Case of Vandermonde
$$\sum_{i=0}^{n} \binom{n}{i}^2 = \binom{2n}{n}$$
### 7 Hockey-stick Identity (Version 1)
$$\binom{r}{r} + \binom{r+1}{r} + ... + \binom{n}{r} = \binom{n+1}{r+1}$$

* $$\sum_{i=r}^{n} \binom{i}{r} = \sum_{i=0}^{k}\binom{r+i}{r}  = \binom{n+1}{r+1}$$
k = n-r
* choose based on ascending/descending
* for last term n choose r . n+1 is the biggest one  , choose rest
### 8 Hockey-stick Identity (Version 2)
$$\binom{r}{0} + \binom{r+1}{1} + ... + \binom{r+k}{k} = \binom{r+k+1}{k}$$
or
$$\sum_{i=0}^{k} \binom{r+i}{i} = \binom{r+k+1}{k}$$
## extra
### solving $\sum_{r=0}^n r \binom{n}{r}$  type of problems 
[[MPC/Maths/Mathematics/Algebra/expressing_power_terms_in_consecutive_form_.md]]
### theorem 1

$(\sqrt{P} + Q)^n = I + f$ , where I and n are positive integers, n being odd and $0 < f < 1$ 
then show that $(I+f)f = k^n$, where $P - Q^2 = k > 0$ and $\sqrt{P} - Q < 1$

U could do this by simply showing that $f = (\sqrt{P} - Q)^n$ 
which can be done by taking $f' = (\sqrt{P} - Q)^n$ and subtracting the two equations $I + f - f'$ to get $f - f' = 0$ 
### theorem 2
$(\sqrt{P} + Q)^n = I + f$ , where I and n are positive integers, 
show that $(I+f)(I-f) = k^n$, where $P - Q^2 = k > 0$ and $\sqrt{P} - Q < 1$  


U could do this by simply showing that $1 - f = (\sqrt{P} - Q)^n$ 
which can be done by taking $f' = (\sqrt{P} - Q)^n$ and adding the two equations $I + f + f'$ to get $f + f' = 1$ 
# images  

