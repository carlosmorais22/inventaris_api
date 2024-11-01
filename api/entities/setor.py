class Setor():

    def __init__(self, nome, sigla, orgao, id=None):
        self.__id = id
        self.__nome = nome
        self.__sigla = sigla
        self.__orgao = orgao

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def sigla(self):
        return self.__sigla

    @sigla.setter
    def sigla(self, sigla):
        self.__sigla = sigla

    @property
    def orgao(self):
        return self.__orgao

    @orgao.setter
    def orgao(self, orgao):
        self.__orgao = orgao

