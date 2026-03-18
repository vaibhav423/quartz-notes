# gallery
```img-gallery
path: Assets/3d-geometry
type: vertical
mobile: 3
columns: 3
gutter: 2
radius: 20
```
# imp
## foot of perpend
* write in this way
$t$ :                    | $kt$: 
$p$ :                    |  $w+kt$ : 
$w$ :                    | if image is needed 
$p-w$:                   |   2I - P
k = $\frac{(p-w).t}{|t|^2}$ :          |  
## distance of point from line
$t$ :
$p$ :
$w$ :
$p-w$ : a b c

$a^2 + b^2 + c^2$ - $\frac{(a b c . t)^2}{t^2}$ (dont add any terms here only square and multiply)
simplify in one go
## dist of point from line along vector v
solve for k:

$\frac{w+kt-p}{v}$

* substitue k in w+kt-p
* and square each component and add to get final answer
# general
## line in space
### projection of line segments
![projection-of-line-segments](Assets/3d-geometry/1772364396.png)
for (l,m,n) as direction cosine for line
$(x_1,y_1,z_1)$ and $(x_2,y_2,z_2)$ as end points of line segment
$$\text{projection} = \sqrt{(l(x_2-x_1))^2 + (m(y_2-y_1))^2 + (n(z_2-z_1))^2}$$
### foot of perpendicular
![foot-of-perpendicular](Assets/3d-geometry/1772365071.png)

line with equation $\frac{x-x_1}{a} = \frac{y-y_1}{b} = \frac{z-z_1}{c}$ and point P: $(\alpha,\beta,\gamma)$
$line = \vec{w} + k\vec{t}$

we need  v : $( \vec{w} + k\vec{t} - P ).t = 0$ , get $k$ and sub in line

⇒ $(\vec{w} - P).t + k(\vec{t}.t) = 0$

⇒ $k = \frac{( P - \vec{w} ).t}{|\vec{t}|^2}$
### distance of point from line
![distance-from-line](Assets/3d-geometry/1772365397.png)

$d = \sqrt{|r_1|^2 - (r_1.r_2)^2}$

r1 is vector from x1 to x2 (x1 = point on line, x2 = point outside line)  
r2 is unit vector along line
### dist bw skew lines
![dist-bw-skew-line](Assets/3d-geometry/1772368170.png)

$d = |\frac{(t_1 × t_2).(w_2 - w_1)}{|t_1 × t_2|}|$

t1 , t2 = direction vectors of lines
w1 , w2 = points on lines

condition for line to intersect

$\begin{vmatrix} x_2-x_1 & y_2-y_1 & z_2-z_1 \\a_1 & b_1 & c_1 \\a_2 & b_2 & c_2 \end{vmatrix} = 0$
### dist bw parallel lines

------------------------>
           ^@
           | @ 
           |  @
           |   @ --> $(a_2 - a_1)$  
           |    @
           |     @
           |      @
-----------.------->---- $b$

dot gives along line , × along perpnd

$d = \frac{|(a_2 - a_1) × b|}{|b|}$
### dist of point from line along vector v
![dist-along-ine](Assets/3d-geometry/1772537658.png)
## plane in space
$r.n = d$ , r = point in plane
# images 
![projection-of-line-segments](Assets/3d-geometry/1772364396.png)
![foot-of-perpendicular](Assets/3d-geometry/1772365071.png)
![distance-from-line](Assets/3d-geometry/1772365397.png)
![dist-bw-skew-line](Assets/3d-geometry/1772368170.png)
![dist-along-ine](Assets/3d-geometry/1772537658.png)
