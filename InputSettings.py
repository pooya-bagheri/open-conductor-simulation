"""
This file contains/generates the input setting data for simulation
"""

import os

Input={
       'SysID': 1, #the ID of test system that is simulated. List of IDs- 1:
       'Systems':{1:'IEEE123Nodes'}, #ID of available test systems
       'CaseStudyID':1, #Assign a unique ID to each case study on a system 
       'dir_path': os.path.dirname(os.path.realpath(__file__)), #active directory where the program is run from
       }