import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# load data and assign column names
filename = 'lr_ak_bright_phys.txt'
df = pd.read_csv(filename, delimiter=',', header=None, comment='%', skip_blank_lines=True)
df.columns = ['trial','refk','refr','refi','testrk','testr','testik','testi',
    'refleft','choosetest','stimt','rt','totaltime']

# create decision spaces, i.e., proportion of times subject chose the test patch
# as looking lighter, as a function of test patch illuminance and reflectance
df = pd.pivot_table(df, index=['refr','testi'], columns='testr', values='choosetest', aggfunc='mean')

# prepare figure
plt.figure(figsize=(12,4))
refrlist = df.index.get_level_values('refr').unique().tolist()

# step through reference reflectances
for i, refr in enumerate(refrlist):

    # get the decision space for this reference reflectance
    dspace = df.loc[refr].dropna(axis=1, how='all').sort_values(by='testi', ascending=False)
    print(dspace)

    # plot the decision space
    plt.subplot(1,3,i+1)
    plt.imshow(dspace, cmap='grey', vmin=0, vmax=1)

    # set x axis ticks and labels
    k = np.arange(0,11,2)
    xlabels = [ f'{dspace.columns[kk]:.2f}' for kk in k]
    plt.xticks(ticks=k, labels=xlabels)
    if i==1: plt.xlabel('reflectance', fontsize=18)

    # set y axis ticks and labels
    ylabels = [ f'{dspace.index[kk]:.0f}' for kk in k]
    plt.yticks(ticks=k, labels=ylabels)
    if i==0: plt.ylabel('illuminance (lux)', fontsize=18)

plt.show()
