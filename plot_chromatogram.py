import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

#This is a code to generate chromatograms for the predicted retention time
def plot_chromatograms(array_rt=[3,5,6], end_time_of_lc_run=10, title='Reverse Phase Chromatography'):

    baseline_time = [round(i,2) for i in np.arange(0, end_time_of_lc_run, 0.01).tolist()]
    
    all_the_peaks = []
    for rt in array_rt:
        baseline_time += [np.round(i,2) for i in np.random.normal(rt, 0.05, 2000)]#5000
    
    fig, ax = plt.subplots(figsize=(20,2))
    #sns.set(color_codes=True)
    sns.set_style("whitegrid")
    ax.set_xlim(0,10)
    ax.grid(False)

    chrom = sns.distplot(baseline_time,hist=True,kde=False,bins=500, color="green",kde_kws={"bw":0.03} )
    chrom.set_ylabel("Intensity",fontsize=20)
    chrom.set_xlabel("min",fontsize=20)
    chrom.axes.set_title(title,fontsize=20)
    chrom.tick_params(labelsize=20)
    plt.show()

plot_chromatograms(array_rt=[3,5,6,5,3.4,2.4,8.9], end_time_of_lc_run=10, title='Reverse Phase Chromatography')
plot_chromatograms(array_rt=[1,3,4,8,9.4,8.4,4.9], end_time_of_lc_run=10, title='Strong Cation Chromatography')
plot_chromatograms(array_rt=[2.1,3,6,4,8.4,6.1,3.2], end_time_of_lc_run=10, title='HILIC')
