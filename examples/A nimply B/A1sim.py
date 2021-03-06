import numpy as np
from subsbml import *

cell = System('cell')
cell.ListOfSharedResources = ['RNAP','Ribo','ATP']

# A1 - promoter sig28 -tetO - utr1 - deGFP
# A1 - pLac - utr1 - sigma28 (constituitively expressed protein sigma28 - input plasmid)
A1 = cell.createSubsystem('models/A1.xml','A1')
# SBML model gets converted to Level 3 Version 1
libsbml.writeSBML(A1.getSBMLDocument(),'models/A1converted.xml')
# Simulate using bioscrape
timepoints = np.linspace(0,14*60*6000,1000)

A1.plotBioscrape(['protein deGFP*','protein sigma28'],timepoints)
