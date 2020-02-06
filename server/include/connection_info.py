class ConnectionInfo():
    server = 'mongodb'
    port = '27017'
    username = 'dnd'
    password = 'Dnd1234$'
    database = 'dnd'

    def get_server(self):
        return self.server
    
    def get_username(self):
        return self.username
    
    def get_password(self):
        return self.password

    def get_database(self):
        return self.database
    
    def get_port(self):
        return self.port