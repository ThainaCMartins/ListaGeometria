import numpy as np

np.set_printoptions(precision=4, suppress=True)

# =============================================================
# QUESTÃO 3 — Mudança de Sistema de Coordenadas J ↔ M
# =============================================================
#
# Sistema J (Janela) — igual nos dois itens:
#   gl.viewport(0, 0, 800, 600)
#   → origem no canto SUPERIOR ESQUERDO
#   → x cresce para a DIREITA (0 até 800 pixels)
#   → y cresce para BAIXO     (0 até 600 pixels)
#
# Pontos clicados na janela (capturados em J):
#   P[J] = (200, 100)
#   Q[J] = (400, 300)

P_J = np.array([200, 100, 1], dtype=float)
Q_J = np.array([400, 300, 1], dtype=float)


# =============================================================
# ==================== PARTE (a) =============================
# =============================================================
#
# Sistema M (Mundo):
#   ortho(l=0, r=800, b=0, t=600, n=-1, f=1)
#   → origem no canto INFERIOR ESQUERDO
#   → x cresce para a DIREITA (0 até 800)
#   → y cresce para CIMA      (0 até 600)
#
# Observação importante: J e M têm o MESMO tamanho (800x600),
# mas os eixos y apontam em direções opostas!

print("=" * 60)
print("  PARTE (a) — ortho(0, 800, 0, 600, -1, 1)")
print("=" * 60)

# ── ITEM (a).1 — Representar J no sistema M ──────────────────
#
# Construção das colunas da matriz (a "dikentinha"):
#
# Quanto vale 1 xJ em xM?
#   Ambos vão de 0 a 800 → mesma escala → 1 xJ = 1 xM
#   Vetor x_J em M = (1, 0)
#
# Quanto vale 1 yJ em yM?
#   J: y vai de 0 a 600 para BAIXO
#   M: y vai de 0 a 600 para CIMA
#   Direções opostas, mesma magnitude → 1 yJ = -1 yM
#   Vetor y_J em M = (0, -1)
#
# Onde fica O_J em M?
#   O_J = canto superior esquerdo.
#   Em M esse ponto tem x=0 (esquerda) e y=600 (topo).
#   O_J em M = (0, 600)
#
# Matriz (cols = x_J[M], y_J[M], O_J[M]):
#
#          x_J   y_J   O_J
#   M_a = [  1    0     0  ]
#          [  0   -1   600  ]
#          [  0    0    1   ]

M_a = np.array([
    [1,  0,   0],   # 1 xJ = 1 xM (mesma escala, mesma direção)
    [0, -1, 600],   # 1 yJ = -1 yM (mesma escala, direção invertida); origem em y=600
    [0,  0,   1],
], dtype=float)

print("\n  (a).1 — Matriz de mudança de base J → M:")
print("          cols = [x_J em M | y_J em M | O_J em M]")
print(M_a)

# ── ITEM (a).2 — Calcular P e Q em M ─────────────────────────

P_M_a = M_a @ P_J
Q_M_a = M_a @ Q_J

print("\n  (a).2 — Coordenadas em M:")
print(f"  P[J] = (200, 100)  →  P[M] = ({P_M_a[0]:.1f}, {P_M_a[1]:.1f})")
print(f"  Q[J] = (400, 300)  →  Q[M] = ({Q_M_a[0]:.1f}, {Q_M_a[1]:.1f})")


# =============================================================
# ==================== PARTE (b) =============================
# =============================================================
#
# Sistema M (Mundo) MUDOU:
#   ortho(l=0, r=100, b=0, t=75, n=-1, f=1)
#   → origem no canto INFERIOR ESQUERDO
#   → x cresce para a DIREITA (0 até 100)
#   → y cresce para CIMA      (0 até 75)
#
# Agora M é MENOR que J: 100x75 unidades vs 800x600 pixels.

print("\n" + "=" * 60)
print("  PARTE (b) — ortho(0, 100, 0, 75, -1, 1)")
print("=" * 60)

# ── ITEM (b).1 — Representar J no sistema M ──────────────────
#
# Quanto vale 1 xJ em xM?
#   J vai de 0 a 800, M vai de 0 a 100.
#   Proporção: 100 / 800 = 1/8 = 0.125
#   Vetor x_J em M = (1/8, 0)
#
# Quanto vale 1 yJ em yM?
#   J vai de 0 a 600 (pra baixo), M vai de 0 a 75 (pra cima).
#   Proporção em magnitude: 75 / 600 = 1/8 = 0.125
#   Direções opostas → negativo.
#   Vetor y_J em M = (0, -1/8)
#
# Onde fica O_J em M?
#   O_J = canto superior esquerdo.
#   Em M esse ponto tem x=0 (esquerda) e y=75 (topo).
#   O_J em M = (0, 75)
#
# Quantas "setinhas" precisamos somar de OM até OJ?
#   OM = (0, 0) em M.
#   OJ = (0, 75) em M.
#   Precisamos de 0 setinhas xM e 75 setinhas yM.

sx_b = 100 / 800   # 1 pixel J = 0.125 unidade M no eixo x
sy_b = 75  / 600   # 1 pixel J = 0.125 unidade M no eixo y (magnitude)

M_b = np.array([
    [sx_b,    0,   0],   # 1 xJ = 1/8 xM (escala menor, mesma direção)
    [   0, -sy_b, 75],   # 1 yJ = -1/8 yM (menor e invertido); origem em y=75
    [   0,    0,   1],
], dtype=float)

print("\n  (b).1 — Matriz de mudança de base J → M:")
print("          cols = [x_J em M | y_J em M | O_J em M]")
print(M_b)

# ── ITEM (b).2 — Calcular P e Q em M ─────────────────────────

P_M_b = M_b @ P_J
Q_M_b = M_b @ Q_J

print("\n  (b).2 — Coordenadas em M:")
print(f"  P[J] = (200, 100)  →  P[M] = ({P_M_b[0]:.2f}, {P_M_b[1]:.2f})")
print(f"  Q[J] = (400, 300)  →  Q[M] = ({Q_M_b[0]:.2f}, {Q_M_b[1]:.2f})")

# ── ITEM (b).3 — Matriz inversa (M → J) ──────────────────────
#
# A inversa converte de volta de M para J.
# Algebricamente:
#   x_M = (1/8) * x_J    →   x_J = 8 * x_M
#   y_M = -(1/8)*y_J+75  →   y_J = (75 - y_M) * 8 = -8*y_M + 600
#
# Então a matriz inversa (M → J) é:
#   [ 8    0    0  ]
#   [ 0   -8   600 ]
#   [ 0    0    1  ]

M_b_inv = np.linalg.inv(M_b)

print("\n  (b).3 — Matriz inversa (M → J):")
print(M_b_inv)

# verificação: produto deve dar identidade
print("  Verificação M_b @ M_b_inv = I?")
print(np.round(M_b @ M_b_inv, 6))

# ── ITEM (b).4 — Converter R[M] = (4, 60) para J ─────────────
#
# Tenho um ponto em M e quero saber em qual pixel ele aparece.
# Uso a matriz inversa (M → J).

R_M = np.array([4, 60, 1], dtype=float)

R_J = M_b_inv @ R_M

print(f"\n  (b).4 — Converter R[M] = (4, 60) para J:")
print(f"  R[J] = M_b_inv @ R[M] = ({R_J[0]:.1f}, {R_J[1]:.1f})")
print(f"  → Pixel na janela: ({int(round(R_J[0]))}, {int(round(R_J[1]))})")

# =============================================================
print("\n" + "=" * 60)
print("  RESUMO GERAL")
print("=" * 60)
print("  (a) ortho igual à viewport (800x600):")
print("      J→M: x não muda, y inverte com offset 600")
print(f"      P[M]=({P_M_a[0]:.0f}, {P_M_a[1]:.0f})  Q[M]=({Q_M_a[0]:.0f}, {Q_M_a[1]:.0f})")
print()
print("  (b) ortho menor (100x75):")
print("      J→M: x e y escalam por 1/8 e y inverte com offset 75")
print(f"      P[M]=({P_M_b[0]:.2f}, {P_M_b[1]:.2f})  Q[M]=({Q_M_b[0]:.2f}, {Q_M_b[1]:.2f})")
print(f"      R[M]=(4,60) → pixel J = ({int(round(R_J[0]))}, {int(round(R_J[1]))})")
print("=" * 60)
