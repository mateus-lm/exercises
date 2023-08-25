def verify_cpf(cpf):
    cpf = cpf.replace('.', '').replace('-', '')
    if len(cpf) != 11:
        return False
    if cpf in [s * 11 for s in [str(n) for n in range(10)]]:
        return False
    calc = lambda t: int(t[1]) * (t[0] + 2)
    d1 = (sum(map(calc, enumerate(reversed(cpf[:-2])))) * 10) % 11
    d2 = (sum(map(calc, enumerate(reversed(cpf[:-1])))) * 10) % 11
    return str(d1) == cpf[-2] and str(d2) == cpf[-1]



def main():
    print(verify_cpf('12345678911'))

if __name__ == '__main__':
    main()