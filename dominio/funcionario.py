from dominio.pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome=None, cpf=None, dataNasc=None, cargo=None, salario=None):
        super().__init__(nome, cpf, dataNasc)
        self._cargo = cargo
        self._salario = salario
    
    @property
    def cargo(self):
        return self._cargo
    
    @cargo.setter
    def cargo(self, cargo):
        self._cargo = cargo
        
    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, salario):
        self._salario = salario
    
    def exibirInfo(self):
        info = super().exibirInfo()
        return f'{info}, Cargo: {self.cargo}, Salário: {self.salario}'