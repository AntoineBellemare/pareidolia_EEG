
import os
import numpy as np
import mne
from scipy.io import loadmat, savemat
from mne.io import read_raw_egi, read_raw_fif
import matplotlib.pyplot as plt
from mne.preprocessing import ICA, create_eog_epochs, create_ecg_epochs
from EEG_pareidolia_utils import get_pareidolia_bids

def pareidolia_preproc(filepath, savepath, reportpath):
    if task == 'pareidolia':
        start_value = 300.0
    if task == 'RS':
        start_value = 30
    order = list(range(40,61))
    report = mne.Report(verbose=True)
    raw_data = read_raw_fif(filepath, preload=True)
    picks = mne.pick_types(raw_data.info, eeg=True, eog=True, exclude='bads')
    fig = raw_data.plot(show=False, start = start_value, order = order);
    report.add_figs_to_section(fig, captions='Time series', section='Raw data')
    plt.close(fig)
    ## Set channel labels
    #Define channels of interest
    EOG_chs = ['E1', 'E8', 'E25', 'E32', 'E126', 'E127']
    Unwanted = ['E43', 'E48', 'E49', 'E128', 'E113', 'E120', 'E125', 'E119', 'E129']
    All_chs = raw_data.info['ch_names'][0:129]
    EEG_chs = [ele for ele in All_chs if ele not in Unwanted]
    EEG_chs = [ele for ele in EEG_chs if ele not in EOG_chs]

    fig = raw_data.plot_psd(average=False, picks=EEG_chs, show=False, xscale = 'log', fmin = 0.5, fmax = 100, n_overlap = 1024);
    report.add_figs_to_section(fig, captions='PSD', section='Raw data')
    #plt.close(fig)
    ## Adding x, y positions of electrodes
    mon = mne.channels.read_montage('GSN-HydroCel-128')
    raw_data.set_montage(mon)



    ## Filtering
    high_cutoff = 150
    low_cutoff = 0.5
    raw_data.filter(low_cutoff, high_cutoff, fir_design="firwin")
    raw_data.notch_filter(np.arange(60, high_cutoff+1, 60), picks=EEG_chs, filter_length='auto',phase='zero', fir_design="firwin")
    fig = raw_data.plot_psd(average=False, picks=EEG_chs, show=False, xscale = 'log', fmin = 0.5, fmax = 100, n_overlap = 1024);
    report.add_figs_to_section(fig, captions='PSD', section='Filtered data')
    plt.close(fig)

    ## ICA
    ##You can vary the number of components here (values between 0 and 1 represent a percentage of explained variance : 0.95 means 95% of the variance explained)
    ica = ICA(n_components=20, random_state=0).fit(raw_data, decim=3, picks = EEG_chs)
    fig = ica.plot_sources(raw_data, show=False, start = start_value);
    report.add_figs_to_section(fig, captions='Independent Components', section='ICA')
    plt.close(fig)

    ## FIND ECG COMPONENTS
    ##Here you can change the ECG threshold
    ecg_threshold = 0.25
    ecg_epochs = create_ecg_epochs(raw_data, ch_name='ECG')
    ecg_inds, ecg_scores = ica.find_bads_ecg(ecg_epochs, ch_name='ECG', method='ctps', threshold=ecg_threshold)
    fig = ica.plot_scores(ecg_scores, ecg_inds, show=False);
    report.add_figs_to_section(fig, captions='Correlation with ECG (EEG059)', section='ICA - ECG')
    plt.close(fig)
    fig = list()
    try:
        fig = ica.plot_properties(ecg_epochs, picks=ecg_inds, image_args={'sigma': 1.}, show=False);
        for i, figure in enumerate(fig):
            report.add_figs_to_section(figure, captions='Detected component ' + str(i), section='ICA - ECG')
            #plt.close(fig)
    except:
        print('No component to remove')

    ## FIND EOG COMPONENTS
    ##Here you can change the EOG threshold
    eog_threshold = 2.5
    eog_epochs = create_eog_epochs(raw_data, ch_name='E127')
    eog_inds, eog_scores = ica.find_bads_eog(eog_epochs, ch_name='E127', threshold=eog_threshold)
    fig = ica.plot_scores(eog_scores, eog_inds, show=False);
    report.add_figs_to_section(fig, captions='Correlation with EOG (E127)', section='ICA - EOG')
    plt.close(fig)
    fig = list()
    try:
        fig = ica.plot_properties(eog_epochs, picks=eog_inds, image_args={'sigma': 1.}, show=False);
        for i, figure in enumerate(fig):
            report.add_figs_to_section(figure, captions='Detected component ' + str(i), section='ICA - EOG')
            #plt.close(fig)
    except:
        print('No component to remove')

    ## EXCLUDE COMPONENTS
    ica.exclude = ecg_inds
    ica.apply(raw_data)
    ica.exclude = eog_inds
    ica.apply(raw_data)
    fig = raw_data.plot(show=False, start = start_value, order=order); # Plot the clean signal.
    report.add_figs_to_section(fig, captions='After filtering + ICA', section='Raw data')
    plt.close(fig)
    ## SAVE PREPROCESSED FILE
    report.save(reportpath, open_browser=True);
    try:
        #raw_data = raw_data
        raw_data.save(savepath, overwrite=True)
    except:
        print('File already exists')

    return raw_data

##Remplacer le path de cette variable
FOLDERPATH = r'E:\PhD\EEG_data\Pareidolia_BIDS'
##Ne pas inclure 'RS' si vous ne voulez pas faire le processing des blocs Resting State
RUN_LIST = {'pareidolia':['1','2','3','4'],
              'RS':['1', '2']}
##Choisir le ou les participants à processer.
SUBJ_LIST = ['01', '02']
TASK_LIST = ['pareidolia', 'RS']

#for subj, ecg, eog in zip(SUBJ_LIST, ECG_DICT, EOG_DICT):
for subj in SUBJ_LIST:
    for task in TASK_LIST:
        for run in RUN_LIST[task]:
            filename, filepath = get_pareidolia_bids(FOLDERPATH, subj, task, run, stage = 'eeg', cond=None)
            preproc_name, preproc_path = get_pareidolia_bids(FOLDERPATH, subj, task, run, stage = 'preproc', cond=None)
            report_name, report_path = get_pareidolia_bids(FOLDERPATH, subj, task, run, stage = 'report_preproc', cond=None)

            pareidolia_preproc(filepath, preproc_path, report_path)
