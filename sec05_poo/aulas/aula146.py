# Criando Exceptions em Python Orientado a Objetos

# Criando exceções
# Só precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# (comum colocar Error ao final do nome)
class MeuError(Exception):
    ...


class OutroError(Exception):
    ...


# Levantando (raise) / Lançando (throw) exceções
def levantar():
    exception_ = MeuError('a', 'b', 'c')
    # Adicionando notas em exceções
    exception_.add_note('Nota 1')
    raise exception_


try:
    levantar()
# Tratando a exceção
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    # Relançando exceções
    exception_ = OutroError('Vou lançar de novo')
    raise exception_ from error
