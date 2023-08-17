def main():
    # num_linhas = int(input('Oi, digite o numero de linhas da piramide:'))
    # for i in range(num_linhas):
    #     print('*' * i)
    list_notas = []
    for i in range(1, 5):
        nota_avaliar = str('Nota do bimestre ' + str(i) + ' : ')
        notas_bimestre = int(input(nota_avaliar))
        list_notas.append(notas_bimestre)
    
    media = int(sum(list_notas)) / int(len(list_notas))
    print(f'{media:.2f}')

if __name__ == '__main__':
    main()  