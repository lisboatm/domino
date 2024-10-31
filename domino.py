# Função para calcular o número de peças do dominó duplo-N
def calcular_pecas_dominio(N):
    return (N + 1) * (N + 2) // 2

# Leitura do valor de N
N = int(input())

# Cálculo e impressão do número de peças
print(calcular_pecas_dominio(N))
