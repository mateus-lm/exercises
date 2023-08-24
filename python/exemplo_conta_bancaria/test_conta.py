from exceptions import SaldoNaoDisponivelException
from Conta import Conta
import pytest

def test_saldo_correto():
    contaDummy = Conta(12341,20)

    assert contaDummy.obter_saldo() == 20

def test_depositar():
    contaDummy = Conta(2131,0)
    contaDummy.depositar(20)
    contaDummy.depositar(20)

    assert contaDummy.obter_saldo() == 40

def test_sacar_valor_incorreto():
    contaDummy = Conta(2131, 100)
    with pytest.raises(SaldoNaoDisponivelException):
        contaDummy.sacar(200)
