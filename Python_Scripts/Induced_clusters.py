import mne
import os.path as op
import numpy as np
import matplotlib.pyplot as plt
from EEG_pareidolia_utils import *
from mne.time_frequency import tfr_morlet
from mne.stats import permutation_cluster_test
from mne.datasets import sample
from param import *


FOLDERPATH = r'E:\PhD\EEG_data\Pareidolia_BIDS'
RUN_LIST = {'pareidolia':['1', '2', '3']}
SUBJ_LIST = ['01', '02']
TASK_LIST = ['pareidolia']

def induced_cluster(epochs, cond1, cond2, chs, ch_str, window = None, threshold = 7, title = 'Hello World'):

    epochs1_tot = []
    epochs2_tot = []
    for run in RUN_LIST[task]:

        chs_int = find_cluster_inds(chs)

        if cond1 == 'par':
            epochs1 = np.concatenate((epochs[run]['par_high_fast'].data, epochs[run]['par_mid_fast'].data, epochs[run]['par_low_fast'].data,
                                      epochs[run]['par_high_slow'].data,
                                    epochs[run]['par_mid_slow'].data, epochs[run]['par_low_slow'].data), axis = 0)
        if cond1 == 'nopar':
            epochs1 = np.concatenate((epochs[run]['nopar_high'].data,
                                              epochs[run]['nopar_mid'].data, epochs[run]['nopar_low'].data), axis = 0)
        if cond1 == 'parFast':
            epochs1 = np.concatenate((epochs[run]['par_high_fast'].data,
                                                  epochs[run]['par_mid_fast'].data, epochs[run]['par_low_fast'].data), axis=0)
        if cond1 == 'parSlow':
            epochs1 = np.concatenate((epochs[run]['par_high_slow'].data,
                                                  epochs[run]['par_mid_slow'].data, epochs[run]['par_low_slow'].data), axis=0)
        if cond1 == 'high':
            epochs1 = np.concatenate((epochs[run]['nopar_high'].data,
                                                  epochs[run]['par_high_fast'].data, epochs[run]['par_high_slow'].data), axis=0)
        if cond1 == 'mid':
            epochs1 = np.concatenate((epochs[run]['nopar_mid'].data,
                                                  epochs[run]['par_mid_fast'].data, epochs[run]['par_mid_slow'].data), axis=0)
        if cond1 == 'low':
            epochs1 = np.concatenate((epochs[run]['nopar_low'].data,
                                                  epochs[run]['par_low_fast'].data, epochs[run]['par_low_slow'].data), axis=0)

        if cond2 == 'par':
            epochs2 = np.concatenate((epochs[run]['par_high_fast'].data, epochs[run]['par_mid_fast'].data, epochs[run]['par_low_fast'].data,
                                      epochs[run]['par_high_slow'].data,
                                    epochs[run]['par_mid_slow'].data, epochs[run]['par_low_slow'].data), axis = 0)
        if cond2 == 'nopar':
            epochs2 = np.concatenate((epochs[run]['nopar_high'].data,
                                              epochs[run]['nopar_mid'].data, epochs[run]['nopar_low'].data), axis = 0)
        if cond2 == 'parFast':
            epochs2 = np.concatenate((epochs[run]['par_high_fast'].data,
                                                  epochs[run]['par_mid_fast'].data, epochs[run]['par_low_fast'].data), axis=0)
        if cond2 == 'parSlow':
            epochs2 = np.concatenate((epochs[run]['par_high_slow'].data,
                                                  epochs[run]['par_mid_slow'].data, epochs[run]['par_low_slow'].data), axis=0)
        if cond2 == 'high':
            epochs2 = np.concatenate((epochs[run]['nopar_high'].data,
                                                  epochs[run]['par_high_fast'].data, epochs[run]['par_high_slow'].data), axis=0)
        if cond2 == 'mid':
            epochs2 = np.concatenate((epochs[run]['nopar_mid'].data,
                                                  epochs[run]['par_mid_fast'].data, epochs[run]['par_mid_slow'].data), axis=0)
        if cond2 == 'low':
            epochs2 = np.concatenate((epochs[run]['nopar_low'].data,
                                                  epochs[run]['par_low_fast'].data, epochs[run]['par_low_slow'].data), axis=0)



        if window == 'RT':
            epochs_high = mne.concatenate_epochs([epochs['early_high'],
                                                      epochs['late_high']])
            epochs_mid = mne.concatenate_epochs([epochs['early_mid'],
                                                      epochs['late_mid']])
            epochs_low = mne.concatenate_epochs([epochs['early_low'],
                                                      epochs['late_low']])
            epochs_parSlow = mne.concatenate_epochs([epochs['late_low'],
                                                      epochs['late_mid'], epochs['late_high']])
            epochs_parFast = mne.concatenate_epochs([epochs['early_low'],
                                                      epochs['early_mid'], epochs['early_high']])

        epochs1_tot.append(epochs1)
        epochs2_tot.append(epochs2)

    epochs1_tot = np.array(epochs1_tot)
    epochs2_tot = np.array(epochs2_tot)

    epochs1_tot = np.concatenate((epochs1_tot[0], epochs1_tot[1], epochs1_tot[2]), axis = 0)
    epochs2_tot = np.concatenate((epochs2_tot[0], epochs2_tot[1], epochs2_tot[2]), axis = 0)

    power1 = np.average((epochs1_tot[:, chs_int, :, :].squeeze()), axis=1)
    power2 = np.average((epochs2_tot[:, chs_int, :, :].squeeze()), axis=1)
    print(power1.shape)

    T_obs, clusters, cluster_p_values, H0 = \
    permutation_cluster_test([power1, power2],
                             n_permutations=100, threshold=threshold, tail=0)
    #if T_obs.shape[0]<113:
    #    T_obs = np.average(T_obs, axis = 0)
        #clusters = np.average(clusters, axis = 0)
    ch_name = chs
    plt.figure()

    # Create new stats image with only significant clusters
    T_obs_plot = np.nan * np.ones_like(T_obs)
    for c, p_val in zip(clusters, cluster_p_values):
        #c2 = np.average(c, axis = 0)
        if p_val <= 0.05:
            T_obs_plot[c] = T_obs[c]

    plt.imshow(T_obs,
               extent=[times[0], times[-1], freqs[0], freqs[-1]],
               aspect='auto', origin='lower', cmap='gray')
    plt.imshow(T_obs_plot,
               extent=[times[0], times[-1], freqs[0], freqs[-1]],
               aspect='auto', origin='lower', cmap='RdBu_r')

    plt.xlabel('Time (ms)')
    plt.ylabel('Frequency (Hz)')
    plt.title('Induced power (%s)' % ch_str)
    save_name, save_path = get_pareidolia_bids(FOLDERPATH, subj, task, run, stage = 'fig_Induced_cluster'+ch_str+cond1+'-'+cond2, cond=None)
    plt.savefig(save_path, dpi=300)
    return



for subj in SUBJ_LIST:
    for task in TASK_LIST:
        epochs_tot = {}
        for run in RUN_LIST[task]:
            epochs_name, epochs_path = get_pareidolia_bids(FOLDERPATH, subj, task, run, stage = 'Morlet', cond=None)
            epochs_tfr = mne.time_frequency.read_tfrs(epochs_path)
            epochs_tfr = epochs_tfr[0].crop(-1.5, 8)
            epochs_tot[run] = epochs_tfr


    #Define channels of interest
    EOG_chs = ['E1', 'E8', 'E25', 'E32', 'E126', 'E127']
    Unwanted = ['E43', 'E48', 'E49', 'E128', 'E113', 'E120', 'E125', 'E119']
    All_chs = epochs_tfr[0].info['ch_names'][0:129]
    EEG_chs = [ele for ele in All_chs if ele not in Unwanted]
    EEG_chs = [ele for ele in EEG_chs if ele not in EOG_chs]

    #Define clusters of channels
    def find_cluster_inds (chs):
        cluster_chs = []
        for e, i in enumerate(EEG_chs):
            if i in chs:
                cluster_chs.append(e)
        cluster_chs = np.array(cluster_chs)
        return cluster_chs

    frontal_L = ['E20', 'E21', 'E22', 'E23', 'E24', 'E26', 'E27', 'E12', 'E18', 'E19', 'E11', 'E15', 'E16']
    frontal_R = ['E2', 'E3', 'E4', 'E5', 'E118', 'E124', 'E123', 'E9', 'E10', 'E14', 'E11', 'E15', 'E16']
    smotor_R = ['E104', 'E105']
    smotor_L = ['E36', 'E30']
    occi_R = ['E76', 'E83', 'E84']
    occi_L = ['E66', 'E70', 'E71']
    CHS_LIST = [frontal_L, frontal_R, occi_L, occi_R, smotor_L, smotor_R]
    CHS_STRING = ['frontal_L', 'frontal_R', 'occi_L', 'occi_R', 'smotor_L', 'smotor_R']
    fmin = 2
    fmax=45
    num=30
    freqs = np.logspace(*np.log10([fmin, fmax]), num=num)
    times = 1e3 * epochs_tfr[0].times  # change unit to ms
    for ch, ch_str in zip(CHS_LIST, CHS_STRING):
        print(ch)
        print(ch_str)
        cond1 = 'mid'
        cond2 = 'high'
        induced_cluster(epochs_tot, cond1, cond2, ch, ch_str, window = None, threshold = None, title = 'Hello World')
