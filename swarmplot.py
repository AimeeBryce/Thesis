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

# Read excel file containing data - 

df=pd.read_csv("/Volumes/aimee_hd/UBQLN2_TIRF_imaging_LLPS/final/NR_conc_changes/full_mean_table_of_data_2.csv")
path=r'/Volumes/aimee_hd/UBQLN2_TIRF_imaging_LLPS/final/NR_conc_changes/'

# Plot swarm graph


sns.set_style('white')

# number of clusters = droplet numbers, this was changed to mean_area when looking at the mean droplet area
## filename = the concentration / altered data e.g. in this situation filename is the different concentrations of NR 
sns.swarmplot(x='filename', y='number_of_clusters', data=df, palette='YlOrRd', zorder=2)


# Reading one column in 
# Statistics below here:
    # number of clusters 
    
values_20=df['number_of_clusters'].where(df['filename']==12.5)
values_20=values_20.dropna()

values_40=df['number_of_clusters'].where(df['filename']==25)
values_40=values_40.dropna()


values_80=df['number_of_clusters'].where(df['filename']==50)
values_80=values_80.dropna()

# Plot 10 min error bar

x1 = ['20'] 
y1 = [values_20.mean()]
  
# creating error 
y_errormin = [values_20.std()] 
y_errormax = [values_20.std()] 
y_error = [y_errormin, y_errormax] 
  
plt.plot(x1, y1) 
plt.errorbar(x1, y1, 
             yerr=y_error,  
             fmt='o',
             markersize=2,
             capsize=2,
             c='black') 



# Plot 60 min error bar

x2 = ['40'] 
y2 = [values_40.mean()] 
  
# creating error 
y_errormin = [values_40.std()] 
y_errormax = [values_40.std()] 
y_error = [y_errormin, y_errormax] 
  
 
plt.plot(x2, y2) 
plt.errorbar(x2, y2, 
             yerr=y_error,  
             fmt='o',
             markersize=2,
             capsize=2,
             c='black')  

x3 = ['80'] 
y3 = [values_80.mean()] 
  
# creating error 
y_errormin = [values_80.std()] 
y_errormax = [values_80.std()] 
y_error = [y_errormin, y_errormax]  
  
# Plot 180 min error bar

plt.plot(x3, y3) 
plt.errorbar(x3, y3, 
             yerr=y_error,  
             fmt='o',
             markersize=2,
             capsize=2,
             c='black') 

# Add title/ axes etc.
plt.ylim((0,300))
plt.title('Mean Number of Droplets vs NR Concentration')
plt.xlabel('NR concentration (nM)')
plt.ylabel('Mean Number of Droplets')
plt.savefig(path+'SwarmPlot_Mean_Number_Droplet_vs_NR_Conc.pdf')
plt.show() 



# One way ANOVA testing 
F_val,p_val=f_oneway(values_20, values_40, values_80)

print("By one-way ANOVA F = %r, p = %r"%(F_val,p_val))

# Tukey post hoc testing:
    
tukey = pairwise_tukeyhsd(endog=df['number_of_clusters'],
                      groups=df['filename'],
                      alpha=0.05)

#display results
print(tukey)
