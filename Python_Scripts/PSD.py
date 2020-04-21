import mne
from mne.datasets.brainstorm import bst_raw
from mne.time_frequency import tfr_morlet, psd_multitaper, psd_welch
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import scipy.io as sio
import brainpipe
from brainpipe import feature
import pandas as pd
import scipy.io as sio
from scipy.io import savemat, loadmat
from EEG_pareidolia_utils import get_pareidolia_bids, reformat_events

FOLDERPATH = r'E:\PhD\EEG_data\Pareidolia_BIDS'
FREQ_BANDS = [[1, 3], [4, 7], [8, 12], [13, 19],[20, 29], [30, 45], [46, 60]]
FREQ_NAMES = ['delta', 'theta', 'alpha', 'low-beta', 'high-beta', 'gamma1', 'gamma2']

RUN_LIST = {'pareidolia':['1', '2', '3','4']}
SUBJ_LIST = ['01', '02']
TASK_LIST = ['pareidolia']

#import pdb; pdb.set_trace

#This function is used to compute power values for each frequency bands on each epochs
def compute_psd(epochs, FREQ_BANDS, function=psd_welch, tmin = None, tmax = None):
    #epochs are cropped as desire (tmin could be before '0', ex: -1.5, depending on the values used during epoching)
    epochs = epochs.apply_baseline((-1.5, -0.1))
    epochs = epochs.crop(tmin, tmax)
    print(epochs.get_data().shape)
    PSDs = []
    #This loop iterates for each epoch
    for t in range(len(epochs[:].get_data())):
        psds_temp = []
        EOG_chs = ['E1', 'E8', 'E25', 'E32', 'E126', 'E127']
        Unwanted = ['E43', 'E48', 'E49', 'E128', 'E113', 'E120', 'E125', 'E119', 'E129']
        All_chs = epochs.info['ch_names'][0:129]
        EEG_chs = [ele for ele in All_chs if ele not in Unwanted]
        EEG_chs = [ele for ele in EEG_chs if ele not in EOG_chs]
        for min, max in FREQ_BANDS:
            psds, freqs = function(epochs[t], fmin=min, fmax=max, n_jobs=1, picks = EEG_chs)  #PSDs are calculated with this function, giving power values and corresponding frequency bins as output
            psds = 10. * np.log10(psds)   #PSDs values are transformed in log scale to compensate for the 1/f natural slope
            psds_mean = np.average(psds, axis=0) #Get rid of an empty dimension
            psds_mean = np.average(psds_mean, axis=1) #Average across bins to obtain one value for the entire frequency range
            psds_temp.append(psds_mean)
        PSDs.append(psds_temp)
    PSDs = np.array(PSDs)
    return PSDs

#We don't use this function for the moment.
'''def compute_PSD_bp(epochs, sf, epochs_length, f=None):
    EEG_chs_n = list(range(1,125))
    if f == None:
        f = [ [4, 8], [8, 12], [12, 20], [20, 30], [30, 60], [60, 90], [90, 120] ]
    # Choose MEG channels
    data = epochs.get_data(picks = EEG_chs_n) # On sort les data de l'objet MNE pour les avoir dans une matrice (un numpy array pour être précis)
    data = data.swapaxes(0,1).swapaxes(1,2) # On réarange l'ordre des dimensions pour que ça correspond à ce qui est requis par Brainpipe
    objet_PSD = feature.power(sf=int(sf), npts=int(sf*epochs_length), width=int((sf*epochs_length)/2), step=int((sf*epochs_length)/4), f=f, method='hilbert1') # La fonction Brainpipe pour créer un objet de calcul des PSD
    #data = data[:,0:960,:] # weird trick pour corriger un pb de segmentation jpense
    #print(data.shape)
    psds = objet_PSD.get(data)[0] # Ici on calcule la PSD !
    return psds'''

##Compute_PSD
for subj in SUBJ_LIST:
    for task in TASK_LIST:
        for run in RUN_LIST[task]:
            epochs_name, epochs_path = get_pareidolia_bids(FOLDERPATH, subj, task, run, stage = 'epo_RT_AR_newEvent', cond=None)
            epochs = mne.read_epochs(epochs_path)
            #Si vous voulez comparer les epochs entières (8sec), il est mieux de laisser de côté le début et la fin des epochs.
            psds_welch= compute_psd(epochs, FREQ_BANDS, psd_multitaper, tmin = 1, tmax = 2.4)
            #le nom du stage doit commencer par PSD, la fin du nom est à votre choix
            psds_file, psds_path = get_pareidolia_bids(FOLDERPATH, subj, task, run, stage = 'PSD_RT_AR_newEvent')
            savemat(psds_path, {'PSD': psds_welch})
