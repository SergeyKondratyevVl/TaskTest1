
def my_sqrt(N: int):
    if N < 0:
            return None

    if N == 0:
        return 0

    def sum_N(N):
        sum = 0
        for i in str(N):
            sum += int(i)
        return sum

    res_sqrt_N = 1
    delta = 1

    while delta != 0:
        N_old = N

        for i in [2,3,7,8]:
            if N % 10 == i:
                return None

        if N % 10 == 4 or N % 10 == 6 or N % 10 == 0:
            if N % 4 == 0:
                res_sqrt_N *= 2
                N //= 4
            else:
                return None

        if N % 10 == 5 or N % 10 == 0:
            if N % 25 == 0:
                res_sqrt_N *= 5
                N //= 25
            else:
                return None

        if sum_N(N) % 9 == 0:
            res_sqrt_N *= 3
            N //= 9
        delta = N - N_old
    
    if N == 1:
        return res_sqrt_N
    
    x = 2
    delta = 2

    while abs(delta) > 1:
        a = (N-x**2)/(2*x)
        b = x + a
        delta = b - a**2 / (2*b) - x
        x = b - a**2 / (2*b) 

    if (round(x)+1)**2 == N:
        res_sqrt_N *= round(x)+1
        return res_sqrt_N
    elif round(x)**2 == N:
        res_sqrt_N *= round(x)
        return res_sqrt_N
    elif (round(x)-1)**2 == N:
        res_sqrt_N *= round(x)-1
        return res_sqrt_N
    else:
        return None

if __name__ == "__main__":
    N = int(input('Enter the number: '))
    print(my_sqrt(N))
