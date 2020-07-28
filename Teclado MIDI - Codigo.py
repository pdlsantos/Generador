import pyo
import numpy as np
import pygame
import time, sys

#### Clase Para el Teclado ###
class Tone:
    def __init__(self, Freq):
        self.Freq = Freq
        self.song = None
        self.estado = False
    def tocar(self):
        self.song = pyo.Sine(freq = self.Freq, mul = 0.5).out()
    def notocar(self):
        self.song = pyo.Sine(freq = self.Freq, mul = 0.5)

### Función para colorear ###
def pintar(newPianoState):
        for x in range(0,  nxC):
            for z in range(0, nyC):
            
                poly = [((x)   * dimCW, (z) * dimCH),
                        ((x+1) * dimCW, (z) * dimCH),
                        ((x+1) * dimCW, (z+1) * dimCH),
                        ((x)   * dimCW, (z+1) * dimCH)]
                    
                if newPianoState[x,z] == 1:
                    pygame.draw.polygon(screen, [71, 231, 226], poly,0)
                if newPianoState[x,z] == 0:
                    pygame.draw.polygon(screen, [255,255,255], poly,0)
                if newPianoState[x,z] == 2:
                    pygame.draw.polygon(screen, [25,25,25], poly,0)

### Inicia la ventana ###
pygame.init()

### Configurar la Pantalla ###
width, height = 400, 2000
screen = pygame.display.set_mode((400, 400))

pygame.display.set_caption("Teclado MIDI")

bg  = 255, 255, 255
screen.fill(bg)
nxC, nyC = 96, 96
dimCW = width / nxC
dimCH = height / nyC
newPianoState = np.zeros((nxC,nyC))

### Inicia el Servidor para reproducir sonidos ###
s = pyo.Server().boot()
s.amp= 1
s.start()

### Asigno un tono a cada tecla ###
letras = "asdfghjklwetyuop"
frecuencias = [261.626, 293.665, 329.628, 
               349.228, 391.995,  440.000, 
               493.883,  523.251, 587.330, 
               277.183, 311.127, 369.994, 
               415.305, 466.164, 554.365, 
               622.254]
tono = dict(zip(letras, [Tone(f) for f in frecuencias]))    

### Inicia el bucle principal ###
salir = False
while not salir:
       
    screen.fill(bg)
    ev =  pygame.event.get()
    
    ### Se fija siempre si se presiono el botón la Cruz ###
    
    for e in ev:
        
        if e.type == pygame.QUIT:
            salir = True
            break
        
    ### Configura cómo va a reaccionar el juego al presionar una tecla ###
    
    if pygame.key.get_pressed()[pygame.K_a] and not tono["a"].estado:   # Si se presiona "a" y el "tono a" no está activo
        tono["a"].tocar()                                                                       # Hace sonar el tono correspondiente a "a"
        tono["a"].estado = True                                                             # Cambia el estado del "tono a" a activo
        newPianoState[0:6,:], newPianoState[6:11,11:] = 1, 1                  # Cambia el color de la tecla del teclado correspondiente a "a" a celeste
        
    elif tono["a"].estado and pygame.key.get_pressed()[pygame.K_a]:      # Si el "tono a" está activo y "a" está presionada
        newPianoState[0:6,:], newPianoState[6:11,11:] = 0, 0                  # Cambia el color de la tecla del teclado correspondiente a "a" a blanco
        
    else:                                                                                            # Si el "tono a" está inactivo y "a" no está presionado
        tono["a"].notocar()                                                                   # Apaga el sonido del "tono a" 
        tono["a"].estado = False                                                            # Cambia el estado del "tono a" a inactivo
        newPianoState[0:6,:], newPianoState[6:11,11:] = 0, 0                  # Cambia el color de la tecla del teclado correspondiente a "a" a blanco
    
    if pygame.key.get_pressed()[pygame.K_s] and not tono["s"].estado:
        tono["s"].tocar()
        tono["s"].estado = True
        newPianoState[11:21,11:] = 1
        
    elif tono["s"].estado and pygame.key.get_pressed()[pygame.K_s]:
        newPianoState[11:21,11:] = 0

    else:
        tono["s"].notocar()
        tono["s"].estado = False
        newPianoState[11:21,11:] = 0
        
    if pygame.key.get_pressed()[pygame.K_d] and not tono["d"].estado:
        tono["d"].tocar()
        tono["d"].estado = True
        newPianoState[21:26,11:], newPianoState[26:31,:] = 1, 1
        
    elif tono["d"].estado and pygame.key.get_pressed()[pygame.K_d]:
        newPianoState[21:26,11:],  newPianoState[26:31,:] = 0, 0
        
    else:
        tono["d"].notocar()
        tono["d"].estado = False
        newPianoState[21:26,11:],  newPianoState[26:31,:] = 0, 0
    
    if pygame.key.get_pressed()[pygame.K_f] and not tono["f"].estado:
        tono["f"].tocar()
        tono["f"].estado = True
        newPianoState[31:36,:],  newPianoState[36:41,11:] = 1,  1
        
    elif tono["f"].estado and pygame.key.get_pressed()[pygame.K_f]:
        newPianoState[31:36,:], newPianoState[36:41,11:] = 0, 0
        
    else:
        tono["f"].notocar()
        tono["f"].estado = False
        newPianoState[31:36,:], newPianoState[36:41,11:] = 0, 0
    
    if pygame.key.get_pressed()[pygame.K_g] and not tono["g"].estado:
        tono["g"].tocar()
        tono["g"].estado= True
        newPianoState[41:51,11:] = 1
        
    elif tono["g"].estado and pygame.key.get_pressed()[pygame.K_g]:
        newPianoState[41:51,11:] = 0
    
    else:
        tono["g"].notocar()
        tono["g"].estado = False
        newPianoState[41:51,11:] = 0
    
    if pygame.key.get_pressed()[pygame.K_h] and not tono["h"].estado:
        tono["h"].tocar()
        tono["h"].estado = True
        newPianoState[51:61,11:] = 1
        
    elif tono["h"].estado and pygame.key.get_pressed()[pygame.K_h]:
        newPianoState[51:61,11:] = 0
        
    else:
        tono["h"].notocar()
        tono["h"].estado = False
        newPianoState[51:61,11:] = 0
        
    if pygame.key.get_pressed()[pygame.K_j] and not tono["j"].estado:
        tono["j"].tocar()
        tono["j"].estado = True
        newPianoState[66:71,:],  newPianoState[61:66,11:] = 1, 1
        
    elif tono["j"].estado and pygame.key.get_pressed()[pygame.K_j]:
        newPianoState[66:71,:],  newPianoState[61:66,11:] = 0, 0
        
    else:
        tono["j"].notocar()
        tono["j"].estado = False
        newPianoState[66:71,:], newPianoState[61:66,11:] = 0, 0
        
    if pygame.key.get_pressed()[pygame.K_k] and not tono["k"].estado:
        tono["k"].tocar()
        tono["k"].estado = True
        newPianoState[71:76,:], newPianoState[76:81,11:] = 1,  1
        
    elif tono["k"].estado and pygame.key.get_pressed()[pygame.K_k]:
        newPianoState[71:76,:], newPianoState[76:81,11:] = 0, 0
        
    else:
        tono["k"].notocar()
        tono["k"].estado = False
        newPianoState[71:76,:], newPianoState[76:81,11:] = 0, 0
        
    if pygame.key.get_pressed()[pygame.K_l] and not tono["l"].estado:
        tono["l"].tocar()
        tono["l"].estado = True
        newPianoState[81:91,11:] = 1
        
    elif tono["l"].estado and pygame.key.get_pressed()[pygame.K_l]:
        newPianoState[81:91,11:] = 0
        
    else:
        tono["l"].notocar()
        tono["l"].estado = False
        newPianoState[81:91,11:] = 0
        
    if pygame.key.get_pressed()[pygame.K_w] and not tono["w"].estado:
        tono["w"].tocar()
        tono["w"].estado = True
        newPianoState[6:16,:11] = 1
        
    elif tono["w"].estado and pygame.key.get_pressed()[pygame.K_w]:
        newPianoState[6:16,:11] = 2
        
    else:
        tono["w"].notocar()
        tono["w"].estado = False
        newPianoState[6:16,:11] = 2
        
    if pygame.key.get_pressed()[pygame.K_e] and not tono["e"].estado:
        tono["e"].tocar()
        tono["e"].estado = True
        newPianoState[16:26,:11] = 1
        
    elif tono["e"].estado and pygame.key.get_pressed()[pygame.K_e]:
        newPianoState[16:26,:11] = 2
        
    else:
        tono["e"].notocar()
        tono["e"].estado = False
        newPianoState[16:26,:11] = 2
        
    if pygame.key.get_pressed()[pygame.K_t] and not tono["t"].estado:
        tono["t"].tocar()
        tono["t"].estado = True
        newPianoState[36:46,:11] = 1
        
    elif tono["t"].estado and pygame.key.get_pressed()[pygame.K_t]:
        newPianoState[36:46,:11] = 2
        
    else:
        tono["t"].notocar()
        tono["t"].estado = False
        newPianoState[36:46,:11] = 2
        
    if pygame.key.get_pressed()[pygame.K_y] and not tono["y"].estado:
        tono["y"].tocar()
        tono["y"].estado = True
        newPianoState[46:56,:11] = 1
        
    elif tono["y"].estado and pygame.key.get_pressed()[pygame.K_y]:
        newPianoState[46:56,:11] = 2
        
    else:
        tono["y"].notocar()
        tono["y"].estado = False
        newPianoState[46:56,:11] = 2
        
    if pygame.key.get_pressed()[pygame.K_u] and not tono["u"].estado:
        tono["u"].tocar()
        tono["u"].estado = True
        newPianoState[56:66,:11] = 1
        
    elif tono["u"].estado and pygame.key.get_pressed()[pygame.K_u]:
        newPianoState[56:66,:11] = 2
        
    else:
        tono["u"].notocar()
        tono["u"].estado = False
        newPianoState[56:66,:11] = 2
        
    if pygame.key.get_pressed()[pygame.K_o] and not tono["o"].estado:
        tono["o"].tocar()
        tono["o"].estado = True
        newPianoState[76:86,:11] = 1
        
    elif tono["o"].estado and pygame.key.get_pressed()[pygame.K_o]:
        newPianoState[76:86,:11] = 2
        
    else:
        tono["o"].notocar()
        tono["o"].estado = False
        newPianoState[76:86,:11] = 2
        
    if pygame.key.get_pressed()[pygame.K_p] and not tono["p"].estado:
        tono["p"].tocar()
        tono["p"].estado = True
        newPianoState[86:96,:11] = 1
        
    elif tono["p"].estado and pygame.key.get_pressed()[pygame.K_p]:
        newPianoState[86:96,:11] = 2
        
    else:
        tono["p"].notocar()
        tono["p"].estado = False
        newPianoState[86:96,:11] = 2
    
    ### pinta el tablero segun lo que paso en esta vuelta ###    
    pintar(newPianoState)
    
    ### Para que la transición sea prolija ###            
    time.sleep(0.05)
    pygame.display.flip()

### Terminar los procesos ###    
s.stop()
pygame.quit()
sys.exit()
