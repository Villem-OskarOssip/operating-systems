def arv(n):
    if n < 3:
        return 0
    return 3 + arv(n - 1) + arv(n - 2) + arv(n - 3)


def f(jarjend, summa, vahesumma=0, index=0):
    if vahesumma >= summa:
        return vahesumma
    if index == len(jarjend):
        return 2 * sum(jarjend)
    return min(f(jarjend, summa, vahesumma, index + 1), f(jarjend, summa, vahesumma + jarjend[index], index + 1),
               f(jarjend, summa, vahesumma + 2 * jarjend[index], index + 1))


def raamat(jarjend, sobivad=0, index=0):
    if index == len(jarjend):
        return sobivad
    if 50 <= jarjend[index] <= 100:
        return raamat(jarjend, sobivad + 1, index + 1)
    return raamat(jarjend, sobivad, index + 1)

print(raamat([50, 100, 75, 129, 111, 49, 58, 222]))