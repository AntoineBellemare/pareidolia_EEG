import mne # Here we import mne, the package that will contain most of the function that we will use today.
from mne.datasets.brainstorm import bst_raw # It is possible to import functions individually. This is helpful since it
                                            # saves time, memory, and makes the calls to the function easier.
from mne.preprocessing import ICA, create_eog_epochs, create_ecg_epochs
from mne.time_frequency import tfr_morlet, psd_multitaper, psd_welch
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
from autoreject import AutoReject
from EEG_pareidolia_utils import *

#Here you need to put the same FOLDERPATH as in the preprocessing script
FOLDERPATH = r'E:\PhD\EEG_data\Pareidolia_BIDS'
#This variable determines which pareidolia trials will be judged as 'early' or 'late'
RT_thresh = 4000
#Here you choose which runs and subjects you want to epoch
RUN_LIST = {'pareidolia':['4']}
SUBJ_LIST = ['02']
TASK_LIST = ['pareidolia']

#Initialize report
report = mne.Report(verbose=True)
##SAVE EVENTS PLOTS IN REPORT
'''for i, b in enumerate(BLOCS):
    fig = mne.viz.plot_events(events[b], raw_preproc['b1'].info['sfreq']);
    report.add_figs_to_section(fig, captions='Events_plot' + str(i), section='Events')
    #plt.close(fig)'''
##EPOCHING
##This is the main EPOCHING function, which takes as input the subject, task, run, as well as a boolean value whether to include information about
##early vs late pareidolia (slowVSfast = True or False) and whether to include fractal
def epoching(subj, task, run, slowVSfast = False, FD = 'class', window = None):
    preproc_name, preproc_path = get_pareidolia_bids(FOLDERPATH, subj, task, run, stage = 'preproc')
    preproc = mne.io.read_raw_fif(preproc_path)
    events = mne.find_events(preproc, shortest_event = 1) #stim_channel= 'STI 014'
    ##Get Fractal dimension info from behavioral data
    if task == 'pareidolia':
        behav_name, behav_path = get_pareidolia_bids(FOLDERPATH, subj, task, '1', stage = 'behav')
        behav = pd.read_csv(behav_path)
        behav = arrange_dataframe(behav)
        if run == '1':
            behav = behav.loc[behav['bloc'] == 1]
            FDlist = list(np.array(behav['FD']))
        if run == '2':
            behav = behav.loc[behav['bloc'] == 2]
            FDlist = list(np.array(behav['FD']))
        if run == '3':
            behav = behav.loc[behav['bloc'] == 3]
            FDlist = list(np.array(behav['FD']))
        if run == '4':
            behav = behav.loc[behav['bloc'] == 4]
            FDlist = list(np.array(behav['FD']))
    if task == 'RS':
        FDlist = None
    ##Fixing bugs of event ids
    if subj == '01':
        if task == 'pareidolia':
            if run == '1':
                events[:, 2] = np.where(events[:, 2]==3, 1, events[:, 2])
                events[:, 2] = np.where(events[:, 2]==4, 2, events[:, 2])
                events[:, 2] = np.where(events[:, 2]==5, 3, events[:, 2])
                events[:, 2] = np.where(events[:, 2]==6, 4, events[:, 2])
                events[:, 2] = np.where(events[:, 2]==7, 5, events[:, 2])
    if subj == '02':
        if task == 'pareidolia':
            if run == '4':
                events[:, 2] = np.where(events[:, 2]==2, 1, events[:, 2])
                events[:, 2] = np.where(events[:, 2]==3, 2, events[:, 2])
                events[:, 2] = np.where(events[:, 2]==4, 3, events[:, 2])
                events[:, 2] = np.where(events[:, 2]==6, 4, events[:, 2])
                events[:, 2] = np.where(events[:, 2]==5, 5, events[:, 2])
    #print(events)
    #print(FDlist)
    #This line uses the function 'reformat_events', which you can find in EEG_pareidolia_utils, to add information about FD and slowVSfast paeidolia in the
    #event ids.
    events, medianRT = reformat_events(events, FDlist, RT_thresh, task, run, slowVSfast, FD)
    print(events[:50])
    #Here is a CRUCIAL part of the function, which determines which part of the signal is use for each epoch, and for the baseline.
    tmin, tmax = -1.5, 2.5  # Here we define the amount of time we want to keep before (tmin) and after (tmax) the event.
    baseline = (-1.5, 0)
    #Identification of channels of interest
    EOG_chs = ['E1', 'E8', 'E25', 'E32', 'E126', 'E127']
    Unwanted = ['E43', 'E48', 'E49', 'E128', 'E113', 'E120', 'E125', 'E119', 'E129']
    All_chs = preproc.info['ch_names'][0:129]
    EEG_chs = [ele for ele in All_chs if ele not in Unwanted]
    EEG_chs = [ele for ele in EEG_chs if ele not in EOG_chs]

    ##This whole section determines which event_id to choose depending on the task, and the values set for slowVSfast and FD.
    if task == 'RS':
        if run == '1':
            event_id = {'RS10': 100}
        if run == '2':
            event_id = {'RS20': 200}

    if task == 'pareidolia':
        if slowVSfast == False:
            event_id = {'Image_on_nopar': 7, 'Image_on_par': 77}
            if FD == 'all':
                event_id = {'Image_on_nopar_08': 78, 'Image_on_par_08': 778,
                    'Image_on_nopar_09': 79, 'Image_on_par_09': 779,
                    'Image_on_nopar_10': 710, 'Image_on_par_10': 7710,
                    'Image_on_nopar_11': 711, 'Image_on_par_11': 7711,
                    'Image_on_nopar_12': 712, 'Image_on_par_12': 7712,
                    'Image_on_nopar_13': 713, 'Image_on_par_13': 7713,
                    'Image_on_nopar_14': 714, 'Image_on_par_14': 7714,
                    'Image_on_nopar_15': 715, 'Image_on_par_15': 7715,
                    'Image_on_nopar_16': 716, 'Image_on_par_16': 7716,
                    'Image_on_nopar_17': 717, 'Image_on_par_17': 7717,
                    'Image_on_nopar_18': 718, 'Image_on_par_18': 7718,
                    'Image_on_nopar_19': 719, 'Image_on_par_19': 7719,
                    'Image_on_nopar_20': 720, 'Image_on_par_20': 7720,
                   }
            if FD == 'class':
                event_id = {'Image_on_nopar_low': 70, 'Image_on_par_low': 770,
                    'Image_on_nopar_mid': 71, 'Image_on_par_mid': 771,
                    'Image_on_nopar_high': 72, 'Image_on_par_high': 772
                   }
        if slowVSfast == True:
            event_id = {'Image_on_nopar': 7, 'Image_on_par_fast': 77, 'Image_on_par_slow': 777}
            if FD == 'class':
                event_id = {'nopar_low': 70, 'par_low_fast': 770, 'par_low_slow': 7770,
                    'nopar_mid': 71, 'par_mid_fast': 771, 'par_mid_slow': 7771,
                    'nopar_high': 72, 'par_high_fast': 772, 'par_high_slow': 7772}
            if window == 'RT':
                for e in range(len(events)):
                    if (events[e][2] == 7 or events[e][2] == 70 or events[e][2] == 71 or events[e][2] == 72):# and events[e+1][2] != 4):
                        events[e][0] = events[e][0] + medianRT
                event_id = {'early_low': 40, 'early_mid': 41, 'early_high': 42, 'late_low': 440, 'late_mid': 441, 'late_high': 442, 'nopar_low':70, 'nopar_mid':71, 'nopar_high':72 }
    #Here we call the function that generates the epochs, using all the necessary information created earlier
    print(event_id)
    epochs = mne.Epochs(preproc, events=events, event_id=event_id, tmin=tmin,
                        tmax=tmax, baseline=baseline, reject=None, preload = True, picks = EEG_chs)
    #You can get rid of those two line (which perform autorejection of bad epochs) if your computer have difficulties
    ar = AutoReject()
    epochs= ar.fit_transform(epochs)
    return epochs

#This is a simple loop that iterates through our runs for each subject (depending on the subject chosen at the beginning of the script)
for i, subj in enumerate(SUBJ_LIST):
    for j, task in enumerate(TASK_LIST):
        for run in range(len(RUN_LIST[task])):
            run_str = str(run+1)
            ## 'Window = None' when you want epochs for the full trial size (8sec), 'window = 'RT'' when you want epochs around the response event
            epochs = epoching(subj, task, run_str, slowVSfast = True, FD = 'class', window = 'RT')
            #In this line, the 'stage' value needs to begin with 'epo', and then you can add anything at the end to identify which epochs
            #have been created. This will represent the end of the name of the epoched file.
            epochs_file, epochs_path = get_pareidolia_bids(FOLDERPATH, subj, task, '4', stage = 'epo_RT_AR_newEvent')
            epochs.save(epochs_path, overwrite=True)
#ar = AutoReject()
#epochs[b]= ar.fit_transform(epochs[b])

#except:
#    print('File already exists')
#report.add_figs_to_section(np.array(epochs_b1), captions='Events_breakdown' + str(i), section='Events')
#report.add_figs_to_section(np.array(epochs_b2), captions='Events_breakdown' + str(i), section='Events')
#report.add_figs_to_section(np.array(epochs_b3), captions='Events_breakdown' + str(i), section='Events')
#report.add_figs_to_section(np.array(epochs_b4), captions='Events_breakdown' + str(i), section='Events')

#report.save(reportpath + r'\epochs_report.html', open_browser=False);
#try:
#    raw_data.save(savepath, overwrite=False)
#except:
#    print('File already exists')
