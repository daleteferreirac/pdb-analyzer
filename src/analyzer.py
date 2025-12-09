# Main module of the structural PDB analyzer project.
from utils import load_pdb

atoms = load_pdb("../data/1CRN.pdb")
print(len(atoms))