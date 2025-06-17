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

# Tempo de simulação: 5 ms para ver o amortecimento
t_end = 5e-3       # 5 ms
dt = Ts / 200      # subdividindo cada período em 200 passos
t = np.arange(0, t_end, dt)

# Vetores de simulação
iL = np.zeros_like(t)     # Corrente do indutor
vO = np.zeros_like(t)   # Tensão do capacitor/saída




