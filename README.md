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
html files in **result/extrapolation** were visualized with ploty which is a tool for generating user interactive graph. You can see the results of materials extrapolation to hit multiple extreme target properties (**Fig. 3** in the manuscript) with the user interactive graph.  
The following gif example of parallel cooridates plot shows the results of generated molecules. The vertical magenta lines indicate constraints. Each horizontal line indicate a set of properties of a generated molecule and it is colored by score if it meets the all constraints simultaneously. pRMSE = 1 is a target bound for each property.
<img src = "plotly_example.gif" width="100%">
|Target_ID|logP     |TPSA   |QED        |HBA|HBD|MW         |DRD2       |
|---------|---------|-------|-----------|---|---|-----------|-----------|
|C1       |13.6112  |293.63 |0.012883689|15 |7  |1312.843003|0.01506572 |
|C2       |3.31534  |464.92 |0.061031881|19 |9  |1269.632228|0.042221135|
|C3       |-12.1461 |483.41 |0.068244547|29 |18 |1026.375124|0.000691099|
|C4       |-7.82963 |810.5  |0.015360798|28 |27 |1921.808718|0.245509655|
|C5       |-14.61686|1447.9 |0.011086205|48 |51 |3324.740114|0.067912293|
|C6       |-1.772   |526.91 |0.03910486 |20 |16 |1421.748941|0.222897802|
|C7       |6.4769   |775.42 |0.028972637|27 |27 |2467.830403|0.000544329|
|C8       |3.47975  |926.85 |0.019203494|31 |40 |2086.96405 |0.031526857|
|C9       |11.22402 |1336.88|0.007296211|40 |51 |3123.678598|0.163774739|
|C10      |-18.0912 |1456.35|0.025148621|49 |49 |3106.504128|0.009998713|



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
  
  
