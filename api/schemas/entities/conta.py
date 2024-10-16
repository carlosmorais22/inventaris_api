class Conta():

    def __init__(self, descricao, tem_numero_serie, vida_util, ativo, id=None):
        self.__id = id
        self.__descricao = descricao
        self.__tem_numero_serie = tem_numero_serie
        self.__vida_util = vida_util
        self.__ativo = ativo

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def cpf(self, descricao):
        self.__descricao = descricao

    @property
    def tem_numero_serie(self):
        return self.__tem_numero_serie

    @tem_numero_serie.setter
    def cpf(self, tem_numero_serie):
        self.__tem_numero_serie = tem_numero_serie

    @property
    def vida_util(self):
        return self.__vida_util

    @vida_util.setter
    def cpf(self, vida_util):
        self.__vida_util = vida_util

    @property
    def ativo(self):
        return self.__ativo

    @ativo.setter
    def cpf(self, ativo):
        self.__ativo = ativo
