import torch
import pickle
from rdkit import Chem
from rdkit.Chem import AllChem

# 定义pkl文件路径和输出pdb文件路径
pkl_file_path = '/home/gaotianyu/GeoDiff-main/logs/qm9_default_2024_04_01__02_57_20/sample_2024_04_08__01_45_45/samples_0.pkl'
pdb_file_prefix = '/home/gaotianyu/GeoDiff-main/PDB/output.pdb'

# 读取pkl文件
with open(pkl_file_path, 'rb') as file:
    data_list = pickle.load(file)

for i, data in enumerate(data_list):
    mol = data.rdmol

    AllChem.EmbedMolecule(mol)

    AllChem.UFFOptimizeMolecule(mol)
    
    pdb_file_path = f'{pdb_file_prefix}_{i}.pdb'
    
    with open(pdb_file_path, 'w') as file:
        file.write(Chem.MolToPDBBlock(mol))
    
    print(f'PDB文件已保存到: {pdb_file_path}')
