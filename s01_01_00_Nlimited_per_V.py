'''
Created on Jul 9, 2018

@author: Keisuke
'''

from pylab import *
from Claquin2002Nlimited import *
from Claquin2002Plimited import *
from Claquin2002Llimited import *
from Claquin2002NlimitedV import *
from FigSet import *
from Savefig2 import *

#rcParams.update({'text.usetex':True})   #to call real latex
#rcParams.update({'text.latex.preamble':['\\usepackage[greek,english]{babel}']})
#rcParams.update({'font.serif': 'Times New Roman'})
rc('text', usetex=True)
rc('font', family='serif')
rc('font', serif='Times New Roman')
rcParams.update({'text.latex.preamble':['\\usepackage[greek,english]{babel}']})

d = claquin2002Nv()
dD = d.D
dNC = d.N/d.C
dSiC = d.Si/d.C
dSiN = d.Si/d.N

D =arange(0.01,1+0.01,0.01)
V = -89.465*D + 560.95 #(um3)
Qc = -2.3549*D + 10.256 #(pmol cell-1)

NCmin =0.03 #(molN molC)
Anc = 0.1
NC = NCmin + Anc*D

VsiV = 0.28#(fmol Si um-3 s-1)
Vsi = VsiV/(Qc/V)/1000  #(mol Si molC s-1)
SiC = Vsi/D
SiN = SiC/NC
SiV = VsiV/D

Xlabel = '\\textrm{\\greektext m} (d^{-1})'

figure(1)
plot(dD,dNC,'o')
plot(D,NC)
xlabel(Xlabel)
ylabel('N/C (mol/mol)')
Savefig2('Si\\Nlim',1,300)

figure(2)
plot(dD,dSiC,'o')
plot(D,SiC)
xlim(0,1)
ylim(0,0.2)
xlabel(Xlabel)
ylabel('Si/C (mol/mol)')
Savefig2('Si\\Nlim',2,300)

figure(3)
plot(dD,dSiN,'o')
plot(D,SiN)
ylim(0,5)
ylabel('Si/N (mol/mol)')
xlabel(Xlabel)
Savefig2('Si\\Nlim',3,300)

figure(10)
plot(dD,d.Si,'o')
plot(D,SiV)
ylim(0,2)
ylabel('Si (fmol/um3)')
xlabel(Xlabel)
Savefig2('Si\\Nlim',10,300)

print(nanmean(d.C))
print(d.C)



show()