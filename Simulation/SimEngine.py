"""
Simulation engine that employs OpenDSS API
"""
import win32com.client
from pandas import DataFrame as df

class SimEngine:
    DSSfilePaths={'IEEE123Nodes':r"\Simulation\IEEE123Bus\IEEE123Master.dss"}
    def __init__(self,SysName,dir_path): 
        #Initialize OpenDSS API as an object inside this class:
        try:
            self.DSSObj = win32com.client.Dispatch("OpenDSSEngine.DSS")
        except:
            print("Unable to start the OpenDSS Engine")
            raise SystemExit
        self.DSS=self.DSSObj.Text #Creating shortcut for entering/reading OpenDSS command/result
        self.DSSCircuit=self.DSSObj.ActiveCircuit #Creating a shortcut to access active circuit object in OpenDSS
        self.DSS.command = "Compile '"+dir_path+self.DSSfilePaths[SysName]+"'"    
    
    def GetBaseLoads(self): #extracting base load information from system model
        repeat=1
        Loads=[]
        LoadItems=self.DSSCircuit.Loads
        LoadItems.First
        while repeat: #this loop iteratively reads load information from OpenDSS object and save into 'Loads' list
            Loads.append([LoadItems.name,LoadItems.kW,LoadItems.kvar])
            repeat=LoadItems.Next
        Loads=df(Loads,columns=["Name","kW","kvar"]) #creating Pandas dataframe containing loads information
        Loads.loc[:,'LoadID']=Loads.index+1
        Loads=Loads[["LoadID","Name","kW","kvar"]] #rearranging dataframe column sequence
        return Loads
    
    def GetLines(self): #extracting powerline (conductors) information from system model
        repeat=1
        Lines=[]
        LineItems=self.DSSCircuit.Lines
        LineItems.First
        while repeat: #this loop iteratively reads powerline (conductors) information from OpenDSS object and save into 'Lines' list
            if LineItems.name[:2] !='sw':
                Lines.append([LineItems.name,LineItems.phases,LineItems.bus1,LineItems.bus2,LineItems.length])
            repeat=LineItems.Next
        Lines=df(Lines,columns=["name","N_phases","bus1","bus2","length"]) #creating Pandas dataframe containing lines information
        return Lines
        