from EEG_pareidolia_utils import get_pareidolia_bids, reformat_events, match_n_trials, split_by_condition, split_FD_anova, array_topoplot, p_values_boolean
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

RUN_LIST = {'pareidolia':['1','2','3'],#,'4'],
              'RS':['1', '2']}
SUBJ_LIST = ['01', '02']
TASK_LIST = ['pareidolia']
report = mne.Report(verbose=True)

for subj in SUBJ_LIST:
    subj_PSD = []
    for task in TASK_LIST:
        task_PSD = []
        sham_PSD = []
        epochs_tot = {}
        for e, run in enumerate(RUN_LIST[task]):
            #I faut changer le nom des 2 variables 'stage' pour qu'ils correspondent à vos noms de fichiers PSD et epochs
            PSD_name, PSD_path = get_pareidolia_bids(FOLDERPATH, subj, task, run, stage = 'PSD_long_AR_cropped(0.3-7.7)', cond=None)
            epo_name, epo_path = get_pareidolia_bids(FOLDERPATH, subj, task, run, stage = 'epo_long_AR', cond=None)
            epochs = mne.read_epochs(epo_path)
            print(epochs)
            epochs_data = epochs.get_data()
            PSD = loadmat(PSD_path)
            PSD = PSD['PSD']
            print(PSD.shape)
            epochs_tot[run] = epochs
            print(e)
            if e < 3:
                task_PSD.append(PSD)
            else:
                sham_PSD = PSD
        task_PSD = np.array(task_PSD)

        sham_PSD = np.array(sham_PSD)

        cond1_tot = []
        cond2_tot = []
        cond3_tot = []
        for i in range(len(task_PSD)):
            epochs_id = str(i+1)
            cond1, cond2, cond3= split_FD_anova(task_PSD[i], epochs_tot[epochs_id])
            cond1_tot.append(cond1)
            cond2_tot.append(cond2)
            cond3_tot.append(cond3)
        cond1_tot = np.array(cond1_tot)
        cond2_tot = np.array(cond2_tot)
        cond3_tot = np.array(cond3_tot)
        all_blocs1 = np.append(cond1_tot[0], cond1_tot[1], axis = 0)
        all_blocs1 = np.append(all_blocs1, cond1_tot[2], axis = 0)
        all_blocs2 = np.append(cond2_tot[0], cond2_tot[1], axis = 0)
        all_blocs2 = np.append(all_blocs2, cond2_tot[2], axis = 0)
        all_blocs3 = np.append(cond3_tot[0], cond3_tot[1], axis = 0)
        all_blocs3 = np.append(all_blocs3, cond3_tot[2], axis = 0)

        import scipy.stats as stats
        EOG_chs = ['E1', 'E8', 'E25', 'E32', 'E126', 'E127']
        Unwanted = ['E43', 'E48', 'E49', 'E128', 'E113', 'E120', 'E125', 'E119', 'E129']#, 'E114']
        layout = mne.channels.find_layout(epochs.info, ch_type='eeg', exclude = EOG_chs + Unwanted)
        ch_xy = layout.pos[0:124]
        f, pval = stats.f_oneway(all_blocs1, all_blocs2, all_blocs3)
        p_welch_multitaper = p_values_boolean(pval*114)
        #Low values indicate that the first element of t-test is lower than the second element
        value_to_plot = f
        extreme = np.max((abs(np.min(np.min(np.array(value_to_plot)))), abs(np.max(np.max(np.array(value_to_plot))))))
        vmax = extreme
        vmin = 0
        fig, ax = array_topoplot(value_to_plot, ch_xy, vmin=vmin, vmax=vmax, showtitle=True, titles=FREQ_NAMES, mask = p_welch_multitaper);
        #array_topoplot(value_to_plot2, ch_xy, vmin=np.min(np.min(np.array(value_to_plot2))), vmax=np.max(np.max(np.array(value_to_plot2))), showtitle=True, titles=FREQ_NAMES);
        #fig = raw_data.plot(show=False, start = start_value, order = order);
        report.add_figs_to_section(fig, captions = 'One-way ANOVA between 3 FD classes (F values)' , section='F values topomap', comments = None)
        plt.close(fig)
        reportname, reportpath = get_pareidolia_bids(FOLDERPATH, subj, task, run, stage = 'report_ANOVA_FD_AR')
        report.save(reportpath, open_browser=True);
