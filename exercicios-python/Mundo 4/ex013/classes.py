class Termostato:

    def __init__(self):
        self.__temperatura = 24

    @property
    def ftemperatura(self):
        return f"{self.__temperatura}°C"

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, temperatura):
        if temperatura < 16:
            self.__temperatura = 16
        elif temperatura > 30:
            self.__temperatura = 30
        elif (temperatura * 2) % 1 != 0:
            raise ValueError("ERRO, somente valores terminados em 0 ou 0.5")
        else:
            self.__temperatura = temperatura
