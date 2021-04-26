#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 10:44:08 2021

@author: aimeebryce
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Read excel file containing data - altered depending on condition being looked at 
# Example used here is NR concentration

df=pd.read_csv("/Volumes/aimee_hd/UBQLN2_TIRF_imaging_LLPS/final/NR_conc_changes/full_mean_table_of_data_2.csv")
path=r'/Volumes/aimee_hd/UBQLN2_TIRF_imaging_LLPS/final/NR_conc_changes/'

# Plot swarm graph

sns.set_style('white')

# number of clusters = droplet numbers, this is changed to mean_area when looking at the mean droplet area
## filename = the concentration / altered data e.g. in this situation filename is the different concentrations of NR 
sns.swarmplot(x='filename', y='number_of_clusters', data=df, palette='YlOrRd', zorder=2)


# Reading one column in 
# Statistics below here:
    # number of clusters 
    
values_1=df['number_of_clusters'].where(df['filename']==12.5)
values_1=values_1.dropna()

values_2=df['number_of_clusters'].where(df['filename']==25)
values_2=values_2.dropna()


values_3=df['number_of_clusters'].where(df['filename']==50)
values_3=values_2.dropna()

# Plot value 1 error bar

x1 = ['1'] 
y1 = [values_1.mean()]
  
# creating error 
y_errormin = [values_1.std()] 
y_errormax = [values_1.std()] 
y_error = [y_errormin, y_errormax] 
  
plt.plot(x1, y1) 
plt.errorbar(x1, y1, 
             yerr=y_error,  
             fmt='o',
             markersize=2,
             capsize=2,
             c='black') 



# Plot values 2 error bar

x2 = ['2'] 
y2 = [values_2.mean()] 
  
# creating error 
y_errormin = [values_2.std()] 
y_errormax = [values_2.std()] 
y_error = [y_errormin, y_errormax] 
  
 
plt.plot(x2, y2) 
plt.errorbar(x2, y2, 
             yerr=y_error,  
             fmt='o',
             markersize=2,
             capsize=2,
             c='black')  

# Plot values 3 error bar

x3 = ['3'] 
y3 = [values_3.mean()] 
  
# creating error 
y_errormin = [values_3.std()] 
y_errormax = [values_3.std()] 
y_error = [y_errormin, y_errormax]  

plt.plot(x3, y3) 
plt.errorbar(x3, y3, 
             yerr=y_error,  
             fmt='o',
             markersize=2,
             capsize=2,
             c='black') 

# Add title/ axes to plots.
plt.ylim((0,300))
plt.title('Mean Number of Droplets vs NR Concentration') # This is altered depending on condition / droplet property being assessed
plt.xlabel('NR concentration (nM)') # This is altered depending on condition being assessed
plt.ylabel('Mean Number of Droplets')# This is altered depending on droplet property being assessed
plt.savefig(path+'SwarmPlot_Mean_Number_Droplet_vs_NR_Conc.pdf')
plt.show() 

## Conducting statistical tests.
# One way analysis of variance (ANOVA) testing 
F_val,p_val=f_oneway(values_20, values_40, values_80)
print("By one-way ANOVA F = %r, p = %r"%(F_val,p_val))

# Tukey post-hoc testing:
tukey = pairwise_tukeyhsd(endog=df['number_of_clusters'],
                      groups=df['filename'],
                      alpha=0.05)

print(tukey)
