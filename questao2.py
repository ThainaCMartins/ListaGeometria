import numpy as np

# =============================================================
# QUESTÃO 2 — Geometria Afim e Euclidiana
# =============================================================
# O enunciado pede pra resolver usando operações de alto nível:
# combinações afins, produto interno e produto vetorial.
# Sem trigonometria, sem manipulação de coordenadas no braço.


# =============================================================
# ITEM 1 — Encontrar o ponto s que completa o paralelogramo
# =============================================================
#
# Dado o triângulo △pqr, quero achar um ponto s tal que
# {p, s, q, r} formem um paralelogramo com pq como diagonal.
#
# RACIOCÍNIO:
# Numa paralelogramo, as diagonais se bissectam — ou seja,
# o ponto médio de uma diagonal é igual ao ponto médio da outra.
#
# As diagonais aqui são: pq  e  sr
#
# Então:
#   ponto_médio(pq) = ponto_médio(sr)
#   (p + q) / 2    = (s + r) / 2
#
# Isolando s:
#   s = p + q - r
#
# Isso é uma COMBINAÇÃO AFIM! Os coeficientes somam 1:
#   1 + 1 + (-1) = 1  ✓
# então s é um ponto válido no espaço afim.

# pontos de exemplo pra testar (2D, mas funciona em qualquer dimensão)
p = np.array([0.0, 2.0])
q = np.array([3.0, 0.0])
r = np.array([4.0, 2.0])

# calculo s usando a combinação afim descoberta acima
s = p + q - r   # s = p + q - r

print("=" * 55)
print("  ITEM 1 — Encontrando s para completar o paralelogramo")
print("=" * 55)
print(f"  p = {p}")
print(f"  q = {q}")
print(f"  r = {r}")
print(f"  s = p + q - r = {s}")

# VERIFICAÇÃO: confirmo que as diagonais se cruzam no mesmo ponto médio
meio_pq = (p + q) / 2
meio_sr = (s + r) / 2
print(f"\n  Verificação (diagonais se bissectam):")
print(f"  Ponto médio de pq: {meio_pq}")
print(f"  Ponto médio de sr: {meio_sr}")
print(f"  São iguais? {np.allclose(meio_pq, meio_sr)}")

# =============================================================
# ITEM 2 — O observador vê a frente ou o verso do triângulo?
# =============================================================
#
# Tenho um triângulo em R³ com vértices p, q, r.
# O "lado da frente" é aquele em que p, q, r aparecem em
# sentido anti-horário.
# Um observador está no ponto e (não coplanar com o triângulo).
#
# RACIOCÍNIO:
# 1) Calculo a normal do triângulo com PRODUTO VETORIAL:
#      n = (q - p) × (r - p)
#    Pela regra da mão direita, se p→q→r é anti-horário,
#    n aponta para o lado da FRENTE do triângulo.
#
# 2) Calculo o vetor do triângulo até o observador:
#      v = e - p
#
# 3) Uso PRODUTO INTERNO para saber se e está do mesmo lado que n:
#      se  n · v > 0  →  e está do lado que n aponta  →  vê a FRENTE
#      se  n · v < 0  →  e está do lado oposto a n    →  vê o VERSO
#      se  n · v = 0  →  e está no plano do triângulo (não deveria por enunciado)

# pontos do triângulo em R³
p3 = np.array([0.0, 0.0, 0.0])
q3 = np.array([1.0, 0.0, 0.0])
r3 = np.array([0.0, 1.0, 0.0])

# exemplo 1: observador acima do plano XY (deve ver a frente)
e_frente = np.array([0.5, 0.5, 1.0])

# exemplo 2: observador abaixo do plano XY (deve ver o verso)
e_verso = np.array([0.5, 0.5, -1.0])

print("\n" + "=" * 55)
print("  ITEM 2 — O observador vê a frente ou o verso?")
print("=" * 55)
print(f"  Triângulo: p={p3}, q={q3}, r={r3}")


def lado_que_observador_ve(p, q, r, e):
    """
    Determina se o observador em e vê a frente ou o verso
    do triângulo pqr, onde a frente é o lado em que p→q→r
    aparece em sentido anti-horário.

    Método:
      1. Normal n = (q-p) × (r-p)   — produto vetorial
      2. Vetor ao observador v = e - p
      3. Sinal de n · v             — produto interno
    """

    # passo 1: vetores das arestas a partir de p
    u = q - p   # aresta pq
    w = r - p   # aresta pr

    # passo 2: normal do triângulo via produto vetorial
    # n aponta para o lado "frente" (onde p,q,r são anti-horários)
    n = np.cross(u, w)

    # passo 3: vetor do triângulo ao observador
    v = e - p

    # passo 4: produto interno entre a normal e o vetor ao observador
    dot = np.dot(n, v)

    print(f"\n  Observador em e = {e}")
    print(f"  Normal n = (q-p) × (r-p) = {n}")
    print(f"  Vetor ao observador v = e - p = {v}")
    print(f"  Produto interno n · v = {dot:.4f}")

    if dot > 0:
        print("  → n · v > 0: observador está do mesmo lado que a normal")
        print("  → Observador vê a FRENTE do triângulo ✓")
    elif dot < 0:
        print("  → n · v < 0: observador está do lado oposto à normal")
        print("  → Observador vê o VERSO do triângulo")
    else:
        print("  → n · v = 0: observador está no plano (coplanar!)")


lado_que_observador_ve(p3, q3, r3, e_frente)
lado_que_observador_ve(p3, q3, r3, e_verso)

print("\n" + "=" * 55)
print("  Resumo do raciocínio geométrico:")
print("  Item 1: s = p + q - r  (combinação afim)")
print("  Item 2: sinal de [(q-p)×(r-p)] · (e-p)")
print("          > 0 → frente  |  < 0 → verso")
print("=" * 55)
