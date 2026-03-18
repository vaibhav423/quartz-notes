# problem (collinearity and cross product find circle)
Let $\vec{\mathrm{c}}$ and $\vec{\mathrm{d}}$ be vectors such that $|\vec{\mathrm{c}}+\vec{\mathrm{d}}|=\sqrt{29}$ and $\vec{\mathrm{c}} \times(2 \hat{i}+3 \hat{j}+4 \hat{k})=(2 \hat{i}+3 \hat{j}+4 \hat{k}) \times \vec{\mathrm{d}}$.
If $\lambda_1, \lambda_2\left(\lambda_1>\lambda_2\right)$ are the possible values of $(\vec{c}+\vec{d}) \cdot(-7 \hat{i}+2 \hat{j}+3 \hat{k})$,
then the equation $\mathrm{K}^2 x^2+\left(\mathrm{K}^2-5 \mathrm{~K}+\lambda_1\right) x y+\left(3 \mathrm{~K}+\frac{\lambda_2}{2}\right) y^2-8 x+12 y+\lambda_2=0$ 
represents a circle, for K equal to :

* notice $(c+d)×(2i+3j+4k)=0$ 
you will get c+d in one variable , use the magnitude to solve for k
# problem (maximumize dot product)
Let $\vec{a}=2 \hat{i}-\hat{j}+\hat{k}$ and $\vec{b}=\lambda \hat{j}+2 \hat{k}, \lambda  ϵ  \textbf{Z}$  be two vectors. Let $\vec{c}=\vec{a} \times \vec{b}$ and $\vec{d}$ be a
vector of magnitude 2 in $y z$-plane. If $|\vec{c}|=\sqrt{53}$, then the
maximum possible value of $(\vec{c} \cdot \vec{d})^2$ is equal to :

find c :(straightforward) 

do cross product , get vector in terms of lambd
solve for it using magnitude of c

geometrically c should be above vector d in yz 

now $(\vec{c}_{yz} \cdot \vec{d})^2 \leq |\vec{c}_{yz}|^2 |\vec{d}|^2$

so rotating d to be in the same direction as c , gives max
# problem (simple question too much time collinearity)
Let $\vec{a}, \vec{b}, \vec{c}$ be three vectors such that $\vec{a} \times \vec{b}=2(\vec{a} \times \vec{c})$. If $|\vec{a}|=1,|\vec{b}|=4,|\vec{c}|=2$,
and the angle between $\vec{b}$ and $\vec{c}$ is $60^{\circ}$, then
$|\vec{a} \cdot \vec{c}|$ is equal to

use collinearity:
$\vec{a} \times ( \vec{b} - 2\vec{c}) = 0$

$\vec{b} - 2\vec{c} = k \vec{a}$

then $|\vec{b} - 2\vec{c}| = |k|$

get k and substitute back to get $|\vec{a} \cdot \vec{c}|$
# problem (very tough find b.c from unobvious conditions)
Let $\vec{a}=\hat{\mathrm{i}}+\hat{\mathrm{j}}+\hat{\mathrm{k}}, \vec{\mathrm{b}}=2 \hat{\mathrm{i}}+2 \hat{\mathrm{j}}+\hat{\mathrm{k}}$ and $\vec{\mathrm{d}}=\vec{a} \times \vec{\mathrm{b}}$. If $\vec{\mathrm{c}}$ is a vector such that $\vec{a} \cdot \vec{\mathrm{c}}=|\vec{\mathrm{c}}|$,
$|\vec{\mathrm{c}}-2 \vec{a}|^2=8$ and the angle between $\vec{\mathrm{d}}$ and $\vec{\mathrm{c}}$ is $\frac{\pi}{4}$, then $|10-3 \vec{\mathrm{~b}} \cdot \vec{\mathrm{c}}|+|\vec{\mathrm{d}} \times \vec{\mathrm{c}}|^2$
is equal to _________.

first solve for |c|

do ×c in d = a × c 
and try to find b.c or follow below

## 1. Vector Parameters

* |a|² = 3, |b|² = 9, a·b = 5
* d = a × b  =>  |d|² = 2, d·a = 0, d·b = 0

## 2. Constraints on Vector c
* |c - 2a|² = 8  =>  |c|² + 4|a|² - 4(a·c) = 8
* Given a·c = |c|:  |c|² - 4|c| + 12 = 8  =>  (|c| - 2)² = 0  =>  |c| = 2, a·c = 2
* Angle(d, c) = π/4  =>  d·c = |d||c|cos(π/4) = √2 * 2 * (1/√2) = 2
* |d × c|² = |d|²|c|²sin²(π/4) = 2 * 4 * (1/2) = 4

## 3. Basis Decomposition (a, d, a × d)
Let c = αa + βd + γ(a × d). Since a ⊥ d:
* c·a = α|a|²  =>  2 = 3α  =>  α = 2/3
* c·d = β|d|²  =>  2 = 2β  =>  β = 1
* |c|² = α²|a|² + β²|d|² + γ²|a × d|²
  4 = (4/9)(3) + (1)(2) + γ²(3*2)  =>  4 = 4/3 + 2 + 6γ²  =>  6γ² = 2/3  =>  γ = ±1/3

## 4. Evaluation of b·c
* b·c = α(b·a) + β(b·d) + γ(b · (a × d))
* b·(a × d) = (b × a)·d = (-d)·d = -|d|² = -2
* b·c = (2/3)(5) + 1(0) + (±1/3)(-2) = 10/3 ∓ 2/3  =>  {4, 8/3}

## 5. Final Result
* Result = |10 - 3(b·c)| + |d × c|²
* Case 1 (b·c = 4): |10 - 12| + 4 = 6
* Case 2 (b·c = 8/3): |10 - 8| + 4 = 6
**ANSWER: 6**
# problem 
