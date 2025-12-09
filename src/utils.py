# Helper functions for the structural analyzer

def load_pdb(filepath):
    """
    Loads a PDB file.
    filepath: path to PDB file
    """
    atoms_lines = []
    with open(filepath, "r") as f:
        for line in f:
            if line.startswith("ATOM") or line.startswith("HETATM"): # atoms or ligands
                atoms_lines.append(line.strip()) # removes \n

    return atoms_lines

