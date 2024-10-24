class Dispositivo():

    def __init__(self, id, nome, cpf, modelo, fabricante, orgao, status, is_adm):
        self.__id = id
        self.__nome = nome
        self.__cpf = cpf
        self.__modelo = modelo
        self.__fabricante = fabricante
        self.__orgao = orgao
        self.__status = status
        self.__is_adm = is_adm

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
    def cpf(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @property
    def fabricante(self):
        return self.__fabricante

    @fabricante.setter
    def fabricante(self, fabricante):
        self.__fabricante = fabricante

    @property
    def orgao(self):
        return self.__orgao

    @orgao.setter
    def orgao(self, orgao):
        self.__orgao = orgao

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    @property
    def is_adm(self):
        return self.__is_adm

    @is_adm.setter
    def is_adm(self, is_adm):
        self.__is_adm = is_adm
