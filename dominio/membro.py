from dominio.pessoa import Pessoa

class Membro(Pessoa):
    def __init__(self, nome=None, cpf=None, dataNasc=None, matricula=None, assinatura=None):
        super().__init__(nome, cpf, dataNasc)
        self._matricula = matricula
        self._assinatura = assinatura
    
    @property
    def matricula(self):
        return self._matricula
    
    @matricula.setter
    def matricula(self, matricula):
        self._matricula = matricula
        
    @property
    def assinatura(self):
        return self._assinatura
    
    @assinatura.setter
    def assinatura(self, assinatura):
        self._assinatura = assinatura
    
    def exibirInfo(self):
        info = super().exibirInfo()
        return f'{info}, Matrícula: {self.matricula}, Assinatura: {self.assinatura}'