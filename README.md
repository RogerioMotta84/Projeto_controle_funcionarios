# Controle de Funcionários RH

Este projeto foi desenvolvido como parte da disciplina de **Lógica de Programação e Algoritmos** da **Faculdade Uninter**, desenvolvendo um software de controle de funcionários para uma empresa de RH. Este software deve ter o seguinte menu e opções:

1 - **Cadastrar Funcionário**

2 - **Consultar Funcionário(s)**

Consultar Todos os Funcionários

Consultar Funcionário por Id

Consultar Funcionário(s) por Setor

Retornar ao menu principal

3 - **Remover Funcionário**

4 - **Sair**

## Requisitos do Projeto

### 1. Função cadastrar_funcionario(id) (EXIGÊNCIA 1)

Esta função:

Recebe um **id exclusivo** para cada funcionário cadastrado (pode ser gerado com um contador);

Solicita os seguintes dados ao usuário:

Nome do funcionário;

Setor do funcionário;

Salário do funcionário.

Armazena os dados de cada funcionário em um dicionário.

### 2. Função consultar_funcionarios() (EXIGÊNCIA 2)

Esta função:

Exibe um **menu de consulta** com as seguintes opções:

Consultar Todos os Funcionários;

Consultar Funcionário por Id;

Consultar Funcionário(s) por Setor;

Retornar ao menu principal.

### 3. Função remover_funcionario() (EXIGÊNCIA 3)

Esta função:

Pergunta ao usuário qual o **ID do funcionário** que deseja remover;

Remove o funcionário do **cadastro (dicionário).**

## Como Executar o Projeto

Certifique-se de ter o Python instalado na sua máquina.

Clone este repositório:

**git clone git@github.com:RogerioMotta84/Projeto_controle_funcionarios.git**

Acesse a pasta do projeto:

**cd Projeto_controle_funcionarios**

Execute o script Python:

**python Controle_de_funcionarios_RH.py**

## Tecnologias Utilizadas

**Python 3.x**

**Dicionários** para armazenar os dados dos funcionários

**Estruturas** de controle para navegação no menu

![Controle de Funcionários](Imagem/Controle%20Funcionários.png)
