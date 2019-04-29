import random
import warnings

class Conductor: #object of this class are single-phase conductors of the powerlines
    def __init__(self,LineName,phase,bus1,bus2):
        if LineName==None:
            self.PowerLine=""
            self.PhaseID=""
            return None
        self.PowerLine=LineName
        allphases=bus1.split('.')[1:] #extract phases from bus name e.g.: b.1.2 >> [1,2]
        if allphases==[]: #sometimes three phase buses are mentioned with no dot at the end, see above line
            allphases=[1,2,3]
        elif allphases != bus2.split('.')[1:]:
            warnings.warn('A conductor is connected between different phases')
        self.PhaseID=allphases[phase]     
    def __str__(self):
        return 'Line:'+self.PowerLine+',ph:'+self.PhaseID

class CaseStudies: #objects from this class includes the information for case studies
    def __init__(self,Input,BaseLoads,PowerLines):
        self.LoadProfiles=[[1 for _ in range(len(BaseLoads))]]
        self.conductors=[] 
        for _,line in PowerLines.iterrows():
            for phase in range(line['N_phases']):
                self.conductors.append(Conductor(line['name'],phase,line['bus1'],line['bus2'])) #creates condocutors using above defined Conductors class
        self.conductors=random.sample(self.conductors,10)  
        self.conductors=[Conductor(None,None,None,None)]+self.conductors #adding the case representing normal situation where no conductor is broken
    def CompltedPerc(self,i,j): #returns percentage of completed case studies
        return (i*len(self.LoadProfiles)+j)/len(self.LoadProfiles)/len(self.conductors)*100