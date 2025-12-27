# Main module of the structural PDB analyzer project.
from utils import multiple_protein_analyzer

protein1 = "../data/1A3N.pdb"
protein2 = "../data/1CRN.pdb"
multiple_protein_analyzer(protein1, protein2)