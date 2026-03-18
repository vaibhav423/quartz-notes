# problem (awesome way to solve for distance)
Let the lines $\mathrm{L}_1: \vec{r}=\hat{\mathrm{i}}+2 \hat{\mathrm{j}}+3 \hat{\mathrm{k}}+\lambda(2 \hat{\mathrm{i}}+3 \hat{\mathrm{j}}+4 \hat{\mathrm{k}}), \lambda \in \mathbb{R}$ and $\mathrm{L}_2: \vec{r}=(4 \hat{\mathrm{i}}+\hat{\mathrm{j}})+\mu(5 \hat{\mathrm{i}}+2 \hat{\mathrm{j}}+\hat{\mathrm{k}}), \mu \in \mathbb{R}$, 
intersect at the point R . Let P and Q be the points lying on lines $L_1$ and $L_2$,
respectively, such that $|\vec{\mathrm{PR}}|=\sqrt{29}$ and $|\vec{\mathrm{PQ}}|=\sqrt{\frac{47}{3}}$. If the point P lies in the first octant,
then $27(\mathrm{QR})^2$ is equal to

instead of finding the points .
notice that , the question asks for $27(\mathrm{QR})^2$ .
which only one Q should exist.  and hence , PQ is perpnd to QR
and hence using pythagorean theorem , we can find QR .
# problem (unintuitive but inituitive way exists solve for a+b+c maximizatio) 
[[vector-leibiniz-identity-squared-sum]]
For three unit vectors $\vec{a}, \vec{b}, \vec{c}$ satisfying

$$ |\vec{a}-\vec{b}|^2+|\vec{b}-\vec{c}|^2+|\vec{c}-\vec{a}|^2=9 \text { and }|2 \vec{a}+k \vec{b}+k \vec{c}|=3 \text {, } $$

the positive value of k is :

Soln:

the normal way :
$2 (\sum a^2 + \sum a.b) = 9$ 

=> $\sum a.b = \frac{-3}{2}$
the expanding the second equation, and realizing we are stuck 

the intuitive way :

realize it is about the sum of the squares of the sides of a triangle formed by the vectors a,b,c

and since we were not able to find with normal , we definitely  need another eqn

if we could show that the first eqn is maximized. we could get a+b+c =0

$\sum_{\text{cyc}} |\vec{a}-\vec{b}|^2 = 3(|\vec{a}|^2 + |\vec{b}|^2 + |\vec{c}|^2) - |\vec{a}+\vec{b}+\vec{c}|^2$
# problem (blunder in question reading stuck for 1 hr circle arc)

Let the arc $A C$ of a circle subtend a right angle at the centre $O$. If the point $B$ on the arc $A C$, divides the arc $A C$ such that $\frac{\text { length of } \operatorname{arc} A B}{\text { length of } \operatorname{arc} B C}=\frac{1}{5}$, and $\vec{O C}=\alpha \vec{O A}+\beta \vec{O B}$, then $\alpha+\sqrt{2}(\sqrt{3}-1) \beta$ is equal to

i took oc as ob and ob as oc 
# problem (stuck 6 hrs experimenting - centroid squared distance) 
Let the three sides of a triangle ABC be given by the vectors $2 \hat{i}-\hat{j}+\hat{k}, \hat{i}-3 \hat{j}-5 \hat{k}$ and $3 \hat{i}-4 \hat{j}-4 \hat{k}$. Let $G$ be 
the centroid of the triangle $A B C$. Then $6\left(|\vec{\mathrm{AG}}|^2+|\vec{\mathrm{BG}}|^2+|\vec{\mathrm{CG}}|^2\right)$ is equal to __________.

concept : [[vector-leibiniz-identity-squared-sum#link with centroid]]

instead of finding the points A,B,C and then G and then the distances, we can directly use the formula 
for the sum of the squares of the distances from the centroid to the vertices of a triangle in terms of the squares of the sides of the triangle.
# problem (eliminating type find α and β)
two methods :

$$\begin{aligned}
& \vec{a}+5 \vec{b}=\lambda \vec{c} \\
& \vec{b}+6 \vec{c}=\mu \vec{a}
\end{aligned}$$

Eliminating $$\vec{a}$$

$$\begin{aligned}
& \lambda \vec{\mathrm{c}}-5 \vec{\mathrm{b}}=\frac{6}{\mu} \vec{\mathrm{c}}+\frac{1}{\mu} \vec{\mathrm{b}} \\
& \therefore \mu=\frac{-1}{5}, \lambda=-30 \\
& \alpha=5, \beta=30
\end{aligned}$$

or

take the cross product of the first eqn with c and the second eqn with a 
# problem (area ration of small triangle 1:2)

Let PQR be a triangle. The points A, B and C are on the sides QR, RP and PQ respectively such that

$${{QA} \over {AR}} = {{RB} \over {BP}} = {{PC} \over {CQ}} = {1 \over 2}$$. Then $${{Area(\Delta PQR)} \over {Area(\Delta ABC)}}$$ is equal to :

quickly find.
Let the position vector of $P, Q, R$ be $\vec{0}, \vec{a}, \vec{b}$
# problem (collinear position vectors)
If the points with position vectors $$\alpha \hat{i}+10 \hat{j}+13 \hat{k}, 6 \hat{i}+11 \hat{j}+11 \hat{k}, \frac{9}{2} \hat{i}+\beta \hat{j}-8 \hat{k}$$ are collinear,
then $$(19 \alpha-6 \beta)^{2}$$ is equal to :

two methods :

cross product of a-b c-b should be zero
or

and $\frac{9}{2} \hat{i}+\beta \hat{j}-8 \hat{k}$ are collinear.

So, $\frac{\alpha-6}{6-\frac{9}{2}}=\frac{10-11}{11-\beta}=\frac{13-11}{11+8}$
# problem  (major blunder pa + pb + pc, orthocentere , circumcenter)
If the points $$\mathrm{P}$$ and $$\mathrm{Q}$$ are respectively the circumcenter and the orthocentre of a $$△ \mathrm{ABC}$$, then $$\vec{\mathrm{PA}}+\vec{\mathrm{PB}}+\vec{\mathrm{PC}}$$ is
equal to :
wrote P - Q as $\vec{PQ}$
which is not true
P - Q = $\vec{QP}$
# problem (cant solve onspot max a b c) 

For any vector $$\vec{a}=a_{1} \hat{i}+a_{2} \hat{j}+a_{3} \hat{k}$$, with $$10\left|a_{i}\right|<1, i=1,2,3$$, consider the following statements :

(A): $$\max \left\{\left|a_{1}\right|,\left|a_{2}\right|,\left|a_{3}\right|\right\} \leq|\vec{a}|$$

(B) : $$|\vec{a}| \leq 3 \max \left\{\left|a_{1}\right|,\left|a_{2}\right|,\left|a_{3}\right|\right\}$$


$$
\begin{aligned}
 10\left|a_i\right|<1, i=1,2,3 \\\\
 \text { Let } \left|a_1\right| \geq\left|a_2\right| \geq\left|a_3\right| \\\\
 |\vec{a}|=\sqrt{a_1^2+a_2^2+a_3^2} \geq \sqrt{a_1^2} \\\\
 \therefore|\vec{a}| \geq\left|a_1\right| \text { or } \max \left\{\left|a_1\right|,\left|a_2\right|,\left|a_3\right|\right\} \text {. }
\end{aligned}
$$

Hence, (A) is true.

$$
\begin{array}{rlrl}
  |\vec{a}|  =\sqrt{a_1^2+a_2^2+a_3^2} \leq \sqrt{a_1^2+a_1^2+a_1^2} \\\\
 =\sqrt{3}\left|a_1\right| \\\\
\therefore   |\vec{a}|=\sqrt{3}\left|a_1\right|<3\left|a_1\right| \\\\
\therefore  |\vec{a}|<3 \max \left\{\left|a_1\right|,\left|a_2\right|,\left|a_3\right|\right\}
\end{array}
$$

Hence, (B) is also true.
# problem  (didnt solve , a b c d e f , find k)
Let $\mathrm{ABCD}$ be a quadrilateral. If $\mathrm{E}$ and $\mathrm{F}$ are the mid points of the diagonals $\mathrm{AC}$ and $\mathrm{BD}$ respectively and $(\vec{A B}-\vec{B C})+(\vec{A D}-\vec{D C})=k \vec{F E}$, then $k$ is equal to :
write all of them as position vectors
# problem (collinear x y z )

If vectors $$\vec {{a_1}}  = x\hat i - \hat j + \hat k$$ and $$\vec {{a_2}}  = \hat i + y\hat j + z\hat k$$ are collinear, then a possible unit vector parallel to the vector $$x\hat i + y\hat j + z\hat k$$ is :


use this or do cross product

$$\vec {{a_2}}  = \lambda \vec {{a_1}} $$

$$\hat i + y\hat j + z\hat k = \lambda (x\hat i - \hat j + \hat k)$$

$$1 = \lambda x,y =  - \lambda ,z = \lambda $$

$$x\hat i + y\hat j + z\hat k = {1 \over \lambda }\hat i - \lambda \hat j + \lambda \hat k$$

Unit vector $$ = {{{1 \over \lambda }\hat i - \lambda \hat j + \lambda \hat k} \over {\sqrt {{1 \over {{\lambda ^2}}} + {\lambda ^2} + {\lambda ^2}} }}$$

$$ = {{\hat i - {\lambda ^2}\hat j + {\lambda ^2}\hat k} \over {\sqrt {1 + 2{\lambda ^4}} }}$$

Let $${\lambda ^2} = 1$$, possible unit vector $$ = {{\hat i - \hat j + \hat k} \over {\sqrt 3 }}$$
# problem (made blunder rotate vector calc area)
Let a vector $$\alpha \hat i + \beta \hat j$$ be obtained by rotating the vector $$\sqrt 3 \hat i + \hat j$$ by an angle 45$$^\circ$$ about the origin in counterclockwise direction in the first quadrant. Then the area of triangle having vertices ($$\alpha$$, $$\beta$$), (0, $$\beta$$) and (0, 0) is equal to :

1st blunder calculated area for a b , √3,1 , 0,0
2nd blunder : rotated the vector , but didnt consider magnitude 
# problem

