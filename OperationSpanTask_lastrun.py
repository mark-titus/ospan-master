#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on October 14, 2021, at 11:15
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'OperationSpanTask'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\mt506\\OneDrive - Canterbury Christ Church University\\Documents\\PsychoPy\\ospan-master\\OperationSpanTask_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='In this task you will have to do two things at the same time.\nOn the one hand, operations with a result will appear on the screen. For example: (2 + 2) x2 = 8\nYou will have to decide if they are correct or incorrect. Press the right arrow on the keyboard if the result is correct and the left arrow if it is incorrect.\nOn the other hand, blue letters will appear briefly in the center of the screen. You will have to memorize them.\nWhen a red question mark appears, press the letters that have appeared on the keyboard in the same order in which they appeared.When you are done, press the space bar.\nAfter the red question mark, a new series begins and you can forget the previous letters.\nBefore we start we will do some examples. Attentive, because the task is becoming increasingly complex, with more operations and more letters to memorize.\n\nPLEASE DO NOT ABANDON THE TEST UNTIL IT IS FINISHED\n\nPress the space bar to start',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "warning"
warningClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='A demo trial will now begin.',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "mem"
memClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Recall"
RecallClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='?',
    font='Arial',
    pos=(0, 0), height=0.25, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "warning1"
warning1Clock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='The next trial will now begin.',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "mem"
memClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Recall"
RecallClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='?',
    font='Arial',
    pos=(0, 0), height=0.25, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "warning1"
warning1Clock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='The next trial will now begin.',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "mem"
memClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Recall"
RecallClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='?',
    font='Arial',
    pos=(0, 0), height=0.25, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "warning1"
warning1Clock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='The next trial will now begin.',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "mem"
memClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Recall"
RecallClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='?',
    font='Arial',
    pos=(0, 0), height=0.25, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "warning1"
warning1Clock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='The next trial will now begin.',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "mem"
memClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Recall"
RecallClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='?',
    font='Arial',
    pos=(0, 0), height=0.25, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "warning1"
warning1Clock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='The next trial will now begin.',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "mem"
memClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Recall"
RecallClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='?',
    font='Arial',
    pos=(0, 0), height=0.25, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()
key_resp_4 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
instructionsComponents = [text_4, key_resp_5]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
demo = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Blocks.xlsx', selection='0:2'),
    seed=None, name='demo')
thisExp.addLoop(demo)  # add the loop to the experiment
thisDemo = demo.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDemo.rgb)
if thisDemo != None:
    for paramName in thisDemo:
        exec('{} = thisDemo[paramName]'.format(paramName))

for thisDemo in demo:
    currentLoop = demo
    # abbreviate parameter names if possible (e.g. rgb = thisDemo.rgb)
    if thisDemo != None:
        for paramName in thisDemo:
            exec('{} = thisDemo[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "warning"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    warningComponents = [text_6]
    for thisComponent in warningComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    warningClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "warning"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = warningClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=warningClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        if text_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_6.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text_6.tStop = t  # not accounting for scr refresh
                text_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
                text_6.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in warningComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "warning"-------
    for thisComponent in warningComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    demo.addData('text_6.started', text_6.tStartRefresh)
    demo.addData('text_6.stopped', text_6.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    trial1 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(SelectBlock, selection='0:2'),
        seed=None, name='trial1')
    thisExp.addLoop(trial1)  # add the loop to the experiment
    thisTrial1 = trial1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial1.rgb)
    if thisTrial1 != None:
        for paramName in thisTrial1:
            exec('{} = thisTrial1[paramName]'.format(paramName))
    
    for thisTrial1 in trial1:
        currentLoop = trial1
        # abbreviate parameter names if possible (e.g. rgb = thisTrial1.rgb)
        if thisTrial1 != None:
            for paramName in thisTrial1:
                exec('{} = thisTrial1[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        text.setText(Stimulus)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        # keep track of which components have finished
        trialComponents = [text, key_resp_2]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            
            # *key_resp_2* updates
            waitOnFlip = False
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['left', 'right'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    # was this correct?
                    if (key_resp_2.keys == str(Answer)) or (key_resp_2.keys == Answer):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trial1.addData('text.started', text.tStartRefresh)
        trial1.addData('text.stopped', text.tStopRefresh)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
            # was no response the correct answer?!
            if str(Answer).lower() == 'none':
               key_resp_2.corr = 1;  # correct non-response
            else:
               key_resp_2.corr = 0;  # failed to respond (incorrectly)
        # store data for trial1 (TrialHandler)
        trial1.addData('key_resp_2.keys',key_resp_2.keys)
        trial1.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            trial1.addData('key_resp_2.rt', key_resp_2.rt)
        trial1.addData('key_resp_2.started', key_resp_2.tStartRefresh)
        trial1.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "mem"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        text_2.setText(Letter)
        # keep track of which components have finished
        memComponents = [text_2]
        for thisComponent in memComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        memClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "mem"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = memClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=memClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                text_2.setAutoDraw(True)
            if text_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_2.tStop = t  # not accounting for scr refresh
                    text_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                    text_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in memComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "mem"-------
        for thisComponent in memComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trial1.addData('text_2.started', text_2.tStartRefresh)
        trial1.addData('text_2.stopped', text_2.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trial1'
    
    
    # ------Prepare to start Routine "Recall"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    RecallComponents = [text_3, key_resp_3, key_resp_4]
    for thisComponent in RecallComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RecallClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Recall"-------
    while continueRoutine:
        # get current time
        t = RecallClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RecallClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['q', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = [key.name for key in _key_resp_3_allKeys]  # storing all keys
                key_resp_3.rt = [key.rt for key in _key_resp_3_allKeys]
                # was this correct?
                if (key_resp_3.keys == str(CorAns)) or (key_resp_3.keys == CorAns):
                    key_resp_3.corr = 1
                else:
                    key_resp_3.corr = 0
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RecallComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Recall"-------
    for thisComponent in RecallComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    demo.addData('text_3.started', text_3.tStartRefresh)
    demo.addData('text_3.stopped', text_3.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
        # was no response the correct answer?!
        if str(CorAns).lower() == 'none':
           key_resp_3.corr = 1;  # correct non-response
        else:
           key_resp_3.corr = 0;  # failed to respond (incorrectly)
    # store data for demo (TrialHandler)
    demo.addData('key_resp_3.keys',key_resp_3.keys)
    demo.addData('key_resp_3.corr', key_resp_3.corr)
    if key_resp_3.keys != None:  # we had a response
        demo.addData('key_resp_3.rt', key_resp_3.rt)
    demo.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    demo.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    demo.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        demo.addData('key_resp_4.rt', key_resp_4.rt)
    demo.addData('key_resp_4.started', key_resp_4.tStartRefresh)
    demo.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
    # the Routine "Recall" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'demo'


# set up handler to look after randomisation of conditions etc
span2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Blocks.xlsx', selection='0:3'),
    seed=None, name='span2')
thisExp.addLoop(span2)  # add the loop to the experiment
thisSpan2 = span2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSpan2.rgb)
if thisSpan2 != None:
    for paramName in thisSpan2:
        exec('{} = thisSpan2[paramName]'.format(paramName))

for thisSpan2 in span2:
    currentLoop = span2
    # abbreviate parameter names if possible (e.g. rgb = thisSpan2.rgb)
    if thisSpan2 != None:
        for paramName in thisSpan2:
            exec('{} = thisSpan2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "warning1"-------
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    warning1Components = [text_5]
    for thisComponent in warning1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    warning1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "warning1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = warning1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=warning1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                text_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in warning1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "warning1"-------
    for thisComponent in warning1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    span2.addData('text_5.started', text_5.tStartRefresh)
    span2.addData('text_5.stopped', text_5.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    trial2 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(SelectBlock, selection='2:4'),
        seed=None, name='trial2')
    thisExp.addLoop(trial2)  # add the loop to the experiment
    thisTrial2 = trial2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial2.rgb)
    if thisTrial2 != None:
        for paramName in thisTrial2:
            exec('{} = thisTrial2[paramName]'.format(paramName))
    
    for thisTrial2 in trial2:
        currentLoop = trial2
        # abbreviate parameter names if possible (e.g. rgb = thisTrial2.rgb)
        if thisTrial2 != None:
            for paramName in thisTrial2:
                exec('{} = thisTrial2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        text.setText(Stimulus)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        # keep track of which components have finished
        trialComponents = [text, key_resp_2]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            
            # *key_resp_2* updates
            waitOnFlip = False
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['left', 'right'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    # was this correct?
                    if (key_resp_2.keys == str(Answer)) or (key_resp_2.keys == Answer):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trial2.addData('text.started', text.tStartRefresh)
        trial2.addData('text.stopped', text.tStopRefresh)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
            # was no response the correct answer?!
            if str(Answer).lower() == 'none':
               key_resp_2.corr = 1;  # correct non-response
            else:
               key_resp_2.corr = 0;  # failed to respond (incorrectly)
        # store data for trial2 (TrialHandler)
        trial2.addData('key_resp_2.keys',key_resp_2.keys)
        trial2.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            trial2.addData('key_resp_2.rt', key_resp_2.rt)
        trial2.addData('key_resp_2.started', key_resp_2.tStartRefresh)
        trial2.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "mem"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        text_2.setText(Letter)
        # keep track of which components have finished
        memComponents = [text_2]
        for thisComponent in memComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        memClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "mem"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = memClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=memClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                text_2.setAutoDraw(True)
            if text_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_2.tStop = t  # not accounting for scr refresh
                    text_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                    text_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in memComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "mem"-------
        for thisComponent in memComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trial2.addData('text_2.started', text_2.tStartRefresh)
        trial2.addData('text_2.stopped', text_2.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trial2'
    
    
    # ------Prepare to start Routine "Recall"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    RecallComponents = [text_3, key_resp_3, key_resp_4]
    for thisComponent in RecallComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RecallClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Recall"-------
    while continueRoutine:
        # get current time
        t = RecallClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RecallClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['q', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = [key.name for key in _key_resp_3_allKeys]  # storing all keys
                key_resp_3.rt = [key.rt for key in _key_resp_3_allKeys]
                # was this correct?
                if (key_resp_3.keys == str(CorAns)) or (key_resp_3.keys == CorAns):
                    key_resp_3.corr = 1
                else:
                    key_resp_3.corr = 0
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RecallComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Recall"-------
    for thisComponent in RecallComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    span2.addData('text_3.started', text_3.tStartRefresh)
    span2.addData('text_3.stopped', text_3.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
        # was no response the correct answer?!
        if str(CorAns).lower() == 'none':
           key_resp_3.corr = 1;  # correct non-response
        else:
           key_resp_3.corr = 0;  # failed to respond (incorrectly)
    # store data for span2 (TrialHandler)
    span2.addData('key_resp_3.keys',key_resp_3.keys)
    span2.addData('key_resp_3.corr', key_resp_3.corr)
    if key_resp_3.keys != None:  # we had a response
        span2.addData('key_resp_3.rt', key_resp_3.rt)
    span2.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    span2.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    span2.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        span2.addData('key_resp_4.rt', key_resp_4.rt)
    span2.addData('key_resp_4.started', key_resp_4.tStartRefresh)
    span2.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
    # the Routine "Recall" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'span2'


# set up handler to look after randomisation of conditions etc
span3 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Blocks.xlsx', selection='0:3'),
    seed=None, name='span3')
thisExp.addLoop(span3)  # add the loop to the experiment
thisSpan3 = span3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSpan3.rgb)
if thisSpan3 != None:
    for paramName in thisSpan3:
        exec('{} = thisSpan3[paramName]'.format(paramName))

for thisSpan3 in span3:
    currentLoop = span3
    # abbreviate parameter names if possible (e.g. rgb = thisSpan3.rgb)
    if thisSpan3 != None:
        for paramName in thisSpan3:
            exec('{} = thisSpan3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "warning1"-------
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    warning1Components = [text_5]
    for thisComponent in warning1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    warning1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "warning1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = warning1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=warning1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                text_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in warning1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "warning1"-------
    for thisComponent in warning1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    span3.addData('text_5.started', text_5.tStartRefresh)
    span3.addData('text_5.stopped', text_5.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    trial3 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(SelectBlock, selection='4:7'),
        seed=None, name='trial3')
    thisExp.addLoop(trial3)  # add the loop to the experiment
    thisTrial3 = trial3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial3.rgb)
    if thisTrial3 != None:
        for paramName in thisTrial3:
            exec('{} = thisTrial3[paramName]'.format(paramName))
    
    for thisTrial3 in trial3:
        currentLoop = trial3
        # abbreviate parameter names if possible (e.g. rgb = thisTrial3.rgb)
        if thisTrial3 != None:
            for paramName in thisTrial3:
                exec('{} = thisTrial3[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        text.setText(Stimulus)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        # keep track of which components have finished
        trialComponents = [text, key_resp_2]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            
            # *key_resp_2* updates
            waitOnFlip = False
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['left', 'right'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    # was this correct?
                    if (key_resp_2.keys == str(Answer)) or (key_resp_2.keys == Answer):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trial3.addData('text.started', text.tStartRefresh)
        trial3.addData('text.stopped', text.tStopRefresh)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
            # was no response the correct answer?!
            if str(Answer).lower() == 'none':
               key_resp_2.corr = 1;  # correct non-response
            else:
               key_resp_2.corr = 0;  # failed to respond (incorrectly)
        # store data for trial3 (TrialHandler)
        trial3.addData('key_resp_2.keys',key_resp_2.keys)
        trial3.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            trial3.addData('key_resp_2.rt', key_resp_2.rt)
        trial3.addData('key_resp_2.started', key_resp_2.tStartRefresh)
        trial3.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "mem"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        text_2.setText(Letter)
        # keep track of which components have finished
        memComponents = [text_2]
        for thisComponent in memComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        memClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "mem"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = memClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=memClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                text_2.setAutoDraw(True)
            if text_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_2.tStop = t  # not accounting for scr refresh
                    text_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                    text_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in memComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "mem"-------
        for thisComponent in memComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trial3.addData('text_2.started', text_2.tStartRefresh)
        trial3.addData('text_2.stopped', text_2.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trial3'
    
    
    # ------Prepare to start Routine "Recall"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    RecallComponents = [text_3, key_resp_3, key_resp_4]
    for thisComponent in RecallComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RecallClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Recall"-------
    while continueRoutine:
        # get current time
        t = RecallClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RecallClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['q', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = [key.name for key in _key_resp_3_allKeys]  # storing all keys
                key_resp_3.rt = [key.rt for key in _key_resp_3_allKeys]
                # was this correct?
                if (key_resp_3.keys == str(CorAns)) or (key_resp_3.keys == CorAns):
                    key_resp_3.corr = 1
                else:
                    key_resp_3.corr = 0
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RecallComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Recall"-------
    for thisComponent in RecallComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    span3.addData('text_3.started', text_3.tStartRefresh)
    span3.addData('text_3.stopped', text_3.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
        # was no response the correct answer?!
        if str(CorAns).lower() == 'none':
           key_resp_3.corr = 1;  # correct non-response
        else:
           key_resp_3.corr = 0;  # failed to respond (incorrectly)
    # store data for span3 (TrialHandler)
    span3.addData('key_resp_3.keys',key_resp_3.keys)
    span3.addData('key_resp_3.corr', key_resp_3.corr)
    if key_resp_3.keys != None:  # we had a response
        span3.addData('key_resp_3.rt', key_resp_3.rt)
    span3.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    span3.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    span3.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        span3.addData('key_resp_4.rt', key_resp_4.rt)
    span3.addData('key_resp_4.started', key_resp_4.tStartRefresh)
    span3.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
    # the Routine "Recall" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'span3'


# set up handler to look after randomisation of conditions etc
span4 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Blocks.xlsx', selection='0:3'),
    seed=None, name='span4')
thisExp.addLoop(span4)  # add the loop to the experiment
thisSpan4 = span4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSpan4.rgb)
if thisSpan4 != None:
    for paramName in thisSpan4:
        exec('{} = thisSpan4[paramName]'.format(paramName))

for thisSpan4 in span4:
    currentLoop = span4
    # abbreviate parameter names if possible (e.g. rgb = thisSpan4.rgb)
    if thisSpan4 != None:
        for paramName in thisSpan4:
            exec('{} = thisSpan4[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "warning1"-------
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    warning1Components = [text_5]
    for thisComponent in warning1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    warning1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "warning1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = warning1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=warning1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                text_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in warning1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "warning1"-------
    for thisComponent in warning1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    span4.addData('text_5.started', text_5.tStartRefresh)
    span4.addData('text_5.stopped', text_5.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    trial4 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(SelectBlock, selection='7:11'),
        seed=None, name='trial4')
    thisExp.addLoop(trial4)  # add the loop to the experiment
    thisTrial4 = trial4.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial4.rgb)
    if thisTrial4 != None:
        for paramName in thisTrial4:
            exec('{} = thisTrial4[paramName]'.format(paramName))
    
    for thisTrial4 in trial4:
        currentLoop = trial4
        # abbreviate parameter names if possible (e.g. rgb = thisTrial4.rgb)
        if thisTrial4 != None:
            for paramName in thisTrial4:
                exec('{} = thisTrial4[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        text.setText(Stimulus)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        # keep track of which components have finished
        trialComponents = [text, key_resp_2]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            
            # *key_resp_2* updates
            waitOnFlip = False
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['left', 'right'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    # was this correct?
                    if (key_resp_2.keys == str(Answer)) or (key_resp_2.keys == Answer):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trial4.addData('text.started', text.tStartRefresh)
        trial4.addData('text.stopped', text.tStopRefresh)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
            # was no response the correct answer?!
            if str(Answer).lower() == 'none':
               key_resp_2.corr = 1;  # correct non-response
            else:
               key_resp_2.corr = 0;  # failed to respond (incorrectly)
        # store data for trial4 (TrialHandler)
        trial4.addData('key_resp_2.keys',key_resp_2.keys)
        trial4.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            trial4.addData('key_resp_2.rt', key_resp_2.rt)
        trial4.addData('key_resp_2.started', key_resp_2.tStartRefresh)
        trial4.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "mem"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        text_2.setText(Letter)
        # keep track of which components have finished
        memComponents = [text_2]
        for thisComponent in memComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        memClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "mem"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = memClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=memClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                text_2.setAutoDraw(True)
            if text_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_2.tStop = t  # not accounting for scr refresh
                    text_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                    text_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in memComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "mem"-------
        for thisComponent in memComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trial4.addData('text_2.started', text_2.tStartRefresh)
        trial4.addData('text_2.stopped', text_2.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trial4'
    
    
    # ------Prepare to start Routine "Recall"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    RecallComponents = [text_3, key_resp_3, key_resp_4]
    for thisComponent in RecallComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RecallClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Recall"-------
    while continueRoutine:
        # get current time
        t = RecallClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RecallClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['q', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = [key.name for key in _key_resp_3_allKeys]  # storing all keys
                key_resp_3.rt = [key.rt for key in _key_resp_3_allKeys]
                # was this correct?
                if (key_resp_3.keys == str(CorAns)) or (key_resp_3.keys == CorAns):
                    key_resp_3.corr = 1
                else:
                    key_resp_3.corr = 0
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RecallComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Recall"-------
    for thisComponent in RecallComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    span4.addData('text_3.started', text_3.tStartRefresh)
    span4.addData('text_3.stopped', text_3.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
        # was no response the correct answer?!
        if str(CorAns).lower() == 'none':
           key_resp_3.corr = 1;  # correct non-response
        else:
           key_resp_3.corr = 0;  # failed to respond (incorrectly)
    # store data for span4 (TrialHandler)
    span4.addData('key_resp_3.keys',key_resp_3.keys)
    span4.addData('key_resp_3.corr', key_resp_3.corr)
    if key_resp_3.keys != None:  # we had a response
        span4.addData('key_resp_3.rt', key_resp_3.rt)
    span4.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    span4.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    span4.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        span4.addData('key_resp_4.rt', key_resp_4.rt)
    span4.addData('key_resp_4.started', key_resp_4.tStartRefresh)
    span4.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
    # the Routine "Recall" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'span4'


# set up handler to look after randomisation of conditions etc
span5 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Blocks.xlsx', selection='0:3'),
    seed=None, name='span5')
thisExp.addLoop(span5)  # add the loop to the experiment
thisSpan5 = span5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSpan5.rgb)
if thisSpan5 != None:
    for paramName in thisSpan5:
        exec('{} = thisSpan5[paramName]'.format(paramName))

for thisSpan5 in span5:
    currentLoop = span5
    # abbreviate parameter names if possible (e.g. rgb = thisSpan5.rgb)
    if thisSpan5 != None:
        for paramName in thisSpan5:
            exec('{} = thisSpan5[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "warning1"-------
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    warning1Components = [text_5]
    for thisComponent in warning1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    warning1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "warning1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = warning1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=warning1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                text_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in warning1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "warning1"-------
    for thisComponent in warning1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    span5.addData('text_5.started', text_5.tStartRefresh)
    span5.addData('text_5.stopped', text_5.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    trial5 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(SelectBlock, selection='11:16'),
        seed=None, name='trial5')
    thisExp.addLoop(trial5)  # add the loop to the experiment
    thisTrial5 = trial5.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial5.rgb)
    if thisTrial5 != None:
        for paramName in thisTrial5:
            exec('{} = thisTrial5[paramName]'.format(paramName))
    
    for thisTrial5 in trial5:
        currentLoop = trial5
        # abbreviate parameter names if possible (e.g. rgb = thisTrial5.rgb)
        if thisTrial5 != None:
            for paramName in thisTrial5:
                exec('{} = thisTrial5[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        text.setText(Stimulus)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        # keep track of which components have finished
        trialComponents = [text, key_resp_2]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            
            # *key_resp_2* updates
            waitOnFlip = False
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['left', 'right'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    # was this correct?
                    if (key_resp_2.keys == str(Answer)) or (key_resp_2.keys == Answer):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trial5.addData('text.started', text.tStartRefresh)
        trial5.addData('text.stopped', text.tStopRefresh)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
            # was no response the correct answer?!
            if str(Answer).lower() == 'none':
               key_resp_2.corr = 1;  # correct non-response
            else:
               key_resp_2.corr = 0;  # failed to respond (incorrectly)
        # store data for trial5 (TrialHandler)
        trial5.addData('key_resp_2.keys',key_resp_2.keys)
        trial5.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            trial5.addData('key_resp_2.rt', key_resp_2.rt)
        trial5.addData('key_resp_2.started', key_resp_2.tStartRefresh)
        trial5.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "mem"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        text_2.setText(Letter)
        # keep track of which components have finished
        memComponents = [text_2]
        for thisComponent in memComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        memClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "mem"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = memClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=memClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                text_2.setAutoDraw(True)
            if text_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_2.tStop = t  # not accounting for scr refresh
                    text_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                    text_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in memComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "mem"-------
        for thisComponent in memComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trial5.addData('text_2.started', text_2.tStartRefresh)
        trial5.addData('text_2.stopped', text_2.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trial5'
    
    
    # ------Prepare to start Routine "Recall"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    RecallComponents = [text_3, key_resp_3, key_resp_4]
    for thisComponent in RecallComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RecallClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Recall"-------
    while continueRoutine:
        # get current time
        t = RecallClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RecallClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['q', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = [key.name for key in _key_resp_3_allKeys]  # storing all keys
                key_resp_3.rt = [key.rt for key in _key_resp_3_allKeys]
                # was this correct?
                if (key_resp_3.keys == str(CorAns)) or (key_resp_3.keys == CorAns):
                    key_resp_3.corr = 1
                else:
                    key_resp_3.corr = 0
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RecallComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Recall"-------
    for thisComponent in RecallComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    span5.addData('text_3.started', text_3.tStartRefresh)
    span5.addData('text_3.stopped', text_3.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
        # was no response the correct answer?!
        if str(CorAns).lower() == 'none':
           key_resp_3.corr = 1;  # correct non-response
        else:
           key_resp_3.corr = 0;  # failed to respond (incorrectly)
    # store data for span5 (TrialHandler)
    span5.addData('key_resp_3.keys',key_resp_3.keys)
    span5.addData('key_resp_3.corr', key_resp_3.corr)
    if key_resp_3.keys != None:  # we had a response
        span5.addData('key_resp_3.rt', key_resp_3.rt)
    span5.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    span5.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    span5.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        span5.addData('key_resp_4.rt', key_resp_4.rt)
    span5.addData('key_resp_4.started', key_resp_4.tStartRefresh)
    span5.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
    # the Routine "Recall" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'span5'


# set up handler to look after randomisation of conditions etc
span6 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Blocks.xlsx', selection='0:3'),
    seed=None, name='span6')
thisExp.addLoop(span6)  # add the loop to the experiment
thisSpan6 = span6.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSpan6.rgb)
if thisSpan6 != None:
    for paramName in thisSpan6:
        exec('{} = thisSpan6[paramName]'.format(paramName))

for thisSpan6 in span6:
    currentLoop = span6
    # abbreviate parameter names if possible (e.g. rgb = thisSpan6.rgb)
    if thisSpan6 != None:
        for paramName in thisSpan6:
            exec('{} = thisSpan6[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "warning1"-------
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    warning1Components = [text_5]
    for thisComponent in warning1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    warning1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "warning1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = warning1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=warning1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                text_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in warning1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "warning1"-------
    for thisComponent in warning1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    span6.addData('text_5.started', text_5.tStartRefresh)
    span6.addData('text_5.stopped', text_5.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    trial6 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(SelectBlock, selection='16:22'),
        seed=None, name='trial6')
    thisExp.addLoop(trial6)  # add the loop to the experiment
    thisTrial6 = trial6.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial6.rgb)
    if thisTrial6 != None:
        for paramName in thisTrial6:
            exec('{} = thisTrial6[paramName]'.format(paramName))
    
    for thisTrial6 in trial6:
        currentLoop = trial6
        # abbreviate parameter names if possible (e.g. rgb = thisTrial6.rgb)
        if thisTrial6 != None:
            for paramName in thisTrial6:
                exec('{} = thisTrial6[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        text.setText(Stimulus)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        # keep track of which components have finished
        trialComponents = [text, key_resp_2]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            
            # *key_resp_2* updates
            waitOnFlip = False
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['left', 'right'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    # was this correct?
                    if (key_resp_2.keys == str(Answer)) or (key_resp_2.keys == Answer):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trial6.addData('text.started', text.tStartRefresh)
        trial6.addData('text.stopped', text.tStopRefresh)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
            # was no response the correct answer?!
            if str(Answer).lower() == 'none':
               key_resp_2.corr = 1;  # correct non-response
            else:
               key_resp_2.corr = 0;  # failed to respond (incorrectly)
        # store data for trial6 (TrialHandler)
        trial6.addData('key_resp_2.keys',key_resp_2.keys)
        trial6.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            trial6.addData('key_resp_2.rt', key_resp_2.rt)
        trial6.addData('key_resp_2.started', key_resp_2.tStartRefresh)
        trial6.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "mem"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        text_2.setText(Letter)
        # keep track of which components have finished
        memComponents = [text_2]
        for thisComponent in memComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        memClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "mem"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = memClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=memClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                text_2.setAutoDraw(True)
            if text_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_2.tStop = t  # not accounting for scr refresh
                    text_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                    text_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in memComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "mem"-------
        for thisComponent in memComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trial6.addData('text_2.started', text_2.tStartRefresh)
        trial6.addData('text_2.stopped', text_2.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trial6'
    
    
    # ------Prepare to start Routine "Recall"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    RecallComponents = [text_3, key_resp_3, key_resp_4]
    for thisComponent in RecallComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RecallClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Recall"-------
    while continueRoutine:
        # get current time
        t = RecallClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RecallClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['q', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = [key.name for key in _key_resp_3_allKeys]  # storing all keys
                key_resp_3.rt = [key.rt for key in _key_resp_3_allKeys]
                # was this correct?
                if (key_resp_3.keys == str(CorAns)) or (key_resp_3.keys == CorAns):
                    key_resp_3.corr = 1
                else:
                    key_resp_3.corr = 0
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RecallComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Recall"-------
    for thisComponent in RecallComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    span6.addData('text_3.started', text_3.tStartRefresh)
    span6.addData('text_3.stopped', text_3.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
        # was no response the correct answer?!
        if str(CorAns).lower() == 'none':
           key_resp_3.corr = 1;  # correct non-response
        else:
           key_resp_3.corr = 0;  # failed to respond (incorrectly)
    # store data for span6 (TrialHandler)
    span6.addData('key_resp_3.keys',key_resp_3.keys)
    span6.addData('key_resp_3.corr', key_resp_3.corr)
    if key_resp_3.keys != None:  # we had a response
        span6.addData('key_resp_3.rt', key_resp_3.rt)
    span6.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    span6.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    span6.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        span6.addData('key_resp_4.rt', key_resp_4.rt)
    span6.addData('key_resp_4.started', key_resp_4.tStartRefresh)
    span6.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
    # the Routine "Recall" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'span6'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
