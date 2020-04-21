from EEG_pareidolia_utils import *
import mne
from mne.datasets.brainstorm import bst_raw
from mne.time_frequency import tfr_morlet, psd_multitaper, psd_welch
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import scipy.io as sio
from scipy.io import savemat, loadmat
from param import *


RUN_LIST = {'pareidolia':['1','2','3','4'],
              'RS':['1', '2']}
SUBJ_LIST = ['01', '02']
TASK_LIST = ['pareidolia']
COMPLEX_LIST = ['Spectral Entropy', 'SVD', 'Hurst']
report = mne.Report(verbose=True)

def p_values_boolean(p_values):
    p_values_boolean = p_values.copy()
    for e in range(p_values.shape[1]):
        for c in range(p_values.shape[0]):
            if p_values[c, e] < 0.05:
                p_values_boolean[c, e] = True
            else:
                p_values_boolean[c, e] = False
    p_values_boolean = np.array(p_values_boolean, dtype='bool')
    return(p_values_boolean)

def comp2array(cp):
    cp01 = []
    for i in range(len(cp)):
        cp_comp = []
        for c in range(len(COMPLEX_LIST)):
            cp_temp = []
            for j in range(len(cp[0])):
                cp_temp.append(cp[i][j][0][0][c][0][0])
            cp_comp.append(cp_temp)
        cp01.append(cp_comp)
    cp01 = np.array(cp01)
    return cp01

CONDITIONS = ['parNOpar', 'slowVSfast', 'FD01', 'FD02', 'FD12']
all_complex = []
for subj in SUBJ_LIST:
    subj_cp = []
    for task in TASK_LIST:
        task_cp = []
        sham_cp = []
        epochs_tot = {}
        for e, run in enumerate(RUN_LIST[task]):
            cp_name, cp_path = get_pareidolia_bids(FOLDERPATH, subj, task, run, stage = 'Complexity_RT_before', cond=None)
            epo_name, epo_path = get_pareidolia_bids(FOLDERPATH, subj, task, run, stage = 'epo_RT_before', cond=None)
            epochs = mne.read_epochs(epo_path)
            epochs_data = epochs.get_data()
            complexity_mat = loadmat(cp_path)
            complexity_mat = complexity_mat['Complexity']
            epochs_tot[run] = epochs
            if e < 3:
                task_cp.append(complexity_mat)
            else:
                sham_cp = complexity_mat
        task_cp = np.array(task_cp)
        print(task_cp.shape)
        sham_cp = np.array(sham_cp)

        for c in CONDITIONS:
                cond1_tot = []
                cond2_tot = []
                #Split by conditions for each of the 3 first blocs (task_PSD)
                for i in range(len(task_cp)):
                    epochs_id = str(i+1)
                    cond1, cond2= split_by_condition(task_cp[i], epochs_tot[epochs_id], None, None, condition = c, epochs_type = 'RT') #epochs_type could be 'Long' or 'RT'
                    cond1 = comp2array(cond1)
                    cond2 = comp2array(cond2)
                    cond1_tot.append(cond1)
                    cond2_tot.append(cond2)
                cond1_tot = np.array(cond1_tot)
                cond2_tot = np.array(cond2_tot)
                all_blocs1 = np.append(cond1_tot[0], cond1_tot[1], axis = 0)
                all_blocs1 = np.append(all_blocs1, cond1_tot[2], axis = 0)
                all_blocs2 = np.append(cond2_tot[0], cond2_tot[1], axis = 0)
                all_blocs2 = np.append(all_blocs2, cond2_tot[2], axis = 0)
                sham1, sham2 = split_by_condition(sham_cp, epochs_tot['4'], c[0], c[1], condition = c)

                TTEST_LIST = [all_blocs1, all_blocs2]#, sham1, sham2]
                TTEST_LIST_str = ['all_blocs1', 'all_blocs2']#, 'sham1', 'sham2']
                conditions_string = str(c)

                #Determine the channels to use in the topomap
                EOG_chs = ['E1', 'E8', 'E25', 'E32', 'E126', 'E127']
                Unwanted = ['E43', 'E48', 'E49', 'E128', 'E113', 'E120', 'E125', 'E119', 'E129']#, 'E114']
                layout = mne.channels.find_layout(epochs_tot['1'].info, ch_type='eeg', exclude = EOG_chs + Unwanted)
                ch_xy = layout.pos[0:124]

                from itertools import combinations
                t_list = list(combinations(TTEST_LIST, 2))
                t_list_str = list(combinations(TTEST_LIST_str, 2))
                for t in range(len(t_list)):
                    #This function take the two conditions matrices and makes them of equal size (equal number of trials for each condition)
                    ttest1, ttest2 = match_n_trials(t_list[t][0], t_list[t][1])
                    print(np.array(ttest1).shape)
                    results_multitaper, t_multitaper, p_multitaper = compute_t_test(ttest1, ttest2)
                    #Generate a matrix of boolean values (0 or 1) to determine if p-value is significant (alpha value can be changed in p_value_boolean function)
                    #p_values are multiplied by the number of electrodes to correct for multiple comparisons (Bonferonni correction)
                    p_welch_multitaper = p_values_boolean(p_multitaper*114)
                    #Low values indicate that the first element of t-test is lower than the second element
                    value_to_plot = t_multitaper #t-values are plotted
                    extreme = np.max((abs(np.min(np.min(np.array(value_to_plot)))), abs(np.max(np.max(np.array(value_to_plot)))))) # adjust the range of values
                    vmax = extreme
                    vmin = -extreme
                    reportname, reportpath = get_pareidolia_bids(FOLDERPATH, subj, 'pareidolia', '-', stage = 'fig_ttest_complexity_RTbefore'+c)
                    fig, ax = array_topoplot(value_to_plot, ch_xy, vmin=vmin, vmax=vmax, showtitle=True, titles=COMPLEX_LIST, mask = p_welch_multitaper, figpath = reportpath);
