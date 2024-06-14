class Livro:
    def __init__(self, titulo=None, autor=None, isbn=None):
        self._titulo = titulo
        self._autor = autor
        self._isbn = isbn
        self._disponivel = True
    
    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo
    
    @property
    def autor(self):
        return self._autor
    
    @autor.setter
    def autor(self, autor):
        self._autor = autor
    
    @property
    def isbn(self):
        return self._isbn
    
    @isbn.setter
    def isbn(self, isbn):
        self._isbn = isbn
    
    @property
    def disponivel(self):
        return self._disponivel
    
    @disponivel.setter
    def disponivel(self, disponivel):
        self._disponivel = disponivel
    
    def emprestar(self):
        if self._disponivel:
            self._disponivel = False
            return True
        return False
    
    def devolver(self):
        self._disponivel = True