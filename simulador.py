import random

def U(a, b):
    return a + (b - a) * random.random()

def simular(servers, capacity, n_random=100000):
    TG = 0
    fila = 0
    perdas = 0

    tempo_estado = [0]*(capacity+1)

    prox_chegada = 2.0
    prox_saida = float('inf')

    ultimo_evento = 0

    count = n_random

    while count > 0:
        if prox_chegada < prox_saida:
            tempo = prox_chegada
            tipo = "chegada"
        else:
            tempo = prox_saida
            tipo = "saida"

        # acumula tempo
        tempo_estado[fila] += tempo - ultimo_evento
        ultimo_evento = tempo
        TG = tempo

        if tipo == "chegada":
            if fila < capacity:
                fila += 1
                if fila <= servers:
                    prox_saida = TG + U(3,5)
                    count -= 1
            else:
                perdas += 1

            prox_chegada = TG + U(2,5)
            count -= 1

        else:  # saída
            fila -= 1
            if fila >= servers:
                prox_saida = TG + U(3,5)
                count -= 1
            else:
                prox_saida = float('inf')

    return tempo_estado, TG, perdas

def imprimir(tempo_estado, TG, perdas):
    print("Tempo global:", TG)
    print("Perdas:", perdas)
    print("\nEstado | Tempo | Probabilidade")

    for i in range(len(tempo_estado)):
        prob = tempo_estado[i]/TG
        print(i, "|", tempo_estado[i], "|", prob)

# G/G/1/5
t1, TG1, p1 = simular(1,5)
print("\n--- G/G/1/5 ---")
imprimir(t1, TG1, p1)

# G/G/2/5
t2, TG2, p2 = simular(2,5)
print("\n--- G/G/2/5 ---")
imprimir(t2, TG2, p2)