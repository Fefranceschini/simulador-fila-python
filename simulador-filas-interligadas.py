import random

def U(a, b):
    return a + (b - a) * random.random()

def simular():
    TG = 0

    fila1 = 0
    fila2 = 0

    perdas1 = 0
    perdas2 = 0

    tempo_estado1 = [0]*4
    tempo_estado2 = [0]*6

    servers1, cap1 = 2, 3
    servers2, cap2 = 1, 5

    prox_chegada = 1.5
    prox_passagem = float('inf')
    prox_saida = float('inf')

    ultimo = 0
    count = 100000

    while count > 0:
        tempo = min(prox_chegada, prox_passagem, prox_saida)

        tempo_estado1[fila1] += tempo - ultimo
        tempo_estado2[fila2] += tempo - ultimo

        ultimo = tempo
        TG = tempo

        if tempo == prox_chegada:
            # chegada fila1
            if fila1 < cap1:
                fila1 += 1
                if fila1 <= servers1:
                    prox_passagem = TG + U(3,4)
            else:
                perdas1 += 1

            prox_chegada = TG + U(1,4)
            count -= 1

        elif tempo == prox_passagem:
            # sai fila1 → vai fila2
            fila1 -= 1

            if fila2 < cap2:
                fila2 += 1
                if fila2 <= servers2:
                    prox_saida = TG + U(2,3)
            else:
                perdas2 += 1

            if fila1 >= servers1:
                prox_passagem = TG + U(3,4)
            else:
                prox_passagem = float('inf')

        else:
            # saída fila2
            fila2 -= 1

            if fila2 >= servers2:
                prox_saida = TG + U(2,3)
            else:
                prox_saida = float('inf')

    return tempo_estado1, tempo_estado2, TG, perdas1, perdas2

t1, t2, TG, p1, p2 = simular()

print("TEMPO GLOBAL:", TG)

print("\nFILA 1")
print("Perdas:", p1)
for i in range(len(t1)):
    print(i, t1[i], t1[i]/TG)

print("\nFILA 2")
print("Perdas:", p2)
for i in range(len(t2)):
    print(i, t2[i], t2[i]/TG)