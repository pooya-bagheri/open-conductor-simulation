# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 16:11:26 2019

@author: Pooya
"""
from datetime import datetime

#Project packages:
from InputSettings  import Input
from Simulation.MainSim import Simulation
from Simulation.CaseGen import CaseStudies
#from Database.MainDB import Database



TimeStartSim=datetime.now()
Sim=Simulation(Input)
Cases=CaseStudies(Input,Sim.GetBaseLoads(),Sim.GetLines())
'''
DB=Database(Input)

for i,conductor in enumerate(Cases.conductors):
   Sim.BreakConductor(conductor)
   for j,LoadProf in enumerate(Cases.LoadProfiles):
        Sim.ModifyLoads(LoadProf)
        result=Sim.get_result()
        DB.save_result(result)
        print('%.1 Done, Time passed: %s' % ((i*len(Cases.LoadProfiles)+j)/len(Cases.LoadProfiles)/len(Cases.conductors)*100,str(datetime.now()-TimeStartSim)))
   Sim.ResetConductors()    '''