import mne
from mne.time_frequency import tfr_morlet, psd_multitaper, psd_welch
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import scipy.io as sio
import pandas as pd
import scipy.io as sio
from scipy.io import savemat, loadmat
from EEG_pareidolia_utils import *

FOLDERPATH = r'E:\PhD\EEG_data\Pareidolia_BIDS'
RUN_LIST = {'pareidolia':['1', '2', '3','4']}
SUBJ_LIST = ['01', '02']
TASK_LIST = ['pareidolia']

def compute_morlet(epochs, fmin, fmax, n_bins):
    EOG_chs = ['E1', 'E8', 'E25', 'E32', 'E126', 'E127']
    Unwanted = ['E43', 'E48', 'E49', 'E128', 'E113', 'E120', 'E125', 'E119']
    All_chs = epochs.info['ch_names'][0:129]
    EEG_chs = [ele for ele in All_chs if ele not in Unwanted]
    EEG_chs = [ele for ele in EEG_chs if ele not in EOG_chs]
    freqs = np.logspace(*np.log10([fmin, fmax]), num=n_bins)
    n_cycles = freqs / 2.  # different number of cycle per frequency

    morlet = tfr_morlet(epochs, freqs=freqs, n_cycles=n_cycles, use_fft=False,
                       return_itc=False, decim=3, n_jobs=1, picks = EEG_chs, average = False)

    return morlet
fmin = 2
fmax = 45
n_bins = 45
##Compute_PSD
for subj in SUBJ_LIST:
    for task in TASK_LIST:
        for run in RUN_LIST[task]:
            epochs_name, epochs_path = get_pareidolia_bids(FOLDERPATH, subj, task, run, stage = 'epo_long_AR', cond=None)
            epochs = mne.read_epochs(epochs_path)
            epochs = epochs.crop(-1.5, 8)
            #Downsampling
            epochs = epochs.copy().resample(500, npad='auto')

            morlet = compute_morlet(epochs, fmin, fmax, n_bins)
            morlet.apply_baseline(mode='ratio', baseline=(None, -0.1))

            psds_file, psds_path = get_pareidolia_bids(FOLDERPATH, subj, task, run, stage = 'Morlet_halfcycle_500Hz')
            morlet.save(psds_path, overwrite = True)
