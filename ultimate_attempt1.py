#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.1),
    on Thu May 18 13:28:10 2017
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound, monitors, tools 
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import random
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'trial'  # from the Builder filename that created this script
expInfo = {u'participant': u'', u'age': u'', u'sex': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

### INFO ABOUT THE NUMBER AND SIZE OF DOTS
totalNumberOfDots = 30;
scopeOfTheDistribution = 160;
mon=monitors.Monitor('myComputer')
sizeOfDots = tools.monitorunittools.deg2pix(6.75/60, mon);


####ADDING TWO FUNCTIONS RESPONSIBLE FOR GENERATION OF NORMAL DISTRIBUTION AND NOISE


#this function generates a bump that was used in the study, num is the parameter for number of dots and rad is the scope 
#this function returns a list of [x,y] coordinates that can be plotted 
def generate_bump(num, rad):
    cov = np.identity(2)*rad
    distribution = np.random.multivariate_normal([0,0],cov, size=num)
    x = distribution[:,0]
    y = distribution[:,1]
    new = [[x[i], y[i]] for i in range(len(x))]
    return new

#this function is supposed to extract the number of dots that are thought to be a noise. it returns a list of [x,y] coordinates - it is a list of length n - number of dots that were taken to create a noise
def extract_noise(array,noise):
    array = np.array(array)
    x_array = array[:,0]
    y_array = array[:,1]
    numberofrandom = int(noise*len(array))
    randomindices = np.array(random.sample(range(0, len(array)), numberofrandom))
    new_x = np.delete(x_array, randomindices)
    new_y = np.delete(y_array, randomindices)
    new = [[new_x[i], new_y[i]] for i in range(len(new_x))]
    return new


# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

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

#default dot variable to be like a placeholder for the components



# Setup the Window
win = visual.Window(
    size=(1280, 800), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor=u'myComputer', color=[0.0,0.0,0.0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='pix')

defaultDot = visual.ElementArrayStim(win=win, name="VisualStandard", 
    units="pix", fieldPos = [0,0], fieldSize=[150,150], 
    nElements=totalNumberOfDots, elementTex=None, elementMask="circle", 
    xys=generate_bump(totalNumberOfDots, scopeOfTheDistribution), sizes=sizeOfDots)

# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "WelcomeMessage"
WelcomeMessageClock = core.Clock()
WelcomeText = visual.TextStim(win=win, name='WelcomeText',
    text='Welcome to the experiment! \n\nIn this experiment, you will be presented with three types of block - one consisting only audio stimuli, one consisting only visual stimuli and one with both types of stimuli. \nYou will have to estimate the location of the presented stimulus.\n\n\nPress space to continue. ',
    font='Arial',
    pos=(0, 0), height=25, wrapWidth=800, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Instruction"
InstructionClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=u'In each block you will be presented with a set of pairs of stimuli. \nYou will have to judge whether the second stimulus in the pair was to the right of the first stimulus. \n\nIf you have any questions, do not hesitate to contact the experimenter before the blocks start. \n\nPress space to begin the experiment.',
    font=u'Arial',
    pos=(0, 0), height=25, wrapWidth=800, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "AudioInstruction"
AudioInstructionClock = core.Clock()
AudioInstr = visual.TextStim(win=win, name='AudioInstr',
    text=u'This is a block with auditory stimuli.\nIn this block, you have to estimate a location of the sound.\nYou will be presented with a set of pairs of sounds. \nYour task is to estimate whether the second sound of the pair was coming from a location to the right of the first sound. \nIf it is to the right, press right arrow. If not, press left arrow. \nPairs are separated with a short beep sound.\n\nPress space to start a block. ',
    font=u'Arial',
    pos=(0, 0), height=25, wrapWidth=800, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "AudioTrials"
AudioTrialsClock = core.Clock()
beforeStimuli1 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='beforeStimuli1')
fixationSound = sound.Sound('A', secs=-1)
fixationSound.setVolume(1)
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
Standard = sound.Sound(_thisDir + '/sounds/legit/equal.wav', secs=-1)
Standard.setVolume(1)
Comparison = sound.Sound('A', secs=-1)
Comparison.setVolume(1)
beforeStimuli2 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='beforeStimuli2')

# Initialize components for Routine "VisualInstruction"
VisualInstructionClock = core.Clock()
VisualInstr = visual.TextStim(win=win, name='VisualInstr',
    text=u'This is a block with visual stimuli.\nIn this block, you have to estimate a location of the visual stimulus.\nYou will be presented with a set of pairs of dot stereograms. \nYour task is to estimate whether the second stimulus of the pair was coming from a location to the right of the first stimulus. \nIf it is to the right, press right arrow. If not, press left arrow. \nPairs are separated with a fixation cross.\n\nPress space to start a block. ',
    font=u'Arial',
    pos=(0, 0), height=25, wrapWidth=800, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "VisualTrials"
VisualTrialsClock = core.Clock()
VisualStandard = defaultDot
VisualISIBefore = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='VisualISIBefore')
VisualBreak = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='VisualBreak')
VisualComparison = defaultDot
VisualNoiseElement = defaultDot
fixationCross = visual.TextStim(win=win, name='fixationCross',
    text=u'+',
    font=u'Arial',
    pos=(0, 0), height=30, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-5.0);

# Initialize components for Routine "CombinedInstruction"
CombinedInstructionClock = core.Clock()
CombinedInstr = visual.TextStim(win=win, name='CombinedInstr',
    text=u'This is a block with mixed (visual and auditory) stimuli.\nIn this block, you have to estimate a location of the multimodal signal.\nYou will be presented with a set of pairs of multimodal signals. \nYour task is to estimate whether the second signal of the pair was coming from a location to the right of the first signal. \nIf it is to the right, press right arrow. If not, press left arrow. \nPairs are separated with short beep and fixation cross.\n\nPress space to start a block. ',
    font=u'Arial',
    pos=(0, 0), height=25, wrapWidth=800, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "CombinedTrials"
CombinedTrialsClock = core.Clock()
CombinedISI1 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='CombinedISI1')
# CombVisualStandard = visual.ImageStim(
#     win=win, name='CombVisualStandard',units='degFlat', 
#     image='/Users/admin/Documents/IT&Cognition/Cognitive Science2/experiment-exam/catimg.png', mask=None,
#     ori=0, pos=[-2.25,0], size=(0.5, 0.5),
#     color=[1,1,1], colorSpace='rgb', opacity=1,
#     flipHoriz=False, flipVert=False,
#     texRes=128, interpolate=True, depth=-1.0)
CombVisualStandard = defaultDot
CombSoundStandard = sound.Sound(_thisDir + '/sounds/legit/right30.wav', secs=-1)
CombSoundStandard.setVolume(1)
AfterStandardISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='AfterStandardISI')
CombSoundComparison = sound.Sound('A', secs=-1)
CombSoundComparison.setVolume(1)
# CombVisualComparison = visual.ImageStim(
#     win=win, name='CombVisualComparison',units='degFlat', 
#     image='sin', mask=None,
#     ori=0, pos=[0,0], size=(0.5, 0.5),
#     color=[1,1,1], colorSpace='rgb', opacity=1,
#     flipHoriz=False, flipVert=False,
#     texRes=128, interpolate=True, depth=-5.0)
CombVisualComparison = defaultDot
CombVisualNoiseElement = defaultDot
combineaudioFix = sound.Sound("A", secs=-1)
combineaudioFix.setVolume(1)
combinedFixationCross = visual.TextStim(win=win, name='combinedFixationCross',
    text=u'+',
    font=u'Arial',
    pos=(0, 0), height=30, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-8.0);
CombinedISI2 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='CombinedISI2')

# Initialize components for Routine "End"
EndClock = core.Clock()
EndMessage = visual.TextStim(win=win, name='EndMessage',
    text='Thank you for participating in the study!',
    font='Arial',
    pos=(0, 0), height=30, wrapWidth=800, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);


####TRIAL HANDLERS:
audiotrials = data.TrialHandler(nReps=15, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('audio_stimuli_description.csv'),
    seed=None, name='audiotrials');

visualTrials = data.TrialHandler(nReps=15, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('visualAndCombined.csv'),
    seed=None, name='visualTrials');

combinedTrials = data.TrialHandler(nReps=15, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('visualAndCombined.csv'),
    seed=None, name='combinedTrials');

# blocks = [audiotrials, visualTrials, combinedTrials];
# random.shuffle(blocks)




# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "WelcomeMessage"-------
t = 0
WelcomeMessageClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
WelcomeKey = event.BuilderKeyResponse()
# keep track of which components have finished
WelcomeMessageComponents = [WelcomeText, WelcomeKey]
for thisComponent in WelcomeMessageComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "WelcomeMessage"-------
while continueRoutine:
    # get current time
    t = WelcomeMessageClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *WelcomeText* updates
    if t >= 0.0 and WelcomeText.status == NOT_STARTED:
        # keep track of start time/frame for later
        WelcomeText.tStart = t
        WelcomeText.frameNStart = frameN  # exact frame index
        WelcomeText.setAutoDraw(True)
    
    # *WelcomeKey* updates
    if t >= 0.0 and WelcomeKey.status == NOT_STARTED:
        # keep track of start time/frame for later
        WelcomeKey.tStart = t
        WelcomeKey.frameNStart = frameN  # exact frame index
        WelcomeKey.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(WelcomeKey.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if WelcomeKey.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            WelcomeKey.keys = theseKeys[-1]  # just the last key pressed
            WelcomeKey.rt = WelcomeKey.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeMessageComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WelcomeMessage"-------
for thisComponent in WelcomeMessageComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if WelcomeKey.keys in ['', [], None]:  # No response was made
    WelcomeKey.keys=None
thisExp.addData('WelcomeKey.keys',WelcomeKey.keys)
if WelcomeKey.keys != None:  # we had a response
    thisExp.addData('WelcomeKey.rt', WelcomeKey.rt)
thisExp.nextEntry()
# the Routine "WelcomeMessage" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instruction"-------
t = 0
InstructionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
InstructionComponents = [text, key_resp_2]
for thisComponent in InstructionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instruction"-------
while continueRoutine:
    # get current time
    t = InstructionClock.getTime()
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
    for thisComponent in InstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruction"-------
for thisComponent in InstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys=None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()



    # ------Prepare to start Routine "AudioInstruction"-------
t = 0
AudioInstructionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
AudioInstrAccept = event.BuilderKeyResponse()
# keep track of which components have finished
AudioInstructionComponents = [AudioInstr, AudioInstrAccept]
for thisComponent in AudioInstructionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "AudioInstruction"-------
while continueRoutine:
    # get current time
    t = AudioInstructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *AudioInstr* updates
    if t >= 0.0 and AudioInstr.status == NOT_STARTED:
        # keep track of start time/frame for later
        AudioInstr.tStart = t
        AudioInstr.frameNStart = frameN  # exact frame index
        AudioInstr.setAutoDraw(True)
    
    # *AudioInstrAccept* updates
    if t >= 1.0 and AudioInstrAccept.status == NOT_STARTED:
        # keep track of start time/frame for later
        AudioInstrAccept.tStart = t
        AudioInstrAccept.frameNStart = frameN  # exact frame index
        AudioInstrAccept.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(AudioInstrAccept.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if AudioInstrAccept.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            AudioInstrAccept.keys = theseKeys[-1]  # just the last key pressed
            AudioInstrAccept.rt = AudioInstrAccept.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in AudioInstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "AudioInstruction"-------
for thisComponent in AudioInstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if AudioInstrAccept.keys in ['', [], None]:  # No response was made
    AudioInstrAccept.keys=None
thisExp.addData('AudioInstrAccept.keys',AudioInstrAccept.keys)
if AudioInstrAccept.keys != None:  # we had a response
    thisExp.addData('AudioInstrAccept.rt', AudioInstrAccept.rt)
thisExp.nextEntry()
# the Routine "AudioInstruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc

thisExp.addLoop(audiotrials)  # add the loop to the experiment
thisAudiotrial = audiotrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisAudiotrial.rgb)
if thisAudiotrial != None:
    for paramName in thisAudiotrial.keys():
        exec(paramName + '= thisAudiotrial.' + paramName)

for thisAudiotrial in audiotrials:
    currentLoop = audiotrials
    # abbreviate parameter names if possible (e.g. rgb = thisAudiotrial.rgb)
    if thisAudiotrial != None:
        for paramName in thisAudiotrial.keys():
            exec(paramName + '= thisAudiotrial.' + paramName)
    
    # ------Prepare to start Routine "AudioTrials"-------
    t = 0
    AudioTrialsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    Comparison.setSound(_thisDir + path, secs=-1)
    LeftorRight = event.BuilderKeyResponse()
    # keep track of which components have finished
    AudioTrialsComponents = [beforeStimuli1, fixationSound, ISI, Standard, Comparison, LeftorRight, beforeStimuli2]
    for thisComponent in AudioTrialsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "AudioTrials"-------
    while continueRoutine:
        # get current time
        t = AudioTrialsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop fixationSound
        if t >= 0.3 and fixationSound.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixationSound.tStart = t
            fixationSound.frameNStart = frameN  # exact frame index
            fixationSound.play()  # start the sound (it finishes automatically)
        # start/stop Standard
        if t >= 1.0 and Standard.status == NOT_STARTED:
            # keep track of start time/frame for later
            Standard.tStart = t
            Standard.frameNStart = frameN  # exact frame index
            Standard.play()  # start the sound (it finishes automatically)
        # start/stop Comparison
        if t >= 2.0 and Comparison.status == NOT_STARTED:
            # keep track of start time/frame for later
            Comparison.tStart = t
            Comparison.frameNStart = frameN  # exact frame index
            Comparison.play()  # start the sound (it finishes automatically)
        
        # *LeftorRight* updates
        if t >= 2.5 and LeftorRight.status == NOT_STARTED:
            # keep track of start time/frame for later
            LeftorRight.tStart = t
            LeftorRight.frameNStart = frameN  # exact frame index
            LeftorRight.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(LeftorRight.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if LeftorRight.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                LeftorRight.keys = theseKeys[-1]  # just the last key pressed
                LeftorRight.rt = LeftorRight.clock.getTime()
                # # was this 'correct'?
                # if (LeftorRight.keys == str(correctAns)) or (LeftorRight.keys == correctAns):
                #     LeftorRight.corr = 1
                # else:
                #     LeftorRight.corr = 0
                # a response ends the routine
                continueRoutine = False
        # *beforeStimuli1* period
        if t >= 0.0 and beforeStimuli1.status == NOT_STARTED:
            # keep track of start time/frame for later
            beforeStimuli1.tStart = t
            beforeStimuli1.frameNStart = frameN  # exact frame index
            beforeStimuli1.start(0.3)
        elif beforeStimuli1.status == STARTED:  # one frame should pass before updating params and completing
            # updating other components during *beforeStimuli1*
            fixationSound.setSound(_thisDir + '/sounds/fixationSound.wav', secs=-1)
            # component updates done
            beforeStimuli1.complete()  # finish the static period
        # *ISI* period
        if t >= 1.5 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(0.5)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            ISI.complete()  # finish the static period
        # *beforeStimuli2* period
        if t >= 0.5 and beforeStimuli2.status == NOT_STARTED:
            # keep track of start time/frame for later
            beforeStimuli2.tStart = t
            beforeStimuli2.frameNStart = frameN  # exact frame index
            beforeStimuli2.start(0.5)
        elif beforeStimuli2.status == STARTED:  # one frame should pass before updating params and completing
            beforeStimuli2.complete()  # finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AudioTrialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AudioTrials"-------
    for thisComponent in AudioTrialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    fixationSound.stop()  # ensure sound has stopped at end of routine
    Standard.stop()  # ensure sound has stopped at end of routine
    Comparison.stop()  # ensure sound has stopped at end of routine
    # check responses
    if LeftorRight.keys in ['', [], None]:  # No response was made
        LeftorRight.keys=None
        # was no response the correct answer?!
        if str(correctAns).lower() == 'none':
           LeftorRight.corr = 1  # correct non-response
        else:
           LeftorRight.corr = 0  # failed to respond (incorrectly)
    # store data for audiotrials (TrialHandler)
    audiotrials.addData('LeftorRight.keys',LeftorRight.keys)
    # audiotrials.addData('LeftorRight.corr', LeftorRight.corr)
    if LeftorRight.keys != None:  # we had a response
        audiotrials.addData('LeftorRight.rt', LeftorRight.rt)
    # the Routine "AudioTrials" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 15 repeats of 'audiotrials'
# ------Prepare to start Routine "VisualInstruction"-------
t = 0
VisualInstructionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
VisualBlock = event.BuilderKeyResponse()
# keep track of which components have finished
VisualInstructionComponents = [VisualInstr, VisualBlock]
for thisComponent in VisualInstructionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "VisualInstruction"-------
while continueRoutine:
    # get current time
    t = VisualInstructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *VisualInstr* updates
    if t >= 0.0 and VisualInstr.status == NOT_STARTED:
        # keep track of start time/frame for later
        VisualInstr.tStart = t
        VisualInstr.frameNStart = frameN  # exact frame index
        VisualInstr.setAutoDraw(True)
    
    # *VisualBlock* updates
    if t >= 1.0 and VisualBlock.status == NOT_STARTED:
        # keep track of start time/frame for later
        VisualBlock.tStart = t
        VisualBlock.frameNStart = frameN  # exact frame index
        VisualBlock.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(VisualBlock.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if VisualBlock.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            VisualBlock.keys = theseKeys[-1]  # just the last key pressed
            VisualBlock.rt = VisualBlock.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in VisualInstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "VisualInstruction"-------
for thisComponent in VisualInstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if VisualBlock.keys in ['', [], None]:  # No response was made
    VisualBlock.keys=None
thisExp.addData('VisualBlock.keys',VisualBlock.keys)
if VisualBlock.keys != None:  # we had a response
    thisExp.addData('VisualBlock.rt', VisualBlock.rt)
thisExp.nextEntry()
# the Routine "VisualInstruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc

thisExp.addLoop(visualTrials)  # add the loop to the experiment
thisVisualTrial = visualTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisVisualTrial.rgb)
if thisVisualTrial != None:
    for paramName in thisVisualTrial.keys():
        exec(paramName + '= thisVisualTrial.' + paramName)

for thisVisualTrial in visualTrials:
    currentLoop = visualTrials
    # abbreviate parameter names if possible (e.g. rgb = thisVisualTrial.rgb)
    if thisVisualTrial != None:
        for paramName in thisVisualTrial.keys():
            exec(paramName + '= thisVisualTrial.' + paramName)
    
    # ------Prepare to start Routine "VisualTrials"-------
    t = 0
    VisualTrialsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # VisualStandard.setImage('/Users/admin/Documents/IT&Cognition/Cognitive Science2/experiment-exam/catimg.png')
    currentBump = generate_bump(totalNumberOfDots, scopeOfTheDistribution)
    VisualStandard = visual.ElementArrayStim(win=win, name="VisualStandard", units="pix", fieldPos = [0,0], fieldSize=[150,150], nElements=totalNumberOfDots, elementTex=None, elementMask="circle", xys=currentBump, sizes=sizeOfDots)
    VisualDecision = event.BuilderKeyResponse()
    # keep track of which components have finished
    VisualTrialsComponents = [VisualStandard, VisualISIBefore, VisualBreak, VisualComparison, VisualNoiseElement, VisualDecision, fixationCross]
    for thisComponent in VisualTrialsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "VisualTrials"-------
    while continueRoutine:
        # get current time
        t = VisualTrialsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # VisualStandard = visual.ElementArrayStim(win=win, name="VisualStandard", 
        #     units="pix", fieldPos = [0,0], fieldSize=[150,150], 
        #     nElements=totalNumberOfDots, elementTex=None, elementMask="circle", 
        #     xys=generate_bump(totalNumberOfDots, scopeOfTheDistribution), sizes=sizeOfDots)
        # *VisualStandard* updates
        if t >= 1 and VisualStandard.status == NOT_STARTED:
            # keep track of start time/frame for later
            VisualStandard.tStart = t
            VisualStandard.frameNStart = frameN  # exact frame index
            VisualStandard.setAutoDraw(True)
        frameRemains = 1 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if VisualStandard.status == STARTED and t >= frameRemains:
            VisualStandard.setAutoDraw(False)
            newBump = generate_bump(totalNumberOfDots, scopeOfTheDistribution)
            comparisonBump = extract_noise(newBump, noise)
            numberOfNoiseDots = totalNumberOfDots - len(comparisonBump)
            currentLocation = tools.monitorunittools.deg2pix(location, mon, correctFlat=True)
            VisualComparison = visual.ElementArrayStim(win=win, name="VisualComparison", 
                units="pix", fieldPos = currentLocation, fieldSize=[150,150], 
                nElements=len(comparisonBump), elementTex=None, elementMask="circle", 
                xys=comparisonBump, sizes=sizeOfDots)
            noiseDotsCoordinates = []
            for x in range(numberOfNoiseDots):
                dot_x = random.uniform(-640+(sizeOfDots/2), 640-(sizeOfDots/2))
                dot_y = random.uniform(-400+(sizeOfDots/2), 400-(sizeOfDots/2))
                noiseDotsCoordinates.append([dot_x, dot_y])
            # VisualComparison.setImage('/Users/admin/Documents/IT&Cognition/Cognitive Science2/experiment-exam/catimg.png')
            # component updates done
            VisualNoiseElement = visual.ElementArrayStim(win=win, name="VisualNoiseElement", 
                units="pix", fieldPos = [0,0], fieldSize=[1280,800], 
                nElements=numberOfNoiseDots, elementTex=None, elementMask="circle", 
                xys=noiseDotsCoordinates, sizes=sizeOfDots)
        
        # *VisualComparison* updates
        if t >= 2.0 and VisualComparison.status == NOT_STARTED:
            # keep track of start time/frame for later
            VisualComparison.tStart = t
            VisualNoiseElement.tStart = t
            VisualComparison.frameNStart = frameN  # exact frame index
            VisualNoiseElement.frameNStart = frameN
            VisualComparison.setAutoDraw(True)
            VisualNoiseElement.setAutoDraw(True)
        frameRemains = 2.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if VisualComparison.status == STARTED and t >= frameRemains:
            VisualComparison.setAutoDraw(False)
            VisualNoiseElement.setAutoDraw(False)
        
        # *VisualDecision* updates
        if t >= 2.5 and VisualDecision.status == NOT_STARTED:
            # keep track of start time/frame for later
            VisualDecision.tStart = t
            VisualDecision.frameNStart = frameN  # exact frame index
            VisualDecision.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(VisualDecision.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if VisualDecision.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                VisualDecision.keys = theseKeys[-1]  # just the last key pressed
                VisualDecision.rt = VisualDecision.clock.getTime()
                # was this 'correct'?
                # if (VisualDecision.keys == str('')) or (VisualDecision.keys == ''):
                #     VisualDecision.corr = 1
                # else:
                #     VisualDecision.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *fixationCross* updates
        if t >= 0.0 and fixationCross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixationCross.tStart = t
            fixationCross.frameNStart = frameN  # exact frame index
            fixationCross.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixationCross.status == STARTED and t >= frameRemains:
            fixationCross.setAutoDraw(False)
        # *VisualISIBefore* period
        if t >= 0.0 and VisualISIBefore.status == NOT_STARTED:
            # keep track of start time/frame for later
            VisualISIBefore.tStart = t
            VisualISIBefore.frameNStart = frameN  # exact frame index
            VisualISIBefore.start(1.0)
        elif VisualISIBefore.status == STARTED:  # one frame should pass before updating params and completing
            VisualISIBefore.complete()  # finish the static period
        # *VisualBreak* period
        if t >= 1.5 and VisualBreak.status == NOT_STARTED:
            # keep track of start time/frame for later
            VisualBreak.tStart = t
            VisualBreak.frameNStart = frameN  # exact frame index
            VisualBreak.start(0.5)
        elif VisualBreak.status == STARTED:  # one frame should pass before updating params and completing
            # updating other components during *VisualBreak*
            VisualBreak.complete()  # finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in VisualTrialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "VisualTrials"-------
    for thisComponent in VisualTrialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if VisualDecision.keys in ['', [], None]:  # No response was made
        VisualDecision.keys=None
        # was no response the correct answer?!
        # if str('').lower() == 'none':
        #    VisualDecision.corr = 1  # correct non-response
        # else:
        #    VisualDecision.corr = 0  # failed to respond (incorrectly)
    # store data for visualTrials (TrialHandler)
    visualTrials.addData('VisualDecision.keys',VisualDecision.keys)
    # visualTrials.addData('VisualDecision.corr', VisualDecision.corr)
    if VisualDecision.keys != None:  # we had a response
        visualTrials.addData('VisualDecision.rt', VisualDecision.rt)
    # the Routine "VisualTrials" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 15 repeats of 'visualTrials'
# ------Prepare to start Routine "CombinedInstruction"-------
t = 0
CombinedInstructionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
CombinedAccept = event.BuilderKeyResponse()
# keep track of which components have finished
CombinedInstructionComponents = [CombinedInstr, CombinedAccept]
for thisComponent in CombinedInstructionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "CombinedInstruction"-------
while continueRoutine:
    # get current time
    t = CombinedInstructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *CombinedInstr* updates
    if t >= 0.0 and CombinedInstr.status == NOT_STARTED:
        # keep track of start time/frame for later
        CombinedInstr.tStart = t
        CombinedInstr.frameNStart = frameN  # exact frame index
        CombinedInstr.setAutoDraw(True)
    
    # *CombinedAccept* updates
    if t >= 0.0 and CombinedAccept.status == NOT_STARTED:
        # keep track of start time/frame for later
        CombinedAccept.tStart = t
        CombinedAccept.frameNStart = frameN  # exact frame index
        CombinedAccept.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(CombinedAccept.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if CombinedAccept.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            CombinedAccept.keys = theseKeys[-1]  # just the last key pressed
            CombinedAccept.rt = CombinedAccept.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CombinedInstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "CombinedInstruction"-------
for thisComponent in CombinedInstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if CombinedAccept.keys in ['', [], None]:  # No response was made
    CombinedAccept.keys=None
thisExp.addData('CombinedAccept.keys',CombinedAccept.keys)
if CombinedAccept.keys != None:  # we had a response
    thisExp.addData('CombinedAccept.rt', CombinedAccept.rt)
thisExp.nextEntry()
# the Routine "CombinedInstruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc

thisExp.addLoop(combinedTrials)  # add the loop to the experiment
thisCombinedTrial = combinedTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCombinedTrial.rgb)
if thisCombinedTrial != None:
    for paramName in thisCombinedTrial.keys():
        exec(paramName + '= thisCombinedTrial.' + paramName)

for thisCombinedTrial in combinedTrials:
    currentLoop = combinedTrials
    # abbreviate parameter names if possible (e.g. rgb = thisCombinedTrial.rgb)
    if thisCombinedTrial != None:
        for paramName in thisCombinedTrial.keys():
            exec(paramName + '= thisCombinedTrial.' + paramName)
    
    # ------Prepare to start Routine "CombinedTrials"-------
    t = 0
    CombinedTrialsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    currentBump = generate_bump(totalNumberOfDots, scopeOfTheDistribution)
    CombVisualStandard = visual.ElementArrayStim(win=win, name="CombVisualStandard", units="pix", fieldPos = [-2.25,0], fieldSize=[150,150], nElements=totalNumberOfDots, elementTex=None, elementMask="circle", xys=currentBump, sizes=sizeOfDots)
    CombComparisonResponse = event.BuilderKeyResponse()
    # keep track of which components have finished
    CombinedTrialsComponents = [CombinedISI1, CombVisualStandard, CombSoundStandard, AfterStandardISI, CombSoundComparison, CombVisualComparison, CombVisualNoiseElement, CombComparisonResponse, combineaudioFix, combinedFixationCross, CombinedISI2]
    for thisComponent in CombinedTrialsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "CombinedTrials"-------
    while continueRoutine:
        # get current time
        t = CombinedTrialsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *CombVisualStandard* updates
        if t >= 1 and CombVisualStandard.status == NOT_STARTED:
            # keep track of start time/frame for later
            CombVisualStandard.tStart = t
            CombVisualStandard.frameNStart = frameN  # exact frame index
            CombVisualStandard.setAutoDraw(True)
        frameRemains = 1 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if CombVisualStandard.status == STARTED and t >= frameRemains:
            CombVisualStandard.setAutoDraw(False)
            newBump = generate_bump(totalNumberOfDots, scopeOfTheDistribution)
            comparisonBump = extract_noise(newBump, noise)
            numberOfNoiseDots = totalNumberOfDots - len(comparisonBump)
            currentLocation = tools.monitorunittools.deg2pix(location, mon, correctFlat=True)
            CombVisualComparison = visual.ElementArrayStim(win=win, name="CombVisualComparison", 
                units="pix", fieldPos = currentLocation, fieldSize=[150,150], 
                nElements=len(comparisonBump), elementTex=None, elementMask="circle", 
                xys=comparisonBump, sizes=sizeOfDots)
            noiseDotsCoordinates = []
            for x in range(numberOfNoiseDots):
                dot_x = random.uniform(-640, 640)
                dot_y = random.uniform(-400, 400)
                noiseDotsCoordinates.append([dot_x, dot_y])
            # VisualComparison.setImage('/Users/admin/Documents/IT&Cognition/Cognitive Science2/experiment-exam/catimg.png')
            # component updates done
            CombVisualNoiseElement = visual.ElementArrayStim(win=win, name="CombVisualNoiseElement", 
                units="pix", fieldPos = [0,0], fieldSize=[1280,800], 
                nElements=numberOfNoiseDots, elementTex=None, elementMask="circle", 
                xys=noiseDotsCoordinates, sizes=sizeOfDots)
        # start/stop CombSoundStandard
        if t >= 1.0 and CombSoundStandard.status == NOT_STARTED:
            # keep track of start time/frame for later
            CombSoundStandard.tStart = t
            CombSoundStandard.frameNStart = frameN  # exact frame index
            CombSoundStandard.play()  # start the sound (it finishes automatically)
        frameRemains = 1.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if CombSoundStandard.status == STARTED and t >= frameRemains:
            CombSoundStandard.stop()  # stop the sound (if longer than duration)
        # start/stop CombSoundComparison
        if t >= 2.0 and CombSoundComparison.status == NOT_STARTED:
            # keep track of start time/frame for later
            CombSoundComparison.tStart = t
            CombSoundComparison.frameNStart = frameN  # exact frame index
            CombSoundComparison.play()  # start the sound (it finishes automatically)
        frameRemains = 2.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if CombSoundComparison.status == STARTED and t >= frameRemains:
            CombSoundComparison.stop()  # stop the sound (if longer than duration)
        
        # *CombVisualComparison* updates
        if t >= 2.0 and CombVisualComparison.status == NOT_STARTED:
            # keep track of start time/frame for later
            CombVisualComparison.tStart = t
            CombVisualNoiseElement.tStart = t
            CombVisualComparison.frameNStart = frameN  # exact frame index
            CombVisualNoiseElement.frameNStart = frameN
            CombVisualComparison.setAutoDraw(True)
            CombVisualNoiseElement.setAutoDraw(True)
        frameRemains = 2.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if CombVisualComparison.status == STARTED and t >= frameRemains:
            CombVisualComparison.setAutoDraw(False)
            CombVisualNoiseElement.setAutoDraw(False)
        
        # *CombComparisonResponse* updates
        if t >= 2.5 and CombComparisonResponse.status == NOT_STARTED:
            # keep track of start time/frame for later
            CombComparisonResponse.tStart = t
            CombComparisonResponse.frameNStart = frameN  # exact frame index
            CombComparisonResponse.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(CombComparisonResponse.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if CombComparisonResponse.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                CombComparisonResponse.keys = theseKeys[-1]  # just the last key pressed
                CombComparisonResponse.rt = CombComparisonResponse.clock.getTime()
                # was this 'correct'?
                # if (CombComparisonResponse.keys == str('')) or (CombComparisonResponse.keys == ''):
                #     CombComparisonResponse.corr = 1
                # else:
                #     CombComparisonResponse.corr = 0
                # a response ends the routine
                continueRoutine = False
        # start/stop combineaudioFix
        if t >= 0.3 and combineaudioFix.status == NOT_STARTED:
            # keep track of start time/frame for later
            combineaudioFix.tStart = t
            combineaudioFix.frameNStart = frameN  # exact frame index
            combineaudioFix.play()  # start the sound (it finishes automatically)
        
        # *combinedFixationCross* updates
        if t >= 0.3 and combinedFixationCross.status == NOT_STARTED:
            # keep track of start time/frame for later
            combinedFixationCross.tStart = t
            combinedFixationCross.frameNStart = frameN  # exact frame index
            combinedFixationCross.setAutoDraw(True)
        frameRemains = 0.3 + 0.2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if combinedFixationCross.status == STARTED and t >= frameRemains:
            combinedFixationCross.setAutoDraw(False)
        # *CombinedISI1* period
        if t >= 0.0 and CombinedISI1.status == NOT_STARTED:
            # keep track of start time/frame for later
            CombinedISI1.tStart = t
            CombinedISI1.frameNStart = frameN  # exact frame index
            CombinedISI1.start(0.3)
        elif CombinedISI1.status == STARTED:  # one frame should pass before updating params and completing
            CombinedISI1.complete()  # finish the static period
        # *AfterStandardISI* period
        if t >= 1.5 and AfterStandardISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            AfterStandardISI.tStart = t
            AfterStandardISI.frameNStart = frameN  # exact frame index
            AfterStandardISI.start(0.5)
        elif AfterStandardISI.status == STARTED:  # one frame should pass before updating params and completing
            # updating other components during *AfterStandardISI*
            CombSoundComparison.setSound(_thisDir + correspondingAudio, secs=0.5)
            # CombVisualComparison.setPos(location)



            # CombVisualComparison.setImage('/Users/admin/Documents/IT&Cognition/Cognitive Science2/experiment-exam/catimg.png')
            # component updates done
            AfterStandardISI.complete()  # finish the static period
        # *CombinedISI2* period
        if t >= 0.5 and CombinedISI2.status == NOT_STARTED:
            # keep track of start time/frame for later
            CombinedISI2.tStart = t
            CombinedISI2.frameNStart = frameN  # exact frame index
            CombinedISI2.start(0.5)
        elif CombinedISI2.status == STARTED:  # one frame should pass before updating params and completing
            CombinedISI2.complete()  # finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CombinedTrialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "CombinedTrials"-------
    for thisComponent in CombinedTrialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    CombSoundStandard.stop()  # ensure sound has stopped at end of routine
    CombSoundComparison.stop()  # ensure sound has stopped at end of routine
    # check responses
    if CombComparisonResponse.keys in ['', [], None]:  # No response was made
        CombComparisonResponse.keys=None
        # was no response the correct answer?!
        # if str('').lower() == 'none':
        #    CombComparisonResponse.corr = 1  # correct non-response
        # else:
        #    CombComparisonResponse.corr = 0  # failed to respond (incorrectly)
    # store data for combinedTrials (TrialHandler)
    combinedTrials.addData('CombComparisonResponse.keys',CombComparisonResponse.keys)
    # combinedTrials.addData('CombComparisonResponse.corr', CombComparisonResponse.corr)
    if CombComparisonResponse.keys != None:  # we had a response
        combinedTrials.addData('CombComparisonResponse.rt', CombComparisonResponse.rt)
    combineaudioFix.stop()  # ensure sound has stopped at end of routine
    # the Routine "CombinedTrials" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
        
    # completed 15 repeats of 'combinedTrials'


# ------Prepare to start Routine "End"-------
t = 0
EndClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = [EndMessage]
for thisComponent in EndComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "End"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EndMessage* updates
    if t >= 0.0 and EndMessage.status == NOT_STARTED:
        # keep track of start time/frame for later
        EndMessage.tStart = t
        EndMessage.frameNStart = frameN  # exact frame index
        EndMessage.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if EndMessage.status == STARTED and t >= frameRemains:
        EndMessage.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
