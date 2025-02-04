import re
import numpy as np
finp1=open("SO_1.out","r")

EnergyRegex = re.compile(r'FINAL SINGLE POINT ENERGY\s+(-\d+.\d+)')
energylist1 = EnergyRegex.findall(finp1.read())
energylist1=list(np.float_(energylist1))

finp1.close()

finp2=open("SO_2.out","r")

EnergyRegex = re.compile(r'FINAL SINGLE POINT ENERGY\s+(-\d+.\d+)')
energylist2 = EnergyRegex.findall(finp2.read())
energylist2=list(np.float_(energylist2))

finp2.close()


finp3=open("SO_3.out","r")

EnergyRegex = re.compile(r'FINAL SINGLE POINT ENERGY\s+(-\d+.\d+)')
energylist3 = EnergyRegex.findall(finp3.read())
energylist3=list(np.float_(energylist3))

finp3.close()

energylist = energylist1 + energylist2 + energylist3

#Conversion of energies from Hartree to kJ/mol
#1 Eh = 0.000 380 88 kJ/mol
energylist = 3.8088*10**(-4.0)*np.array(energylist)


#Calculate energies relative to minimum
minim = min(energylist)
energylist=energylist-minim

#Print energies to file 
fenergies = open("energies.txt","w")
fenergies.write(str(energylist))
fenergies.close()
