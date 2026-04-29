import numpy as np

np.set_printoptions(precision=2, suppress=True)

# Valor dado no enunciado
sin45 = cos45 = 0.71

print("=" * 55)
print("  MATRIZES DE TRANSFORMAÇÃO — COORDENADAS HOMOGÊNEAS")
print("=" * 55)

# ─────────────────────────────────────────────
# 1. Translação 2D: t = (4, 9)
# ─────────────────────────────────────────────
T = np.array([
    [1, 0, 4],
    [0, 1, 9],
    [0, 0, 1],
], dtype=float)

print("\n1. Translação 2D  t=(4,9)")
print(T)

# ─────────────────────────────────────────────
# 2. Rotação 2D no eixo Z: θ = π/4
# ─────────────────────────────────────────────
R = np.array([
    [ cos45, -sin45, 0],
    [ sin45,  cos45, 0],
    [     0,      0, 1],
], dtype=float)

print("\n2. Rotação 2D  θ=π/4  (sin=cos=0.71)")
print(R)

# ─────────────────────────────────────────────
# 3. Escala não uniforme: Sx=2, Sy=0.75
# ─────────────────────────────────────────────
S = np.array([
    [2,    0, 0],
    [0, 0.75, 0],
    [0,    0, 1],
], dtype=float)

print("\n3. Escala não uniforme  Sx=2, Sy=0.75")
print(S)

# ─────────────────────────────────────────────
# 4. Reflexão pelos eixos X e Y
# ─────────────────────────────────────────────
REF = np.array([
    [-1,  0, 0],
    [ 0, -1, 0],
    [ 0,  0, 1],
], dtype=float)

print("\n4. Reflexão pelos eixos X e Y")
print(REF)

# ─────────────────────────────────────────────
# 5. Composta: Rotação + Translação (objeto na origem)
#    M = T · R
# ─────────────────────────────────────────────
T49 = np.array([
    [1, 0, 4],
    [0, 1, 9],
    [0, 0, 1],
], dtype=float)

M5 = T49 @ R   # leitura direita→esquerda: primeiro R, depois T

print("\n5. Composta: T(4,9) · R(π/4)  [objeto na origem]")
print("   T(4,9):")
print(T49)
print("   R(π/4):")
print(R)
print("   Resultado M = T · R:")
print(M5)

# ─────────────────────────────────────────────
# 6. Composta: objeto centrado em (2,3)
#    M = T(4,9) · R(π/4) · T(-2,-3)
# ─────────────────────────────────────────────
T_neg = np.array([
    [1, 0, -2],
    [0, 1, -3],
    [0, 0,  1],
], dtype=float)

M6 = T49 @ R @ T_neg

print("\n6. Composta: T(4,9) · R(π/4) · T(-2,-3)  [objeto em (2,3)]")
print("   T(-2,-3):")
print(T_neg)
print("   R(π/4):")
print(R)
print("   T(4,9):")
print(T49)
print("   Resultado M = T(4,9) · R · T(-2,-3):")
print(M6)

# ─────────────────────────────────────────────
# 7. Composta 3D: Terra no Sistema Solar
#    M = Ry(phi) · T(d,0,0) · Ry(theta)
#    Variáveis simbólicas → usamos valores de exemplo
# ─────────────────────────────────────────────
import math

def Ry(angle):
    """Rotação 3D em torno do eixo Y (matriz 4x4)."""
    c, s = math.cos(angle), math.sin(angle)
    return np.array([
        [ c, 0, s, 0],
        [ 0, 1, 0, 0],
        [-s, 0, c, 0],
        [ 0, 0, 0, 1],
    ], dtype=float)

def T3d(tx, ty, tz):
    """Translação 3D (matriz 4x4)."""
    return np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0,  1],
    ], dtype=float)

# Exemplo com valores concretos (dia do ano + hora do dia)
theta = math.pi / 6   # rotação da Terra em torno de si (hora do dia)
phi   = math.pi / 3   # ângulo orbital em torno do Sol (dia do ano)
d     = 10.0          # distância Terra–Sol (unidades arbitrárias)

M7 = Ry(phi) @ T3d(d, 0, 0) @ Ry(theta)

print("\n7. Matriz modelo da Terra (3D)  M = Ry(φ) · T(d,0,0) · Ry(θ)")
print(f"   θ={theta:.4f} rad, φ={phi:.4f} rad, d={d}")
print("\n   Ry(φ)  — órbita ao redor do Sol:")
print(Ry(phi))
print("\n   T(d,0,0)  — afasta do Sol:")
print(T3d(d, 0, 0))
print("\n   Ry(θ)  — rotação da Terra em torno de si:")
print(Ry(theta))
print("\n   Resultado M = Ry(φ) · T(d,0,0) · Ry(θ):")
print(M7)

print("\n" + "=" * 55)
print("  Ordem de aplicação (direita → esquerda):")
print("  1) Ry(θ)    — gira a Terra em torno de si")
print("  2) T(d,0,0) — posiciona a distância d do Sol")
print("  3) Ry(φ)    — orbita em torno do Sol (plano XZ)")
print("=" * 55)
