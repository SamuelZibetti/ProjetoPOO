import sys
import os
from datetime import date

# Adicionando o diretório raiz ao PYTHONPATH para que os módulos possam ser importados corretamente
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from dominio.membro import Membro
from dominio.funcionario import Funcionario
from dominio.livro import Livro
from dominio.emprestimo import Emprestimo

# Definindo as listas globais
lista_pessoas = []
lista_livros = []
lista_emprestimos = []

def main():
    global lista_pessoas, lista_livros, lista_emprestimos
    
    # Criando instâncias de Membro e Funcionario
    membro1 = Membro("João Silva", "123.456.789-00", "2000-04-22", 1001, "Standard")
    membro2 = Membro()
    membro2.nome = "Ana Pereira"
    membro2.cpf = "234.567.890-01"
    membro2.dataNasc = "2003-11-06"
    membro2.matricula = 1002
    membro2.assinatura = "Premium"

    funcionario1 = Funcionario("Maria Souza", "987.654.321-00", "2001-07-10", "Bibliotecária", 1500)
    funcionario2 = Funcionario()
    funcionario2.nome = "José Santos"
    funcionario2.cpf = "456.789.012-23"
    funcionario2.dataNasc = "1998-10-25"
    funcionario2.cargo = "Assistente Administrativo"
    funcionario2.salario = 1800
    
    # Adicionando membros e funcionários à lista de pessoas
    lista_pessoas.append(membro1)
    lista_pessoas.append(membro2)

    lista_pessoas.append(funcionario1)
    lista_pessoas.append(funcionario2)
    
    # Criando instância de Livro
    livro1 = Livro("Python para Todos", "John Smith", "978-3-16-148410-0")
    livro2 = Livro("Algoritmos e Estruturas de Dados", "Alice Silva", "978-3-16-148411-0")
    livro3 = Livro("Introdução à Banco de Dados", "Bob Oliveira", "978-3-16-148412-0")
    
    # Adicionando livro à lista de livros
    lista_livros.append(livro1)
    lista_livros.append(livro2)
    lista_livros.append(livro3)
    
    # Exibindo informações das pessoas
    print('----------------------------------- Aplicativo Biblioteca -----------------------------------')
    print()
    for pessoa in lista_pessoas:
        if isinstance(pessoa, Membro):
            print('Membro')
            print(f'Nome: {pessoa.nome}')
            print(f'CPF: {pessoa.cpf}')
            print(f'Data de Nascimento: {pessoa.dataNasc}')
            print(f'Matrícula: {pessoa.matricula}')
            print(f'Assinatura: {pessoa.assinatura}')
            print()
        elif isinstance(pessoa, Funcionario):
            print('Funcionário')
            print(f'Nome: {pessoa.nome}')
            print(f'CPF: {pessoa.cpf}')
            print(f'Data de Nascimento: {pessoa.dataNasc}')
            print(f'Cargo: {pessoa.cargo}')
            print(f'Salário: R${pessoa.salario:.2f}')
            print()
    
    # Exibindo informações do livro
    print('---------------------------------- Informações dos Livros ----------------------------------')
    print()
    for livro in lista_livros:
        print(f'Título do livro: {livro.titulo}')
        print(f'Disponível: {livro.disponivel}')
    print()
    
    # Criando instância de Emprestimo e registrando empréstimo
    print('-------------------------------- Registrando os Empréstimos --------------------------------')
    print()
    emprestimo1 = Emprestimo(membro1, livro1)
    print(emprestimo1.alugando())
    emprestimo2 = Emprestimo(membro2, livro2)
    print(emprestimo2.alugando())
    
    # Exemplo apenas para mostrar quando um empréstimo não pode ser feito
    emprestimo2 = Emprestimo(membro2, livro2)
    print(emprestimo2.alugando())
    print()
    
    # Adicionando empréstimo à lista de empréstimos
    lista_emprestimos.append(emprestimo1)
    lista_emprestimos.append(emprestimo2)
    
    print('---------------------------------- Informações Adicionais ----------------------------------')
    print()

    # Exibindo status do livro antes da devolução
    print(f'Título do livro: {livro1.titulo}, Disponível: {livro1.disponivel}')

    # Registrando devolução do livro
    print(emprestimo1.devolvendo())

    # Removendo empréstimo da lista de empréstimos após devolução
    lista_emprestimos.remove(emprestimo1)
    
    # Exibindo status do livro após a devolução
    print(f'Título do livro: {livro1.titulo}, Disponível: {livro1.disponivel}')
    print()

if __name__ == "__main__":
    main()