# -------- Início das Variáveis Globais --------
lista_funcionario = []
codigo_funcionario = 7400

# -------- Fim das Variáveis Globais --------

# -------- Início de cadastrar_funcionário() --------
def cadastrar_funcionario(codigo):
    print('*******************************************************************************')
    print('-------------------------- MENU CADASTRAR FUNCIONÁRIO -------------------------')
    print('Código do Funcionário: {}'.format(codigo))
    nome = input('Por favor entre com o NOME: ')
    setor = input('Por favor entre com o SETOR: ')
    salario = float(input('Por favor entre com o SALÁRIO (R$): '))
    dicionario_funcionario = {
        'id': codigo,
        'nome': nome,
        'setor': setor,
        'salario': salario
    }
    lista_funcionario.append(dicionario_funcionario.copy())

# -------- Fim de cadastrar_funcionário() --------

# -------- Início de consultar_funcionário() --------
def consultar_funcionario():
    print('*******************************************************************************')
    print('-------------------------- MENU CONSULTAR FUNCIONÁRIO -------------------------')
    while True:
        opcao_consultar = input('\nEscolha a opção desejada:\n' +
                                '1-Consultar Todos os Funcionários\n' +
                                '2-Consultar Funcionários por ID\n' +
                                '3-Consultar Funcionários por SETOR\n' +
                                '4-Retornar\n' +
                                '>> ')
        print('-----------------------------')
        if opcao_consultar == '1':
           primeiro = True  # Variável para evitar linha extra no início
           for funcionario in lista_funcionario:
               if not primeiro:
                  print('----------------------------')  # Adiciona separação apenas entre funcionários
               primeiro = False
               for key, value in funcionario.items():
                   if key == 'salario':
                      print(' {}: R$ {:,.2f}'.format(key, value))
                   else:
                      print(' {}: {}'.format(key, value))

        elif opcao_consultar == '2':
            valor_desejado = int(input('Digite o ID do funcionário: '))
            for funcionario in lista_funcionario:
                if funcionario['id'] == valor_desejado:
                    for key, value in funcionario.items():
                        if key == 'salario':
                            print(' {}: R$ {:,.2f}'.format(key, value))
                        else:
                            print(' {}: {}'.format(key, value))
        elif opcao_consultar == '3':
            valor_desejado = input('Digite o setor do(s) funcionário(s): ')
            for funcionario in lista_funcionario:
                if funcionario['setor'] == valor_desejado:
                    for key, value in funcionario.items():
                        if key == 'salario':
                            print(' {}: R$ {:,.2f}'.format(key, value))
                        else:
                            print(' {}: {}'.format(key, value))
        elif opcao_consultar == '4':
            print('*******************************************************************************')
            print('-------------------------------MENU PRINCIPAL----------------------------------')
            return
        else:
            print('Opção Inválida. Tente Novamente')
            continue
        print('-----------------------------')


# -------- Fim de consultar_funcionário() --------

# -------- Início de remover_funcionário() --------
def remover_funcionario():
    print('*******************************************************************************')
    print('-------------------------- MENU REMOVER FUNCIONÁRIO -------------------------')
    valor_desejado = int(input('Digite o código do Funcionário a ser removido: '))
    for funcionario in lista_funcionario:
        if funcionario['id'] == valor_desejado:
            lista_funcionario.remove(funcionario)
            print('Funcionário Removido')
            print('*******************************************************************************')
            print('-------------------------------MENU PRINCIPAL----------------------------------')

# --------Fim de remover_funcionário() --------

# -------- Início de Main --------
print('Controle de Funcionários')
print('*******************************************************************************')
print('-------------------------------MENU PRINCIPAL----------------------------------')
while True:
    opcao_principal = input('Escolha a opção desejada:\n' +
                            '1-Cadastrar Funcionário\n' +
                            '2-Consultar Funcionário(s)\n' +
                            '3-Remover Funcionário\n' +
                            '4-Sair\n' +
                            '>> ')

    if opcao_principal == '1':
        codigo_funcionario = codigo_funcionario + 1
        cadastrar_funcionario(codigo_funcionario)
        print('*******************************************************************************')
        print('-------------------------------MENU PRINCIPAL----------------------------------')
    elif opcao_principal == '2':
        consultar_funcionario()
    elif opcao_principal == '3':
        remover_funcionario()
    elif opcao_principal == '4':
        break
    else:
        print('Opçao Inválida. Tente Novamente')
        continue

# -------- Fim de Main --------


