filename = '5ht1b'

import gym
from gym import spaces
from gym.utils import seeding
import copy

from collections import Counter
import pickle
import re
import numpy as np
import pandas as pd
import random

from rdkit import Chem
from rdkit.Chem.BRICS import reactionDefs
from rdkit.Chem import QED

import subprocess
from openbabel import pybel

import time

train_smiles = []
fragment_path = "/home/cysdh02/PycharmProjects/AID-CC/evaluate/data/fragment/chembl_save_data.pkl"
with open(fragment_path, 'rb') as f:
	data = pickle.load(f)
	data_2 = data['fragment_counts']

for i in range(len(data_2)):
    if data_2['frequency'][i] > 1.37512e-07 * 150:
        train_smiles.append(data_2['fragment'][i])

train = []
for i in range(len(train_smiles)):
    train.extend([Chem.MolFromSmiles(train_smiles[i])])

fragment_dict = {}
for i in range(len(train)):
    fragment_dict[i] = train[i]

isotope_re = re.compile(r'\[([0-9]+)[ab]?\*\]')

"""
Prepare binary connection rules
"""
binary_defs = {}
connection_rules = set()
for row in reactionDefs:
    for a, b, t in row:
        if a in ['7a', '7b']:
            binary_defs[7] = 2 ** 7
            connection_rules.add((7, 7))
        else:
            a = int(a)
            b = int(b)
            binary_defs[a] = binary_defs.get(a, 0) | 2 ** b
            binary_defs[b] = binary_defs.get(b, 0) | 2 ** a
            connection_rules.add((a, b))
            connection_rules.add((b, a))

fragment_rule = {}
for i in range(16):
    fragment_rule[i] = []

for i in train_smiles:
    for k in range(1,17,1):
        for j in isotope_re.findall(i):
            if int(j) == int(k):
                fragment_rule[k-1].append(train_smiles.index(i))


class CombinatorialGenerator:
    def __init__(self, n_jobs=1):
        self.n_jobs = n_jobs

    def generate_molecular(self, mol, fragment):
        """
        :param mol: existed molecular (.mol)
        :param fragment: fragment that will be added (.mol)
        :return:
        """
        if mol is None:
            mol = fragment
        else:
            # connection points of 'mol'
            connections_mol = self.get_connection_points(mol)

            # mask fragments with possible reactions
            fragment_mol = fragment
            connections_fragment = self.get_connection_points(fragment_mol)

            possible_connections = self.filter_connections(
                connections_mol,
                connections_fragment
            )

            if not possible_connections:
                pass
            else:
                c_i = np.random.choice(len(possible_connections))
                a1, a2 = possible_connections[c_i]

                mol = self.connect_mols(mol, fragment_mol, a1, a2)

        return mol

    def get_connection_rule(self, fragment):
        """
        return OR combination for possible incoming reactions

        Arguments:
            fragment: fragment smiles

        Returns:
            int
        """
        rule = 0
        for i in map(int, set(isotope_re.findall(fragment))):
            rule |= binary_defs[i]
        return rule

    @staticmethod
    def get_connection_filter(atoms):
        """
        Return OR(2**isotopes)
        """
        connection_rule = 0
        for atom in atoms:
            connection_rule |= 2 ** atom.GetIsotope()
        return connection_rule

    @staticmethod
    def get_connection_points(mol):
        """
        Return connection points

        Arguments:
            mol: ROMol

        Returns:
            atom list
        """
        atoms = []
        for atom in mol.GetAtoms():
            if atom.GetSymbol() == '*':
                atoms.append(atom)
        return atoms

    @staticmethod
    def filter_connections(atoms1, atoms2, unique=True):
        possible_connections = []
        for a1 in atoms1:
            i1 = a1.GetIsotope()
            for a2 in atoms2:
                i2 = a2.GetIsotope()
                if (i1, i2) in connection_rules:
                    possible_connections.append((a1, a2))
        return possible_connections

    @staticmethod
    def connect_mols(mol1, mol2, atom1, atom2):
        combined = Chem.CombineMols(mol1, mol2)
        emol = Chem.EditableMol(combined)
        neighbor1_idx = atom1.GetNeighbors()[0].GetIdx()
        neighbor2_idx = atom2.GetNeighbors()[0].GetIdx()
        atom1_idx = atom1.GetIdx()
        atom2_idx = atom2.GetIdx()
        bond_order = atom2.GetBonds()[0].GetBondType()
        emol.AddBond(neighbor1_idx,
                     neighbor2_idx + mol1.GetNumAtoms(),
                     order=bond_order)
        emol.RemoveAtom(atom2_idx + mol1.GetNumAtoms())
        emol.RemoveAtom(atom1_idx)
        mol = emol.GetMol()
        return mol




class DrugDiscoveryEnv(gym.Env):
    def __init__(self, *args, **kwargs):
        self.N = len(train)
        self.current_fragment = 1

        self.current_molecule = fragment_dict[np.random.choice(self.N)]
        self.min_fragment = 2
        self.target_fragment = 4

        self.attached_fragments = []
        self.attached_fragments.append(Chem.MolToSmiles(self.current_molecule))

        # self.done = 0
        self.number = 0

        self.data = {
            'SMILES': [],
            'receptor': [],
            'fragment_num': [],
            'docking_score': [],
            'fragments': []
        }

        self.action_space = spaces.Discrete(self.N)

        self.obs_space = spaces.Box(-100, 100, shape=(1,), dtype=np.float64)

        self.observation_space = spaces.Dict({
            "action_mask": spaces.Box(0, 1, shape=(self.N,), dtype=np.float64),
            "observations": self.obs_space
        })

        self.reset()

    def _RESET(self):
        self.current_fragment = 1
        self.number += 1
        self.current_molecule = fragment_dict[np.random.choice(self.N)]
        self.attached_fragments = []
        self.attached_fragments.append(Chem.MolToSmiles(self.current_molecule))

        self.data = {
            'SMILES': [],
            'receptor': [],
            'fragment_num': [],
            'docking_score': [],
            'fragments': []
        }

        self.state = {
            "action_mask": np.ones(shape=(self.N,), dtype=np.float64),
            "observations": np.zeros(shape=(1,), dtype=np.float64)
        }

        return self.state

    def _STEP(self, action):
        start = time.time()
        if self.current_molecule is None:
            fragment = fragment_dict[np.random.choice(self.N)]
        else:
            fragment = fragment_dict[action]

        self.attached_fragments.append(Chem.MolToSmiles(fragment))
        pre_molecule = self.current_molecule
        self.current_molecule = CombinatorialGenerator().generate_molecular(pre_molecule, fragment)

        self.current_fragment += 1

        # add Hydrogen
        smi = Chem.MolToSmiles(self.current_molecule)
        smi = re.sub("[0-9]{2}[*]", 'H', smi)
        smi = re.sub("[0-9][*]", 'H', smi)

        mol = Chem.MolFromSmiles(smi)
        self.MW_CM = QED.properties(mol)[0]

        ligand_mol = f'mol/ligand_{self.number}_4step.mol'
        run_line = 'obabel -:%s --gen3d -O %s' % (smi, ligand_mol)
        result = subprocess.check_output(run_line.split(),
                                         stderr=subprocess.STDOUT,
                                         # timeout=self.timeout_gen3d,
                                         universal_newlines=True)
        self.ms = list(pybel.readfile("mol", f"mol/ligand_{self.number}_4step.mol"))
        print(len(self.ms))

        if len(self.ms) != 0:
            m = self.ms[0]
            m.write("pdbqt", f"pdbqt/ligand_{self.number}_4step.pdbqt", overwrite=True)

            vina_program = 'qvina2'
            receptor_file = '5ht1b.pdbqt'
            ligand_pdbqt_file = f'pdbqt/ligand_{self.number}_4step.pdbqt'
            docking_pdbqt_file = f'docked/docked_{self.number}_4step.pdbqt'
            box_center = 10, 10, 10
            box_size = 60, 60, 60
            num_cpu_dock = 1
            num_modes = 10
            exhaustiveness = 1

            run_line = '%s --receptor %s --ligand %s --out %s' % (
            vina_program, receptor_file, ligand_pdbqt_file, docking_pdbqt_file)
            run_line += ' --center_x %s --center_y %s --center_z %s' % (box_center)
            run_line += ' --size_x %s --size_y %s --size_z %s' % (box_size)
            run_line += ' --cpu %d' % (num_cpu_dock)
            run_line += ' --num_modes %d' % (num_modes)
            run_line += ' --exhaustiveness %d ' % (exhaustiveness)

            result = subprocess.check_output(run_line.split(),
                                             stderr=subprocess.STDOUT,
                                             # timeout=self.timeout_dock,
                                             universal_newlines=True)
            result_lines = result.split('\n')
            check_result = False

            affinity_list = list()
            for result_line in result_lines:
                if result_line.startswith('-----+'):
                    check_result = True
                    continue
                if not check_result:
                    continue
                if result_line.startswith('Writing output'):
                    break
                if result_line.startswith('Refine time'):
                    break
                lis = result_line.strip().split()
                if not lis[0].isdigit():
                    break
                #            mode = int(lis[0])
                affinity = float(lis[1])
                affinity_list += [affinity]

            if len(affinity_list) == 0:
                affinity_list.append(99.9)

            affinity = affinity_list[0]
            print(affinity)

            c_reward = - affinity
            self.aff = affinity

        if len(self.ms) == 0:
            done = True
            self.aff = 99.9
            reward = 0


        if CombinatorialGenerator().get_connection_rule(Chem.MolToSmiles(self.current_molecule)) == 0:
            # no more connection point
            if self.current_fragment < self.min_fragment:
                done = True
                reward = 0
            else:
                done = True
                reward = 0

        else:
            # there exists possible connections
            if self.current_fragment < self.target_fragment:
                done = False
                reward = 0

            else:
                # over maximum fragment number
                done = True
                reward = 0

        if done:
            self.data['SMILES'].append(smi)
            self.data['receptor'].append('5ht1b')
            self.data['fragment_num'].append(self.current_fragment)
            self.data['docking_score'].append(0)
            self.data['fragments'].append(self.attached_fragments)

            pd.DataFrame(self.data).to_csv(f'/home/cysdh02/PycharmProjects/AID-CC/result/docking/evaluate_{filename}.csv', mode='a',
                                           na_rep='NaN', header=False)
        end = time.time()
        print(f"{end - start:.3f} sec")

        self._update_state()

        return self.state, reward, done, {}

    def _update_state(self):
        p = CombinatorialGenerator().get_connection_rule(Chem.MolToSmiles(self.current_molecule))
        k = '{0:0>17}'.format(int(bin(p)[2:]))
        rules = []
        for pos, char in enumerate(k):
            if char == '1':
                rules.append(-pos + 16)
        list = []
        for i in rules:
            for k in fragment_rule[i - 1]:
                list.append(k)

        mask = np.zeros(shape=(self.N,))
        for i in list:
            mask[i] = 1

        state = np.array([0])

        self.state = {
            "action_mask": mask,
            "observations": state
        }

    def reset(self):
        return self._RESET()

    def step(self, action):
        return self._STEP(action)
