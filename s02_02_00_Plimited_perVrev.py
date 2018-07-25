'''
Created on Jul 9, 2018

@author: Keisuke
'''

from pylab import *
from Claquin2002Nlimited import *
from Claquin2002Plimited import *
from Claquin2002Llimited import *
from Claquin2002PlimitedV import *
from FigSet import *
from Savefig2 import *

rc('text', usetex=True)
rc('font', family='serif')
rc('font', serif='Times New Roman')
rcParams.update({'text.latex.preamble':['\\usepackage[greek,english]{babel}']})

d = claquin2002Pv()
dD = d.D
dNC = d.N/d.C
dSiC = d.Si/d.C
dSiN = d.Si/d.N

D =arange(0.01,1+0.01,0.01)

V = -113.18*D + 578.86 #(m3 cell-1)
Qc = -16.552*D + 25.409 #(pmol cell-1)
VsiV = 0.28 #(fmol Si um-3 d-1)
NCmin =0.03 #(molN molC)
Anc = 0.1
NCstoMax = 0.035
NC = NCmin + Anc*D + NCstoMax

Vsi = VsiV/(Qc/V)/1000 #(mol Si mol C-1 d-1)
SiC = Vsi/D
SiN = SiC/NC

Si = VsiV/D  

Xlabel = '\\textrm{\\greektext m} (d^{-1})'

figure(1)
plot(dD,dNC,'o')
plot(D,NC)
xlabel(Xlabel)
ylabel('N/C (mol/mol)')
Savefig2('Si\\Plim',1,300)

figure(2)
plot(dD,dSiC,'o')
plot(D,SiC)
xlim(0,1)
ylim(0,0.1)
xlabel(Xlabel)
ylabel('Si/C (mol/mol)')
Savefig2('Si\\Plim',2,300)

figure(3)
plot(dD,dSiN,'o')
plot(D,SiN)
ylim(0,1)
ylabel('Si/N (mol/mol)')
xlabel(Xlabel)
Savefig2('Si\\Plim',3,300)

figure(10)
plot(dD,d.Si,'o')
plot(D,Si)
ylim(0,2)
ylabel('Si (fmol/um3)')
xlabel(Xlabel)
Savefig2('Si\\Plim',10,300)

print(nanmean(d.C))
print(d.C)



show()