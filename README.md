<div align="center"> 

  # Materials Discovery with Extreme Properties via AI-Driven Combinatorial Chemistry
  # Under Construction

</div>

This repository is the implementation code for [Materials Discovery with Extreme Properties via AI-Driven Combinatorial Chemistry](https://arxiv.org/abs/2303.11833)

If you find this code or idea useful, please consider citing our paper:

```bibtex
@article{kim2023materials,
  title={Materials Discovery with Extreme Properties via AI-Driven Combinatorial Chemistry},
  author={Kim, Hyunseung and Choi, Haeyeon and Kang, Dongju and Lee, Won Bo and Na, Jonggeol},
  journal={arXiv preprint arXiv:2303.11833},
  year={2023}
}
```


html files in **result/extrapolation** were generated with ploty, a tool for generating user interactive graph.
  You can see the results of materials extrapolation to hit multiple extreme target properties (**Fig. 3** in the manuscript) with the user interactive graph.
<img src = "plotly_example.gif" width="100%">  

  ## Implimentation
### Hit ot multiple targets:
  python evaluate_extrapolation.py data/checkpoints/extrapolation/checkpoint-750-1 --run PPO --env DrugDiscoveryEnv --episodes 1000

### Docking:
  python evaluate_docking.py data/checkpoints/docking/checkpoint-80 --run PPO --env DrugDiscoveryEnv --episodes 1000
  
### HIV:
  python evaluate_HIV.py data/checkpoints/HIV/checkpoint-250-ccr5 --run PPO --env DrugDiscoveryEnv --episodes 1000
