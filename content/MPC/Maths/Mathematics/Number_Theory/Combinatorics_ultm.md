# gallery

```img-gallery
path: Google_Keep/Assets/Combinatorics_ultm
type: vertical
mobile: 3
columns: 3
gutter: 2
radius: 20
```

# Bell Number and Distribution Problems

## Bell Numbers

The Bell number, denoted as $B_n$, represents the number of ways to distribute $n$ distinct (D) things (T) into infinitely many identical (I) boxes (B), which can be represented as (DT IB).

*   Formula: $B_n = \sum_{k=1}^{n} S(n, k)$, where $S(n, k)$ represents the Stirling numbers of the second kind.

### Stirling Numbers of the Second Kind

$S(n, k)$ counts the number of ways to partition a set of $n$ objects into $k$ non-empty subsets.

## Distribution of Distinct Things into Identical Boxes

The number of ways to distribute $n$ distinct (D) things into $r$ identical (I) boxes (B) is given by:

$\sum_{k=1}^{r} S(n, k)$

This is because we sum the Stirling numbers of the second kind from 1 to $r$, accounting for all possible numbers of non-empty boxes.

## Partition Function

The partition function, often denoted as $p(n)$, represents the number of ways to distribute identical (I) things into infinitely many identical boxes (IT IB).  $p(n, r)$ represents the number of ways to distribute $n$ identical things into $r$ identical boxes.

*   Recurrence Relation: $p(n, r) = \sum_{k=1}^{r} p(n-r, k)$ 

## Star and Bars

The "stars and bars" technique is used for distributing identical (I) things into distinct (D) boxes (IT DB).

## Summary Table

| Feature                      | Things (T) | Boxes (B) | Empty Allowed? | Formula                                  |
| ---------------------------- | ---------- | --------- | -------------- | ---------------------------------------- |
| Distinct Things into Distinct Boxes | Distinct   | Distinct  | Yes            | $r^n$                                    |
| Distinct Things into Identical Boxes| Distinct   | Identical | Yes            | $\sum_{k=1}^{r} S(n, k)$                  |
| Distinct Things into Distinct Boxes| Distinct   | Distinct  | No             | $r! S(n,r)$                              |
| Distinct Things into Identical Boxes| Distinct   | Identical | No             | $S(n,r)$                                 |
| Identical Things into Distinct Boxes| Identical  | Distinct  | Yes            | ${n+r-1 \choose r-1}$                    |
| Identical Things into Distinct Boxes| Identical  | Distinct  | No             | ${n-1 \choose r-1}$                      |

## Explanation of Key Distributions

### Distinct Things into Distinct Boxes (Empty Allowed)

*   Each of the $n$ distinct things can go into any of the $r$ distinct boxes.
*   Total number of ways: $r^n$

### Distinct Things into Identical Boxes (Empty Not Allowed)

*   The number of ways to distribute $n$ distinct things into $r$ distinct boxes such that no box is empty is given by $r! \cdot S(n, r)$, where $S(n, r)$ is the Stirling number of the second kind.
*   If empty boxes are allowed, the formula becomes $\sum_{k=1}^{r} S(n, k)$.

### Distinct Things into Identical Boxes (Empty Allowed)

*   This is given by $\sum_{k=1}^{r} S(n, k)$.

### Distinct Things into Identical Boxes (Empty Not Allowed)

*   This is given by $S(n, r)$.

## Example and Clarification

### Why DT into IB ≠ r^n/r!

Consider distributing 2 distinct things into 3 identical boxes. The expression $r^n/r!$ would suggest $3^2 / 3! = 9 / 6 = 1.5$, which is not an integer and doesn't make sense in this context.

The correct approach is to consider the Stirling numbers of the second kind.

### Distribution (2, 3, 0, 0)

The distribution (2, 3, 0, 0) is not applicable because we only have 2 distinct things and not 5.  The example is meant to illustrate why simply dividing $r^n$ by $r!$ doesn't work for distinct things into identical boxes.












bell number - distribution of distinct (D) things (T)into infinitely many identical (I)boxes(B) (DT IB)
 $B_n$=  $\sum\limits_{k=1}^{n} s(n,k)$
 
similar : Distribution of n (D) things into r (I B) =  $\sum\limits_{k=1}^{r} s(n,k)$
partition func - distribution of identical things into infinitely many identical boxes (IT IB)
$p(n, r) = \sum\limits_{k=1}^{r} p(n-r, k)$


star bar (IT DB)


Things - T - n , Box - B - r

empty allowed

Dstb of D T into D B = $r^n$

DT into  I B   ≠ r^n/r! consider Dstb (2,3,0,0)     = sum of s(n,k) 1 to r
no empty
DT into  D B                 = r!s(n,r)
DT into  I B                   = s(n,r)

# images

