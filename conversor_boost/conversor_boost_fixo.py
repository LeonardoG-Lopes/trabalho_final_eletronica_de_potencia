## Importando bibliotecas
import numpy as np
import matplotlib.pyplot as plt

## Definição dos parâmetros a partir das intenções de projeto
Vin = 150.0           # Tensão de entrada (V)
Vout = 350.0          # Tensão de saída (V)
Pout = 1250.0         # Potência máxima na saída (W)
Fs = 40e3             # Frequência de chaveamento (Hz)
Ts = 1 / Fs           # Período de chaveamento (s)
VIl = 0.2             # Ondulação da corrente no indutor (%)
VVl = 0.01            # Ondulação da tensão no capacitor (%)

## Cálculo dos valores nominais e dimensionameno de componentes
D = (Vout - Vin)/Vout      # Razão Cíclica
Iout = Pout/Vout           # Corrente de saída
Iin = Pout/Vin             # Corrente de entrada
R = (Vout**2)/Pout         # Resistência da carga
L = (Vin*D)/(Fs*VIl*Iin)   # Indutãncia de entrada
C = (Iout*D)/(Fs*VVl*Vout) # Capacitância de saída

# Tempo de simulação: 20 ms para ver o amortecimento
t_end = 20e-3       # 20 ms
dt = Ts / 200      # subdividindo cada período em 200 passos
t = np.arange(0, t_end, dt)

# Vetores de simulação
iL = np.zeros_like(t)     # Corrente do indutor
vO = np.zeros_like(t)   # Tensão do capacitor/saída

# Condições iniciais
iL[0] = 0.0
vO[0] = 0.0

# Loop de chaveamento
for k in range(len(t) - 1):
    t_cycle = t[k] % Ts
    # Determinar ON ou OFF
    if t_cycle < D * Ts:
        vL = Vin           # ON: tensão no indutor
    else:
        vL = Vin - vO[k]   # OFF: tensão no indutor

    # Atualizar corrente do indutor
    iL[k + 1] = iL[k] + (vL / L) * dt

    # Atualizar a tensão no capacitor
    iC = vO[k] / R
    vO[k + 1] = vO[k] + (iL[k] - iC) / C * dt

    # Plot dos resultados
plt.figure(figsize=(10, 4))
plt.plot(t * 1e3, vO, label='Tensão de Saída (vout)')
plt.axhline(Vout, color='red', linestyle='--', label=f'Média Teórica = {Vout:.1f} V')
plt.title('Tensão de saída - Conversor Boost (150 V → 350 V)')
plt.xlabel('Tempo (ms)')
plt.ylabel('Tensão (V)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
