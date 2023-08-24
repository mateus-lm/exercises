class SaldoNaoDisponivelException(Exception):
    def __init__(self, saldo_atual, valor_solicitado) -> None:
        super().__init__(f"Saldo insuficiente. Saldo atual: {saldo_atual}, Valor solicitado: {valor_solicitado}")
        self.saldo_atual = saldo_atual
        self.valor_solicitado = valor_solicitado