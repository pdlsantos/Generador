from pyo import *
import numpy as np
import pygame
import time, sys

pygame.init()

width,height = 400, 2000
screen = pygame.display.set_mode((400, 400))

pygame.display.set_caption("Piano para expe")

bg  = 255, 255, 255
screen.fill(bg)

nxC, nyC = 96, 96

dimCW = width / nxC
dimCH = height / nyC

pianoState = np.zeros((nxC,nyC))
pianoState[6:16,:11] = 2
pianoState[16:26,:11] = 2
pianoState[36:46,:11] = 2
pianoState[46:56,:11] = 2
pianoState[56:66,:11] = 2
pianoState[76:86,:11] = 2
pianoState[86:96,:11] = 2

salir = False
pauseExect = False
s = Server().boot()
s.amp= 0.5
s.start()
i=1
a_e, s_e, w_e, e_e, d_e, f_e, t_e, y_e, u_e, g_e,\
h_e, j_e, k_e, l_e, o_e, p_e=False, False, False, False, \
False, False, False, False, False, False, False, False, \
False, False, False, False

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
    
while not salir:
    
    newPianoState = np.copy(pianoState)
    
    screen.fill(bg)
    ev =  pygame.event.get()
    for e in ev:
        
        if e.type == pygame.QUIT:
            salir = True
            break
        
        MouseClick = pygame.mouse.get_pressed()
        
        if sum(MouseClick) > 0:
            i=i+1
            
    if pygame.key.get_pressed()[pygame.K_a] and not a_e:
        a=Sine(freq = 261.626, mul = 1).out()
        a_e = True
        newPianoState[0:6,:] = 1
        newPianoState[6:11,11:] = 1
        
    elif a_e and pygame.key.get_pressed()[pygame.K_a]:
        newPianoState[0:6,:] = 0
        newPianoState[6:11,11:] = 0
    else:
        a=Sine(freq = 261.626, mul = 0.5)
        a_e=False
        newPianoState[0:6,:] = 0
        newPianoState[6:11,11:] = 0
    
    if pygame.key.get_pressed()[pygame.K_s] and not s_e:
        ss=Sine(freq = 293.665, mul = 1).out()
        s_e = True
        newPianoState[11:21,11:] = 1
        
    elif s_e and pygame.key.get_pressed()[pygame.K_s]:
        newPianoState[11:21,11:] = 0

    else:
        ss=Sine(freq = 261.626, mul = 0.5)
        s_e=False
        newPianoState[11:21,11:] = 0
        
    if pygame.key.get_pressed()[pygame.K_d] and not d_e:
        d=Sine(freq = 329.628, mul = 1).out()
        d_e = True
        newPianoState[21:26,11:] = 1
        newPianoState[26:31,:] = 1
        
    elif d_e and pygame.key.get_pressed()[pygame.K_d]:
        newPianoState[21:26,11:] = 0
        newPianoState[26:31,:] = 0
        
    else:
        d=Sine(freq = 261.626, mul = 0.5)
        d_e=False
        newPianoState[21:26,11:] = 0
        newPianoState[26:31,:] = 0
    
    if pygame.key.get_pressed()[pygame.K_f] and not f_e:
        f=Sine(freq = 349.228, mul = 1).out()
        f_e = True
        newPianoState[31:36,:] = 1
        newPianoState[36:41,11:] = 1
    elif f_e and pygame.key.get_pressed()[pygame.K_f]:
        newPianoState[31:36,:] = 0
        newPianoState[36:41,11:] = 0
    else:
        f=Sine(freq = 261.626, mul = 0.5)
        f_e=False
        newPianoState[31:36,:] = 0
        newPianoState[36:41,11:] = 0
    
    if pygame.key.get_pressed()[pygame.K_g] and not g_e:
        g=Sine(freq = 391.995, mul = 1).out()
        g_e = True
        newPianoState[41:51,11:] = 1
    elif g_e and pygame.key.get_pressed()[pygame.K_g]:
        newPianoState[41:51,11:] = 0
    else:
        g=Sine(freq = 391.995, mul = 0.5)
        g_e=False
        newPianoState[41:51,11:] = 0
    
    if pygame.key.get_pressed()[pygame.K_h] and not h_e:
        h=Sine(freq = 440.000, mul = 1).out()
        h_e = True
        newPianoState[51:61,11:] = 1
    elif h_e and pygame.key.get_pressed()[pygame.K_h]:
        newPianoState[51:61,11:] = 0
    else:
        h=Sine(freq = 261.626, mul = 0.5)
        h_e=False
        newPianoState[51:61,11:] = 0
        
    if pygame.key.get_pressed()[pygame.K_j] and not j_e:
        j=Sine(freq = 493.883, mul = 1).out()
        j_e = True
        newPianoState[66:71,:] = 1
        newPianoState[61:66,11:] = 1
        
    elif j_e and pygame.key.get_pressed()[pygame.K_j]:
        newPianoState[66:71,:] = 0
        newPianoState[61:66,11:] = 0
        
    else:
        j=Sine(freq = 261.626, mul = 0.5)
        j_e=False
        newPianoState[66:71,:] = 0
        newPianoState[61:66,11:] = 0
        
    if pygame.key.get_pressed()[pygame.K_k] and not k_e:
        k=Sine(freq = 523.251, mul = 1).out()
        k_e = True
        newPianoState[71:76,:] = 1
        newPianoState[76:81,11:] = 1
    elif k_e and pygame.key.get_pressed()[pygame.K_k]:
        newPianoState[71:76,:] = 0
        newPianoState[76:81,11:] = 0
    else:
        k=Sine(freq = 261.626, mul = 0.5)
        k_e=False
        newPianoState[71:76,:] = 0
        newPianoState[76:81,11:] = 0
        
    if pygame.key.get_pressed()[pygame.K_l] and not l_e:
        l=Sine(freq = 587.330, mul = 1).out()
        l_e = True
        newPianoState[81:91,11:] = 1
    elif l_e and pygame.key.get_pressed()[pygame.K_l]:
        newPianoState[81:91,11:] = 0
    else:
        l=Sine(freq = 261.626, mul = 0.5)
        l_e=False
        newPianoState[81:91,11:] = 0
        
    if pygame.key.get_pressed()[pygame.K_w] and not w_e:
        w=Sine(freq = 277.183, mul = 1).out()
        w_e = True
        newPianoState[6:16,:11] = 1
    elif w_e and pygame.key.get_pressed()[pygame.K_w]:
        newPianoState[6:16,:11] = 2
    else:
        w=Sine(freq = 261.626, mul = 0.5)
        w_e=False
        newPianoState[6:16,:11] = 2
        
    if pygame.key.get_pressed()[pygame.K_e] and not e_e:
        e=Sine(freq = 311.127, mul = 1).out()
        e_e = True
        newPianoState[16:26,:11] = 1
    elif e_e and pygame.key.get_pressed()[pygame.K_e]:
        newPianoState[16:26,:11] = 2
    else:
        e=Sine(freq = 261.626, mul = 0.5)
        e_e=False
        newPianoState[16:26,:11] = 2
        
    if pygame.key.get_pressed()[pygame.K_t] and not t_e:
        t=Sine(freq = 369.994, mul = 1).out()
        t_e = True
        newPianoState[36:46,:11] = 1
    elif t_e and pygame.key.get_pressed()[pygame.K_t]:
        newPianoState[36:46,:11] = 2
    else:
        t=Sine(freq = 261.626, mul = 0.5)
        t_e=False
        newPianoState[36:46,:11] = 2
        
    if pygame.key.get_pressed()[pygame.K_y] and not y_e:
        y=Sine(freq = 415.305, mul = 1).out()
        y_e = True
        newPianoState[46:56,:11] = 1
    elif y_e and pygame.key.get_pressed()[pygame.K_y]:
        newPianoState[46:56,:11] = 2
    else:
        y=Sine(freq = 261.626, mul = 0.5)
        y_e = False
        newPianoState[46:56,:11] = 2
        
    if pygame.key.get_pressed()[pygame.K_u] and not u_e:
        u=Sine(freq = 466.164, mul = 1).out()
        u_e = True
        newPianoState[56:66,:11] = 1
    elif u_e and pygame.key.get_pressed()[pygame.K_u]:
        newPianoState[56:66,:11] = 2
    else:
        u=Sine(freq = 261.626, mul = 0.5)
        u_e=False
        newPianoState[56:66,:11] = 2
        
    if pygame.key.get_pressed()[pygame.K_o] and not o_e:
        o=Sine(freq = 369.994, mul = 1).out()
        o_e = True
        newPianoState[76:86,:11] = 1
    elif o_e and pygame.key.get_pressed()[pygame.K_o]:
        newPianoState[76:86,:11] = 2
    else:
        o=Sine(freq = 554.365, mul = 0.5)
        o_e=False
        newPianoState[76:86,:11] = 2
        
    if pygame.key.get_pressed()[pygame.K_p] and not p_e:
        p=Sine(freq = 622.254, mul = 1).out()
        p_e = True
        newPianoState[86:96,:11] = 1
    elif p_e and pygame.key.get_pressed()[pygame.K_p]:
        newPianoState[86:96,:11] = 2
    else:
        p=Sine(freq = 261.626, mul = 0.5)
        newPianoState[86:96,:11] = 2
        p_e=False
       
    pintar(newPianoState)
                
    time.sleep(0.05)
    pianoState  = np.copy(newPianoState)
    pygame.display.flip()
s.stop()
pygame.quit()
sys.exit()
