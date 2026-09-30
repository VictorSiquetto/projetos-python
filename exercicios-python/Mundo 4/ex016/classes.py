class Retangulo:

    def __init__(self, base=1, altura=1):
        self._base = None
        self._altura = None
        self._area = None
        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):
        if not isinstance(base, float) and not isinstance(base, int):
            raise TypeError("O valor da base deve ser um número")
        elif base < 0:
            raise ValueError("O valor da base deve ser maior que 0")
        else:
            self._base = base

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        if not isinstance(altura, float) and not isinstance(altura, int):
            raise TypeError("O valor da altura deve ser um número")
        elif altura < 0:
            raise ValueError("O valor da altura deve ser maior que 0")
        else:
            self._altura = altura

    @property
    def area(self):
        self._area = self._base * self._altura
        return self._area

    @area.setter
    def area(self):
        raise PermissionError("Erro, área nao pode ser definida dessa maneira")

    @property
    def medidas(self):
        return f"Base = {self._base}\nAltura = {self._altura}\nArea = {self.area}"

    @medidas.setter
    def medidas(self, medidas: tuple):
        if not isinstance(medidas, tuple):
            raise TypeError("As medidas devem estar dentro de uma tupla")
        if len(medidas) != 2:
            raise SyntaxError("Informe uma tupla com os dois valores")
        if isinstance(medidas[0], float) or isinstance(medidas[0], int):
            self.base = medidas[0]
        else:
            raise TypeError("A base deve ser um numero")
        if isinstance(medidas[1], float) or isinstance(medidas[1], int):
            self.altura = medidas[1]
        else:
            raise TypeError("A altura deve ser um numero")
