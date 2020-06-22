from Stack.stack import Stack


def reverse_string(s1, s):
    for i in range(len(s)):
        s1.push(s[i])
    rev_str = ""
    while not s1.is_empty():
        rev_str += s1.pop()

    return rev_str


if __name__ == '__main__':
    s1 = Stack()
    s = "!evitacudE ot emocleW"
    print(reverse_string(s1, s))
