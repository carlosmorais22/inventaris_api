class Situacao():

    def __init__(self, descricao, status, id=None):
        self.__id = id
        self.__descricao = descricao
        self.__status = status

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
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    def to_dict(self):
        return {
            "id" : self.__id, 
            "descricao" : self.__descricao,
            "status" : self.__status,
        }
