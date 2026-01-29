# super() e a sobreposição de membros

# super() -> Chama um método da superclasse

# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super(MinhaString, self).upper()
#         print('DEPOIS DO UPPER')
#         return retorno


# string = MinhaString('Luiz')
# print(string.upper())


# Sobreposição de atributos e métodos
# class A:
#     atributo_a = 'valor a'

#     def metodo(self):
#         print('A')


# class B(A):
#     atributo_b = 'valor b'

#     def metodo(self):
#         print('B')


# class C(B):
#     atributo_c = 'valor c'

#     def metodo(self):
#         print('C')

# c = C()
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)


# Usando super() para chamar o método sobrescrito
# class A:
#     atributo_a = 'valor a'

#     def metodo(self):
#         print('A')


# class B(A):
#     atributo_b = 'valor b'

#     def metodo(self):
#         print('B')


# class C(B):
#     atributo_c = 'valor c'

#     def metodo(self):
#         # (C, self) é implícito, poderia ser apenas super().metodo()
#         # Busca na MRO de self o método definido na classe após C (neste caso, B).
#         super(C, self).metodo()

#         # Se fosse super(B, self).metodo(), chamaria A.metodo()
#         super(B, self).metodo()

#         print('C')


# c = C()
# c.metodo()
# print(C.mro())  # Mostra a Method Resolution Order (MRO)


# Herança e Inicialização com super()
class A:
    atributo_a = 'valor a'

    def __init__(self, atributo):
        # A classe A espera receber um parâmetro 'atributo'
        self.atributo = atributo

    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        # super() aqui chama o __init__ de A.
        # Repassamos o 'atributo' para A, senão A.atributo nunca seria criado.
        super().__init__(atributo)

        # Agora B define o que é específico dela
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')


class C(B):
    atributo_c = 'valor c'

    # esse init não seria necessário, o Python chamaria B.__init__ automaticamente

    # *args e **kwargs são usados para "pegar tudo" que for enviado
    # e repassar para as classes acima (B e A) sem precisar nomear um por um.
    def __init__(self, *args, **kwargs):
        # super() aqui chama o __init__ de B.
        # B vai receber esses argumentos, usar o que precisa e passar o resto para A.
        super().__init__(*args, **kwargs)

    def metodo(self):
        # Chamada direta via NomeDaClasse:
        # Útil quando você quer pular a ordem do super() e chamar alguém específico.
        # Note que aqui precisamos passar o 'self' manualmente.
        A.metodo(self)  # Força a execução do método de A
        B.metodo(self)  # Força a execução do método de B
        print('C')


# Criando a instância:
# 'Atributo' vai para o *args (e acaba em A)
# 'Qualquer' vai para o *args (e acaba em B como 'outra_coisa')
c = C('Atributo', 'Qualquer')

c.metodo()
