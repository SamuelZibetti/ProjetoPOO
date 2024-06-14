class Pessoa:
    def __init__(self, nome=None, cpf=None, dataNasc=None):
        self._nome = nome
        self._cpf = cpf
        self._dataNasc = dataNasc
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf
    
    @property
    def dataNasc(self):
        return self._dataNasc
    
    @dataNasc.setter
    def dataNasc(self, dataNasc):
        self._dataNasc = dataNasc
    
    def exibirInfo(self):
        return f'Nome: {self.nome}, CPF: {self.cpf}, Data de Nascimento: {self.dataNasc}'