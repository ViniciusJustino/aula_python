from app_senha import valida_senha


minhaSenha = input('Digite a sua senha:')

if valida_senha(minhaSenha):
    print('Deu certo!')