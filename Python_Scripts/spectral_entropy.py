from EEG_pareidolia_utils import get_pareidolia_bids, reformat_events, match_n_trials, split_by_condition, compute_t_test, array_topoplot
import mne # Here we import mne, the package that will contain most of the function that we will use today.
from mne.datasets.brainstorm import bst_raw # It is possible to import functions individually. This is helpful since it
                                            # saves time, memory, and makes the calls to the function easier.
from mne.preprocessing import ICA, create_eog_epochs, create_ecg_epochs
import time
import numpy as np
import scipy.io as sio
from scipy.io import savemat, loadmat
import nolds
import neurokit as nk
from pyentrp import entropy as ent
from scipy import stats
import matplotlib.pyplot as plt

FOLDERPATH = r'E:\PhD\EEG_data\Pareidolia_BIDS'
FREQ_BANDS = [[1, 3], [4, 7], [8, 12], [13, 19], [20, 29], [30, 45], [46, 60]]
SPECTRAL_NAMES = ['spectral_delta', 'spectral_theta', 'spectral_alpha', 'spectral_low-beta', 'spectral_high-beta', 'spectral_gamma1', 'spectral_gamma2']

RUN_LIST = {'pareidolia':['1','2','3','4'],
              'RS':['1', '2']}
SUBJ_LIST = ['01', '02']
TASK_LIST = ['pareidolia', 'RS']


##Compute complexity

for freq, name in zip(FREQ_BANDS, SPECTRAL_NAMES):
    for subj in SUBJ_LIST:
        for task in TASK_LIST:
            for run in RUN_LIST[task]:
                epochs_name, epochs_path = get_pareidolia_bids(FOLDERPATH, subj, task, run, stage = 'epo_FDclass_slowVSfast', cond=None)
                epochs = mne.read_epochs(epochs_path)
                epochs_data = epochs.get_data()
                complex_tot = []
                for i in range(len(epochs_data)):
                    complex_trials = []
                    for j in range(114):
                        complexity_eeg = nk.complexity(epochs_data[i, j, :], sampling_rate=epochs.info['sfreq'],
                                            shannon=False, sampen=False, multiscale=False, spectral=True, svd=False,
                                            correlation=False, higushi=False, petrosian=False, fisher=False, hurst=False,
                                             dfa=False, lyap_r=False, lyap_e=False, bands=freq)
                        #print(complexity_eeg.shape)
                        complex_trials.append(complexity_eeg)
                    complex_tot.append(complex_trials)
                complex_tot = np.array(complex_tot)
                complex_file, complex_path = get_pareidolia_bids(FOLDERPATH, subj, task, run, stage = name)
                savemat(complex_path, {name: complex_tot})
