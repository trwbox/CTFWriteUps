def define_false(s):
    lstr = []
    u = 0
    packed = ''
    for c in s:
        if c == '[':
            lstr.append((u, packed))
            packed = ''
            u = 0 
        elif c == ']':
            num, prev_string = lstr.pop()
            packed = prev_string + packed * num 
        elif c.isdigit():
            u = u * 10 + int(c)
        else:
            packed = packed + c
    return packed

def define_true(p):
    res = ''
    for packed in p:
        res = str(len(packed)) + '[:]' + packed + res
    return res

def define_both(p):
    unpacked = []
    for i in p:
        packed = i.split(')')
        char = ''
        for j in packed:
            if j == '':
                break
            j = j + ')'

            char = char + eval(j)
        unpacked.append(char)
    return unpacked


if __name__ == '__main__':
    s = ['chr(103)chr(48)chr(79)chr(97)chr(116)chr(125)', 'chr(105)chr(115)', 'chr(109)chr(69)chr(51)chr(115)chr(115)chr(105)', 'chr(115)chr(105)chr(85)chr(85)chr(85)', 'chr(75)chr(67)chr(84)chr(70)chr(123)']
    print(define_false(define_true(define_both(s))))