def korni_main(a, b, c):
    a, b, c = int(a), int(b), int(c)
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + (d) ** 0.5) / (2 * a)
        x2 = (-b - (d) ** 0.5) / (2 * a)
        reshen = "Дискриминант равен: " + str(d) + "\n\nx1 равен: " + str(int(x1)) + "\n\nх2 равен: " + str(int(x2))
    elif d == 0:
        x1 = -b / 2 * a
        reshen = "Дискриминант равен: " + str(d) + "\n\nx1 и х2 равны: " + str(x1)
    else:
        reshen = "Действительных корней нет"
    return reshen