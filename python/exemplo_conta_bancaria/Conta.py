from exceptions import SaldoNaoDisponivelException
class Conta():
    def __init__(self, numero_conta:int, saldo:int=0) -> None:
        self.__numero_conta = numero_conta
        self.__saldo = saldo

    def depositar(self, valor:int):
        self.__saldo += valor

    def sacar(self, valor_saque:int):
        if self.obter_saldo() > valor_saque:
            self.__saldo -= valor_saque
            return f"Saque de {valor_saque}R$ efetuado, saldo restante: {self.obter_saldo()}R$ "
        else:
            raise SaldoNaoDisponivelException(self.obter_saldo(), valor_saque)

    def obter_saldo(self):
        return self.__saldo
    
    def __str__(self) -> str:
        return f"Conta número: {self.__numero_conta} Saldo: {self.obter_saldo()}"

if __name__ == '__main__':
    agnelo = Conta(12313)
    print(agnelo)
    agnelo.depositar(20)
    print(agnelo)
    try:
        print(agnelo.sacar(100))
    except:
        pass
    print(agnelo)
