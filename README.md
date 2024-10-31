# README - Cálculo de Peças no Jogo de Dominó Duplo-N

## Descrição do Problema

Este problema consiste em calcular quantas peças existem em um jogo de dominó do tipo duplo-N, onde N é um número natural que representa o maior número de círculos em cada quadrado das peças. O número total de peças pode ser calculado usando a fórmula:

\[
\text{Total de peças} = \frac{(N + 1) \times (N + 2)}{2}
\]

## Especificações

1. O programa deve ler um número natural \( N \) que representa o tipo do jogo de dominó (duplo-N).
2. Com base no valor de \( N \), o programa deve calcular o número total de peças utilizando a fórmula mencionada.
3. O resultado deve ser impresso como um número natural.

## Entrada

A entrada consiste de uma única linha contendo um número natural \( N \) que representa o tipo do jogo de dominó:

- \( 0 \leq N \leq 10000 \)

## Saída

A saída deve consistir de uma única linha com um número natural que representa quantas peças existem em um jogo de dominó do tipo duplo-N.

## Exemplos

### Exemplo 1
**Entrada:**
```
6
```

**Saída:**
```
28
```

### Exemplo 2
**Entrada:**
```
12
```

**Saída:**
```
91
```

## Implementação

Aqui está um exemplo de implementação em Python para resolver o problema:

```python
# Função para calcular o número de peças do dominó duplo-N
def calcular_pecas_dominio(N):
    return (N + 1) * (N + 2) // 2

# Leitura do valor de N
N = int(input())

# Cálculo e impressão do número de peças
print(calcular_pecas_dominio(N))
```

## Considerações Finais

- A fórmula utilizada para calcular o número de peças no dominó duplo-N é eficiente, com complexidade O(1), pois envolve apenas operações matemáticas simples.
- O programa deve funcionar corretamente para qualquer valor de \( N \) dentro das restrições estabelecidas.
