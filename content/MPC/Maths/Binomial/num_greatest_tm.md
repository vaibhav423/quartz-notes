# shortcut

$m = \frac{n+1}{|x| + 1}.|x|$ for $(1+x)^n$
if m ϵ N then there are two greatest terms $T_m$ and $T_{m+1}$

if m not ϵ N then there is only one greatest term $T_{[m]+1}$    

# imp thing to understand for num_greatest_tm
* $T_{r}=\binom{n}{r} a^r b^{n-r}$ is a function of r.
## and we need to maximize $T_{r}$ for r ϵ N 
* $T_{r}$ also can be thought of gaussian
* since $\binom{n}{r}$ can be approxated as $k.e^{-x{2}}$ 
* so overall $k.e^{-t{2}}.t^{r}$ is a bell curve 

* ( **1.** ) so the sequence $T_{r}$ must be like $T_{1} > T_{2} .. > T_{m} > or = T_{m+1} < T_{m+2} < T_{m+3} ... $

# Derivation

from ( **1.** ) we can say that $T_{r+1} > or = T_{r}$

if we take $\frac{T_{r+1}}{T_r} > 1$

$$\frac{T_{r+1}}{T_r} = \frac{\binom{n}{r} a^{r} b^{n-r}}{\binom{n}{r-1} a^{r-1} b^{n-r+1}}$$


$\Rightarrow  r < \frac{n+1}{\frac{b}{a} + 1} = m$

this holds only if take > 1 in ( **1.** )st step ,
it changes to r > m if we take < 1 in 1st step or = if we take = in 1st step
## Conditions for m ϵ N :

* **Condition (a) $r < m$:** $T_1 < T_2 < T_3 < \dots < T_{m-1} < T_m$
* **Condition (b) $r = m$:** $T_m = T_{m+1}$ 
(Both $T_m$ and $T_{m+1}$ are the numerically greatest terms)*
this is equivalent to saying that if we set $T_m = T_{m+1}$ we get a value m statisfying that eqn 
this is a  very important case which wont be true if we have m as non integer
* **Condition (c) $r > m$:** $T_{m+1} > T_{m+2} > T_{m+3} > \dots$
##  Conditions for m not ϵ N :
let $[m]$ be the integral part of $m$.


for $r < m$ we have $T_{r+1} > T_r$  
so now we would start writing the sequence for r < m starting from $T_1$ 

and it would satisfy upto r just less than m , which is $[m]$
$\Rightarrow  T_{[m]} < T_{[m]+1}$

now we cant write $T_{[m]+1} < T_{[m]+2}$ because $[m]+1$ is just greater than m
and we have $T_{r+1} < T_r$ for r > m

* so **Condition (a) $r < m$:** $T_1 < T_2 < T_3 < \dots < T_{[m]} < T_{[m]+1}$


for $r > m$ we have $T_{r+1} < T_r$  

i.e r just greater than m is $[m]+1$ 

$T_{[m]+2} < T_{[m]+1}$

* so **Condition (b) $r > m$:** $T_{[m]+1} > T_{[m]+2} > T_{[m]+3} > \dots$
* There is only **one** numerically greatest term.

* The greatest term is $T_{[m]+1}$.


