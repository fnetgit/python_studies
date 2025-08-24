# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro

def multip(multi_fact):
    def action(number):
        return number * multi_fact
    return action


double = multip(2)
triple = multip(3)
quadruple = multip(4)

print(double(3))
print(double(4))
print(double(5))

# user_number = int(input('Digite um número: '))
# user_factor = int(input('Digite o multiplicador: '))

# result = multip(user_factor)(user_number)
# print(result)
