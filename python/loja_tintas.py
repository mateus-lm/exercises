def main():
    rendimento_metros = 6
    lata = {'conteudo': 18, 'preco': 80}
    galao = {'conteudo': 3.6, 'preco': 25}
    lata['rendimento'] = lata['conteudo'] * rendimento_metros
    galao['rendimento'] = galao['conteudo'] * rendimento_metros
    #print(lata, galao)

    area = float(input("Entre com a área a ser pintada em m²: "))

    print(
        f"Comprando apenas latas de 18L serão utilizadas {area//lata['rendimento']} lata(s) na área de {area}m²")
    print(
        f"Comprando apenas latas de 3.6L serão utilizadas {area//galao['rendimento']} galões na área de {area}m²")
    print(
        f"Para obter a melhor eficiência seria comprando {(area * 1.1)//lata['rendimento']} latas de 18L e {((area * 1.1)%lata['rendimento'])//galao['rendimento']} galões de 3.6L para cobrir a área de {area}m²")


if __name__ == '__main__':
    main()
