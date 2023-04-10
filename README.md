<div align="center"> 

  # Under Construction
  # Materials Discovery with Extreme Properties via AI-Driven Combinatorial Chemistry

</div>

This repository is the implementation code for [Materials Discovery with Extreme Properties via AI-Driven Combinatorial Chemistry](https://arxiv.org/abs/2303.11833)

If you find this code or idea useful, please consider citing our paper (arXiv preprint):

```bibtex
@article{kim2023materials,
  title={Materials Discovery with Extreme Properties via AI-Driven Combinatorial Chemistry},
  author={Kim, Hyunseung and Choi, Haeyeon and Kang, Dongju and Lee, Won Bo and Na, Jonggeol},
  journal={arXiv preprint arXiv:2303.11833},
  year={2023}
}
```

  ## Visualization of results: interactive plot (plotly)
html files in **result/extrapolation** were visualized with ploty, a tool for generating user interactive graph. You can see the results of materials extrapolation to hit multiple extreme target properties (**Fig. 3** in the manuscript) with the user interactive graph.  
The following gif example of parallel cooridates plot shows the results of generated molecules. The vertical magenta lines indicate constraints. Each horizontal line indicate a set of properties of a generated molecule and it is colored by score if it meets the all constraints simultaneously. pRMSE = 1 is a target bound for each property.
<img src = "plotly_example.gif" width="100%">

|Target_ID|MW         |logP     |TPSA   |QED        |HBA|HBD|DRD2       |Ref_SMILES                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|---------|-----------|---------|-------|-----------|---|---|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|C1       |1312.843003|13.6112  |293.63 |0.012883689|15 |7  |0.01506572 |CCCCCCCCCCCC(=O)CC(=O)N[C@@H]1[C@H]([C@@H]([C@H](O[C@@H]1OP(=O)(O)O)CO[C@H]2[C@@H]([C@H]([C@@H]([C@H](O2)COC)OP(=O)(O)O)OCC[C@@H](CCCCCCC)OC)NC(=O)CCCCCCCCC/C=C\\CCCCCC)O)OCCCCCCCCCC                                                                                                                                                                                                                                                                                                                                                                                                |
|C2       |1269.632228|3.31534  |464.92 |0.061031881|19 |9  |0.042221135|CC1=CC2=C(C=C1C)N(C=N2)[C@@H]3[C@@H]([C@@H]([C@H](O3)CO)OP(=O)([O-])O[C@H](C)CNC(=O)CC[C@@]\\4([C@H]([C@@H]5[C@]6([C@@]([C@@H](C(=N6)/C(=C\\7/[C@@]([C@@H](C(=N7)/C=C\\8/C([C@@H](C(=N8)/C(=C4\\[N-]5)/C)CCC(=O)N)(C)C)CCC(=O)N)(C)CC(=O)N)/C)CCC(=O)N)(C)CC(=O)N)C)CC(=O)N)C)O                                                                                                                                                                                                                                                                                                       |
|C3       |1026.375124|-12.1461 |483.41 |0.068244547|29 |18 |0.000691099|C[C@H]1[C@H]([C@H]([C@@H]([C@@H](O1)O[C@H]2[C@@H]([C@H](OC([C@@H]2NC(=O)C)O)CO)O[C@H]3[C@@H]([C@H]([C@@H]([C@H](O3)CO)O[C@H]4[C@H]([C@H]([C@@H]([C@H](O4)CO[C@@H]5[C@H]([C@H]([C@@H]([C@H](O5)CO)O)O)O)O)O)O[C@H]6[C@@H]([C@H]([C@@H](CO6)O)O)O)O)NC(=O)C)O)O)O                                                                                                                                                                                                                                                                                                                       |
|C4       |1921.808718|-7.82963 |810.5  |0.015360798|28 |27 |0.245509655|C[C@H]1C(=O)N[C@H](C(=O)N[C@H](C(=O)N[C@H](C(=O)N2CCC[C@H]2C(=O)N[C@H](C(=O)N[C@H](C(=O)N[C@@H](CSSC[C@@H](C(=O)NCC(=O)N[C@H](C(=O)N[C@H](C(=O)N[C@H](C(=O)N[C@H](C(=O)N3CCC[C@H]3C(=O)N[C@H](C(=O)NCC(=O)N1)CCC(=O)O)[C@@H](C)O)CCC(=O)O)CCCNC(=N)N)CCC(=O)N)N)C(=O)O)CC4=CC=C(C=C4)O)CC5=CNC6=CC=CC=C65)CCCCN)C)CCC(=O)O                                                                                                                                                                                                                                                            |
|C5       |3324.740114|-14.61686|1447.9 |0.011086205|48 |51 |0.067912293|CC[C@H](C)[C@@H](C(=O)N[C@@H](CC(C)C)C(=O)N[C@@H](CC(=O)N)C(=O)O)NC(=O)[C@H](CO)NC(=O)[C@H](CC(=O)N)NC(=O)[C@H](CC(C)C)NC(=O)[C@H](CC1=CC=C(C=C1)O)NC(=O)[C@H](CCCCN)NC(=O)[C@H](CCCCN)NC(=O)[C@H](C(C)C)NC(=O)[C@H](C)NC(=O)[C@H](CCSC)NC(=O)[C@H](CCC(=O)N)NC(=O)[C@H](CCCCN)NC(=O)[C@H](CCCNC(=N)N)NC(=O)[C@H](CC(C)C)NC(=O)[C@H](CCCNC(=N)N)NC(=O)[C@H]([C@@H](C)O)NC(=O)[C@H](CC2=CC=C(C=C2)O)NC(=O)[C@H](CC(=O)N)NC(=O)[C@H](CC(=O)O)NC(=O)[C@H]([C@@H](C)O)NC(=O)[C@H](CC3=CC=CC=C3)NC(=O)[C@H](C(C)C)NC(=O)[C@H](C)NC(=O)[C@H](CC(=O)O)NC(=O)[C@H](CO)NC(=O)[C@H](CC4=CN=CN4)N|
|C6       |1421.748941|-1.772   |526.91 |0.03910486 |20 |16 |0.222897802|CCC(C)C1C(=O)NC(C(=O)NC(C(=O)NC(C(=O)NC(C(=O)NCCCCC(C(=O)NC(C(=O)N1)CCCN)NC(=O)C(C(C)CC)NC(=O)C(CCC(=O)O)NC(=O)C(CC(C)C)NC(=O)C2CSC(=N2)C(C(C)CC)N)CC(=O)N)CC(=O)O)CC3C=NC=N3)CC4=CC=CC=C4                                                                                                                                                                                                                                                                                                                                                                                            |
|C7       |2467.830403|6.4769   |775.42 |0.028972637|27 |27 |0.000544329|CC(C)C[C@@H](C(=O)N[C@@H](CC(C)C)C(=O)N[C@@H](CC(C)C)C(=O)N[C@@H](CC(C)C)C(=O)N[C@@H](CCCCN)C(=O)N[C@@H](CC(C)C)C(=O)N[C@@H](CC(C)C)C(=O)N[C@@H](CC(C)C)C(=O)N[C@@H](CC(C)C)C(=O)N[C@@H](CCCCN)C(=O)N[C@@H](CC(C)C)C(=O)N[C@@H](CC(C)C)C(=O)N[C@@H](CC(C)C)C(=O)N[C@@H](CC(C)C)C(=O)N[C@@H](CCCCN)C(=O)N[C@@H](CC(C)C)C(=O)N[C@@H](CC(C)C)C(=O)N[C@@H](CC(C)C)C(=O)N[C@@H](CC(C)C)C(=O)N[C@@H](CCCCN)C(=O)O)NC(=O)[C@H](CCCCN)N                                                                                                                                                       |
|C8       |2086.96405 |3.47975  |926.85 |0.019203494|31 |40 |0.031526857|CC[C@@H](C)[C@@H](C(=N[C@H](CS)C(=N[C@@H](C(C)O)C(=N[C@@H](CCCNC(=N)N)[C]=O)O)O)O)N=C([C@H](CS)N=C([C@H](CCCNC(=N)N)N=C([C@H](CS)N=C([C@@H](C(C)C)N=C(CN=C([C@H](CCCNC(=N)N)N=C([C@H](CCCNC(=N)N)N=C([C@H](CS)N=C([C@H](CC(C)C)N=C([C@H](CS)N=C(C(CCCNC(=N)N)N=C([C@H](CS)N=C([C@@H](CC1=CC=CC=C1)N=C(CN)O)O)O)O)O)O)O)O)O)O)O)O)O)O                                                                                                                                                                                                                                                  |
|C9       |3123.678598|11.22402 |1336.88|0.007296211|40 |51 |0.163774739|CC[C@H](C)[C@@H](C(=N[C@@H]([C@@H](C)O)C(=N[C@@H](CS)C(=N[C@@H](C(C)C)C(=N[C@@H](CCCNC(=N)N)C(=N[C@@H](CCCNC(=N)N)C(=N[C@@H](C)C(=N[C@@H](CC1=CC=CC=C1)C(=O)O)O)O)O)O)O)O)O)N=C([C@H](CO)N=C([C@@H]2CCCN2C(=O)[C@H](C)N=C(CN=C([C@H](CC(C)C)N=C([C@H](CCCCN)N=C([C@H](CCCCN)N=C([C@H](CCSC)N=C([C@H](CCCNC(=N)N)N=C([C@H](CC3=CNC4=CC=CC=C43)N=C([C@H](CCC(=N)O)N=C([C@H](CC5=CNC6=CC=CC=C65)N=C([C@H](CCCNC(=N)N)N=C([C@H](CCCNC(=N)N)N=C([C@H](CS)N=C([C@H](CCCCN)N=C([C@H](CC7=CC=CC=C7)N)O)O)O)O)O)O)O)O)O)O)O)O)O)O)O)O                                                          |
|C10      |3106.504128|-18.0912 |1456.35|0.025148621|49 |49 |0.009998713|CC[C@H](C)[C@@H](C(=O)N[C@@H]([C@@H](C)O)C(=O)N[C@@H]([C@@H](C)O)C(=O)N[C@@H](CCCCN)C(=O)N[C@@H](CC(=O)O)C(=O)N[C@@H](CC(C)C)C(=O)N[C@@H](CCCCN)C(=O)N[C@@H](CCC(=O)O)C(=O)N[C@@H](CCCCN)C(=O)N[C@@H](CCCCN)C(=O)N[C@@H](CCC(=O)O)C(=O)N[C@@H](C(C)C)C(=O)N[C@@H](C(C)C)C(=O)N[C@@H](CCC(=O)O)C(=O)N[C@@H](CCC(=O)O)C(=O)N[C@@H](C)C(=O)N[C@@H](CCC(=O)O)C(=O)N[C@@H](CC(=O)N)C(=O)O)NC(=O)[C@H](CCC(=O)O)NC(=O)[C@H](CO)NC(=O)[C@H](CO)NC(=O)[C@H]([C@@H](C)O)NC(=O)[C@H](CC(=O)O)NC(=O)[C@H](C(C)C)NC(=O)[C@H](C)NC(=O)[C@H](C)NC(=O)[C@H](CC(=O)O)NC(=O)[C@H](CO)NC(=O)C           |


  ## Commands for code implimentation
### Materials extrapolation to hit multiple extreme targets properties; targets C1 to C10:
  python inference_extrapolation.py data/checkpoints/extrapolation/checkpoint-750-1 --run PPO --env DrugDiscoveryEnv --episodes 1000  
  python inference_extrapolation.py data/checkpoints/extrapolation/checkpoint-750-2 --run PPO --env DrugDiscoveryEnv --episodes 1000  
  python inference_extrapolation.py data/checkpoints/extrapolation/checkpoint-750-3 --run PPO --env DrugDiscoveryEnv --episodes 1000  
  ...  
  python inference_extrapolation.py data/checkpoints/extrapolation/checkpoint-750-10 --run PPO --env DrugDiscoveryEnv --episodes 1000  
 
 
### Application to the discovery of protein docking materials; 5-HT<sub>1B</sub> receptor:
  python inference_docking.py data/checkpoints/docking/checkpoint-80 --run PPO --env DrugDiscoveryEnv --episodes 1000
  
  
### HIV to three targets; CCR5, INT, and RT:
  python inference_HIV.py data/checkpoints/HIV/checkpoint-250-ccr5 --run PPO --env DrugDiscoveryEnv --episodes 1000  
  python inference_HIV.py data/checkpoints/HIV/checkpoint-250-int --run PPO --env DrugDiscoveryEnv --episodes 1000  
  python inference_HIV.py data/checkpoints/HIV/checkpoint-250-rt --run PPO --env DrugDiscoveryEnv --episodes 1000  
  
  
