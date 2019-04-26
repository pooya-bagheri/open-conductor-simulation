import random
import warnings

class Conductor:
    def __init__(LineName,phase,bus1,bus2):
        self.PowerLine=LineName
        allphases=bus1.split(.)[1:] #extract phases from bus name e.g.: b.1.2 >> [1,2]
        if allphases==[]: #sometimes three phase buses are mentioned with no dot at the end, see above line
            allphases=[1,2,3]
        elif allphases != bus2.split(.)[1:]:
            warning.warn('A conductor is connected between different phases')
        self.PhaseID=allphases[phase-1]     
    def __str__(self):
        return self.PowerLine+',ph:'+self.PhaseID

class CaseStudies: #objects from this class includes the information for case studies
    def __init__(self,Input,BaseLoads,PowerLines):
        self.LoadProfiles=[[1 for _ in range(len(BaseLoads))]]
        self.conductors=[]
        for _,line in PowerLines.iterrows():
            for phase in range(1,line['N_phases']+1):
                self.conductors.append(Conductor(line['name'],phase,line[''])) #each conductor is tuple of (Powerline Name, phaseID)
        self.conductors=random.sample(self.conductors,10)    