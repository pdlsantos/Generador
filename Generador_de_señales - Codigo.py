import pyo as p
import sys

def nombredeltipo(x):
    if x == 0:
        return "Default"
    elif x== 1:
        return "Saw Down"
    elif x == 2:
        return "Onda Cuadrada"
    elif x == 3:
        return "Onda Triangular"
    elif x == 4:
        return "Pulsante"
    elif x == 5:
        return "Pulsante Bipolar"
    elif x == 6:
        return "Muestra sostenida"
    elif x == 7:
        return "Señal Modulada"


def bienvenida():
    print("Generador de Señales - Experiencia Virtual\n")
    print("Ingrese El Tipo de señal a generar\n 0 default"+\
          " \n 1 Saw Down"+ \
          " \n 2 Onda Cuadrada"+\
          " \n 3 Onda Triangular"+\
          " \n 4 Pulsante \n 5 Pulsante Bipolar"+\
          " \n 6 Aleatoria \n 7 Modulada")
    opcion1 = input()
    return opcion1
    
def osc(type, freq=100, mul=0.5,sharp = 0.5):
    osc = p.LFO(freq,sharp, type)
    return osc.out(chnl = [0, 1])

ele = bienvenida()

print("\n¿Graficar con opciones avanzadas? 1 /  [0]")
mas = input()
if mas == 1:
    print("\nFrecuencia de la señal\t")
    fe = input()
    print("\nFactor de Forma de la señal (Varia entre 0 y 1) \t")
    sh = input()
    print("\nFactor de escala de la señal (default 0.5) \t")
    es =  input()
    print("\nGenerando gráficas de "+nombredeltipo(ele))
    s = p.Server(nchnls=2).boot()
    actual = osc(ele,fe,sh,es)
    actual.ctrl()
else:
    print("\nGenerando gráficas de "+ str(nombredeltipo(ele)))
    s = p.Server(nchnls=2).boot()
    actual = osc(int(ele))
    actual.ctrl()


s.amp = 1   
scc = p.Scope(actual,wintitle= "Osciloscopio / Generador de Señales")
sp = p.Spectrum(actual,wintitle = "FFT / Generador de Señales")
s.gui()
sys.exit()