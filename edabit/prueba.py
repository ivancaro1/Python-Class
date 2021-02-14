def is_curzon(num):
    num1 = 2 ** num + 1
    num2 = 2 * num + 1
    if(num1%num2 == 0):
        return True
    else:
        return False

print(is_curzon(14))
