from EEG_pareidolia_utils import *
import mne
from mne.datasets.brainstorm import bst_raw
from mne.time_frequency import tfr_morlet, psd_multitaper, psd_welch
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import scipy.io as sio
from scipy.io import savemat, loadmat

FOLDERPATH = r'E:\PhD\EEG_data\Pareidolia_BIDS'
FREQ_BANDS = [[1, 3], [4, 7], [8, 12], [13, 19], [20, 29], [30, 45], [46, 60]]
FREQ_NAMES = ['delta', 'theta', 'alpha', 'low-beta', 'high-beta', 'gamma1', 'gamma2']
RUN_LIST = {'pareidolia':['1','2','3'],
              'RS':['1', '2']}
SUBJ_LIST = ['01', '02']
TASK_LIST = ['pareidolia']

#CONDITIONS_LIST = [[770, 771], [771, 772], [770, 772], [70, 71], [71, 72], [70, 72], [70, 770], [71, 771], [72, 772]]
CONDITIONS_LIST = [[770, 7770], [71, 771], [72, 772]]

CONDITIONS = ['parNOpar', 'slowVSfast', 'FD01', 'FD02', 'FD12'] #Here you define the conditions you want to compare
                                                                #FD01: low vs mid ; FD02: low vs high ; FD12: mid vs high

#all_PSDs = []
for subj in SUBJ_LIST:
    #subj_PSD = []
    task_PSD, sham_PSD, epochs_tot = taskVSsham(subj, 'PSD_long_AR_pnp', 'epo_long_AR_pnp', FOLDERPATH)
    for c in CONDITIONS_LIST:
            cond1_tot = []
            cond2_tot = []
            #Split by conditions for each of the 3 first blocs (task_PSD)
            for i in range(len(task_PSD)):
                epochs_id = str(i+1)
                cond1, cond2= split_by_condition(task_PSD[i], epochs_tot[epochs_id], a=c[0], b=c[1], condition = None, epochs_type = 'Long') #epochs_type could be 'Long' or 'RT'
                cond1_tot.append(cond1)
                cond2_tot.append(cond2)
            cond1_tot = np.array(cond1_tot)
            cond2_tot = np.array(cond2_tot)
            all_blocs1 = np.append(cond1_tot[0], cond1_tot[1], axis = 0)
            all_blocs1 = np.append(all_blocs1, cond1_tot[2], axis = 0)
            all_blocs2 = np.append(cond2_tot[0], cond2_tot[1], axis = 0)
            all_blocs2 = np.append(all_blocs2, cond2_tot[2], axis = 0)
            sham1, sham2 = split_by_condition(sham_PSD, epochs_tot['4'], c[0], c[1], condition = None)

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
                reportname, reportpath = get_pareidolia_bids(FOLDERPATH, subj, 'pareidolia', '-', stage = 'fig_ttest_RT_1secAfter'+str(c[0])+''+str(c[1]))
                fig, ax = array_topoplot(value_to_plot, ch_xy, vmin=vmin, vmax=vmax, showtitle=True, titles=FREQ_NAMES, mask = p_welch_multitaper, figpath = reportpath);
