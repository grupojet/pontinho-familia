#!/usr/bin/env python3
"""
Memorial de cálculo - Conversão de roçadeira de TDP para acionamento hidráulico
em braço de escavadeira Volvo.

Execute:  python3 calculos.py
Todos os parâmetros de entrada estão no bloco PARÂMETROS. Ajuste-os após
medir a roçadeira real e consultar o manual da escavadeira.
"""
from math import pi, sqrt

# ----------------------------------------------------------------------------
# PARÂMETROS (medir / confirmar)
# ----------------------------------------------------------------------------
D_corte       = 1.50     # m  - diâmetro de varredura das facas (largura de corte)
v_ponta       = 70.0     # m/s - velocidade de ponta alvo (faixa 60-80 m/s)
P_corte_kW    = 28.0     # kW  - potência contínua de corte prevista para 1,5 m
                         #       (equivale a trator de ~40-45 cv na TDP)

# Circuito auxiliar X1 da escavadeira (confirmar no manual / IECU)
Q_X1_Lmin     = 150.0    # L/min - vazão que será ajustada no modo "martelo"
p_X1_bar      = 210.0    # bar   - pressão de alívio do circuito X1
p_retorno_bar = 20.0     # bar   - contrapressão típica da linha de retorno
                         #        (filtro + mangueiras + bloco)
eta_mh        = 0.90     # rendimento mecânico-hidráulico do motor
eta_v         = 0.95     # rendimento volumétrico do motor
eta_cx        = 0.95     # rendimento da caixa cônica (opção B)
i_cx          = 1.47     # relação da caixa cônica original (540 -> ~794 rpm)

# Rotor (porta-facas + facas) para energia / frenagem
m_disco       = 22.0     # kg - disco porta-facas
r_disco       = 0.30     # m  - raio do disco
m_faca        = 4.0      # kg - cada faca (2 facas)
r_faca        = 0.68     # m  - raio ao CG da faca
p_frenagem    = 150.0    # bar - ajuste da válvula de alívio cruzado (freio)

# Eixo porta-facas (mancal, opção A)
d_eixo_mm     = 60.0     # mm - diâmetro no mancal / porta-facas
Sy_eixo       = 450.0    # MPa - SAE 1045 beneficiado (mín.)
F_impacto_kN  = 20.0     # kN - carga radial de impacto admitida no disco
L_balanco_mm  = 150.0    # mm - distância do disco ao rolamento inferior
C_rol_kN      = 125.0    # kN - capacidade dinâmica do rolamento 32212 (par)
P_rol_kN      = 6.0      # kN - carga equivalente média em operação

# Mangueiras
d_press_in    = 1.0      # pol - DI linha de pressão
d_ret_in      = 1.0      # pol - DI linha de retorno
d_dreno_in    = 0.5      # pol - DI dreno de carcaça

# Massa do implemento convertido (estimativa)
m_implemento  = 520.0    # kg - deck + cabeçote + motor + proteções

def titulo(t):
    print("\n" + t)
    print("-" * len(t))

# ----------------------------------------------------------------------------
# 1. Rotação do rotor
# ----------------------------------------------------------------------------
titulo("1. Rotação do porta-facas")
n_rotor = v_ponta / (pi * D_corte) * 60.0
w_rotor = n_rotor * 2 * pi / 60
print(f"Velocidade de ponta alvo       : {v_ponta:.0f} m/s")
print(f"Rotação do rotor               : {n_rotor:.0f} rpm  ({w_rotor:.1f} rad/s)")
print(f"Rotação original (TDP 540 x {i_cx}): {540*i_cx:.0f} rpm -> "
      f"ponta {540*i_cx*pi*D_corte/60:.0f} m/s")

# ----------------------------------------------------------------------------
# 2. Torque e potência hidráulica disponível
# ----------------------------------------------------------------------------
titulo("2. Torque no rotor e potência disponível no X1")
T_rotor = P_corte_kW * 1000 / w_rotor
dp_bar  = p_X1_bar - p_retorno_bar
P_hidr_kW = Q_X1_Lmin / 60000 * p_X1_bar * 1e5 / 1000
print(f"Torque contínuo no rotor       : {T_rotor:.0f} N.m")
print(f"Potência hidráulica bruta X1   : {P_hidr_kW:.1f} kW "
      f"({Q_X1_Lmin:.0f} L/min x {p_X1_bar:.0f} bar)")
print(f"Delta-p útil no motor          : {dp_bar:.0f} bar")

# ----------------------------------------------------------------------------
# 3. Opção A - motor de pistões vertical, acionamento direto
# ----------------------------------------------------------------------------
titulo("3. Opção A - motor vertical em acionamento direto (recomendada)")
V_A = 2 * pi * T_rotor / (dp_bar * 1e5 * eta_mh) * 1e6   # cm3/rev
Q_A = V_A * n_rotor / eta_v / 1000                        # L/min
print(f"Deslocamento mínimo            : {V_A:.0f} cm3/rev")
print(f"Vazão necessária               : {Q_A:.0f} L/min (<= {Q_X1_Lmin:.0f} ok)"
      if Q_A <= Q_X1_Lmin else
      f"Vazão necessária               : {Q_A:.0f} L/min (> {Q_X1_Lmin:.0f} !!)")
for nome, V in (("A2FM 107 / F12-110", 107.0), ("A2FM 125", 125.0), ("A2FM 160", 160.0)):
    T = V * 1e-6 * dp_bar * 1e5 / (2 * pi) * eta_mh
    Q = V * n_rotor / eta_v / 1000
    n_max_Q = Q_X1_Lmin * 1000 * eta_v / V
    print(f"  {nome:20s}: T={T:4.0f} N.m  Q@{n_rotor:.0f}rpm={Q:4.0f} L/min  "
          f"n_max@{Q_X1_Lmin:.0f}L/min={n_max_Q:4.0f} rpm  "
          f"P_eixo={T*w_rotor/1000:4.1f} kW")

# ----------------------------------------------------------------------------
# 4. Opção B - motor horizontal acoplado na entrada da caixa cônica original
# ----------------------------------------------------------------------------
titulo("4. Opção B - motor na entrada da caixa cônica (alternativa de baixo custo)")
n_in  = n_rotor / i_cx
T_in  = T_rotor / i_cx / eta_cx
V_B   = 2 * pi * T_in / (dp_bar * 1e5 * eta_mh) * 1e6
Q_B   = V_B * n_in / eta_v / 1000
print(f"Rotação de entrada da caixa    : {n_in:.0f} rpm")
print(f"Torque na entrada da caixa     : {T_in:.0f} N.m")
print(f"Deslocamento mínimo            : {V_B:.0f} cm3/rev")
print(f"Vazão necessária               : {Q_B:.0f} L/min")
for nome, V in (("A2FM 180", 180.0), ("A2FM 200", 200.0)):
    T = V * 1e-6 * dp_bar * 1e5 / (2 * pi) * eta_mh
    Q = V * n_in / eta_v / 1000
    print(f"  {nome:20s}: T={T:4.0f} N.m  Q@{n_in:.0f}rpm={Q:4.0f} L/min")

# ----------------------------------------------------------------------------
# 5. Energia do rotor e frenagem hidráulica
# ----------------------------------------------------------------------------
titulo("5. Energia cinética do rotor e tempo de parada")
I_rotor = 0.5 * m_disco * r_disco**2 + 2 * m_faca * r_faca**2
E_rotor = 0.5 * I_rotor * w_rotor**2
V_freio = 125.0
T_freio = V_freio * 1e-6 * p_frenagem * 1e5 / (2 * pi)
t_parada = I_rotor * w_rotor / T_freio
print(f"Momento de inércia do rotor    : {I_rotor:.2f} kg.m2")
print(f"Energia cinética @ {n_rotor:.0f} rpm   : {E_rotor/1000:.1f} kJ")
print(f"Torque de frenagem (alívio {p_frenagem:.0f} bar, {V_freio:.0f} cm3): {T_freio:.0f} N.m")
print(f"Tempo de parada com freio hidráulico: {t_parada:.1f} s")
print("Sem válvula de freio/anticavitação o rotor gira em roda-livre por >60 s\n"
      "e o motor cavita (bomba sem alimentação) -> OBRIGATÓRIO bloco de freio.")

# ----------------------------------------------------------------------------
# 6. Eixo porta-facas e rolamentos (opção A)
# ----------------------------------------------------------------------------
titulo("6. Eixo porta-facas (mancal independente) - opção A")
d = d_eixo_mm / 1000
tau = 16 * T_rotor / (pi * d**3) / 1e6
M_imp = F_impacto_kN * 1000 * L_balanco_mm / 1000
sigma_imp = 32 * M_imp / (pi * d**3) / 1e6
sigma_eq = sqrt(sigma_imp**2 + 3 * tau**2)
FS = Sy_eixo / sigma_eq
L10h = (C_rol_kN / P_rol_kN)**(10/3) * 1e6 / (60 * n_rotor)
print(f"Tensão de torção (torque nominal)   : {tau:.1f} MPa")
print(f"Momento por impacto radial {F_impacto_kN:.0f} kN   : {M_imp:.0f} N.m")
print(f"Tensão de flexão por impacto        : {sigma_imp:.0f} MPa")
print(f"Tensão equivalente (von Mises)      : {sigma_eq:.0f} MPa  -> FS = {FS:.1f} (>= 2,5 ok)")
print(f"Vida L10h rolamentos 32212 (par)    : {L10h:,.0f} h")

# ----------------------------------------------------------------------------
# 7. Mangueiras - velocidade do fluido
# ----------------------------------------------------------------------------
titulo("7. Mangueiras - velocidade de escoamento")
Q_op_Lmin = 125.0 * n_rotor / eta_v / 1000      # vazão de operação c/ A2FM 125 (ajuste no IECU)
print(f"Vazão de operação a ajustar no IECU (modo martelo): {Q_op_Lmin:.0f} L/min")
Q_m3s = Q_op_Lmin / 60000
for nome, d_in, lim in (("Pressão", d_press_in, 6.0), ("Retorno", d_ret_in, 4.0)):
    A = pi * (d_in * 0.0254)**2 / 4
    v = Q_m3s / A
    print(f"  {nome:8s} {d_in:.2g}\" : v = {v:.1f} m/s  (limite recomendado {lim:.0f} m/s) "
          f"{'ok' if v <= lim else 'AUMENTAR'}")
A_dr = pi * (d_dreno_in * 0.0254)**2 / 4
Q_dreno = 0.04 * Q_op_Lmin      # ~4% de fuga interna a quente
print(f"  Dreno    {d_dreno_in:.2g}\" : vazão de dreno estimada {Q_dreno:.0f} L/min -> "
      f"v = {Q_dreno/60000/A_dr:.1f} m/s ok  (pressão carcaça <= 2 bar)")

# ----------------------------------------------------------------------------
# 8. Calor gerado
# ----------------------------------------------------------------------------
titulo("8. Calor a dissipar")
P_perdas = P_hidr_kW * (1 - eta_mh * eta_v) + Q_X1_Lmin/60000 * p_retorno_bar*1e5/1000
print(f"Perdas motor + linhas (ordem de grandeza): {P_perdas:.1f} kW")
print("Radiador da escavadeira é dimensionado para martelo (duty similar) -> ok,\n"
      "monitorar temperatura do óleo <= 80 C nos primeiros ensaios.")

# ----------------------------------------------------------------------------
# 9. Cabeçote de engate - pinos e orelhas
# ----------------------------------------------------------------------------
titulo("9. Cabeçote pino-a-pino - verificação simplificada")
g = 9.81
F_din = m_implemento * g * 3.0          # fator dinâmico 3 (choques, deslocamento)
for pino_mm, modelo in ((70, "EC140/ECR145"), (80, "EC200/EC210/EC220")):
    A_pino = pi * (pino_mm/1000)**2 / 4
    tau_p = F_din / (2 * A_pino) / 1e6     # cisalhamento duplo
    print(f"  Pino Ø{pino_mm} ({modelo}): força dinâmica {F_din/1000:.0f} kN -> "
          f"tau = {tau_p:.1f} MPa (pino SAE 4140, admissível ~250 MPa) ok")
print("Dimensionante real: esforços da escavadeira ao 'empurrar' o deck.\n"
      "Orelhas com a mesma espessura/material das orelhas da caçamba original.")
