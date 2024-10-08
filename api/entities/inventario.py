class Inventario():

    def __init__(self, ano, bem, estado, situacao, plaqueta, observacao, cadastrado_por, situacao_observacao, tem_numero_serie, numero_serie, created_at=None, updated_at=None, deleted_at=None, id=None):
        self.__id = id
        self.__ano = ano
        self.__bem = bem
        self.__estado = estado
        self.__situacao = situacao
        self.__plaqueta = plaqueta
        self.__observacao = observacao
        self.__cadastrado_por = cadastrado_por
        self.__situacao_observacao = situacao_observacao
        self.__tem_numero_serie = tem_numero_serie
        self.__numero_serie = numero_serie
        self.__created_at = created_at
        self.__updated_at = updated_at
        self.__deleted_at = deleted_at

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def bem(self):
        return self.__bem

    @bem.setter
    def bem(self, bem):
        self.__bem = bem

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado):
        self.__estado = estado

    @property
    def situacao(self):
        return self.__situacao

    @situacao.setter
    def situacao(self, situacao):
        self.__situacao = situacao

    @property
    def plaqueta(self):
        return self.__plaqueta

    @plaqueta.setter
    def plaqueta(self, plaqueta):
        self.__plaqueta = plaqueta

    @property
    def observacao(self):
        return self.__observacao

    @observacao.setter
    def observacao(self, observacao):
        self.__observacao = observacao

    @property
    def cadastrado_por(self):
        return self.__cadastrado_por

    @cadastrado_por.setter
    def cadastrado_por(self, cadastrado_por):
        self.__cadastrado_por = cadastrado_por

    @property
    def situacao_observacao(self):
        return self.__situacao_observacao

    @situacao_observacao.setter
    def situacao_observacao(self, situacao_observacao):
        self.__situacao_observacao = situacao_observacao

    @property
    def tem_numero_serie(self):
        return self.__tem_numero_serie

    @tem_numero_serie.setter
    def tem_numero_serie(self, tem_numero_serie):
        self.__tem_numero_serie = tem_numero_serie

    @property
    def numero_serie(self):
        return self.__numero_serie

    @numero_serie.setter
    def numero_serie(self, numero_serie):
        self.__numero_serie = numero_serie

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, created_at):
        self.__created_at = created_at

    @property
    def updated_at(self):
        return self.__updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        self.__updated_at = updated_at

    @property
    def deleted_at(self):
        return self.__deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        self.__deleted_at = deleted_at

    def to_dict(self):
        return {
            "id" : self.__id, 
            "ano" : self.__ano,
            "bem" : self.__bem,
            "estado" : self.__estado,
            "situacao" : self.__situacao,
            "plaqueta" : self.__plaqueta,
            "observacao" : self.__observacao,
            "cadastrado_por" : self.__cadastrado_por,
            "situacao_observacao" : self.__situacao_observacao,
            "tem_numero_serie" : self.tem_numero_serie,
            "numero_serie" : self.__numero_serie,
            "created_at" : self.__created_at,
            "updated_at" : self.__updated_at,
            "deleted_at" : self.__deleted_at,
        }
