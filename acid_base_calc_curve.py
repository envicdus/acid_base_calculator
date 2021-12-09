import math
import numpy as np
import matplotlib.pyplot as plt
import pyinputplus as pyip
#create input values

titration_title = pyip.inputStr(prompt = "What is your analyte? Please type it here: ")
analyte = pyip.inputChoice(['acid', 'base'], prompt = "what type of solution is the analyte, acid or base?: ")
#type of titration
sol_strength = pyip.inputChoice(['strong', 'weak'], prompt = "strong or weak?: ")
#strength of solution
titrant_conc = pyip.inputFloat(prompt = "titrant concentration in millimolar: ", min = 0, lessThan = 10 )
analyte_conc = pyip.inputFloat(prompt = "analyte concentration in millimolar: ", min = 0, lessThan = 10 )
analyte_vol = pyip.inputFloat(prompt = "analyte volume in mL: ", min = 0, lessThan = 100 )
#inputs for values needed in calculating titration

if sol_strength == "weak":
    if analyte == "acid":
        print("What is the Ka value of the acid?")
    if analyte == "base":
        print("What is the Ka value of the base?")
    K = pyip.inputFloat(prompt = "please enter Ka value ex. 6.9e-6: ", min = 0, lessThan = 2 )
    # input values for dissociation constants
tit_range = pyip.inputFloat(prompt = "What is the maximum range of the titration curve?: ", min = 0)
titrant_vol = 0
x_volume = []
y_pH = []
    
#computation part
while titrant_vol <= tit_range:
    if True:
        if sol_strength == "strong":
            #when acid is greater than the base
            molcompare = (((analyte_vol)*analyte_conc) - ((titrant_vol)*titrant_conc))
            if molcompare > 0:
                Logcon = (np.log10((molcompare)/((analyte_vol + titrant_vol)))) * (-1)
                
            #at equivalence point
            if molcompare == 0:
                Logcon = 7.00
                print(f"titrant volume at equivalence point: {titrant_vol}")

            #after equivalence point
            if molcompare < 0:
                Hcon = (-1*molcompare)/((analyte_vol + titrant_vol))
                LogHcon = -np.log10(Hcon)
                Logcon = 14 - LogHcon
                

                
        if sol_strength == "weak": #<--edit later
            #at volume = 0, this is already correct
            molcompare = (((analyte_vol)*analyte_conc) - ((titrant_vol)*titrant_conc))
            if molcompare == ((analyte_vol)*analyte_conc):
                Logcon = -np.log10(np.sqrt(K*analyte_conc))
                #after addition of titrant, before equivalence point
            if molcompare > 0 and titrant_vol > 0:
                HAcon = float((molcompare)/((analyte_vol + titrant_vol)))
                Acon = float(((titrant_conc * titrant_vol))/((analyte_vol + titrant_vol)))
                Logcon = -np.log10((K * HAcon)/ Acon)
                
            #at equivalence point
            if molcompare == 0:
                con_A = (titrant_conc*titrant_vol)/(analyte_vol + titrant_vol)
                log_OH = -math.log(np.sqrt((((1e-14) * con_A)/K)), 10)
                Logcon = 14 - log_OH

            #after equivalence point (correct computations)
            if molcompare < 0:
                Hcon = (-1*molcompare)/((analyte_vol + titrant_vol))
                OHcon = -np.log10(Hcon)
                Logcon = 14 - OHcon
        if analyte == "base":
            Logcon = 14 - Logcon
        x_volume.append(titrant_vol)
        y_pH.append(Logcon)
        titrant_vol += 0.25

a = np.array([x_volume, y_pH], dtype=float)
b = np.transpose(a)

fig = plt.figure(figsize=[15,8])
plt.plot(x_volume,y_pH)
plt.xlabel(f"$mL$ of {titration_title}", fontsize = 18)
plt.ylabel("pH", fontsize = 18)
plt.title(label= f"Titration curve of {titration_title}", fontsize = 24)
plt.show()
