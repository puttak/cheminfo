# cheminfo

1. plot_chromatogram: generate chromatograms for retention time prediction from a machine learning model. 
2. clustering: generate 2D chemical space using PCA and T-SNE. 
3. chem_tools:
    functions to convert smiles to descriptors (ECFP4, RDkit),
    desalt/neutralize molecules,
    generate feature importance using random forest,
    evaluate standard metrics. 
4. building_ml_models: buidling lasso, random forest, gradient descent decision tree and simple neural network models for a regression task. The small molecules dataset (n= 10000) were extracted from the paper below and converted to ECFP4 using RDkit. 

    Domingo-Almenara, X., Guijas, C., Billings, E. et al. The METLIN small molecule dataset for machine learning-based retention time prediction. Nat Commun 10, 5811 (2019). 
    
3. optimize_lightgbm_with_optuna: hyper-parameters using optuna by PFN.