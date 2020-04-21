import mne_bids
import mne
import os
import os.path as op
import numpy as np
from EEG_pareidolia_utils import reformat_events
from mne_bids import make_bids_folders, make_bids_basename, write_raw_bids


BIDS_PATH = r'E:\PhD\EEG_data\Pareidolia_BIDS'
ACQ_PATH = r'E:\PhD\EEG_data\Pareidolia_Acquisition'
EVENT_ID = {'Gray': 0, 'Cross': 1,
            'Image_on_nopar': 2, 'Image_on_par': 21, 'Image_off': 3,
            'RT': 4, 'lateRT': 44, 'RS10': 100,
            'RS11': 101, 'RS20': 200,
            'RS21': 201}

EVENT_ID_SHORT = {
            'Image_on_nopar': 7,
            'Image_on_par': 77, 'RT': 4, 'lateRT': 44, 'RS10': 100,
            'RS20': 200
            }
RT_thresh = 2000
# check if BIDS_PATH exists, if not, create it
if not os.path.isdir(BIDS_PATH):
    os.mkdir(BIDS_PATH)
    print('BIDS folder created at : {}'.format(BIDS_PATH))
else:
    print('{} already exists.'.format(BIDS_PATH))

# list folders in acquisition folder
recording_folders = os.listdir(ACQ_PATH)
session = 'EEG'
# loop across recording folders (folder containing the recordings of the day)
for participants in recording_folders: # folders are named by date in format YYYYMMDD
    for file in os.listdir(op.join(ACQ_PATH, participants)):
        # Rewrite in BIDS format if doesn't exist yet
        subject = file[1:3]
        if 'b' in file:
            task = 'pareidolia'
            run = file[5]
        else:
            task = 'RS'
            run = file[11]

        bids_basename = make_bids_basename(subject=subject, session=session, task=task, run=run)
        if not op.isdir(op.join(BIDS_PATH, 'sub-{}'.format(subject), 'ses-{}'.format(session), 'EEG', bids_basename + '_eeg.ds')):
            raw_fname = op.join(ACQ_PATH, participants, file)
            raw = mne.io.read_raw_fif(raw_fname, preload=False)

            try:
                events = mne.find_events(raw, shortest_event = 1)

                if subject == '01':
                    if task == 'pareidolia':
                        if run ==    '1':
                            events[:, 2] = np.where(events[:, 2]==3, 0, events[:, 2])
                            events[:, 2] = np.where(events[:, 2]==4, 1, events[:, 2])
                            events[:, 2] = np.where(events[:, 2]==5, 2, events[:, 2])
                            events[:, 2] = np.where(events[:, 2]==6, 3, events[:, 2])
                            events[:, 2] = np.where(events[:, 2]==7, 4, events[:, 2])
                events = reformat_events(events, FDlist = None, RT_thresh = 4000, task = task, run = run, slowVSfast = False, FD = None)
                #raw.add_events(self, events, stim_channel='STI 014', replace=True)
                write_raw_bids(raw, bids_basename, BIDS_PATH, events_data=events, event_id=EVENT_ID_SHORT, overwrite=True)
            except:
                write_raw_bids(raw, bids_basename, BIDS_PATH, overwrite=True)
