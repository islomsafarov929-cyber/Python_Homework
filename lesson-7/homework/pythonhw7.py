# Problem 1.is_prime(n) funksiyasini hosil qiling (n > 0). Agar n soni tub bo'lsa True, aks holda False qiymat qaytarsin. 

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int((n**0.5))+ 1):
        if n % i == 0:
            return False
    else:
        return True
    
is_prime(5) # True


# Problem 2.digit_sum(k) funksiyasini yozing, u k sonining raqamlari yig'indisini hisoblaydi.

def digit_sum(k):
    return sum((int(i) for i in str(k))) # for memory efficent i used tuple comperehension

digit_sum(123456789) # 45


# Problem 3.Berilgan N sonidan oshmaydigan barcha 2 ning darajalarini (ya'ni, 2**k shaklidagi sonlarni) chop etuvchi funksiyani yozing.

def pow_func(n):
    num = []
    p = 1 # i started from 1 because in the example started with 2 not 1(if example started with 1 i would start from 0 )
    while 2 ** p <= n:
        num.append(2 ** p)
        p += 1
    return num

pow_func(10) # [2,4,8]

    
