#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.3),
    on February 16, 2021, at 14:21
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock, parallel
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'Cloud_Experiment_FR_REAL'  # from the Builder filename that created this script
expInfo = {'session': '001', 'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1024, 768], fullscr=True, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
Instruction = visual.TextStim(win=win, name='Instruction',
    text=u"Bienvenue \xe0 cette exp\xe9rience sur la par\xe9idolie.\nL'exp\xe9rience se divise en quatre blocs.\nChaque bloc sera s\xe9par\xe9 d'une question sur votre \xe9tat de fatigue mentale.\nVous aurez l'occasion, entre chaque bloc, de prendre quelques minutes de repos.\n\nAppuyez sur la barre d'espacement.\n\n",
    font='Arial',
    pos=[0, 0], height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Instructions2"
Instructions2Clock = core.Clock()
instructions2 = visual.TextStim(win=win, name='instructions2',
    text=u"T\xe2che:\n\nDes images de nuages informatiques vous seront pr\xe9sent\xe9es.\nVotre t\xe2che consistera \xe0 percevoir le plus grand nombre de formes figuratives dans chaque image.\nLorsque vous aurez d\xe9tect\xe9 une premi\xe8re forme figurative, vous devrez appuyer sur la barre d'espacement.\nVous aurez par la suite \xe0 continuer votre recherche de formes figuratives pendant toute la pr\xe9sentation de l'image.\nApr\xe8s chaque image, il vous sera demand\xe9 le nombre total de formes per\xe7ues.\nSi vous n'avez per\xe7u aucune forme lors de la pr\xe9sentation d'une image, appuyez sur ''q'' pour passer \xe0 l'image suivante \nSi toutefois vous r\xe9pondez \xe0 la question sur le nombre de formes per\xe7ues, il vous sera demand\xe9 d'indiquer la vividit\xe9 de votre perception. \n\n\xc0 la fin de l'exp\xe9rience, les images pour lesquelles vous avez r\xe9pondu avoir per\xe7u une forme figurative fortement vivide vous seront pr\xe9sent\xe9es \xe0 nouveau\nafin que vous partagiez vos perceptions avec l'exp\xe9rimentateur.\n\nAppuyez sur la barre d'espacement pour continuer",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Instruction3"
Instruction3Clock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text=u"La vividit\xe9 r\xe9f\xe8re \xe0 la clart\xe9 de l'image mentale.\nSi l'image est vivide, cela signifie qu'elle est tr\xe8s claire dans votre esprit et facilement rem\xe9morable.\nSi vous avez per\xe7u plusieurs formes, Veuillez r\xe9pondre \xe0 la question sur la vividit\xe9 en vous r\xe9f\xe9rant \xe0 la forme la plus vivide.\n\nVous commencerez par un bloc d'essai pour vous familiariser avec la t\xe2che.\n\nVeuillez appuyer sur la barre d'espacement pour r\xe9pondre \xe0 la premi\xe8re question sur votre fatigue mentale.\n\nBonne exp\xe9rience!",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Mental_fatigue"
Mental_fatigueClock = core.Clock()
Fatigue = visual.RatingScale(win=win, name='Fatigue', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=10, labels=[u'\xc9tat de fatigue absolu', u" \xc9tat d'\xe9veil absolu"], scale='Veuillez indiquer votre niveau de fatigue mentale')

# Initialize components for Routine "Resting_state_instructions"
Resting_state_instructionsClock = core.Clock()
Resting = visual.TextStim(win=win, name='Resting',
    text=u"Avant de d\xe9buter l'exp\xe9rience,\nnous allons vous demander de rester immobile\npendant 3 min, les yeux ouverts.\nVous n'avez aucune t\xe2che particuli\xe8re \xe0 effectuer\npendant ces 3 minutes, mis \xe0 part garder votre\nregard fix\xe9 sur la croix de fixation.\n\nIl vous sera demand\xe9 de faire le m\xeame exercice\n\xe0 la fin de l'exp\xe9rience.\n\nAppuyez sur la barre d'espacement pour d\xe9buter le 3 minutes",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Resting_state"
Resting_stateClock = core.Clock()
fix_resting_state = visual.ImageStim(
    win=win, name='fix_resting_state',
    image=u'fixation_cross', mask=None,
    ori=0, pos=(0, 0), size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
RS01_in = parallel.ParallelPort(address=u'0x0378')
RS01_out = parallel.ParallelPort(address=u'0x0378')

# Initialize components for Routine "Start_pratique"
Start_pratiqueClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text=u"Le bloc de pratique est constitu\xe9 de 10 essais.\nVeuillez appuyer sur la barre d'espacement pour commencer le bloc de pratique.\n",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
empty_gray = visual.ImageStim(
    win=win, name='empty_gray',
    image='empty_gray', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fixation_cross = visual.ImageStim(
    win=win, name='fixation_cross',
    image='fixation_cross', mask=None,
    ori=0, pos=(0, 0), size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
n_objets = visual.RatingScale(win=win, name='n_objets', marker='triangle', size=1.0, pos=[0.0, 0.0], low=1, high=5, labels=['1', ' 5 et plus'], scale=u"Veuillez indiquer le nombre d'objets significatifs per\xe7us", disappear=True)
vividness = visual.RatingScale(win=win, name='vividness', marker='triangle', size=1, pos=[0.0, 0.0], low=1, high=5, labels=[u'Tr\xe8s peu vivide', u' Fortement vivide'], scale=u'Veuillez indiquer la vividit\xe9 de votre perception', disappear=True)
cross = parallel.ParallelPort(address=u'0x0378')
image_in = parallel.ParallelPort(address=u'0x0378')
image_out = parallel.ParallelPort(address=u'0x0378')
RT = parallel.ParallelPort(address=u'0x0378')

# Initialize components for Routine "Startx"
StartxClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=u"Appuyez sur la barre d'espacement \npour commencer l'exp\xe9rience\n",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
empty_gray = visual.ImageStim(
    win=win, name='empty_gray',
    image='empty_gray', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fixation_cross = visual.ImageStim(
    win=win, name='fixation_cross',
    image='fixation_cross', mask=None,
    ori=0, pos=(0, 0), size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
n_objets = visual.RatingScale(win=win, name='n_objets', marker='triangle', size=1.0, pos=[0.0, 0.0], low=1, high=5, labels=['1', ' 5 et plus'], scale=u"Veuillez indiquer le nombre d'objets significatifs per\xe7us", disappear=True)
vividness = visual.RatingScale(win=win, name='vividness', marker='triangle', size=1, pos=[0.0, 0.0], low=1, high=5, labels=[u'Tr\xe8s peu vivide', u' Fortement vivide'], scale=u'Veuillez indiquer la vividit\xe9 de votre perception', disappear=True)
cross = parallel.ParallelPort(address=u'0x0378')
image_in = parallel.ParallelPort(address=u'0x0378')
image_out = parallel.ParallelPort(address=u'0x0378')
RT = parallel.ParallelPort(address=u'0x0378')

# Initialize components for Routine "Fin_bloc"
Fin_blocClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text=u"Vous venez de terminer le bloc.\n\nAppuyez la sur la barre d'espacement pour r\xe9pondre \xe0 quelques questions avant de prendre votre pause.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Mental_fatigue"
Mental_fatigueClock = core.Clock()
Fatigue = visual.RatingScale(win=win, name='Fatigue', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=10, labels=[u'\xc9tat de fatigue absolu', u" \xc9tat d'\xe9veil absolu"], scale='Veuillez indiquer votre niveau de fatigue mentale')

# Initialize components for Routine "Flow"
FlowClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text=u"Court questionnaire sur l'\xe9tat de flow\n\nVeuillez r\xe9pondre aux questions suivantes concernant votre exp\xe9rience du bloc que vous venez de terminer.\n\n1 = Total d\xe9saccord  //  7 = Total accord\n\nAppuyez sur la barre d'espacement pour commencer",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Flow_questions"
Flow_questionsClock = core.Clock()
Flow01 = visual.RatingScale(win=win, name='Flow01', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u'Je ressens le parfait niveau de d\xe9fi', disappear=True)
Flow02 = visual.RatingScale(win=win, name='Flow02', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u'Mes pens\xe9es/actions se d\xe9roulent fluidement', disappear=True)
Flow03 = visual.RatingScale(win=win, name='Flow03', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u'Je ne vois pas le temps pass\xe9', disappear=True)
Flow04 = visual.RatingScale(win=win, name='Flow04', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u"Je n'ai pas de difficult\xe9 \xe0 me concentrer", disappear=True)
Flow05 = visual.RatingScale(win=win, name='Flow05', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u'Mon esprit est compl\xe8tement clair', disappear=True)
Flow06 = visual.RatingScale(win=win, name='Flow06', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u'Je suis totalement absorb\xe9 par ce que je fais', disappear=True)
Flow07 = visual.RatingScale(win=win, name='Flow07', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u"Les bonnes pens\xe9es/mouvements se produisent d'eux-m\xeames", disappear=True)
Flow08 = visual.RatingScale(win=win, name='Flow08', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u'Je sais ce que je dois faire \xe0 chaque \xe9tape', disappear=True)
Flow09 = visual.RatingScale(win=win, name='Flow09', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u'Je sens que tout est sous contr\xf4le', disappear=True)
Flow10 = visual.RatingScale(win=win, name='Flow10', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[''], scale=u'Je suis compl\xe8tement perdu dans mes pens\xe9es')

# Initialize components for Routine "StartXX"
StartXXClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text=u"Appuyez sur la barre d'espacement \npour continuer l'exp\xe9rience",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
empty_gray = visual.ImageStim(
    win=win, name='empty_gray',
    image='empty_gray', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fixation_cross = visual.ImageStim(
    win=win, name='fixation_cross',
    image='fixation_cross', mask=None,
    ori=0, pos=(0, 0), size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
n_objets = visual.RatingScale(win=win, name='n_objets', marker='triangle', size=1.0, pos=[0.0, 0.0], low=1, high=5, labels=['1', ' 5 et plus'], scale=u"Veuillez indiquer le nombre d'objets significatifs per\xe7us", disappear=True)
vividness = visual.RatingScale(win=win, name='vividness', marker='triangle', size=1, pos=[0.0, 0.0], low=1, high=5, labels=[u'Tr\xe8s peu vivide', u' Fortement vivide'], scale=u'Veuillez indiquer la vividit\xe9 de votre perception', disappear=True)
cross = parallel.ParallelPort(address=u'0x0378')
image_in = parallel.ParallelPort(address=u'0x0378')
image_out = parallel.ParallelPort(address=u'0x0378')
RT = parallel.ParallelPort(address=u'0x0378')

# Initialize components for Routine "Fin_bloc"
Fin_blocClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text=u"Vous venez de terminer le bloc.\n\nAppuyez la sur la barre d'espacement pour r\xe9pondre \xe0 quelques questions avant de prendre votre pause.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Mental_fatigue"
Mental_fatigueClock = core.Clock()
Fatigue = visual.RatingScale(win=win, name='Fatigue', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=10, labels=[u'\xc9tat de fatigue absolu', u" \xc9tat d'\xe9veil absolu"], scale='Veuillez indiquer votre niveau de fatigue mentale')

# Initialize components for Routine "Flow"
FlowClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text=u"Court questionnaire sur l'\xe9tat de flow\n\nVeuillez r\xe9pondre aux questions suivantes concernant votre exp\xe9rience du bloc que vous venez de terminer.\n\n1 = Total d\xe9saccord  //  7 = Total accord\n\nAppuyez sur la barre d'espacement pour commencer",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Flow_questions"
Flow_questionsClock = core.Clock()
Flow01 = visual.RatingScale(win=win, name='Flow01', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u'Je ressens le parfait niveau de d\xe9fi', disappear=True)
Flow02 = visual.RatingScale(win=win, name='Flow02', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u'Mes pens\xe9es/actions se d\xe9roulent fluidement', disappear=True)
Flow03 = visual.RatingScale(win=win, name='Flow03', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u'Je ne vois pas le temps pass\xe9', disappear=True)
Flow04 = visual.RatingScale(win=win, name='Flow04', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u"Je n'ai pas de difficult\xe9 \xe0 me concentrer", disappear=True)
Flow05 = visual.RatingScale(win=win, name='Flow05', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u'Mon esprit est compl\xe8tement clair', disappear=True)
Flow06 = visual.RatingScale(win=win, name='Flow06', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u'Je suis totalement absorb\xe9 par ce que je fais', disappear=True)
Flow07 = visual.RatingScale(win=win, name='Flow07', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u"Les bonnes pens\xe9es/mouvements se produisent d'eux-m\xeames", disappear=True)
Flow08 = visual.RatingScale(win=win, name='Flow08', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u'Je sais ce que je dois faire \xe0 chaque \xe9tape', disappear=True)
Flow09 = visual.RatingScale(win=win, name='Flow09', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u'Je sens que tout est sous contr\xf4le', disappear=True)
Flow10 = visual.RatingScale(win=win, name='Flow10', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[''], scale=u'Je suis compl\xe8tement perdu dans mes pens\xe9es')

# Initialize components for Routine "StartXX"
StartXXClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text=u"Appuyez sur la barre d'espacement \npour continuer l'exp\xe9rience",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
empty_gray = visual.ImageStim(
    win=win, name='empty_gray',
    image='empty_gray', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fixation_cross = visual.ImageStim(
    win=win, name='fixation_cross',
    image='fixation_cross', mask=None,
    ori=0, pos=(0, 0), size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
n_objets = visual.RatingScale(win=win, name='n_objets', marker='triangle', size=1.0, pos=[0.0, 0.0], low=1, high=5, labels=['1', ' 5 et plus'], scale=u"Veuillez indiquer le nombre d'objets significatifs per\xe7us", disappear=True)
vividness = visual.RatingScale(win=win, name='vividness', marker='triangle', size=1, pos=[0.0, 0.0], low=1, high=5, labels=[u'Tr\xe8s peu vivide', u' Fortement vivide'], scale=u'Veuillez indiquer la vividit\xe9 de votre perception', disappear=True)
cross = parallel.ParallelPort(address=u'0x0378')
image_in = parallel.ParallelPort(address=u'0x0378')
image_out = parallel.ParallelPort(address=u'0x0378')
RT = parallel.ParallelPort(address=u'0x0378')

# Initialize components for Routine "Fin_bloc"
Fin_blocClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text=u"Vous venez de terminer le bloc.\n\nAppuyez la sur la barre d'espacement pour r\xe9pondre \xe0 quelques questions avant de prendre votre pause.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Mental_fatigue"
Mental_fatigueClock = core.Clock()
Fatigue = visual.RatingScale(win=win, name='Fatigue', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=10, labels=[u'\xc9tat de fatigue absolu', u" \xc9tat d'\xe9veil absolu"], scale='Veuillez indiquer votre niveau de fatigue mentale')

# Initialize components for Routine "Flow"
FlowClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text=u"Court questionnaire sur l'\xe9tat de flow\n\nVeuillez r\xe9pondre aux questions suivantes concernant votre exp\xe9rience du bloc que vous venez de terminer.\n\n1 = Total d\xe9saccord  //  7 = Total accord\n\nAppuyez sur la barre d'espacement pour commencer",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Flow_questions"
Flow_questionsClock = core.Clock()
Flow01 = visual.RatingScale(win=win, name='Flow01', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u'Je ressens le parfait niveau de d\xe9fi', disappear=True)
Flow02 = visual.RatingScale(win=win, name='Flow02', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u'Mes pens\xe9es/actions se d\xe9roulent fluidement', disappear=True)
Flow03 = visual.RatingScale(win=win, name='Flow03', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u'Je ne vois pas le temps pass\xe9', disappear=True)
Flow04 = visual.RatingScale(win=win, name='Flow04', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u"Je n'ai pas de difficult\xe9 \xe0 me concentrer", disappear=True)
Flow05 = visual.RatingScale(win=win, name='Flow05', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u'Mon esprit est compl\xe8tement clair', disappear=True)
Flow06 = visual.RatingScale(win=win, name='Flow06', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u'Je suis totalement absorb\xe9 par ce que je fais', disappear=True)
Flow07 = visual.RatingScale(win=win, name='Flow07', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u"Les bonnes pens\xe9es/mouvements se produisent d'eux-m\xeames", disappear=True)
Flow08 = visual.RatingScale(win=win, name='Flow08', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u'Je sais ce que je dois faire \xe0 chaque \xe9tape', disappear=True)
Flow09 = visual.RatingScale(win=win, name='Flow09', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u'Je sens que tout est sous contr\xf4le', disappear=True)
Flow10 = visual.RatingScale(win=win, name='Flow10', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[''], scale=u'Je suis compl\xe8tement perdu dans mes pens\xe9es')

# Initialize components for Routine "Redondance"
RedondanceClock = core.Clock()
Redondance_question = visual.RatingScale(win=win, name='Redondance_question', marker='triangle', size=0.8, pos=[0.0, -0.4], low=1, high=7, labels=[u'Presque toujours la m\xeame cat\xe9gorie', u' Cat\xe9gories vari\xe9es'], scale=u"Pour l'ensemble des trois premiers blocs, veuillez indiquer \xe0 quel point vos perceptions \xe9taient diversifi\xe9es")

# Initialize components for Routine "Instructions_sham"
Instructions_shamClock = core.Clock()
instructions_sham = visual.TextStim(win=win, name='instructions_sham',
    text=u"Au courant des trois premiers blocs que vous venez de compl\xe9ter, \nun algorithme d\u2019apprentissage-machine s\u2019est entra\xeen\xe9 \xe0 diff\xe9rencier l\nes images pour lesquelles vous rapportiez une forte par\xe9idolie \nde celles o\xf9 la par\xe9idolie \xe9tait inexistante ou faible. \nPour le dernier bloc, cet algorithme d'apprentissage-machine utilisera \nvotre activit\xe9 c\xe9r\xe9brale afin de cr\xe9er en temps r\xe9el \nles images de nuages g\xe9n\xe9ratifs de mani\xe8re \xe0 maximiser la par\xe9idolie. \n\nAppuyez sur la barre d'espacement afin de d\xe9buter le bloc.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
empty_gray = visual.ImageStim(
    win=win, name='empty_gray',
    image='empty_gray', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fixation_cross = visual.ImageStim(
    win=win, name='fixation_cross',
    image='fixation_cross', mask=None,
    ori=0, pos=(0, 0), size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
n_objets = visual.RatingScale(win=win, name='n_objets', marker='triangle', size=1.0, pos=[0.0, 0.0], low=1, high=5, labels=['1', ' 5 et plus'], scale=u"Veuillez indiquer le nombre d'objets significatifs per\xe7us", disappear=True)
vividness = visual.RatingScale(win=win, name='vividness', marker='triangle', size=1, pos=[0.0, 0.0], low=1, high=5, labels=[u'Tr\xe8s peu vivide', u' Fortement vivide'], scale=u'Veuillez indiquer la vividit\xe9 de votre perception', disappear=True)
cross = parallel.ParallelPort(address=u'0x0378')
image_in = parallel.ParallelPort(address=u'0x0378')
image_out = parallel.ParallelPort(address=u'0x0378')
RT = parallel.ParallelPort(address=u'0x0378')

# Initialize components for Routine "Mental_fatigue"
Mental_fatigueClock = core.Clock()
Fatigue = visual.RatingScale(win=win, name='Fatigue', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=10, labels=[u'\xc9tat de fatigue absolu', u" \xc9tat d'\xe9veil absolu"], scale='Veuillez indiquer votre niveau de fatigue mentale')

# Initialize components for Routine "Flow"
FlowClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text=u"Court questionnaire sur l'\xe9tat de flow\n\nVeuillez r\xe9pondre aux questions suivantes concernant votre exp\xe9rience du bloc que vous venez de terminer.\n\n1 = Total d\xe9saccord  //  7 = Total accord\n\nAppuyez sur la barre d'espacement pour commencer",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Flow_questions"
Flow_questionsClock = core.Clock()
Flow01 = visual.RatingScale(win=win, name='Flow01', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u'Je ressens le parfait niveau de d\xe9fi', disappear=True)
Flow02 = visual.RatingScale(win=win, name='Flow02', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u'Mes pens\xe9es/actions se d\xe9roulent fluidement', disappear=True)
Flow03 = visual.RatingScale(win=win, name='Flow03', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u'Je ne vois pas le temps pass\xe9', disappear=True)
Flow04 = visual.RatingScale(win=win, name='Flow04', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u"Je n'ai pas de difficult\xe9 \xe0 me concentrer", disappear=True)
Flow05 = visual.RatingScale(win=win, name='Flow05', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u'Mon esprit est compl\xe8tement clair', disappear=True)
Flow06 = visual.RatingScale(win=win, name='Flow06', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u'Je suis totalement absorb\xe9 par ce que je fais', disappear=True)
Flow07 = visual.RatingScale(win=win, name='Flow07', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u"Les bonnes pens\xe9es/mouvements se produisent d'eux-m\xeames", disappear=True)
Flow08 = visual.RatingScale(win=win, name='Flow08', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u'Je sais ce que je dois faire \xe0 chaque \xe9tape', disappear=True)
Flow09 = visual.RatingScale(win=win, name='Flow09', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'Total d\xe9saccord', u' Total accord'], scale=u'Je sens que tout est sous contr\xf4le', disappear=True)
Flow10 = visual.RatingScale(win=win, name='Flow10', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[''], scale=u'Je suis compl\xe8tement perdu dans mes pens\xe9es')

# Initialize components for Routine "Resting_state_instructions2"
Resting_state_instructions2Clock = core.Clock()
resting_instructions_end = visual.TextStim(win=win, name='resting_instructions_end',
    text=u"Nous allons maintenant vous demander\nde rester immobile pendant 3 minutes\nde la m\xeame fa\xe7on que lorsqu'au d\xe9but de\nl'exp\xe9rience, en fixant la croix au centre de\nl'\xe9cran et en ne faisant aucune t\xe2che particuli\xe8re",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Resting_state"
Resting_stateClock = core.Clock()
fix_resting_state = visual.ImageStim(
    win=win, name='fix_resting_state',
    image=u'fixation_cross', mask=None,
    ori=0, pos=(0, 0), size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
RS01_in = parallel.ParallelPort(address=u'0x0378')
RS01_out = parallel.ParallelPort(address=u'0x0378')

# Initialize components for Routine "Sham"
ShamClock = core.Clock()
rating = visual.RatingScale(win=win, name='rating', marker='triangle', size=1.0, pos=[0.0, -0.4], low=0, high=1, precision=100, showValue=False, scale=u'\xc0 quel point avez-vous per\xe7u une diff\xe9rence entre le dernier bloc et les blocs pr\xe9c\xe9dents ?')

# Initialize components for Routine "Finito"
FinitoClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text=u"Merci d'avoir particit\xe9 \xe0 cette exp\xe9rience sur la par\xe9idolie.\nVous pouvez faire signe \xe0 l'exp\xe9rimentateur.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
t = 0
InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
end_instructions = event.BuilderKeyResponse()
# keep track of which components have finished
InstructionsComponents = [Instruction, end_instructions]
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instruction* updates
    if t >= 0.0 and Instruction.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instruction.tStart = t
        Instruction.frameNStart = frameN  # exact frame index
        Instruction.setAutoDraw(True)
    
    # *end_instructions* updates
    if t >= 0.0 and end_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_instructions.tStart = t
        end_instructions.frameNStart = frameN  # exact frame index
        end_instructions.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(end_instructions.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if end_instructions.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            end_instructions.keys = theseKeys[-1]  # just the last key pressed
            end_instructions.rt = end_instructions.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if end_instructions.keys in ['', [], None]:  # No response was made
    end_instructions.keys=None
thisExp.addData('end_instructions.keys',end_instructions.keys)
if end_instructions.keys != None:  # we had a response
    thisExp.addData('end_instructions.rt', end_instructions.rt)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions2"-------
t = 0
Instructions2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()
# keep track of which components have finished
Instructions2Components = [instructions2, key_resp_4]
for thisComponent in Instructions2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instructions2"-------
while continueRoutine:
    # get current time
    t = Instructions2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions2* updates
    if t >= 0.0 and instructions2.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions2.tStart = t
        instructions2.frameNStart = frameN  # exact frame index
        instructions2.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_4.keys = theseKeys[-1]  # just the last key pressed
            key_resp_4.rt = key_resp_4.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions2"-------
for thisComponent in Instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys=None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.nextEntry()
# the Routine "Instructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instruction3"-------
t = 0
Instruction3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_6 = event.BuilderKeyResponse()
# keep track of which components have finished
Instruction3Components = [text_4, key_resp_6]
for thisComponent in Instruction3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instruction3"-------
while continueRoutine:
    # get current time
    t = Instruction3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if t >= 0.0 and text_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_4.tStart = t
        text_4.frameNStart = frameN  # exact frame index
        text_4.setAutoDraw(True)
    
    # *key_resp_6* updates
    if t >= 0.0 and key_resp_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_6.tStart = t
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_6.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_6.keys = theseKeys[-1]  # just the last key pressed
            key_resp_6.rt = key_resp_6.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instruction3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruction3"-------
for thisComponent in Instruction3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys=None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.nextEntry()
# the Routine "Instruction3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Mental_fatigue"-------
t = 0
Mental_fatigueClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
Fatigue.reset()
# keep track of which components have finished
Mental_fatigueComponents = [Fatigue]
for thisComponent in Mental_fatigueComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Mental_fatigue"-------
while continueRoutine:
    # get current time
    t = Mental_fatigueClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *Fatigue* updates
    if t >= 0.0 and Fatigue.status == NOT_STARTED:
        # keep track of start time/frame for later
        Fatigue.tStart = t
        Fatigue.frameNStart = frameN  # exact frame index
        Fatigue.setAutoDraw(True)
    continueRoutine &= Fatigue.noResponse  # a response ends the trial
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Mental_fatigueComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Mental_fatigue"-------
for thisComponent in Mental_fatigueComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('Fatigue.response', Fatigue.getRating())
thisExp.addData('Fatigue.rt', Fatigue.getRT())
thisExp.nextEntry()
# the Routine "Mental_fatigue" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Resting_state_instructions"-------
t = 0
Resting_state_instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_9 = event.BuilderKeyResponse()
# keep track of which components have finished
Resting_state_instructionsComponents = [Resting, key_resp_9]
for thisComponent in Resting_state_instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Resting_state_instructions"-------
while continueRoutine:
    # get current time
    t = Resting_state_instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Resting* updates
    if t >= 0.0 and Resting.status == NOT_STARTED:
        # keep track of start time/frame for later
        Resting.tStart = t
        Resting.frameNStart = frameN  # exact frame index
        Resting.setAutoDraw(True)
    
    # *key_resp_9* updates
    if t >= 0.0 and key_resp_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_9.tStart = t
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_9.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_9.keys = theseKeys[-1]  # just the last key pressed
            key_resp_9.rt = key_resp_9.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Resting_state_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Resting_state_instructions"-------
for thisComponent in Resting_state_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys=None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.nextEntry()
# the Routine "Resting_state_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Resting_state"-------
t = 0
Resting_stateClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_10 = event.BuilderKeyResponse()
# keep track of which components have finished
Resting_stateComponents = [fix_resting_state, key_resp_10, RS01_in, RS01_out]
for thisComponent in Resting_stateComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Resting_state"-------
while continueRoutine:
    # get current time
    t = Resting_stateClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fix_resting_state* updates
    if t >= 0.0 and fix_resting_state.status == NOT_STARTED:
        # keep track of start time/frame for later
        fix_resting_state.tStart = t
        fix_resting_state.frameNStart = frameN  # exact frame index
        fix_resting_state.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if fix_resting_state.status == STARTED and t >= frameRemains:
        fix_resting_state.setAutoDraw(False)
    
    # *key_resp_10* updates
    if t >= 0.0 and key_resp_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_10.tStart = t
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_10.status == STARTED:
        theseKeys = event.getKeys(keyList=['q'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_10.keys = theseKeys[-1]  # just the last key pressed
            key_resp_10.rt = key_resp_10.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    # *RS01_in* updates
    if t >= 0.0 and RS01_in.status == NOT_STARTED:
        # keep track of start time/frame for later
        RS01_in.tStart = t
        RS01_in.frameNStart = frameN  # exact frame index
        RS01_in.status = STARTED
        win.callOnFlip(RS01_in.setData, int(1))
    frameRemains = 0.0 + 0.1- win.monitorFramePeriod * 0.75  # most of one frame period left
    if RS01_in.status == STARTED and t >= frameRemains:
        RS01_in.status = STOPPED
        win.callOnFlip(RS01_in.setData, int(0))
    # *RS01_out* updates
    if t >= 5 and RS01_out.status == NOT_STARTED:
        # keep track of start time/frame for later
        RS01_out.tStart = t
        RS01_out.frameNStart = frameN  # exact frame index
        RS01_out.status = STARTED
        win.callOnFlip(RS01_out.setData, int(2))
    frameRemains = 5 + 0.1- win.monitorFramePeriod * 0.75  # most of one frame period left
    if RS01_out.status == STARTED and t >= frameRemains:
        RS01_out.status = STOPPED
        win.callOnFlip(RS01_out.setData, int(0))
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Resting_stateComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Resting_state"-------
for thisComponent in Resting_stateComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_10.keys in ['', [], None]:  # No response was made
    key_resp_10.keys=None
thisExp.addData('key_resp_10.keys',key_resp_10.keys)
if key_resp_10.keys != None:  # we had a response
    thisExp.addData('key_resp_10.rt', key_resp_10.rt)
thisExp.nextEntry()
if RS01_in.status == STARTED:
    win.callOnFlip(RS01_in.setData, int(0))
if RS01_out.status == STARTED:
    win.callOnFlip(RS01_out.setData, int(0))
# the Routine "Resting_state" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Start_pratique"-------
t = 0
Start_pratiqueClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_5 = event.BuilderKeyResponse()
# keep track of which components have finished
Start_pratiqueComponents = [text_3, key_resp_5]
for thisComponent in Start_pratiqueComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Start_pratique"-------
while continueRoutine:
    # get current time
    t = Start_pratiqueClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    
    # *key_resp_5* updates
    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_5.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_5.keys = theseKeys[-1]  # just the last key pressed
            key_resp_5.rt = key_resp_5.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start_pratiqueComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start_pratique"-------
for thisComponent in Start_pratiqueComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys=None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.nextEntry()
# the Routine "Start_pratique" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Images_pratique.xlsx'),
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4:
        exec('{} = thisTrial_4[paramName]'.format(paramName))

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial1"-------
    t = 0
    trial1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image.setImage(ImageFile)
    n_objets.reset()
    reaction_time = event.BuilderKeyResponse()
    vividness.reset()
    If_No_Resp = event.BuilderKeyResponse()
    # keep track of which components have finished
    trial1Components = [empty_gray, fixation_cross, image, n_objets, reaction_time, vividness, If_No_Resp, cross, image_in, image_out, RT]
    for thisComponent in trial1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial1"-------
    while continueRoutine:
        # get current time
        t = trial1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *empty_gray* updates
        if t >= 0.0 and empty_gray.status == NOT_STARTED:
            # keep track of start time/frame for later
            empty_gray.tStart = t
            empty_gray.frameNStart = frameN  # exact frame index
            empty_gray.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if empty_gray.status == STARTED and t >= frameRemains:
            empty_gray.setAutoDraw(False)
        
        # *fixation_cross* updates
        if t >= 1 and fixation_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_cross.tStart = t
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.setAutoDraw(True)
        frameRemains = 1 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_cross.status == STARTED and t >= frameRemains:
            fixation_cross.setAutoDraw(False)
        
        # *image* updates
        if t >= 2.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        frameRemains = 2.5 + 8.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
        # *n_objets* updates
        if (t >=10.5) and n_objets.status == NOT_STARTED:
            # keep track of start time/frame for later
            n_objets.tStart = t
            n_objets.frameNStart = frameN  # exact frame index
            n_objets.setAutoDraw(True)
        
        # *reaction_time* updates
        if t >= 2.5 and reaction_time.status == NOT_STARTED:
            # keep track of start time/frame for later
            reaction_time.tStart = t
            reaction_time.frameNStart = frameN  # exact frame index
            reaction_time.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(reaction_time.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 2.5 + 8.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if reaction_time.status == STARTED and t >= frameRemains:
            reaction_time.status = STOPPED
        if reaction_time.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if reaction_time.keys == []:  # then this was the first keypress
                    reaction_time.keys = theseKeys[0]  # just the first key pressed
                    reaction_time.rt = reaction_time.clock.getTime()
        # *vividness* updates
        if (n_objets.status == FINISHED) and vividness.status == NOT_STARTED:
            # keep track of start time/frame for later
            vividness.tStart = t
            vividness.frameNStart = frameN  # exact frame index
            vividness.setAutoDraw(True)
        continueRoutine &= vividness.noResponse  # a response ends the trial
        
        # *If_No_Resp* updates
        if t >= 10.5 and If_No_Resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            If_No_Resp.tStart = t
            If_No_Resp.frameNStart = frameN  # exact frame index
            If_No_Resp.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if If_No_Resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['q'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        # *cross* updates
        if t >= 1 and cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            cross.tStart = t
            cross.frameNStart = frameN  # exact frame index
            cross.status = STARTED
            win.callOnFlip(cross.setData, int(3))
        frameRemains = 1 + 0.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if cross.status == STARTED and t >= frameRemains:
            cross.status = STOPPED
            win.callOnFlip(cross.setData, int(0))
        # *image_in* updates
        if t >= 2.5 and image_in.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_in.tStart = t
            image_in.frameNStart = frameN  # exact frame index
            image_in.status = STARTED
            win.callOnFlip(image_in.setData, int(4))
        frameRemains = 2.5 + 0.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_in.status == STARTED and t >= frameRemains:
            image_in.status = STOPPED
            win.callOnFlip(image_in.setData, int(0))
        # *image_out* updates
        if t >= 10.5 and image_out.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_out.tStart = t
            image_out.frameNStart = frameN  # exact frame index
            image_out.status = STARTED
            win.callOnFlip(image_out.setData, int(5))
        frameRemains = 10.5 + 0.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_out.status == STARTED and t >= frameRemains:
            image_out.status = STOPPED
            win.callOnFlip(image_out.setData, int(0))
        # *RT* updates
        if (reaction_time==True) and RT.status == NOT_STARTED:
            # keep track of start time/frame for later
            RT.tStart = t
            RT.frameNStart = frameN  # exact frame index
            RT.status = STARTED
            win.callOnFlip(RT.setData, int(6))
        if RT.status == STARTED and t >= (RT.tStart + 0.1):
            RT.status = STOPPED
            win.callOnFlip(RT.setData, int(0))
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial1"-------
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_4 (TrialHandler)
    trials_4.addData('n_objets.response', n_objets.getRating())
    # check responses
    if reaction_time.keys in ['', [], None]:  # No response was made
        reaction_time.keys=None
    trials_4.addData('reaction_time.keys',reaction_time.keys)
    if reaction_time.keys != None:  # we had a response
        trials_4.addData('reaction_time.rt', reaction_time.rt)
    # store data for trials_4 (TrialHandler)
    trials_4.addData('vividness.response', vividness.getRating())
    trials_4.addData('vividness.rt', vividness.getRT())
    if cross.status == STARTED:
        win.callOnFlip(cross.setData, int(0))
    if image_in.status == STARTED:
        win.callOnFlip(image_in.setData, int(0))
    if image_out.status == STARTED:
        win.callOnFlip(image_out.setData, int(0))
    if RT.status == STARTED:
        win.callOnFlip(RT.setData, int(0))
    # the Routine "trial1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_4'


# ------Prepare to start Routine "Startx"-------
t = 0
StartxClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
StartxComponents = [text, key_resp_2]
for thisComponent in StartxComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Startx"-------
while continueRoutine:
    # get current time
    t = StartxClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartxComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Startx"-------
for thisComponent in StartxComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys=None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "Startx" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Images_01.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial1"-------
    t = 0
    trial1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image.setImage(ImageFile)
    n_objets.reset()
    reaction_time = event.BuilderKeyResponse()
    vividness.reset()
    If_No_Resp = event.BuilderKeyResponse()
    # keep track of which components have finished
    trial1Components = [empty_gray, fixation_cross, image, n_objets, reaction_time, vividness, If_No_Resp, cross, image_in, image_out, RT]
    for thisComponent in trial1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial1"-------
    while continueRoutine:
        # get current time
        t = trial1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *empty_gray* updates
        if t >= 0.0 and empty_gray.status == NOT_STARTED:
            # keep track of start time/frame for later
            empty_gray.tStart = t
            empty_gray.frameNStart = frameN  # exact frame index
            empty_gray.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if empty_gray.status == STARTED and t >= frameRemains:
            empty_gray.setAutoDraw(False)
        
        # *fixation_cross* updates
        if t >= 1 and fixation_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_cross.tStart = t
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.setAutoDraw(True)
        frameRemains = 1 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_cross.status == STARTED and t >= frameRemains:
            fixation_cross.setAutoDraw(False)
        
        # *image* updates
        if t >= 2.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        frameRemains = 2.5 + 8.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
        # *n_objets* updates
        if (t >=10.5) and n_objets.status == NOT_STARTED:
            # keep track of start time/frame for later
            n_objets.tStart = t
            n_objets.frameNStart = frameN  # exact frame index
            n_objets.setAutoDraw(True)
        
        # *reaction_time* updates
        if t >= 2.5 and reaction_time.status == NOT_STARTED:
            # keep track of start time/frame for later
            reaction_time.tStart = t
            reaction_time.frameNStart = frameN  # exact frame index
            reaction_time.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(reaction_time.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 2.5 + 8.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if reaction_time.status == STARTED and t >= frameRemains:
            reaction_time.status = STOPPED
        if reaction_time.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if reaction_time.keys == []:  # then this was the first keypress
                    reaction_time.keys = theseKeys[0]  # just the first key pressed
                    reaction_time.rt = reaction_time.clock.getTime()
        # *vividness* updates
        if (n_objets.status == FINISHED) and vividness.status == NOT_STARTED:
            # keep track of start time/frame for later
            vividness.tStart = t
            vividness.frameNStart = frameN  # exact frame index
            vividness.setAutoDraw(True)
        continueRoutine &= vividness.noResponse  # a response ends the trial
        
        # *If_No_Resp* updates
        if t >= 10.5 and If_No_Resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            If_No_Resp.tStart = t
            If_No_Resp.frameNStart = frameN  # exact frame index
            If_No_Resp.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if If_No_Resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['q'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        # *cross* updates
        if t >= 1 and cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            cross.tStart = t
            cross.frameNStart = frameN  # exact frame index
            cross.status = STARTED
            win.callOnFlip(cross.setData, int(3))
        frameRemains = 1 + 0.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if cross.status == STARTED and t >= frameRemains:
            cross.status = STOPPED
            win.callOnFlip(cross.setData, int(0))
        # *image_in* updates
        if t >= 2.5 and image_in.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_in.tStart = t
            image_in.frameNStart = frameN  # exact frame index
            image_in.status = STARTED
            win.callOnFlip(image_in.setData, int(4))
        frameRemains = 2.5 + 0.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_in.status == STARTED and t >= frameRemains:
            image_in.status = STOPPED
            win.callOnFlip(image_in.setData, int(0))
        # *image_out* updates
        if t >= 10.5 and image_out.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_out.tStart = t
            image_out.frameNStart = frameN  # exact frame index
            image_out.status = STARTED
            win.callOnFlip(image_out.setData, int(5))
        frameRemains = 10.5 + 0.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_out.status == STARTED and t >= frameRemains:
            image_out.status = STOPPED
            win.callOnFlip(image_out.setData, int(0))
        # *RT* updates
        if (reaction_time==True) and RT.status == NOT_STARTED:
            # keep track of start time/frame for later
            RT.tStart = t
            RT.frameNStart = frameN  # exact frame index
            RT.status = STARTED
            win.callOnFlip(RT.setData, int(6))
        if RT.status == STARTED and t >= (RT.tStart + 0.1):
            RT.status = STOPPED
            win.callOnFlip(RT.setData, int(0))
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial1"-------
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('n_objets.response', n_objets.getRating())
    # check responses
    if reaction_time.keys in ['', [], None]:  # No response was made
        reaction_time.keys=None
    trials.addData('reaction_time.keys',reaction_time.keys)
    if reaction_time.keys != None:  # we had a response
        trials.addData('reaction_time.rt', reaction_time.rt)
    # store data for trials (TrialHandler)
    trials.addData('vividness.response', vividness.getRating())
    trials.addData('vividness.rt', vividness.getRT())
    if cross.status == STARTED:
        win.callOnFlip(cross.setData, int(0))
    if image_in.status == STARTED:
        win.callOnFlip(image_in.setData, int(0))
    if image_out.status == STARTED:
        win.callOnFlip(image_out.setData, int(0))
    if RT.status == STARTED:
        win.callOnFlip(RT.setData, int(0))
    # the Routine "trial1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "Fin_bloc"-------
t = 0
Fin_blocClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_8 = event.BuilderKeyResponse()
# keep track of which components have finished
Fin_blocComponents = [text_7, key_resp_8]
for thisComponent in Fin_blocComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Fin_bloc"-------
while continueRoutine:
    # get current time
    t = Fin_blocClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if t >= 0.0 and text_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_7.tStart = t
        text_7.frameNStart = frameN  # exact frame index
        text_7.setAutoDraw(True)
    
    # *key_resp_8* updates
    if t >= 0.0 and key_resp_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_8.tStart = t
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_8.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_8.keys = theseKeys[-1]  # just the last key pressed
            key_resp_8.rt = key_resp_8.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Fin_blocComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Fin_bloc"-------
for thisComponent in Fin_blocComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys=None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.nextEntry()
# the Routine "Fin_bloc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Mental_fatigue"-------
t = 0
Mental_fatigueClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
Fatigue.reset()
# keep track of which components have finished
Mental_fatigueComponents = [Fatigue]
for thisComponent in Mental_fatigueComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Mental_fatigue"-------
while continueRoutine:
    # get current time
    t = Mental_fatigueClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *Fatigue* updates
    if t >= 0.0 and Fatigue.status == NOT_STARTED:
        # keep track of start time/frame for later
        Fatigue.tStart = t
        Fatigue.frameNStart = frameN  # exact frame index
        Fatigue.setAutoDraw(True)
    continueRoutine &= Fatigue.noResponse  # a response ends the trial
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Mental_fatigueComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Mental_fatigue"-------
for thisComponent in Mental_fatigueComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('Fatigue.response', Fatigue.getRating())
thisExp.addData('Fatigue.rt', Fatigue.getRT())
thisExp.nextEntry()
# the Routine "Mental_fatigue" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Flow"-------
t = 0
FlowClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_7 = event.BuilderKeyResponse()
# keep track of which components have finished
FlowComponents = [text_6, key_resp_7]
for thisComponent in FlowComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Flow"-------
while continueRoutine:
    # get current time
    t = FlowClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if t >= 0.0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    
    # *key_resp_7* updates
    if t >= 0.0 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_7.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FlowComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Flow"-------
for thisComponent in FlowComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Flow" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Flow_questions"-------
t = 0
Flow_questionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
Flow01.reset()
Flow02.reset()
Flow03.reset()
Flow04.reset()
Flow05.reset()
Flow06.reset()
Flow07.reset()
Flow08.reset()
Flow09.reset()
Flow10.reset()
# keep track of which components have finished
Flow_questionsComponents = [Flow01, Flow02, Flow03, Flow04, Flow05, Flow06, Flow07, Flow08, Flow09, Flow10]
for thisComponent in Flow_questionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Flow_questions"-------
while continueRoutine:
    # get current time
    t = Flow_questionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *Flow01* updates
    if t >= 0.0 and Flow01.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow01.tStart = t
        Flow01.frameNStart = frameN  # exact frame index
        Flow01.setAutoDraw(True)
    # *Flow02* updates
    if t >= Flow01.status == FINISHED and Flow02.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow02.tStart = t
        Flow02.frameNStart = frameN  # exact frame index
        Flow02.setAutoDraw(True)
    # *Flow03* updates
    if t >= Flow02.status == FINISHED and Flow03.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow03.tStart = t
        Flow03.frameNStart = frameN  # exact frame index
        Flow03.setAutoDraw(True)
    # *Flow04* updates
    if t >= Flow03.status == FINISHED and Flow04.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow04.tStart = t
        Flow04.frameNStart = frameN  # exact frame index
        Flow04.setAutoDraw(True)
    # *Flow05* updates
    if t >= Flow04.status == FINISHED and Flow05.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow05.tStart = t
        Flow05.frameNStart = frameN  # exact frame index
        Flow05.setAutoDraw(True)
    # *Flow06* updates
    if t >= Flow05.status == FINISHED and Flow06.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow06.tStart = t
        Flow06.frameNStart = frameN  # exact frame index
        Flow06.setAutoDraw(True)
    # *Flow07* updates
    if t >= Flow06.status == FINISHED and Flow07.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow07.tStart = t
        Flow07.frameNStart = frameN  # exact frame index
        Flow07.setAutoDraw(True)
    # *Flow08* updates
    if t >= Flow07.status == FINISHED and Flow08.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow08.tStart = t
        Flow08.frameNStart = frameN  # exact frame index
        Flow08.setAutoDraw(True)
    # *Flow09* updates
    if t >= Flow08.status == FINISHED and Flow09.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow09.tStart = t
        Flow09.frameNStart = frameN  # exact frame index
        Flow09.setAutoDraw(True)
    # *Flow10* updates
    if t >= Flow09.status == FINISHED and Flow10.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow10.tStart = t
        Flow10.frameNStart = frameN  # exact frame index
        Flow10.setAutoDraw(True)
    continueRoutine &= Flow10.noResponse  # a response ends the trial
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Flow_questionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Flow_questions"-------
for thisComponent in Flow_questionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow01.response', Flow01.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow02.response', Flow02.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow03.response', Flow03.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow04.response', Flow04.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow05.response', Flow05.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow06.response', Flow06.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow07.response', Flow07.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow08.response', Flow08.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow09.response', Flow09.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow10.response', Flow10.getRating())
thisExp.nextEntry()
# the Routine "Flow_questions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "StartXX"-------
t = 0
StartXXClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()
# keep track of which components have finished
StartXXComponents = [text_2, key_resp_3]
for thisComponent in StartXXComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "StartXX"-------
while continueRoutine:
    # get current time
    t = StartXXClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartXXComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "StartXX"-------
for thisComponent in StartXXComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys=None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "StartXX" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Images_02.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial1"-------
    t = 0
    trial1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image.setImage(ImageFile)
    n_objets.reset()
    reaction_time = event.BuilderKeyResponse()
    vividness.reset()
    If_No_Resp = event.BuilderKeyResponse()
    # keep track of which components have finished
    trial1Components = [empty_gray, fixation_cross, image, n_objets, reaction_time, vividness, If_No_Resp, cross, image_in, image_out, RT]
    for thisComponent in trial1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial1"-------
    while continueRoutine:
        # get current time
        t = trial1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *empty_gray* updates
        if t >= 0.0 and empty_gray.status == NOT_STARTED:
            # keep track of start time/frame for later
            empty_gray.tStart = t
            empty_gray.frameNStart = frameN  # exact frame index
            empty_gray.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if empty_gray.status == STARTED and t >= frameRemains:
            empty_gray.setAutoDraw(False)
        
        # *fixation_cross* updates
        if t >= 1 and fixation_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_cross.tStart = t
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.setAutoDraw(True)
        frameRemains = 1 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_cross.status == STARTED and t >= frameRemains:
            fixation_cross.setAutoDraw(False)
        
        # *image* updates
        if t >= 2.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        frameRemains = 2.5 + 8.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
        # *n_objets* updates
        if (t >=10.5) and n_objets.status == NOT_STARTED:
            # keep track of start time/frame for later
            n_objets.tStart = t
            n_objets.frameNStart = frameN  # exact frame index
            n_objets.setAutoDraw(True)
        
        # *reaction_time* updates
        if t >= 2.5 and reaction_time.status == NOT_STARTED:
            # keep track of start time/frame for later
            reaction_time.tStart = t
            reaction_time.frameNStart = frameN  # exact frame index
            reaction_time.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(reaction_time.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 2.5 + 8.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if reaction_time.status == STARTED and t >= frameRemains:
            reaction_time.status = STOPPED
        if reaction_time.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if reaction_time.keys == []:  # then this was the first keypress
                    reaction_time.keys = theseKeys[0]  # just the first key pressed
                    reaction_time.rt = reaction_time.clock.getTime()
        # *vividness* updates
        if (n_objets.status == FINISHED) and vividness.status == NOT_STARTED:
            # keep track of start time/frame for later
            vividness.tStart = t
            vividness.frameNStart = frameN  # exact frame index
            vividness.setAutoDraw(True)
        continueRoutine &= vividness.noResponse  # a response ends the trial
        
        # *If_No_Resp* updates
        if t >= 10.5 and If_No_Resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            If_No_Resp.tStart = t
            If_No_Resp.frameNStart = frameN  # exact frame index
            If_No_Resp.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if If_No_Resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['q'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        # *cross* updates
        if t >= 1 and cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            cross.tStart = t
            cross.frameNStart = frameN  # exact frame index
            cross.status = STARTED
            win.callOnFlip(cross.setData, int(3))
        frameRemains = 1 + 0.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if cross.status == STARTED and t >= frameRemains:
            cross.status = STOPPED
            win.callOnFlip(cross.setData, int(0))
        # *image_in* updates
        if t >= 2.5 and image_in.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_in.tStart = t
            image_in.frameNStart = frameN  # exact frame index
            image_in.status = STARTED
            win.callOnFlip(image_in.setData, int(4))
        frameRemains = 2.5 + 0.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_in.status == STARTED and t >= frameRemains:
            image_in.status = STOPPED
            win.callOnFlip(image_in.setData, int(0))
        # *image_out* updates
        if t >= 10.5 and image_out.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_out.tStart = t
            image_out.frameNStart = frameN  # exact frame index
            image_out.status = STARTED
            win.callOnFlip(image_out.setData, int(5))
        frameRemains = 10.5 + 0.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_out.status == STARTED and t >= frameRemains:
            image_out.status = STOPPED
            win.callOnFlip(image_out.setData, int(0))
        # *RT* updates
        if (reaction_time==True) and RT.status == NOT_STARTED:
            # keep track of start time/frame for later
            RT.tStart = t
            RT.frameNStart = frameN  # exact frame index
            RT.status = STARTED
            win.callOnFlip(RT.setData, int(6))
        if RT.status == STARTED and t >= (RT.tStart + 0.1):
            RT.status = STOPPED
            win.callOnFlip(RT.setData, int(0))
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial1"-------
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('n_objets.response', n_objets.getRating())
    # check responses
    if reaction_time.keys in ['', [], None]:  # No response was made
        reaction_time.keys=None
    trials_2.addData('reaction_time.keys',reaction_time.keys)
    if reaction_time.keys != None:  # we had a response
        trials_2.addData('reaction_time.rt', reaction_time.rt)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('vividness.response', vividness.getRating())
    trials_2.addData('vividness.rt', vividness.getRT())
    if cross.status == STARTED:
        win.callOnFlip(cross.setData, int(0))
    if image_in.status == STARTED:
        win.callOnFlip(image_in.setData, int(0))
    if image_out.status == STARTED:
        win.callOnFlip(image_out.setData, int(0))
    if RT.status == STARTED:
        win.callOnFlip(RT.setData, int(0))
    # the Routine "trial1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


# ------Prepare to start Routine "Fin_bloc"-------
t = 0
Fin_blocClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_8 = event.BuilderKeyResponse()
# keep track of which components have finished
Fin_blocComponents = [text_7, key_resp_8]
for thisComponent in Fin_blocComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Fin_bloc"-------
while continueRoutine:
    # get current time
    t = Fin_blocClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if t >= 0.0 and text_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_7.tStart = t
        text_7.frameNStart = frameN  # exact frame index
        text_7.setAutoDraw(True)
    
    # *key_resp_8* updates
    if t >= 0.0 and key_resp_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_8.tStart = t
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_8.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_8.keys = theseKeys[-1]  # just the last key pressed
            key_resp_8.rt = key_resp_8.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Fin_blocComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Fin_bloc"-------
for thisComponent in Fin_blocComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys=None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.nextEntry()
# the Routine "Fin_bloc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Mental_fatigue"-------
t = 0
Mental_fatigueClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
Fatigue.reset()
# keep track of which components have finished
Mental_fatigueComponents = [Fatigue]
for thisComponent in Mental_fatigueComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Mental_fatigue"-------
while continueRoutine:
    # get current time
    t = Mental_fatigueClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *Fatigue* updates
    if t >= 0.0 and Fatigue.status == NOT_STARTED:
        # keep track of start time/frame for later
        Fatigue.tStart = t
        Fatigue.frameNStart = frameN  # exact frame index
        Fatigue.setAutoDraw(True)
    continueRoutine &= Fatigue.noResponse  # a response ends the trial
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Mental_fatigueComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Mental_fatigue"-------
for thisComponent in Mental_fatigueComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('Fatigue.response', Fatigue.getRating())
thisExp.addData('Fatigue.rt', Fatigue.getRT())
thisExp.nextEntry()
# the Routine "Mental_fatigue" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Flow"-------
t = 0
FlowClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_7 = event.BuilderKeyResponse()
# keep track of which components have finished
FlowComponents = [text_6, key_resp_7]
for thisComponent in FlowComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Flow"-------
while continueRoutine:
    # get current time
    t = FlowClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if t >= 0.0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    
    # *key_resp_7* updates
    if t >= 0.0 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_7.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FlowComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Flow"-------
for thisComponent in FlowComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Flow" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Flow_questions"-------
t = 0
Flow_questionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
Flow01.reset()
Flow02.reset()
Flow03.reset()
Flow04.reset()
Flow05.reset()
Flow06.reset()
Flow07.reset()
Flow08.reset()
Flow09.reset()
Flow10.reset()
# keep track of which components have finished
Flow_questionsComponents = [Flow01, Flow02, Flow03, Flow04, Flow05, Flow06, Flow07, Flow08, Flow09, Flow10]
for thisComponent in Flow_questionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Flow_questions"-------
while continueRoutine:
    # get current time
    t = Flow_questionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *Flow01* updates
    if t >= 0.0 and Flow01.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow01.tStart = t
        Flow01.frameNStart = frameN  # exact frame index
        Flow01.setAutoDraw(True)
    # *Flow02* updates
    if t >= Flow01.status == FINISHED and Flow02.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow02.tStart = t
        Flow02.frameNStart = frameN  # exact frame index
        Flow02.setAutoDraw(True)
    # *Flow03* updates
    if t >= Flow02.status == FINISHED and Flow03.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow03.tStart = t
        Flow03.frameNStart = frameN  # exact frame index
        Flow03.setAutoDraw(True)
    # *Flow04* updates
    if t >= Flow03.status == FINISHED and Flow04.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow04.tStart = t
        Flow04.frameNStart = frameN  # exact frame index
        Flow04.setAutoDraw(True)
    # *Flow05* updates
    if t >= Flow04.status == FINISHED and Flow05.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow05.tStart = t
        Flow05.frameNStart = frameN  # exact frame index
        Flow05.setAutoDraw(True)
    # *Flow06* updates
    if t >= Flow05.status == FINISHED and Flow06.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow06.tStart = t
        Flow06.frameNStart = frameN  # exact frame index
        Flow06.setAutoDraw(True)
    # *Flow07* updates
    if t >= Flow06.status == FINISHED and Flow07.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow07.tStart = t
        Flow07.frameNStart = frameN  # exact frame index
        Flow07.setAutoDraw(True)
    # *Flow08* updates
    if t >= Flow07.status == FINISHED and Flow08.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow08.tStart = t
        Flow08.frameNStart = frameN  # exact frame index
        Flow08.setAutoDraw(True)
    # *Flow09* updates
    if t >= Flow08.status == FINISHED and Flow09.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow09.tStart = t
        Flow09.frameNStart = frameN  # exact frame index
        Flow09.setAutoDraw(True)
    # *Flow10* updates
    if t >= Flow09.status == FINISHED and Flow10.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow10.tStart = t
        Flow10.frameNStart = frameN  # exact frame index
        Flow10.setAutoDraw(True)
    continueRoutine &= Flow10.noResponse  # a response ends the trial
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Flow_questionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Flow_questions"-------
for thisComponent in Flow_questionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow01.response', Flow01.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow02.response', Flow02.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow03.response', Flow03.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow04.response', Flow04.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow05.response', Flow05.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow06.response', Flow06.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow07.response', Flow07.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow08.response', Flow08.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow09.response', Flow09.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow10.response', Flow10.getRating())
thisExp.nextEntry()
# the Routine "Flow_questions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "StartXX"-------
t = 0
StartXXClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()
# keep track of which components have finished
StartXXComponents = [text_2, key_resp_3]
for thisComponent in StartXXComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "StartXX"-------
while continueRoutine:
    # get current time
    t = StartXXClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartXXComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "StartXX"-------
for thisComponent in StartXXComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys=None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "StartXX" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Images_03.xlsx'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial1"-------
    t = 0
    trial1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image.setImage(ImageFile)
    n_objets.reset()
    reaction_time = event.BuilderKeyResponse()
    vividness.reset()
    If_No_Resp = event.BuilderKeyResponse()
    # keep track of which components have finished
    trial1Components = [empty_gray, fixation_cross, image, n_objets, reaction_time, vividness, If_No_Resp, cross, image_in, image_out, RT]
    for thisComponent in trial1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial1"-------
    while continueRoutine:
        # get current time
        t = trial1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *empty_gray* updates
        if t >= 0.0 and empty_gray.status == NOT_STARTED:
            # keep track of start time/frame for later
            empty_gray.tStart = t
            empty_gray.frameNStart = frameN  # exact frame index
            empty_gray.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if empty_gray.status == STARTED and t >= frameRemains:
            empty_gray.setAutoDraw(False)
        
        # *fixation_cross* updates
        if t >= 1 and fixation_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_cross.tStart = t
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.setAutoDraw(True)
        frameRemains = 1 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_cross.status == STARTED and t >= frameRemains:
            fixation_cross.setAutoDraw(False)
        
        # *image* updates
        if t >= 2.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        frameRemains = 2.5 + 8.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
        # *n_objets* updates
        if (t >=10.5) and n_objets.status == NOT_STARTED:
            # keep track of start time/frame for later
            n_objets.tStart = t
            n_objets.frameNStart = frameN  # exact frame index
            n_objets.setAutoDraw(True)
        
        # *reaction_time* updates
        if t >= 2.5 and reaction_time.status == NOT_STARTED:
            # keep track of start time/frame for later
            reaction_time.tStart = t
            reaction_time.frameNStart = frameN  # exact frame index
            reaction_time.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(reaction_time.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 2.5 + 8.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if reaction_time.status == STARTED and t >= frameRemains:
            reaction_time.status = STOPPED
        if reaction_time.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if reaction_time.keys == []:  # then this was the first keypress
                    reaction_time.keys = theseKeys[0]  # just the first key pressed
                    reaction_time.rt = reaction_time.clock.getTime()
        # *vividness* updates
        if (n_objets.status == FINISHED) and vividness.status == NOT_STARTED:
            # keep track of start time/frame for later
            vividness.tStart = t
            vividness.frameNStart = frameN  # exact frame index
            vividness.setAutoDraw(True)
        continueRoutine &= vividness.noResponse  # a response ends the trial
        
        # *If_No_Resp* updates
        if t >= 10.5 and If_No_Resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            If_No_Resp.tStart = t
            If_No_Resp.frameNStart = frameN  # exact frame index
            If_No_Resp.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if If_No_Resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['q'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        # *cross* updates
        if t >= 1 and cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            cross.tStart = t
            cross.frameNStart = frameN  # exact frame index
            cross.status = STARTED
            win.callOnFlip(cross.setData, int(3))
        frameRemains = 1 + 0.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if cross.status == STARTED and t >= frameRemains:
            cross.status = STOPPED
            win.callOnFlip(cross.setData, int(0))
        # *image_in* updates
        if t >= 2.5 and image_in.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_in.tStart = t
            image_in.frameNStart = frameN  # exact frame index
            image_in.status = STARTED
            win.callOnFlip(image_in.setData, int(4))
        frameRemains = 2.5 + 0.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_in.status == STARTED and t >= frameRemains:
            image_in.status = STOPPED
            win.callOnFlip(image_in.setData, int(0))
        # *image_out* updates
        if t >= 10.5 and image_out.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_out.tStart = t
            image_out.frameNStart = frameN  # exact frame index
            image_out.status = STARTED
            win.callOnFlip(image_out.setData, int(5))
        frameRemains = 10.5 + 0.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_out.status == STARTED and t >= frameRemains:
            image_out.status = STOPPED
            win.callOnFlip(image_out.setData, int(0))
        # *RT* updates
        if (reaction_time==True) and RT.status == NOT_STARTED:
            # keep track of start time/frame for later
            RT.tStart = t
            RT.frameNStart = frameN  # exact frame index
            RT.status = STARTED
            win.callOnFlip(RT.setData, int(6))
        if RT.status == STARTED and t >= (RT.tStart + 0.1):
            RT.status = STOPPED
            win.callOnFlip(RT.setData, int(0))
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial1"-------
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_3 (TrialHandler)
    trials_3.addData('n_objets.response', n_objets.getRating())
    # check responses
    if reaction_time.keys in ['', [], None]:  # No response was made
        reaction_time.keys=None
    trials_3.addData('reaction_time.keys',reaction_time.keys)
    if reaction_time.keys != None:  # we had a response
        trials_3.addData('reaction_time.rt', reaction_time.rt)
    # store data for trials_3 (TrialHandler)
    trials_3.addData('vividness.response', vividness.getRating())
    trials_3.addData('vividness.rt', vividness.getRT())
    if cross.status == STARTED:
        win.callOnFlip(cross.setData, int(0))
    if image_in.status == STARTED:
        win.callOnFlip(image_in.setData, int(0))
    if image_out.status == STARTED:
        win.callOnFlip(image_out.setData, int(0))
    if RT.status == STARTED:
        win.callOnFlip(RT.setData, int(0))
    # the Routine "trial1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_3'


# ------Prepare to start Routine "Fin_bloc"-------
t = 0
Fin_blocClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_8 = event.BuilderKeyResponse()
# keep track of which components have finished
Fin_blocComponents = [text_7, key_resp_8]
for thisComponent in Fin_blocComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Fin_bloc"-------
while continueRoutine:
    # get current time
    t = Fin_blocClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if t >= 0.0 and text_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_7.tStart = t
        text_7.frameNStart = frameN  # exact frame index
        text_7.setAutoDraw(True)
    
    # *key_resp_8* updates
    if t >= 0.0 and key_resp_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_8.tStart = t
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_8.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_8.keys = theseKeys[-1]  # just the last key pressed
            key_resp_8.rt = key_resp_8.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Fin_blocComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Fin_bloc"-------
for thisComponent in Fin_blocComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys=None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.nextEntry()
# the Routine "Fin_bloc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Mental_fatigue"-------
t = 0
Mental_fatigueClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
Fatigue.reset()
# keep track of which components have finished
Mental_fatigueComponents = [Fatigue]
for thisComponent in Mental_fatigueComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Mental_fatigue"-------
while continueRoutine:
    # get current time
    t = Mental_fatigueClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *Fatigue* updates
    if t >= 0.0 and Fatigue.status == NOT_STARTED:
        # keep track of start time/frame for later
        Fatigue.tStart = t
        Fatigue.frameNStart = frameN  # exact frame index
        Fatigue.setAutoDraw(True)
    continueRoutine &= Fatigue.noResponse  # a response ends the trial
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Mental_fatigueComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Mental_fatigue"-------
for thisComponent in Mental_fatigueComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('Fatigue.response', Fatigue.getRating())
thisExp.addData('Fatigue.rt', Fatigue.getRT())
thisExp.nextEntry()
# the Routine "Mental_fatigue" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Flow"-------
t = 0
FlowClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_7 = event.BuilderKeyResponse()
# keep track of which components have finished
FlowComponents = [text_6, key_resp_7]
for thisComponent in FlowComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Flow"-------
while continueRoutine:
    # get current time
    t = FlowClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if t >= 0.0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    
    # *key_resp_7* updates
    if t >= 0.0 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_7.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FlowComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Flow"-------
for thisComponent in FlowComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Flow" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Flow_questions"-------
t = 0
Flow_questionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
Flow01.reset()
Flow02.reset()
Flow03.reset()
Flow04.reset()
Flow05.reset()
Flow06.reset()
Flow07.reset()
Flow08.reset()
Flow09.reset()
Flow10.reset()
# keep track of which components have finished
Flow_questionsComponents = [Flow01, Flow02, Flow03, Flow04, Flow05, Flow06, Flow07, Flow08, Flow09, Flow10]
for thisComponent in Flow_questionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Flow_questions"-------
while continueRoutine:
    # get current time
    t = Flow_questionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *Flow01* updates
    if t >= 0.0 and Flow01.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow01.tStart = t
        Flow01.frameNStart = frameN  # exact frame index
        Flow01.setAutoDraw(True)
    # *Flow02* updates
    if t >= Flow01.status == FINISHED and Flow02.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow02.tStart = t
        Flow02.frameNStart = frameN  # exact frame index
        Flow02.setAutoDraw(True)
    # *Flow03* updates
    if t >= Flow02.status == FINISHED and Flow03.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow03.tStart = t
        Flow03.frameNStart = frameN  # exact frame index
        Flow03.setAutoDraw(True)
    # *Flow04* updates
    if t >= Flow03.status == FINISHED and Flow04.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow04.tStart = t
        Flow04.frameNStart = frameN  # exact frame index
        Flow04.setAutoDraw(True)
    # *Flow05* updates
    if t >= Flow04.status == FINISHED and Flow05.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow05.tStart = t
        Flow05.frameNStart = frameN  # exact frame index
        Flow05.setAutoDraw(True)
    # *Flow06* updates
    if t >= Flow05.status == FINISHED and Flow06.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow06.tStart = t
        Flow06.frameNStart = frameN  # exact frame index
        Flow06.setAutoDraw(True)
    # *Flow07* updates
    if t >= Flow06.status == FINISHED and Flow07.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow07.tStart = t
        Flow07.frameNStart = frameN  # exact frame index
        Flow07.setAutoDraw(True)
    # *Flow08* updates
    if t >= Flow07.status == FINISHED and Flow08.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow08.tStart = t
        Flow08.frameNStart = frameN  # exact frame index
        Flow08.setAutoDraw(True)
    # *Flow09* updates
    if t >= Flow08.status == FINISHED and Flow09.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow09.tStart = t
        Flow09.frameNStart = frameN  # exact frame index
        Flow09.setAutoDraw(True)
    # *Flow10* updates
    if t >= Flow09.status == FINISHED and Flow10.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow10.tStart = t
        Flow10.frameNStart = frameN  # exact frame index
        Flow10.setAutoDraw(True)
    continueRoutine &= Flow10.noResponse  # a response ends the trial
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Flow_questionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Flow_questions"-------
for thisComponent in Flow_questionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow01.response', Flow01.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow02.response', Flow02.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow03.response', Flow03.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow04.response', Flow04.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow05.response', Flow05.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow06.response', Flow06.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow07.response', Flow07.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow08.response', Flow08.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow09.response', Flow09.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow10.response', Flow10.getRating())
thisExp.nextEntry()
# the Routine "Flow_questions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Redondance"-------
t = 0
RedondanceClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
Redondance_question.reset()
# keep track of which components have finished
RedondanceComponents = [Redondance_question]
for thisComponent in RedondanceComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Redondance"-------
while continueRoutine:
    # get current time
    t = RedondanceClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *Redondance_question* updates
    if t >= 0.0 and Redondance_question.status == NOT_STARTED:
        # keep track of start time/frame for later
        Redondance_question.tStart = t
        Redondance_question.frameNStart = frameN  # exact frame index
        Redondance_question.setAutoDraw(True)
    continueRoutine &= Redondance_question.noResponse  # a response ends the trial
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RedondanceComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Redondance"-------
for thisComponent in RedondanceComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('Redondance_question.response', Redondance_question.getRating())
thisExp.nextEntry()
# the Routine "Redondance" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions_sham"-------
t = 0
Instructions_shamClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_11 = event.BuilderKeyResponse()
# keep track of which components have finished
Instructions_shamComponents = [instructions_sham, key_resp_11]
for thisComponent in Instructions_shamComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instructions_sham"-------
while continueRoutine:
    # get current time
    t = Instructions_shamClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_sham* updates
    if t >= 0.0 and instructions_sham.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions_sham.tStart = t
        instructions_sham.frameNStart = frameN  # exact frame index
        instructions_sham.setAutoDraw(True)
    
    # *key_resp_11* updates
    if t >= 0.0 and key_resp_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_11.tStart = t
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_11.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_11.keys = theseKeys[-1]  # just the last key pressed
            key_resp_11.rt = key_resp_11.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions_shamComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions_sham"-------
for thisComponent in Instructions_shamComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_11.keys in ['', [], None]:  # No response was made
    key_resp_11.keys=None
thisExp.addData('key_resp_11.keys',key_resp_11.keys)
if key_resp_11.keys != None:  # we had a response
    thisExp.addData('key_resp_11.rt', key_resp_11.rt)
thisExp.nextEntry()
# the Routine "Instructions_sham" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_sham = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Images_sham.xlsx'),
    seed=None, name='trials_sham')
thisExp.addLoop(trials_sham)  # add the loop to the experiment
thisTrials_sham = trials_sham.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_sham.rgb)
if thisTrials_sham != None:
    for paramName in thisTrials_sham:
        exec('{} = thisTrials_sham[paramName]'.format(paramName))

for thisTrials_sham in trials_sham:
    currentLoop = trials_sham
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_sham.rgb)
    if thisTrials_sham != None:
        for paramName in thisTrials_sham:
            exec('{} = thisTrials_sham[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial1"-------
    t = 0
    trial1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image.setImage(ImageFile)
    n_objets.reset()
    reaction_time = event.BuilderKeyResponse()
    vividness.reset()
    If_No_Resp = event.BuilderKeyResponse()
    # keep track of which components have finished
    trial1Components = [empty_gray, fixation_cross, image, n_objets, reaction_time, vividness, If_No_Resp, cross, image_in, image_out, RT]
    for thisComponent in trial1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial1"-------
    while continueRoutine:
        # get current time
        t = trial1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *empty_gray* updates
        if t >= 0.0 and empty_gray.status == NOT_STARTED:
            # keep track of start time/frame for later
            empty_gray.tStart = t
            empty_gray.frameNStart = frameN  # exact frame index
            empty_gray.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if empty_gray.status == STARTED and t >= frameRemains:
            empty_gray.setAutoDraw(False)
        
        # *fixation_cross* updates
        if t >= 1 and fixation_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_cross.tStart = t
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.setAutoDraw(True)
        frameRemains = 1 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_cross.status == STARTED and t >= frameRemains:
            fixation_cross.setAutoDraw(False)
        
        # *image* updates
        if t >= 2.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        frameRemains = 2.5 + 8.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
        # *n_objets* updates
        if (t >=10.5) and n_objets.status == NOT_STARTED:
            # keep track of start time/frame for later
            n_objets.tStart = t
            n_objets.frameNStart = frameN  # exact frame index
            n_objets.setAutoDraw(True)
        
        # *reaction_time* updates
        if t >= 2.5 and reaction_time.status == NOT_STARTED:
            # keep track of start time/frame for later
            reaction_time.tStart = t
            reaction_time.frameNStart = frameN  # exact frame index
            reaction_time.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(reaction_time.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 2.5 + 8.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if reaction_time.status == STARTED and t >= frameRemains:
            reaction_time.status = STOPPED
        if reaction_time.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if reaction_time.keys == []:  # then this was the first keypress
                    reaction_time.keys = theseKeys[0]  # just the first key pressed
                    reaction_time.rt = reaction_time.clock.getTime()
        # *vividness* updates
        if (n_objets.status == FINISHED) and vividness.status == NOT_STARTED:
            # keep track of start time/frame for later
            vividness.tStart = t
            vividness.frameNStart = frameN  # exact frame index
            vividness.setAutoDraw(True)
        continueRoutine &= vividness.noResponse  # a response ends the trial
        
        # *If_No_Resp* updates
        if t >= 10.5 and If_No_Resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            If_No_Resp.tStart = t
            If_No_Resp.frameNStart = frameN  # exact frame index
            If_No_Resp.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if If_No_Resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['q'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        # *cross* updates
        if t >= 1 and cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            cross.tStart = t
            cross.frameNStart = frameN  # exact frame index
            cross.status = STARTED
            win.callOnFlip(cross.setData, int(3))
        frameRemains = 1 + 0.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if cross.status == STARTED and t >= frameRemains:
            cross.status = STOPPED
            win.callOnFlip(cross.setData, int(0))
        # *image_in* updates
        if t >= 2.5 and image_in.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_in.tStart = t
            image_in.frameNStart = frameN  # exact frame index
            image_in.status = STARTED
            win.callOnFlip(image_in.setData, int(4))
        frameRemains = 2.5 + 0.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_in.status == STARTED and t >= frameRemains:
            image_in.status = STOPPED
            win.callOnFlip(image_in.setData, int(0))
        # *image_out* updates
        if t >= 10.5 and image_out.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_out.tStart = t
            image_out.frameNStart = frameN  # exact frame index
            image_out.status = STARTED
            win.callOnFlip(image_out.setData, int(5))
        frameRemains = 10.5 + 0.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_out.status == STARTED and t >= frameRemains:
            image_out.status = STOPPED
            win.callOnFlip(image_out.setData, int(0))
        # *RT* updates
        if (reaction_time==True) and RT.status == NOT_STARTED:
            # keep track of start time/frame for later
            RT.tStart = t
            RT.frameNStart = frameN  # exact frame index
            RT.status = STARTED
            win.callOnFlip(RT.setData, int(6))
        if RT.status == STARTED and t >= (RT.tStart + 0.1):
            RT.status = STOPPED
            win.callOnFlip(RT.setData, int(0))
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial1"-------
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_sham (TrialHandler)
    trials_sham.addData('n_objets.response', n_objets.getRating())
    # check responses
    if reaction_time.keys in ['', [], None]:  # No response was made
        reaction_time.keys=None
    trials_sham.addData('reaction_time.keys',reaction_time.keys)
    if reaction_time.keys != None:  # we had a response
        trials_sham.addData('reaction_time.rt', reaction_time.rt)
    # store data for trials_sham (TrialHandler)
    trials_sham.addData('vividness.response', vividness.getRating())
    trials_sham.addData('vividness.rt', vividness.getRT())
    if cross.status == STARTED:
        win.callOnFlip(cross.setData, int(0))
    if image_in.status == STARTED:
        win.callOnFlip(image_in.setData, int(0))
    if image_out.status == STARTED:
        win.callOnFlip(image_out.setData, int(0))
    if RT.status == STARTED:
        win.callOnFlip(RT.setData, int(0))
    # the Routine "trial1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_sham'


# ------Prepare to start Routine "Mental_fatigue"-------
t = 0
Mental_fatigueClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
Fatigue.reset()
# keep track of which components have finished
Mental_fatigueComponents = [Fatigue]
for thisComponent in Mental_fatigueComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Mental_fatigue"-------
while continueRoutine:
    # get current time
    t = Mental_fatigueClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *Fatigue* updates
    if t >= 0.0 and Fatigue.status == NOT_STARTED:
        # keep track of start time/frame for later
        Fatigue.tStart = t
        Fatigue.frameNStart = frameN  # exact frame index
        Fatigue.setAutoDraw(True)
    continueRoutine &= Fatigue.noResponse  # a response ends the trial
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Mental_fatigueComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Mental_fatigue"-------
for thisComponent in Mental_fatigueComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('Fatigue.response', Fatigue.getRating())
thisExp.addData('Fatigue.rt', Fatigue.getRT())
thisExp.nextEntry()
# the Routine "Mental_fatigue" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Flow"-------
t = 0
FlowClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_7 = event.BuilderKeyResponse()
# keep track of which components have finished
FlowComponents = [text_6, key_resp_7]
for thisComponent in FlowComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Flow"-------
while continueRoutine:
    # get current time
    t = FlowClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if t >= 0.0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    
    # *key_resp_7* updates
    if t >= 0.0 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_7.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FlowComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Flow"-------
for thisComponent in FlowComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Flow" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Flow_questions"-------
t = 0
Flow_questionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
Flow01.reset()
Flow02.reset()
Flow03.reset()
Flow04.reset()
Flow05.reset()
Flow06.reset()
Flow07.reset()
Flow08.reset()
Flow09.reset()
Flow10.reset()
# keep track of which components have finished
Flow_questionsComponents = [Flow01, Flow02, Flow03, Flow04, Flow05, Flow06, Flow07, Flow08, Flow09, Flow10]
for thisComponent in Flow_questionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Flow_questions"-------
while continueRoutine:
    # get current time
    t = Flow_questionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *Flow01* updates
    if t >= 0.0 and Flow01.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow01.tStart = t
        Flow01.frameNStart = frameN  # exact frame index
        Flow01.setAutoDraw(True)
    # *Flow02* updates
    if t >= Flow01.status == FINISHED and Flow02.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow02.tStart = t
        Flow02.frameNStart = frameN  # exact frame index
        Flow02.setAutoDraw(True)
    # *Flow03* updates
    if t >= Flow02.status == FINISHED and Flow03.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow03.tStart = t
        Flow03.frameNStart = frameN  # exact frame index
        Flow03.setAutoDraw(True)
    # *Flow04* updates
    if t >= Flow03.status == FINISHED and Flow04.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow04.tStart = t
        Flow04.frameNStart = frameN  # exact frame index
        Flow04.setAutoDraw(True)
    # *Flow05* updates
    if t >= Flow04.status == FINISHED and Flow05.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow05.tStart = t
        Flow05.frameNStart = frameN  # exact frame index
        Flow05.setAutoDraw(True)
    # *Flow06* updates
    if t >= Flow05.status == FINISHED and Flow06.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow06.tStart = t
        Flow06.frameNStart = frameN  # exact frame index
        Flow06.setAutoDraw(True)
    # *Flow07* updates
    if t >= Flow06.status == FINISHED and Flow07.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow07.tStart = t
        Flow07.frameNStart = frameN  # exact frame index
        Flow07.setAutoDraw(True)
    # *Flow08* updates
    if t >= Flow07.status == FINISHED and Flow08.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow08.tStart = t
        Flow08.frameNStart = frameN  # exact frame index
        Flow08.setAutoDraw(True)
    # *Flow09* updates
    if t >= Flow08.status == FINISHED and Flow09.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow09.tStart = t
        Flow09.frameNStart = frameN  # exact frame index
        Flow09.setAutoDraw(True)
    # *Flow10* updates
    if t >= Flow09.status == FINISHED and Flow10.status == NOT_STARTED:
        # keep track of start time/frame for later
        Flow10.tStart = t
        Flow10.frameNStart = frameN  # exact frame index
        Flow10.setAutoDraw(True)
    continueRoutine &= Flow10.noResponse  # a response ends the trial
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Flow_questionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Flow_questions"-------
for thisComponent in Flow_questionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow01.response', Flow01.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow02.response', Flow02.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow03.response', Flow03.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow04.response', Flow04.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow05.response', Flow05.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow06.response', Flow06.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow07.response', Flow07.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow08.response', Flow08.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow09.response', Flow09.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('Flow10.response', Flow10.getRating())
thisExp.nextEntry()
# the Routine "Flow_questions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Resting_state_instructions2"-------
t = 0
Resting_state_instructions2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Resting_state_instructions2Components = [resting_instructions_end]
for thisComponent in Resting_state_instructions2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Resting_state_instructions2"-------
while continueRoutine:
    # get current time
    t = Resting_state_instructions2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *resting_instructions_end* updates
    if t >= 0.0 and resting_instructions_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        resting_instructions_end.tStart = t
        resting_instructions_end.frameNStart = frameN  # exact frame index
        resting_instructions_end.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Resting_state_instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Resting_state_instructions2"-------
for thisComponent in Resting_state_instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Resting_state_instructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Resting_state"-------
t = 0
Resting_stateClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_10 = event.BuilderKeyResponse()
# keep track of which components have finished
Resting_stateComponents = [fix_resting_state, key_resp_10, RS01_in, RS01_out]
for thisComponent in Resting_stateComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Resting_state"-------
while continueRoutine:
    # get current time
    t = Resting_stateClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fix_resting_state* updates
    if t >= 0.0 and fix_resting_state.status == NOT_STARTED:
        # keep track of start time/frame for later
        fix_resting_state.tStart = t
        fix_resting_state.frameNStart = frameN  # exact frame index
        fix_resting_state.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if fix_resting_state.status == STARTED and t >= frameRemains:
        fix_resting_state.setAutoDraw(False)
    
    # *key_resp_10* updates
    if t >= 0.0 and key_resp_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_10.tStart = t
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_10.status == STARTED:
        theseKeys = event.getKeys(keyList=['q'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_10.keys = theseKeys[-1]  # just the last key pressed
            key_resp_10.rt = key_resp_10.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    # *RS01_in* updates
    if t >= 0.0 and RS01_in.status == NOT_STARTED:
        # keep track of start time/frame for later
        RS01_in.tStart = t
        RS01_in.frameNStart = frameN  # exact frame index
        RS01_in.status = STARTED
        win.callOnFlip(RS01_in.setData, int(1))
    frameRemains = 0.0 + 0.1- win.monitorFramePeriod * 0.75  # most of one frame period left
    if RS01_in.status == STARTED and t >= frameRemains:
        RS01_in.status = STOPPED
        win.callOnFlip(RS01_in.setData, int(0))
    # *RS01_out* updates
    if t >= 5 and RS01_out.status == NOT_STARTED:
        # keep track of start time/frame for later
        RS01_out.tStart = t
        RS01_out.frameNStart = frameN  # exact frame index
        RS01_out.status = STARTED
        win.callOnFlip(RS01_out.setData, int(2))
    frameRemains = 5 + 0.1- win.monitorFramePeriod * 0.75  # most of one frame period left
    if RS01_out.status == STARTED and t >= frameRemains:
        RS01_out.status = STOPPED
        win.callOnFlip(RS01_out.setData, int(0))
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Resting_stateComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Resting_state"-------
for thisComponent in Resting_stateComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_10.keys in ['', [], None]:  # No response was made
    key_resp_10.keys=None
thisExp.addData('key_resp_10.keys',key_resp_10.keys)
if key_resp_10.keys != None:  # we had a response
    thisExp.addData('key_resp_10.rt', key_resp_10.rt)
thisExp.nextEntry()
if RS01_in.status == STARTED:
    win.callOnFlip(RS01_in.setData, int(0))
if RS01_out.status == STARTED:
    win.callOnFlip(RS01_out.setData, int(0))
# the Routine "Resting_state" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Sham"-------
t = 0
ShamClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating.reset()
# keep track of which components have finished
ShamComponents = [rating]
for thisComponent in ShamComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Sham"-------
while continueRoutine:
    # get current time
    t = ShamClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *rating* updates
    if t >= 0.0 and rating.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating.tStart = t
        rating.frameNStart = frameN  # exact frame index
        rating.setAutoDraw(True)
    continueRoutine &= rating.noResponse  # a response ends the trial
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ShamComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Sham"-------
for thisComponent in ShamComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating.response', rating.getRating())
thisExp.addData('rating.rt', rating.getRT())
thisExp.nextEntry()
# the Routine "Sham" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Finito"-------
t = 0
FinitoClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
FinitoComponents = [text_5]
for thisComponent in FinitoComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Finito"-------
while continueRoutine:
    # get current time
    t = FinitoClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if t >= 0.0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t
        text_5.frameNStart = frameN  # exact frame index
        text_5.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FinitoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Finito"-------
for thisComponent in FinitoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Finito" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
