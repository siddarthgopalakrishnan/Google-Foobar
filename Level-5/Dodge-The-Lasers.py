sq2 = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727

def n1(n):
    return (sq2*n)//(10**100)

def s(n):
    if n == 1:
        return 1
    if n < 1:
        return 0
    return n*n1(n) + n*(n+1)/2 - n1(n)*(n1(n)+1)/2 - s(n1(n))

def solution(n):
    #Your code here
    n = long(n)
    return str(s(n))

## Read up on Beaty Sequence
## Check below link for explanation:-
## https://surajshetiya.github.io/Google-foobar/
