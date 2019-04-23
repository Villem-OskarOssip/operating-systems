def f(jarjend, summa, vahesumma=0, index=0):
    if vahesumma >= summa:
        return vahesumma
    if index == len(jarjend):
        return 2 * sum(jarjend)
    return min(f(jarjend, summa, vahesumma, index + 1), f(jarjend, summa, vahesumma + jarjend[index], index + 1),
               f(jarjend, summa, vahesumma + 2 * jarjend[index], index + 1))

print(f([2,4],7))