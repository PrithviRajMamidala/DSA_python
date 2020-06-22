from Stack.stack import Stack


def convert_int_to_bin(dec_num):
    s = Stack()
    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2
    Res = ""
    while not s.is_empty():
        Res += str(s.pop())

    return Res


print(convert_int_to_bin(42))