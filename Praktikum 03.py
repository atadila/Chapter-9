def starFormation(n):
    x = 0
    y = n
    i = 0
    rumus = 1 + 2*(n-1)
    rumus += rumus
    while(i < n):
        x += 1
        i += 1
        star = '* '*x
        print(star.center(rumus))

    while i >- y :
        x -= 1
        i -= 1
        star = '* '*x
        print(star.center(rumus))
        if(i == 0):
            break
starFormation(7)