# imp type problem.
14 (simple line eqn) , 15 (perpend dist) 16 ( foot of perpend) 17 (dstance of poing along line)

write each with fastest step including writing procedure in paper

## foot of perpend
* write in this way
$t$ :                    | $kt$: 
$p$ :                    |  $w+kt$ : 
$w$ :                    | if image is needed 
$p-w$:                   |   2I - P
k = $\frac{(p-w).t}{|t|^2}$ :          |  
### example
## distance of point from line
$t$ :
$p$ :
$w$ :
$p-w$ : a b c

$a^2 + b^2 + c^2$ - $\frac{(a b c . t)^2}{t^2}$ (dont add any terms here only square and multiply)
simplify in one go
### example
## dist of point from line along vector v
solve for k:

$\frac{w+kt-p}{v}$

substitue k in w+kt
### example
# problem (smart solve line via 2 lines

Q.) Let the line $L_1$ be parallel to the vector $-3\hat{i} + 2\hat{j} + 4\hat{k}$ and
pass through the point $(2, 6, 7)$, and the line $L_2$ be parallel to the 
vector $2\hat{i} + \hat{j} + 3\hat{k}$ and pass through the point $(4, 3, 5)$. 
If the line $L_3$ is parallel to the vector $-3\hat{i} + 5\hat{j} + 16\hat{k}$ and
intersects the lines $L_1$ and $L_2$ at the points $C$ and $D$, respectively,
then $\left|\vec{CD}\right|^2$ is equal to:

to solve : there are two ways .
* (normal way) write the points which takes two variable , then apply parallel condn.
* other way use one variable

* $P_1 = (2, 6, 7)$ and $\mathbf{v}_1 = (-3, 2, 4)$
* $P_2 = (4, 3, 5)$ and $\mathbf{v}_2 = (2, 1, 3)$
* $\mathbf{v}_3 = (-3, 5, 16)$
$$\vec{CD} = (P_2 - P_1) + t_2\mathbf{v}_2 - t_1\mathbf{v}_1$$
Since $\vec{CD} \parallel \mathbf{v}_3$, there exists a scalar $k$ such that:
$$(P_2 - P_1) + t_2\mathbf{v}_2 - t_1\mathbf{v}_1 = k\mathbf{v}_3$$

Instead of solving for all variables, we use the scalar triple product to isolate $k$. By dotting the equation with the cross product of the line directions ($\mathbf{v}_1 \times \mathbf{v}_2$), we eliminate the $t_1$ and $t_2$ terms.

1.  **Calculate $\mathbf{n} = \mathbf{v}_1 \times \mathbf{v}_2$:**

2.  **Apply the Triple Product Identity:**
    $$(P_2 - P_1) \cdot \mathbf{n} = k(\mathbf{v}_3 \cdot \mathbf{n})$$
3.  **Compute $|\vec{CD}|^2$:**
    Since $\vec{CD} = \vec{AB} k\mathbf{v}_3$ and $k=1$:
# problem (smart solve , image of point sym for 2 lines)
If the image of the point $\mathrm{P}(a, 2, a)$ in the line $\frac{x}{2}=\frac{y+a}{1}=\frac{z}{1}$ is Q and the image
of Q in the line $\frac{x-2 b}{2}=\frac{y-a}{1}=\frac{z+2 b}{-5}$ is P , then $a+b$ is equal to 

1. Symmetry: Lines $L_1$ and $L_2$ are perpendicular bisectors of $PQ$. 
   Intersection $M = L_1 \cap L_2$.
2. Parametric Intersection: 
   $M = (2\lambda, \lambda-a, \lambda) \in L_2 \implies \frac{2\lambda-2b}{2} = \lambda-2a = \frac{\lambda+2b}{-5}$.
   From $\lambda-b = \lambda-2a \implies b = 2a$.
   From $-5\lambda+10a = \lambda+2b \implies 6a = 6\lambda \implies \lambda = a$.
   $M = (2a, 0, a)$.
3. Orthogonality: $\vec{PQ} = 2(M-P) = (2a, -4, 0)$.
   $\vec{PQ} \cdot \mathbf{v}_1 = (2a, -4, 0) \cdot (2, 1, 1) = 0 \implies 4a - 4 = 0$.
# problem (in exam dont leave this problem)
question seems big , but its not . see the numbers are small

Let a line L passing through the point $\mathrm{P}(1,1,1)$ be perpendicular to the lines $\frac{x-4}{4}=\frac{y-1}{1}=\frac{z-1}{1}$ and $\frac{x-17}{1}=\frac{y-71}{1}=\frac{z}{0}$. Let the line L intersect the $y z-$ plane at the point Q . Another line parallel to L and passing through the point $\mathrm{S}(1,0,-1)$ intersects the $y z$-plane at the point R . Then the square of the area of the parallelogram PQRS is equal to $\_\_\_\_$ .
# problem (tough to find parallel condn)

If the distances of the point $(1,2, a)$ from the line $\frac{x-1}{1} = \frac{y}{2} = \frac{z-1}{1}$ along the 
lines $\mathrm{L}_1: \frac{x-1}{3} = \frac{y-2}{4} = \frac{z-a}{b}$ and $\mathrm{L}_2: \frac{x-1}{1} = \frac{y-2}{4} = \frac{z-a}{c}$ are equal, then $a+b+c$ is equal to

sol:
Let $Q_1\left(t_1+1,2 t_1, t_1+1\right)$ be point on $L$ and $d_1$ be the distance measured from $P(1,2, a)$ along $L_1$ such that $\left|P Q_1\right| = d_1$.

So, direction ratio of $\vec{P Q_1}$ and line $L_1$ are proportional.

Equating

$$ \frac{t_1}{3} = \frac{2 t_1-2}{4} \quad \text { and } \quad \frac{t_1}{3} = \frac{t_1-a+1}{b} $$

$4 t_1 = 6 t_1-6 \quad$ and put $t_1 = 3$
# problem (solving via planes - nice one)


Let $\mathrm{L}_1: \frac{x-1}{2}=\frac{y-2}{3}=\frac{z-3}{4}$ and $\mathrm{L}_2: \frac{x-2}{3}=\frac{y-4}{4}=\frac{z-5}{5}$ be two lines. Then which of the following points lies on the line of the shortest distance between $\mathrm{L}_1$ and $\mathrm{L}_2$ ?


**1. Direction Vector ($\vec{n}$):**
Common perpendicular to $\vec{d}_1(2, 3, 4)$ and $\vec{d}_2(3, 4, 5)$:
$$\vec{n} = \vec{d}_1 \times \vec{d}_2 = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 2 & 3 & 4 \\ 3 & 4 & 5 \end{vmatrix} = \langle -1, 2, -1 \rangle$$

**2. System of Planes Defining LSD:**
The LSD is the intersection of plane $\pi_1$ (containing $L_1, \vec{n}$) and $\pi_2$ (containing $L_2, \vec{n}$).
* $\pi_1: \det(\vec{r}-\vec{a}_1, \vec{d}_1, \vec{n}) = 0 \implies 11x + 2y - 7z + 6 = 0$
* $\pi_2: \det(\vec{r}-\vec{a}_2, \vec{d}_2, \vec{n}) = 0 \implies 7x + y - 5z + 7 = 0$

**3. Point Verification (Option A):**
Substitute $P(\frac{14}{3}, -3, \frac{22}{3})$ into the system:
* $\pi_1: 11(\frac{14}{3}) + 2(-3) - 7(\frac{22}{3}) + 6 = \frac{154-154}{3} + 0 = 0$
* $\pi_2: 7(\frac{14}{3}) + (-3) - 5(\frac{22}{3}) + 7 = \frac{98-110}{3} + 4 = -4 + 4 = 0$

* if told to find p , q write the points , then equate with parrel condn 
# problem (area of triangle) 

Let $A B C D$ be a tetrahedron such that the edges $A B, A C$ and $A D$ are mutually
perpendicular. Let the areas of the triangles $\mathrm{ABC}, \mathrm{ACD}$ and ADB be 5,6 and 7 square units respectively. Then the area (in square units) of the $\triangle B C D$ is equal to :

A be origin , AB = a , AC = b , AD = c
we need , $\frac{1}{2}|(b-a) × (c-a)|$ = $\frac{1}{2}|a×b + b×c + c×a|$ 
use |a+b+c|^2 = |a|^2 + |b|^2 + |c|^2 + 2(a.b + b.c + c.a) 
# problem (left hope too early)
Let a line passing through the point $(4,1,0)$ intersect the line $\mathrm{L}_1: \frac{x-1}{2}=\frac{y-2}{3}=\frac{z-3}{4}$ at 
the point $A(\alpha, \beta, \gamma)$ and the line $\mathrm{L}_2: x-6=y=-z+4$ at the point $B(a, b, c)$. 

Then $\left|\begin{array}{lll}1 & 0 & 1 \\ \alpha & \beta & \gamma \\ a & b & c\end{array}\right|$ is equal to

* i quickly figured those 3 points are coplanar , wrote a-b / a-c = b-a / b-c = c-a / c-b 
then left 🫥 , simply

$$\frac{2\lambda-3}{\mu+2} = \frac{3\lambda+1}{\mu-1} = \frac{4\lambda+3}{4-\mu} = k$$

* From Ratio 1 & 2: $k = \frac{(3\lambda+1) - (2\lambda-3)}{(\mu-1) - (\mu+2)} = \frac{\lambda+4}{-3}$

* From Ratio 2 & 3: $k = \frac{(3\lambda+1) + (4\lambda+3)}{(\mu-1) + (4-\mu)} = \frac{7\lambda+4}{3}$

Equating both expressions for $k$:
$$\frac{\lambda+4}{-3} = \frac{7\lambda+4}{3} \implies \lambda+4 = -7\lambda-4 \implies \mathbf{\lambda = -1}$$
Substitute $\lambda$ to find $\mu$:
$$\frac{-1+4}{-3} = -1 \implies \frac{-5}{\mu+2} = -1 \implies \mathbf{\mu = 3}$$
# problem (done faster)
Let $A$ and $B$ be two distinct points on the line $L: \frac{x-6}{3}=\frac{y-7}{2}=\frac{z-7}{-2}$. Both $A$ and $B$ are at
a distance $2 \sqrt{17}$ from the foot of perpendicular drawn from the point $(1,2,3)$ on the 
line $L$. If $O$ is the origin, then $\vec{O A} \cdot \vec{O B}$ is equal to

instead of finding the points A and B , find the foot of perpendicular F first 

$$\vec{O A} \cdot \vec{O B} = (a+d.\hat{t})(a-d.\hat{t}) = a^2-d^2$$d^2
# problem (solve for area without finding points)

Let A be the point of intersection of the lines $\mathrm{L}_1: \frac{x-7}{1}=\frac{y-5}{0}=\frac{z-3}{-1}$ and $\mathrm{L}_2: \frac{x-1}{3}=\frac{y+3}{4}=\frac{z+7}{5}$. 
Let B and C be the points on the lines $\mathrm{L}_1$ and $\mathrm{L}_2$ respectively such that $A B=A C=\sqrt{15}$. 
Then the square of the area of the triangle $A B C$ is :


$L_1: \frac{x-7}{1}=\frac{y-5}{0}=\frac{z-3}{-1} ; L_2: \frac{x-1}{3}=\frac{y+3}{4}=\frac{z+7}{5}$

$$\begin{aligned}
& \cos \theta=\left|\frac{3+0-5}{\sqrt{2} \times \sqrt{50}}\right| \\
& \therefore \sin \theta=\frac{2 \sqrt{6}}{5} \\
& \text { Area }=\frac{1}{2} a b \sin \theta \\
\end{aligned}$$
# problem (could have done better)

Let the line L pass through $(1,1,1)$ and intersect the lines 
$\frac{x-1}{2}=\frac{y+1}{3}=\frac{z-1}{4}$ and $\frac{x-3}{1}=\frac{y-4}{2}=\frac{z}{1}$. Then, which of the following points lies on the line $L$ ?


Now $\frac{2 \lambda}{\mu+2}=\frac{3 \lambda-7}{2 \mu+3}=\frac{4 \lambda}{\mu-1}$

in this notice that 1 and 3 , would give the value of $\mu$
and u need only one point

find that by substituting the value of $\mu$ 

then find the parallel vector, and two satisfy other point 
subtract 1,1,1 from them and see if they are parallel 
# problem (radii of circle given 3 point)
$A = \frac{1}{2}ab\sin \theta$
$\sin \theta = \frac{c}{2R}$
$A = \frac{abc}{4R}$

i made blunder while calculating for circumcenter.
the eqn reuired are line passing via midpoint, but took via vertex
# problem (took too much time , instead of doing the problem by conventional way) 

Let O be the origin, and M and $$\mathrm{N}$$ be the points on the lines $$\frac{x-5}{4}=\frac{y-4}{1}=\frac{z-5}{3}$$ and 
$$\frac{x+8}{12}=\frac{y+2}{5}=\frac{z+11}{9}$$ respectively such that $$\mathrm{MN}$$ is the shortest distance between the given lines.
Then $$\vec{O M} \cdot \vec{O N}$$ is equal to _________.

write m and n in terms of $t_1$ and $t_2$ , then apply parallel condn 
# problem ( nice way to solve for 3 mutually perpendicular lines, like (i , j ,k))

Let $$L_1: \vec{r}=(\hat{i}-\hat{j}+2 \hat{k})+\lambda(\hat{i}-\hat{j}+2 \hat{k}), \lambda \in \mathbb{R}$$, $$L_2: \vec{r}=(\hat{j}-\hat{k})+\mu(3 \hat{i}+\hat{j}+p \hat{k}),$$
$$\mu \in \mathbb{R} \text {, and } L_3: \vec{r}=\delta(\ell \hat{i}+m \hat{j}+n \hat{k}), \delta \in \mathbb{R}$$ be three lines such that $$L_1$$ is perpendicular to $$L_2$$ and $$L_3$$
is perpendicular to both $$L_1$$ and $$L_2$$. Then, the point which lies on $$L_3$$ is

$l_3 = k (l_2×l_1)$
