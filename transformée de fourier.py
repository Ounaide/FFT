from matplotlib.pyplot import figure,legend,show
from numpy import *
from easygui import enterbox, msgbox
from scipy.signal import *
import sys

pas=1000
x=linspace(0,2*pi,pas)

def enter():   
    try:
        global y
        global sy
        sy=enterbox("Fonction y(x):")
        y=eval(sy)
    except:
        if sy!=None:
            msgbox("Erreur de syntaxe")
            enter()
        else:
            sys.exit()
    return y,sy

enter()
ft=fft.fft(y)

f=figure('transformée de fourier')
ax1=f.add_subplot(211)
ax1.plot(x,y,label=f'fonction: {sy}')
ax1.set_xlabel("t(s)")
ax1.set_ylabel("signal")
legend()

ax2=f.add_subplot(212)
ax2.plot(abs(ft)/max(ft.imag),label='transformée de Fourier',color='r')
ax2.set_xlabel("fréquence(Hz)")
ax2.set_ylabel("|A|")
ax2.set_xlim(0,pas/2)
legend()

show()
