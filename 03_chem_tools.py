"""
Packages/codes from following repos are used:
https://raw.githubusercontent.com/PatWalters/workshop/master/predictive_models/neutralize.py
https://raw.githubusercontent.com/yamasakih/docker-compose-razi/feature/customize-for-souyakuRB2018/work/souyakuRB2018/desalt.py
https://github.com/ageron/handson-ml
"""

import matplotlib.figure as figure
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import desalt
import rdkit.Chem as Chem
from sklearn import metrics
from neutralize import NeutraliseCharges
from rdkit.Chem import AllChem
from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.ML.Descriptors import MoleculeDescriptors

def evaluate_metrics(y, pre_y):
    print("mean_absolute_error:",metrics.mean_absolute_error(y, pre_y))
    print("median_absolute_error:",metrics.median_absolute_error(y, pre_y))
    print("r2_score:",metrics.r2_score(y, pre_y))
    print("mean_squared_error:",metrics.mean_squared_error(y, pre_y))

def desalt_neutralize(df_series_smiles,length=10000000,debug=False):
    desalted_smiles = []
    
    for i in df_series_smiles[0:length]:
        if debug == True:
            print(i)
        i = i +'\tname'
        desalted_smiles.append(NeutraliseCharges(desalt.desalt(i)[0])[0])
    return desalted_smiles

def generate_rdkit_descriptors(smiles_series,y_series, y_name="target"):
    descriptor_names = []
    for descriptor_information in Descriptors.descList:
        descriptor_names.append(descriptor_information[0])

    descriptor_calculator = MoleculeDescriptors.MolecularDescriptorCalculator(descriptor_names)
    descriptors = [] 

    for index, smiles_i in enumerate(smiles_series):
        molecule = Chem.MolFromSmiles(smiles_i)
        descriptors.append(descriptor_calculator.CalcDescriptors(molecule))
    descriptors = pd.DataFrame(descriptors, index=smiles_series.index, columns=descriptor_names)

    y = pd.DataFrame(y_series)  
    y.columns = [y_name]
    descriptors_with_y = pd.concat([y, descriptors], axis=1) 
    return  descriptors_with_y

def generate_ecfp4_descriptors (smiles_series, y_series, y_name ="target", fp_length=2048, fp_radius=2, bi={}):
    descriptors = []
    for i in smiles_series:
        m = Chem.MolFromSmiles(i)
        fp_string = AllChem.GetMorganFingerprintAsBitVect(m, fp_radius, nBits=fp_length, bitInfo=bi).ToBitString()
        descriptors.append(np.array(list(fp_string), dtype=int))
    
    descriptors = pd.DataFrame(descriptors, index=smiles_series.index)
     
    y = pd.DataFrame(y_series)  
    y.columns = [y_name]
    descriptors_with_y = pd.concat([y, descriptors], axis=1) 
    return  descriptors_with_y

def concatenate_chunk(df_chunk):
    chunk_list = []

    for chunk in df_chunk:
        chunk_filter = generate_ecfp4_descriptors(chunk.d_smiles, chunk.RETENTION_TIME, "rt")
        chunk_list.append(chunk_filter)
    return pd.concat(chunk_list)
