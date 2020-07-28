import pyo
import sys
import wx

def bienvenida():
    print("Generador de Señales - Experiencia Virtual\n")
    print("Amplitude  -> varia la aimplitud, en dB")
    print("\nfreq  -> varia la frecuencia, en Hz")
    print("Sharp  -> cambia la suavidad de la onda")
    print("Tipos de señales \n 0 default"+\
          " \n 1 Saw Down"+ \
          " \n 2 Onda Cuadrada"+\
          " \n 3 Onda Triangular"+\
          " \n 4 Pulsante \n 5 Pulsante Bipolar"+\
          " \n 6 Aleatoria \n 7 Modulada\n")
    print("mul   -> es un facto de amplitudd")   
bienvenida()
s = pyo.Server(nchnls=2).boot()
actual = pyo.LFO().out(chnl = [0, 1])
actual.ctrl()
s.amp = 1   

scc = pyo.Scope(actual,wintitle= "Osciloscopio / Generador de Señales")
sp = pyo.Spectrum(actual,wintitle = "FFT / Generador de Señales")
s.gui(locals())
s.stop()
sys.exit()