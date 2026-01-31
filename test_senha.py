from app_senha import valida_senha

def test_erro_de_senha():
    retorno = valida_senha("senha");

    print( f"Erro de senha fraca, com 5 caracteres {retorno}")

    assert retorno == False


def test_erro_caracter_especial_senha():

    retorno = valida_senha("EscolaSantos1");

    assert retorno == False

def test_erro_caracter_maisculo_senha():
    
    retorno = valida_senha("escolasantos1!");

    assert retorno == False