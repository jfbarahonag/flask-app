import os

class CustomFile():
    def __init__(self, filename) -> None:
        self.__filename = filename

    ## Setters & Getters

    def get_filename(self):
        return self.__filename

    def set_filename(self, filename):
        self.__filename = filename


    ## Boolean

    def exists(self):
        return os.path.exists(self.__filename)

    def is_open(self):
        print(f"Here {self.__f.closed}")
        return not self.__f.closed


    ## Open & Close

    def open_for_reading(self):
        if self.is_open() == False:
            self.__f = open(self.__filename, "r")

    def open_for_writing(self, overwrite=True):
        self.__f = open(self.__filename, f'{"w" if overwrite == True else "a"}')
        print(f"File {self.__f.name} opened")

    def close(self):
        self.__f.close()
        print(f"File {self.__f.name} closed")


    ## Create & delete

    def create(self):
        self.__f = open(self.__filename, 'x')
        print(f"File {self.__f.name} created")
        self.__f.close()

    def remove(self):
        if self.exists():
            try:
                self.close()
                print("Delete ", self.__f.name)
                os.remove(self.__filename)
            except OSError as e:
                print("Error ", e.errno)


    ## Read & Write

    def read(self):
        self.open_for_reading()
        data = self.__f.read()
        self.close()
        return data

    def write(self, data, overwrite=False):
        self.open_for_writing(overwrite)
        self.__f.write(data)
        self.close()
    
