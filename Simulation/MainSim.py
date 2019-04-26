
"""
Sim
"""

from Simulation.SimEngine import SimEngine

class Simulation: #Takes care of simulations using OpenDSS API
    def __init__(self,Input):
        self.__SysName=Input['Systems'][Input['SysID']]
        self.__Engine=SimEngine(self.__SysName,Input['dir_path']) #initialize simulation engine
        self.__BaseLoads=self.__Engine.GetBaseLoads()
        self.__PowerLines=self.__Engine.GetLines()
        
    def GetLines(self):
        return self.__PowerLines
    def GetBaseLoads(self):
        return self.__BaseLoads
    def GetSysName(self):
        return self.__SysName
  