class Trip:

    __id = ""
    __headSign = ""

    def __init__(self, id, headSign):
        self.__id = id
        self.__headSign = headSign

    def get_id(self):
        return self.__id

    def get_head_sign(self):
        return self.__headSign

