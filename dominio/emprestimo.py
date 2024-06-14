from datetime import date

class Emprestimo:
    def __init__(self, membro=None, livro=None):
        self._membro = membro
        self._livro = livro
        self._dataEmprestimo = date.today()
        self._dataDevolucao = None
    
    @property
    def membro(self):
        return self._membro
    
    @membro.setter
    def membro(self, membro):
        self._membro = membro
    
    @property
    def livro(self):
        return self._livro
    
    @livro.setter
    def livro(self, livro):
        self._livro = livro
    
    @property
    def dataEmprestimo(self):
        return self._dataEmprestimo
    
    @dataEmprestimo.setter
    def dataEmprestimo(self, dataEmprestimo):
        self._dataEmprestimo = dataEmprestimo
    
    @property
    def dataDevolucao(self):
        return self._dataDevolucao
    
    @dataDevolucao.setter
    def dataDevolucao(self, dataDevolucao):
        self._dataDevolucao = dataDevolucao
    
    def alugando(self):
        if self._livro.emprestar():
            return f'Empréstimo registrado: {self._livro.titulo} para {self._membro.nome} na data {self._dataEmprestimo}'
        return 'Livro não disponível para empréstimo'
    
    def devolvendo(self):
        self._livro.devolver()
        self._dataDevolucao = date.today()
        return f'Livro {self._livro.titulo} devolvido por {self._membro.nome} na data {self._dataDevolucao}'