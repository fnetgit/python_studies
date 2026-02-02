# Relações de Objetos e Hierarquia

# ASSOCIAÇÃO: Vínculo comportamental (Usa). Baixo acoplamento.
# Uma classe pode usar outras, mas são independentes.
# ex: Pessoa (usa) Carro

# AGREGAÇÃO: Vínculo estrutural (Tem um). Partes podem existir sem o todo.
# Uma classe agrupa outras(um todo que tem partes), mas as partes podem existir mesmo sem o todo.
# ex: PostoDeCombustivel (tem) Funcionarios(lista de objetos funcionário), Bombas... 


# COMPOSIÇÃO: Vínculo de existência (Dono de). Partes morrem com o todo.
# Uma classe é dona de outras classes, e as partes não podem existir sem o todo.
# ex: Carro (é dono) Motor

# HERANÇA: Extensão de tipo (É um). Alto acoplamento.
# Uma classe herda de outra, especializando seu comportamento.
# ex: Cachorro (é um) Animal

# Papéis na Hierarquia:
# Superclasse (Base/Parent): Define o contrato e estado genérico.
# Subclasse (Child/Derived): Especializa o comportamento.
