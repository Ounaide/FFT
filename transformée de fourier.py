from matplotlib.pyplot import *
from numpy import *
from easygui import enterbox, msgbox
from scipy.signal import unit_impulse
import sys

x=linspace(0,2*pi,1000)

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
ax2.plot(ft,label='transformée de Fourier',color='r')
ax2.set_xlabel("fréquence(Hz)")
ax2.set_ylabel("Amplitude")
ax2.set_xlim(0,100)
ft.sort()
print(ft[-1:-5])

legend()
show()
