for tc in range(int(input())):
    number = input()
    A = number
    B = ''.join('1' if d == '4' else '0' for d in number).lstrip('0')
    A = A.replace('4', '3')
    print('Case #{}: {} {}'.format(tc+1, A, B))
