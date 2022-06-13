/************************** 
 * Operationspantask Test *
 **************************/

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'OperationSpanTask';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// Start code blocks for 'Before Experiment'
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(instruccionesRoutineBegin());
flowScheduler.add(instruccionesRoutineEachFrame());
flowScheduler.add(instruccionesRoutineEnd());
const ensayosLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(ensayosLoopBegin, ensayosLoopScheduler);
flowScheduler.add(ensayosLoopScheduler);
flowScheduler.add(ensayosLoopEnd);
const span2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(span2LoopBegin, span2LoopScheduler);
flowScheduler.add(span2LoopScheduler);
flowScheduler.add(span2LoopEnd);
const span3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(span3LoopBegin, span3LoopScheduler);
flowScheduler.add(span3LoopScheduler);
flowScheduler.add(span3LoopEnd);
const span4LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(span4LoopBegin, span4LoopScheduler);
flowScheduler.add(span4LoopScheduler);
flowScheduler.add(span4LoopEnd);
const span5LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(span5LoopBegin, span5LoopScheduler);
flowScheduler.add(span5LoopScheduler);
flowScheduler.add(span5LoopEnd);
const span6LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(span6LoopBegin, span6LoopScheduler);
flowScheduler.add(span6LoopScheduler);
flowScheduler.add(span6LoopEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.1.2';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var instruccionesClock;
var text_4;
var key_resp_5;
var warningeClock;
var text_6;
var trialClock;
var text;
var key_resp_2;
var memClock;
var text_2;
var RecallClock;
var text_3;
var key_resp_3;
var key_resp_4;
var warning1Clock;
var text_5;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "instrucciones"
  instruccionesClock = new util.Clock();
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'En esta tarea deberás hacer dos cosas a la vez.\nPor un lado, aparecerán operaciones con un resultado en la pantalla. Por ejemplo: (2+2)x2=8\nDeberás decidir si son correctas o incorrectas. Pulsa la flecha derecha del teclado si el resultado es correcto y la flecha izquierda si es incorrecto.\nPor otro lado, aparecerán brevemente letras azules en el centro de la pantalla. Deberás memorizarlas.\nCuando aparezca un signo de interrogación rojo deberás pulsar en el teclado las letras que han aparecido en el mismo orden en el que han aparecido.Cuando hayas terminado, pulsa la barra espaciadora.\nTras el signo de interrogación rojo, comienza una nueva serie y puedes olvidar las letras anteriores.\nAntes de empezar haremos algunos ejemplos. Atento, porque la tarea se va haciendo cada vez más compleja, con más operaciones y más letras para memorizar.\nPulsa la barra espaciadora para comenzar',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.07,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "warninge"
  warningeClock = new util.Clock();
  text_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_6',
    text: 'Comienza una serie de ensayo',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "mem"
  memClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.3,  wrapWidth: undefined, ori: 0,
    color: new util.Color('blue'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Recall"
  RecallClock = new util.Clock();
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: '?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.25,  wrapWidth: undefined, ori: 0,
    color: new util.Color('red'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "warning1"
  warning1Clock = new util.Clock();
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: '¡Atención!\nComienza una nueva serie',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "mem"
  memClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.3,  wrapWidth: undefined, ori: 0,
    color: new util.Color('blue'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Recall"
  RecallClock = new util.Clock();
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: '?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.25,  wrapWidth: undefined, ori: 0,
    color: new util.Color('red'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "warning1"
  warning1Clock = new util.Clock();
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: '¡Atención!\nComienza una nueva serie',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "mem"
  memClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.3,  wrapWidth: undefined, ori: 0,
    color: new util.Color('blue'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Recall"
  RecallClock = new util.Clock();
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: '?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.25,  wrapWidth: undefined, ori: 0,
    color: new util.Color('red'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "warning1"
  warning1Clock = new util.Clock();
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: '¡Atención!\nComienza una nueva serie',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "mem"
  memClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.3,  wrapWidth: undefined, ori: 0,
    color: new util.Color('blue'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Recall"
  RecallClock = new util.Clock();
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: '?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.25,  wrapWidth: undefined, ori: 0,
    color: new util.Color('red'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "warning1"
  warning1Clock = new util.Clock();
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: '¡Atención!\nComienza una nueva serie',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "mem"
  memClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.3,  wrapWidth: undefined, ori: 0,
    color: new util.Color('blue'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Recall"
  RecallClock = new util.Clock();
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: '?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.25,  wrapWidth: undefined, ori: 0,
    color: new util.Color('red'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "warning1"
  warning1Clock = new util.Clock();
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: '¡Atención!\nComienza una nueva serie',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "mem"
  memClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.3,  wrapWidth: undefined, ori: 0,
    color: new util.Color('blue'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Recall"
  RecallClock = new util.Clock();
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: '?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.25,  wrapWidth: undefined, ori: 0,
    color: new util.Color('red'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _key_resp_5_allKeys;
var instruccionesComponents;
function instruccionesRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instrucciones'-------
    t = 0;
    instruccionesClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    // keep track of which components have finished
    instruccionesComponents = [];
    instruccionesComponents.push(text_4);
    instruccionesComponents.push(key_resp_5);
    
    instruccionesComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instruccionesRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instrucciones'-------
    // get current time
    t = instruccionesClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_4* updates
    if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }

    
    // *key_resp_5* updates
    if (t >= 1.0 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.clearEvents(); });
    }

    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].name;  // just the last key pressed
        key_resp_5.rt = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instruccionesComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instruccionesRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instrucciones'-------
    instruccionesComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "instrucciones" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var ensayos;
var currentLoop;
function ensayosLoopBegin(ensayosLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  ensayos = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'Bloques.xlsx', '0:2'),
    seed: undefined, name: 'ensayos'
  });
  psychoJS.experiment.addLoop(ensayos); // add the loop to the experiment
  currentLoop = ensayos;  // we're now the current loop

  // Schedule all the trials in the trialList:
  ensayos.forEach(function() {
    const snapshot = ensayos.getSnapshot();

    ensayosLoopScheduler.add(importConditions(snapshot));
    ensayosLoopScheduler.add(warningeRoutineBegin(snapshot));
    ensayosLoopScheduler.add(warningeRoutineEachFrame(snapshot));
    ensayosLoopScheduler.add(warningeRoutineEnd(snapshot));
    const ensayosejemLoopScheduler = new Scheduler(psychoJS);
    ensayosLoopScheduler.add(ensayosejemLoopBegin, ensayosejemLoopScheduler);
    ensayosLoopScheduler.add(ensayosejemLoopScheduler);
    ensayosLoopScheduler.add(ensayosejemLoopEnd);
    ensayosLoopScheduler.add(RecallRoutineBegin(snapshot));
    ensayosLoopScheduler.add(RecallRoutineEachFrame(snapshot));
    ensayosLoopScheduler.add(RecallRoutineEnd(snapshot));
    ensayosLoopScheduler.add(endLoopIteration(ensayosLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var ensayosejem;
function ensayosejemLoopBegin(ensayosejemLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  ensayosejem = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, Eligebloque, '0:2'),
    seed: undefined, name: 'ensayosejem'
  });
  psychoJS.experiment.addLoop(ensayosejem); // add the loop to the experiment
  currentLoop = ensayosejem;  // we're now the current loop

  // Schedule all the trials in the trialList:
  ensayosejem.forEach(function() {
    const snapshot = ensayosejem.getSnapshot();

    ensayosejemLoopScheduler.add(importConditions(snapshot));
    ensayosejemLoopScheduler.add(trialRoutineBegin(snapshot));
    ensayosejemLoopScheduler.add(trialRoutineEachFrame(snapshot));
    ensayosejemLoopScheduler.add(trialRoutineEnd(snapshot));
    ensayosejemLoopScheduler.add(memRoutineBegin(snapshot));
    ensayosejemLoopScheduler.add(memRoutineEachFrame(snapshot));
    ensayosejemLoopScheduler.add(memRoutineEnd(snapshot));
    ensayosejemLoopScheduler.add(endLoopIteration(ensayosejemLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function ensayosejemLoopEnd() {
  psychoJS.experiment.removeLoop(ensayosejem);

  return Scheduler.Event.NEXT;
}


function ensayosLoopEnd() {
  psychoJS.experiment.removeLoop(ensayos);

  return Scheduler.Event.NEXT;
}


var span2;
function span2LoopBegin(span2LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  span2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'Bloques.xlsx', '0:3'),
    seed: undefined, name: 'span2'
  });
  psychoJS.experiment.addLoop(span2); // add the loop to the experiment
  currentLoop = span2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  span2.forEach(function() {
    const snapshot = span2.getSnapshot();

    span2LoopScheduler.add(importConditions(snapshot));
    span2LoopScheduler.add(warning1RoutineBegin(snapshot));
    span2LoopScheduler.add(warning1RoutineEachFrame(snapshot));
    span2LoopScheduler.add(warning1RoutineEnd(snapshot));
    const ensayos2LoopScheduler = new Scheduler(psychoJS);
    span2LoopScheduler.add(ensayos2LoopBegin, ensayos2LoopScheduler);
    span2LoopScheduler.add(ensayos2LoopScheduler);
    span2LoopScheduler.add(ensayos2LoopEnd);
    span2LoopScheduler.add(RecallRoutineBegin(snapshot));
    span2LoopScheduler.add(RecallRoutineEachFrame(snapshot));
    span2LoopScheduler.add(RecallRoutineEnd(snapshot));
    span2LoopScheduler.add(endLoopIteration(span2LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var ensayos2;
function ensayos2LoopBegin(ensayos2LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  ensayos2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, Eligebloque, '2:4'),
    seed: undefined, name: 'ensayos2'
  });
  psychoJS.experiment.addLoop(ensayos2); // add the loop to the experiment
  currentLoop = ensayos2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  ensayos2.forEach(function() {
    const snapshot = ensayos2.getSnapshot();

    ensayos2LoopScheduler.add(importConditions(snapshot));
    ensayos2LoopScheduler.add(trialRoutineBegin(snapshot));
    ensayos2LoopScheduler.add(trialRoutineEachFrame(snapshot));
    ensayos2LoopScheduler.add(trialRoutineEnd(snapshot));
    ensayos2LoopScheduler.add(memRoutineBegin(snapshot));
    ensayos2LoopScheduler.add(memRoutineEachFrame(snapshot));
    ensayos2LoopScheduler.add(memRoutineEnd(snapshot));
    ensayos2LoopScheduler.add(endLoopIteration(ensayos2LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function ensayos2LoopEnd() {
  psychoJS.experiment.removeLoop(ensayos2);

  return Scheduler.Event.NEXT;
}


function span2LoopEnd() {
  psychoJS.experiment.removeLoop(span2);

  return Scheduler.Event.NEXT;
}


var span3;
function span3LoopBegin(span3LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  span3 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'Bloques.xlsx', '0:3'),
    seed: undefined, name: 'span3'
  });
  psychoJS.experiment.addLoop(span3); // add the loop to the experiment
  currentLoop = span3;  // we're now the current loop

  // Schedule all the trials in the trialList:
  span3.forEach(function() {
    const snapshot = span3.getSnapshot();

    span3LoopScheduler.add(importConditions(snapshot));
    span3LoopScheduler.add(warning1RoutineBegin(snapshot));
    span3LoopScheduler.add(warning1RoutineEachFrame(snapshot));
    span3LoopScheduler.add(warning1RoutineEnd(snapshot));
    const ensayos3LoopScheduler = new Scheduler(psychoJS);
    span3LoopScheduler.add(ensayos3LoopBegin, ensayos3LoopScheduler);
    span3LoopScheduler.add(ensayos3LoopScheduler);
    span3LoopScheduler.add(ensayos3LoopEnd);
    span3LoopScheduler.add(RecallRoutineBegin(snapshot));
    span3LoopScheduler.add(RecallRoutineEachFrame(snapshot));
    span3LoopScheduler.add(RecallRoutineEnd(snapshot));
    span3LoopScheduler.add(endLoopIteration(span3LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var ensayos3;
function ensayos3LoopBegin(ensayos3LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  ensayos3 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, Eligebloque, '4:7'),
    seed: undefined, name: 'ensayos3'
  });
  psychoJS.experiment.addLoop(ensayos3); // add the loop to the experiment
  currentLoop = ensayos3;  // we're now the current loop

  // Schedule all the trials in the trialList:
  ensayos3.forEach(function() {
    const snapshot = ensayos3.getSnapshot();

    ensayos3LoopScheduler.add(importConditions(snapshot));
    ensayos3LoopScheduler.add(trialRoutineBegin(snapshot));
    ensayos3LoopScheduler.add(trialRoutineEachFrame(snapshot));
    ensayos3LoopScheduler.add(trialRoutineEnd(snapshot));
    ensayos3LoopScheduler.add(memRoutineBegin(snapshot));
    ensayos3LoopScheduler.add(memRoutineEachFrame(snapshot));
    ensayos3LoopScheduler.add(memRoutineEnd(snapshot));
    ensayos3LoopScheduler.add(endLoopIteration(ensayos3LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function ensayos3LoopEnd() {
  psychoJS.experiment.removeLoop(ensayos3);

  return Scheduler.Event.NEXT;
}


function span3LoopEnd() {
  psychoJS.experiment.removeLoop(span3);

  return Scheduler.Event.NEXT;
}


var span4;
function span4LoopBegin(span4LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  span4 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'Bloques.xlsx', '0:3'),
    seed: undefined, name: 'span4'
  });
  psychoJS.experiment.addLoop(span4); // add the loop to the experiment
  currentLoop = span4;  // we're now the current loop

  // Schedule all the trials in the trialList:
  span4.forEach(function() {
    const snapshot = span4.getSnapshot();

    span4LoopScheduler.add(importConditions(snapshot));
    span4LoopScheduler.add(warning1RoutineBegin(snapshot));
    span4LoopScheduler.add(warning1RoutineEachFrame(snapshot));
    span4LoopScheduler.add(warning1RoutineEnd(snapshot));
    const ensayos4LoopScheduler = new Scheduler(psychoJS);
    span4LoopScheduler.add(ensayos4LoopBegin, ensayos4LoopScheduler);
    span4LoopScheduler.add(ensayos4LoopScheduler);
    span4LoopScheduler.add(ensayos4LoopEnd);
    span4LoopScheduler.add(RecallRoutineBegin(snapshot));
    span4LoopScheduler.add(RecallRoutineEachFrame(snapshot));
    span4LoopScheduler.add(RecallRoutineEnd(snapshot));
    span4LoopScheduler.add(endLoopIteration(span4LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var ensayos4;
function ensayos4LoopBegin(ensayos4LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  ensayos4 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, Eligebloque, '7:11'),
    seed: undefined, name: 'ensayos4'
  });
  psychoJS.experiment.addLoop(ensayos4); // add the loop to the experiment
  currentLoop = ensayos4;  // we're now the current loop

  // Schedule all the trials in the trialList:
  ensayos4.forEach(function() {
    const snapshot = ensayos4.getSnapshot();

    ensayos4LoopScheduler.add(importConditions(snapshot));
    ensayos4LoopScheduler.add(trialRoutineBegin(snapshot));
    ensayos4LoopScheduler.add(trialRoutineEachFrame(snapshot));
    ensayos4LoopScheduler.add(trialRoutineEnd(snapshot));
    ensayos4LoopScheduler.add(memRoutineBegin(snapshot));
    ensayos4LoopScheduler.add(memRoutineEachFrame(snapshot));
    ensayos4LoopScheduler.add(memRoutineEnd(snapshot));
    ensayos4LoopScheduler.add(endLoopIteration(ensayos4LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function ensayos4LoopEnd() {
  psychoJS.experiment.removeLoop(ensayos4);

  return Scheduler.Event.NEXT;
}


function span4LoopEnd() {
  psychoJS.experiment.removeLoop(span4);

  return Scheduler.Event.NEXT;
}


var span5;
function span5LoopBegin(span5LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  span5 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'Bloques.xlsx', '0:3'),
    seed: undefined, name: 'span5'
  });
  psychoJS.experiment.addLoop(span5); // add the loop to the experiment
  currentLoop = span5;  // we're now the current loop

  // Schedule all the trials in the trialList:
  span5.forEach(function() {
    const snapshot = span5.getSnapshot();

    span5LoopScheduler.add(importConditions(snapshot));
    span5LoopScheduler.add(warning1RoutineBegin(snapshot));
    span5LoopScheduler.add(warning1RoutineEachFrame(snapshot));
    span5LoopScheduler.add(warning1RoutineEnd(snapshot));
    const ensayos5LoopScheduler = new Scheduler(psychoJS);
    span5LoopScheduler.add(ensayos5LoopBegin, ensayos5LoopScheduler);
    span5LoopScheduler.add(ensayos5LoopScheduler);
    span5LoopScheduler.add(ensayos5LoopEnd);
    span5LoopScheduler.add(RecallRoutineBegin(snapshot));
    span5LoopScheduler.add(RecallRoutineEachFrame(snapshot));
    span5LoopScheduler.add(RecallRoutineEnd(snapshot));
    span5LoopScheduler.add(endLoopIteration(span5LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var ensayos5;
function ensayos5LoopBegin(ensayos5LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  ensayos5 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, Eligebloque, '11:16'),
    seed: undefined, name: 'ensayos5'
  });
  psychoJS.experiment.addLoop(ensayos5); // add the loop to the experiment
  currentLoop = ensayos5;  // we're now the current loop

  // Schedule all the trials in the trialList:
  ensayos5.forEach(function() {
    const snapshot = ensayos5.getSnapshot();

    ensayos5LoopScheduler.add(importConditions(snapshot));
    ensayos5LoopScheduler.add(trialRoutineBegin(snapshot));
    ensayos5LoopScheduler.add(trialRoutineEachFrame(snapshot));
    ensayos5LoopScheduler.add(trialRoutineEnd(snapshot));
    ensayos5LoopScheduler.add(memRoutineBegin(snapshot));
    ensayos5LoopScheduler.add(memRoutineEachFrame(snapshot));
    ensayos5LoopScheduler.add(memRoutineEnd(snapshot));
    ensayos5LoopScheduler.add(endLoopIteration(ensayos5LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function ensayos5LoopEnd() {
  psychoJS.experiment.removeLoop(ensayos5);

  return Scheduler.Event.NEXT;
}


function span5LoopEnd() {
  psychoJS.experiment.removeLoop(span5);

  return Scheduler.Event.NEXT;
}


var span6;
function span6LoopBegin(span6LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  span6 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'Bloques.xlsx', '0:3'),
    seed: undefined, name: 'span6'
  });
  psychoJS.experiment.addLoop(span6); // add the loop to the experiment
  currentLoop = span6;  // we're now the current loop

  // Schedule all the trials in the trialList:
  span6.forEach(function() {
    const snapshot = span6.getSnapshot();

    span6LoopScheduler.add(importConditions(snapshot));
    span6LoopScheduler.add(warning1RoutineBegin(snapshot));
    span6LoopScheduler.add(warning1RoutineEachFrame(snapshot));
    span6LoopScheduler.add(warning1RoutineEnd(snapshot));
    const ensayos6LoopScheduler = new Scheduler(psychoJS);
    span6LoopScheduler.add(ensayos6LoopBegin, ensayos6LoopScheduler);
    span6LoopScheduler.add(ensayos6LoopScheduler);
    span6LoopScheduler.add(ensayos6LoopEnd);
    span6LoopScheduler.add(RecallRoutineBegin(snapshot));
    span6LoopScheduler.add(RecallRoutineEachFrame(snapshot));
    span6LoopScheduler.add(RecallRoutineEnd(snapshot));
    span6LoopScheduler.add(endLoopIteration(span6LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var ensayos6;
function ensayos6LoopBegin(ensayos6LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  ensayos6 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, Eligebloque, '16:22'),
    seed: undefined, name: 'ensayos6'
  });
  psychoJS.experiment.addLoop(ensayos6); // add the loop to the experiment
  currentLoop = ensayos6;  // we're now the current loop

  // Schedule all the trials in the trialList:
  ensayos6.forEach(function() {
    const snapshot = ensayos6.getSnapshot();

    ensayos6LoopScheduler.add(importConditions(snapshot));
    ensayos6LoopScheduler.add(trialRoutineBegin(snapshot));
    ensayos6LoopScheduler.add(trialRoutineEachFrame(snapshot));
    ensayos6LoopScheduler.add(trialRoutineEnd(snapshot));
    ensayos6LoopScheduler.add(memRoutineBegin(snapshot));
    ensayos6LoopScheduler.add(memRoutineEachFrame(snapshot));
    ensayos6LoopScheduler.add(memRoutineEnd(snapshot));
    ensayos6LoopScheduler.add(endLoopIteration(ensayos6LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function ensayos6LoopEnd() {
  psychoJS.experiment.removeLoop(ensayos6);

  return Scheduler.Event.NEXT;
}


function span6LoopEnd() {
  psychoJS.experiment.removeLoop(span6);

  return Scheduler.Event.NEXT;
}


var warningeComponents;
function warningeRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'warninge'-------
    t = 0;
    warningeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    warningeComponents = [];
    warningeComponents.push(text_6);
    
    warningeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function warningeRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'warninge'-------
    // get current time
    t = warningeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_6* updates
    if (t >= 0.0 && text_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_6.tStart = t;  // (not accounting for frame time here)
      text_6.frameNStart = frameN;  // exact frame index
      
      text_6.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_6.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    warningeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function warningeRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'warninge'-------
    warningeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_2_allKeys;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'trial'-------
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    text.setText(Estimulo);
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(text);
    trialComponents.push(key_resp_2);
    
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'trial'-------
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.3 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
    // *key_resp_2* updates
    if (t >= 0.3 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // was this correct?
        if (key_resp_2.keys == Respuesta) {
            key_resp_2.corr = 1;
        } else {
            key_resp_2.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'trial'-------
    trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (key_resp_2.keys === undefined) {
      if (['None','none',undefined].includes(Respuesta)) {
         key_resp_2.corr = 1;  // correct non-response
      } else {
         key_resp_2.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    psychoJS.experiment.addData('key_resp_2.corr', key_resp_2.corr);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var memComponents;
function memRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'mem'-------
    t = 0;
    memClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    text_2.setText(Letra);
    // keep track of which components have finished
    memComponents = [];
    memComponents.push(text_2);
    
    memComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function memRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'mem'-------
    // get current time
    t = memClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    memComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function memRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'mem'-------
    memComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_3_allKeys;
var _key_resp_4_allKeys;
var RecallComponents;
function RecallRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Recall'-------
    t = 0;
    RecallClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    // keep track of which components have finished
    RecallComponents = [];
    RecallComponents.push(text_3);
    RecallComponents.push(key_resp_3);
    RecallComponents.push(key_resp_4);
    
    RecallComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function RecallRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Recall'-------
    // get current time
    t = RecallClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }

    
    // *key_resp_3* updates
    if (t >= 0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }

    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['q', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys.map((key) => key.name);  // storing all keys
        key_resp_3.rt = _key_resp_3_allKeys.map((key) => key.rt);
        // was this correct?
        if (key_resp_3.keys == CorRec) {
            key_resp_3.corr = 1;
        } else {
            key_resp_3.corr = 0;
        }
      }
    }
    
    
    // *key_resp_4* updates
    if (t >= 0.5 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.clearEvents(); });
    }

    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_4.rt = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    RecallComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function RecallRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Recall'-------
    RecallComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (key_resp_3.keys === undefined) {
      if (['None','none',undefined].includes(CorRec)) {
         key_resp_3.corr = 1;  // correct non-response
      } else {
         key_resp_3.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    psychoJS.experiment.addData('key_resp_3.corr', key_resp_3.corr);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        }
    
    key_resp_3.stop();
    psychoJS.experiment.addData('key_resp_4.keys', key_resp_4.keys);
    if (typeof key_resp_4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_4.rt', key_resp_4.rt);
        routineTimer.reset();
        }
    
    key_resp_4.stop();
    // the Routine "Recall" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var warning1Components;
function warning1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'warning1'-------
    t = 0;
    warning1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.500000);
    // update component parameters for each repeat
    // keep track of which components have finished
    warning1Components = [];
    warning1Components.push(text_5);
    
    warning1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function warning1RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'warning1'-------
    // get current time
    t = warning1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_5* updates
    if (t >= 0.0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_5.tStart = t;  // (not accounting for frame time here)
      text_5.frameNStart = frameN;  // exact frame index
      
      text_5.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_5.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    warning1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function warning1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'warning1'-------
    warning1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
