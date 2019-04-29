"""

@author: Pooya
"""

#Importing Project packages:
from InputSettings  import Input
from Simulation.MainSim import Simulation
from Simulation.CaseGen import CaseStudies
from Database.MainDB import Database




Sim=Simulation(Input)
Cases=CaseStudies(Input,Sim.GetBaseLoads(),Sim.GetLines())
DB=Database(Input,Sim.GetBaseLoads())
'''
for i,conductor in enumerate(Cases.conductors):
   Sim.BreakConductor(conductor)
   for j,LoadProf in enumerate(Cases.LoadProfiles):
        Sim.ModifyLoads(LoadProf)
        DB.save_result(Sim.get_result())
        print('%.1f%% Done, Time passed: %s' % (Cases.CompltedPerc(i,j),Sim.GetElapsedTime()))
   Sim.ResetConductors()    
print(DB) #gives the information on created DB from simulation results   
   '''