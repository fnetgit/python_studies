# method vs @classmethod vs @staticmethod

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    # METODO DE INSTÂNCIA: Útil quando precisamos de dados do objeto (self)
    # Ex: Alterar o usuário de uma conexão que já existe.
    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    # CLASS METHOD: Atua como uma "Fábrica" (Factory)
    # Recebe 'cls' (a classe) em vez de 'self' (a instância).
    # Útil para criar o objeto de formas diferentes sem sujar o __init__.
    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()  # Cria a instância usando a própria classe
        connection.user = user
        connection.password = password
        return connection

    # STATIC METHOD: É uma função comum que "mora" dentro da classe.
    # Não recebe nem 'self' nem 'cls'.
    # Útil para funções utilitárias que não alteram nada na classe ou no objeto.
    @staticmethod
    def log(msg):
        print('LOG:', msg)


# usando class method
c1 = Connection.create_with_auth('fco', '1234')

# usando método de instância
c1.set_user('novo_usuario')
c1.set_password('nova_senha')
print(f"Usuário: {c1.user} | Senha: {c1.password}")

# usando static method
Connection.log('Essa é a mensagem de log')
