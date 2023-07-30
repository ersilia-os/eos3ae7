# imports
import os
#Set backend to TensorFlow
os.environ['KERAS_BACKEND'] = 'tensorflow'

import csv
import pandas as pd
import sys
from rdkit import RDLogger
from chemvae.vae_utils import VAEUtils
from chemvae import mol_utils as mu
import time

#Load model
vae = VAEUtils()

#Turn off RDKit Warnings
RDLogger.DisableLog('rdApp.*')

#Parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

#Read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    smiles_list = [r[0] for r in reader]

#Sampling approach - For every molecule, generate n molecules by doing a noise parameter sweep
noise_list = [i for i in range(5, 20)] #Stop at 19 because average distance between molecules is 19.66
smi_gen_dict = {smi: [[]] for smi in smiles_list}
num_molecules_gen = 20
MAX_ITER = 5 #To avoid infinite loop

for smi in smiles_list:
    iteration = 0
    while(len(smi_gen_dict[smi][0]) < num_molecules_gen) and (iteration < MAX_ITER):
        for i in range(len(noise_list)):
            smi_canon = mu.canon_smiles(smi)
            smi_X = vae.smiles_to_hot(smi_canon, canonize_smiles=True)
            smi_z = vae.encode(smi_X)
            df = vae.z_to_smiles(smi_z, decode_attempts=250, noise_norm=noise_list[i])
            smi_gen_dict[smi][0] += df.smiles.values.tolist()
            smi_gen_dict[smi][0] = list(set(smi_gen_dict[smi][0])) #Avoid repeat molecules
        iteration += 1
        
#Write output in a .csv file
output_df = pd.DataFrame.from_dict(smi_gen_dict, orient='index', columns=["generated_molecules"])
output_df = output_df.reset_index().rename(columns={"index":"smiles"})
output_df.to_csv(output_file)