class Bem():

    def __init__(self, orgao, setor, tombo, descricao, conta, estado, estado_descricao, valor, valor_remanescente, numero_serie, data, data_aquisicao, ativo, inventariado=None, id=None):

        self.__id = id
        self.__orgao = orgao
        self.__setor = setor
        self.__tombo = tombo
        self.__descricao = descricao
        self.__conta = conta
        self.__estado = estado
        self.__estado_descricao = estado_descricao
        self.__valor = valor
        self.__valor_remanescente = valor_remanescente
        self.__numero_serie = numero_serie
        self.__data = data
        self.__data_aquisicao = data_aquisicao
        self.__ativo = ativo
        self.__inventariado = inventariado

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def orgao(self):
        return self.__orgao

    @orgao.setter
    def orgao(self, orgao):
        self.__orgao = orgao

    @property
    def setor(self):
        return self.__setor

    @setor.setter
    def setor(self, setor):
        self.__setor = setor

    @property
    def tombo(self):
        return self.__tombo

    @tombo.setter
    def tombo(self, tombo):
        self.__tombo = tombo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def conta(self):
        return self.__conta

    @conta.setter
    def conta(self, conta):
        self.__conta = conta

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado):
        self.__estado = estado

    @property
    def estado_descricao(self):
        return self.__estado_descricao

    @estado_descricao.setter
    def estado_descricao(self, estado_descricao):
        self.__estado_descricao = estado_descricao

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def valor_remanescente(self):
        return self.__valor_remanescente

    @valor_remanescente.setter
    def valor_remanescente(self, valor_remanescente):
        self.__valor_remanescente = valor_remanescente

    @property
    def numero_serie(self):
        return self.__numero_serie

    @numero_serie.setter
    def numero_serie(self, numero_serie):
        self.__numero_serie = numero_serie

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def data_aquisicao(self):
        return self.__data_aquisicao

    @data_aquisicao.setter
    def data_aquisicao(self, data_aquisicao):
        self.__data_aquisicao = data_aquisicao

    @property
    def ativo(self):
        return self.__ativo

    @ativo.setter
    def ativo(self, ativo):
        self.__ativo = ativo

    @property
    def inventariado(self):
        return self.__inventariado

    @inventariado.setter
    def inventariado(self, inventariado):
        self.__inventariado = inventariado
