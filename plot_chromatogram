def generate_chromatograms(array_rt=[3,5,6], end_time_of_lc_run=10, title='Reverse Phase Chromatography'):
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    from scipy import stats
    %matplotlib inline

    baseline_time = [round(i,2) for i in np.arange(0, end_time_of_lc_run, 0.01).tolist()]
    
    all_the_peaks = []
    for rt in array_rt:
        baseline_time += [np.round(i,2) for i in np.random.normal(rt, 0.05, 8000)]#5000
    
    fig, ax = plt.subplots(figsize=(20,5))
    #sns.set(color_codes=True)
    sns.set_style("whitegrid")
    ax.set_xlim(0,10)
    ax.grid(False)

    chrom = sns.distplot(baseline_time,hist=True,kde=False,bins=500, color="Red",kde_kws={"bw":0.03} )
    chrom.set_ylabel("Intensity",fontsize=20)
    chrom.set_xlabel("min",fontsize=20)
    chrom.axes.set_title("Reverse Phase Chromatography",fontsize=20)
    chrom.tick_params(labelsize=20)
    plt.show()

generate_chromatograms(array_rt=[3,5,6,5,3.4,2.4,8.9], end_time_of_lc_run=10, title='Reverse Phase Chromatography')
generate_chromatograms(array_rt=[3,5,6,5,3.4,2.4,8.9], end_time_of_lc_run=10, title='Strong Cation Chromatography')
generate_chromatograms(array_rt=[3,5,6,5,3.4,2.4,8.9], end_time_of_lc_run=10, title='HILIC')
