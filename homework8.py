def test(*args, **kwargs):
    print(f'{args =}')
    print(f'{kwargs =}')

test(143, 'hello', [1, 4, 67], volvo=45, жигули=30)


def factoreal(n):
    if n == 1:
        return 1
    factoreal_n_minus_1 = factoreal(n=n - 1)
    return n * factoreal_n_minus_1

print(factoreal(7))