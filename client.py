class Client:
    def __init__(self, name,lastName,cel):
        self.name = name
        self.lastName = lastName
        self.cel = cel

    def toDBCollection(self):
        return{
            'name': self.name,
            'lastname': self.lastName,
            'cel': self.cel
        }