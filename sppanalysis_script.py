import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp

"""
NOTES 

check significance of reaction time with similarity from SPP 

check significance of wordnet synonym synset path sim with SPP similarity 

PATH SIM 

path similarity is best metric for comparising in wordnet since the implementation for 
path sim is taking shortest path that connects 

if 2 words are more related, path sim >= a certain threshold

if 2 words less related - path sim < a certain threshold

For example, dog and canine have a path similarity of 1, because they are synonyms and 
belong to the same synset. Dog and cat have a path similarity of 0.2, 
because they are connected by four edges in the WordNet hierarchy. 
Dog and book have a path similarity of 0.0714, because they are connected by 13 edges 
in the WordNet hierarchy
"""

def data_processing(wordnet_sim, raw_data):
    """
    function cleans up data and gets isi from spp to join with wordnet table

    wordnet_sim: pandas df from wordnet

    raw_data: df from SPP - "all naming subjects.xlsx"
    """

    data_isi = raw_data[['Session', 'isi', 'prime', 'target', 'target.RT',
       'target.ACC']].dropna()

    data_isi['prime'] = [word.lower() for word in data_isi['prime']]

    data_isi = data_isi.rename(columns={'target.RT': 'RT', 'target.ACC': 'accuracy'})

    # merge data to get isi and session
    data = pd.merge(wordnet_sim, data_isi, how='inner', on=['prime','target', 'RT', 'accuracy'])
    data = data.drop_duplicates(subset=['prime','target','RT','accuracy','Session'])

    # split data into 50ms lag and 1050ms lag
    isi_data = data.groupby(['isi'])
    isi50 = isi_data.get_group(50)
    isi1050 = isi_data.get_group(1050)

    return isi50, isi1050

def sim_split(rating_type, upper, lower):
    """
    to compare the difference between less related and more related words, we can split the dataframes 
    using a threshold. if we use rating_type == pathsim and set upper = 0.8 and lower = 0.2, we are 
    essentially comparing the data for very similar pairings with path sim >= 0.8 to 
    less similar pairings with path sim < 0.2 or lower.

    rating_type: the rating used to split isi data e.g. path similarity, etc

    upper_thresh: upper threshold for splitting isi data e.g. for path sim, we can compare data that 
        has higher than 0.8 rating and compare it with data with lower threshold of 0.2

    lower_thresh: lower threshold for splitting data

    pathsim_isi_0: less related - found using lower threshold
    pathsim_isi_1: more related - found using upper threshold
    """

    isi50 = isi50.dropna(subset=[rating_type])
    isi1050 = isi1050.dropna(subset=[rating_type])

    # find different path sim values
    pathsim_50_0 = isi50[isi50[rating_type] < lower]
    pathsim_50_1 = isi50[isi50[rating_type] >= upper]

    pathsim_1050_0 = isi1050[isi1050[rating_type] < lower]
    pathsim_1050_1 = isi1050[isi1050[rating_type] >= upper]

    return pathsim_50_0, pathsim_50_1, pathsim_1050_0, pathsim_1050_1

def get_tscore(less_related, more_related):
    """
    this function uses the t-test to compare between less similar word pairings with more similar 
    word pairings to see if there's a significant difference between the 2. pvalue < 0.05 means 
    difference is significant. 

    less_related: pandas df with less similar word pairings
    more_related: pandas df with more similar word pairings

    this function should be used twice; once with isi = 50, once with isi = 1050

    this function's input parameter takes the dfs from sim_split

    returns t_test score for reaction time and accuracy.
    """

    rt_sig = sp.ttest_ind(less_related['RT'], more_related['RT'])
    acc_sig = sp.ttest_ind(less_related['accuracy'], more_related['accuracy'])

    return rt_sig, acc_sig

def get_descrip(less, more):
    """
    gets description of dataset. returns mean and standard deviation (std) of the data. 
    we can use this description to compare the means and std between less and more similar 

    less: less similar pairing df
    more: more similar pairing df

    returns df containing std and mean of the 2 input frames
    returned frame contains reaction time and accuracy data
    """

    return pd.DataFrame({'RT_mean':[less['RT'].mean(), more['RT'].mean()], \
                         'RT_std': [less['RT'].std(), more['RT'].std()], \
                            'acc_mean': [less['accuracy'].mean(), more['accuracy'].mean()], \
                                'acc_std': [less['accuracy'].std(), more['accuracy'].std()]},\
                              index=['less related','more related'])

