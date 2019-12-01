class Stop:
    __id = ""
    __name = ""
    __url = ""

    def __init__(self, id, name, url):
        self.__id = id
        self.__name = name
        self.__url = url

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name

    def get_url(self):
        return self.__url

    def display(self):
        print("ID: " + self.__id + ", name: " + self.__name + ", url: " + self.__url)
