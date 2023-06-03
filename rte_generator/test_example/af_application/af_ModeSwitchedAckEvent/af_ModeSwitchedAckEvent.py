from autosarfactory import autosarfactory
import os, sys
mod_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, mod_path)

componentFile = os.path.join(os.path.dirname(__file__), 'af_ModeSwitchedAckEvent_Component.arxml')
#print("component = ",componentFile)
interfaceFile = os.path.join(os.path.dirname(__file__), 'af_ModeSwitchedAckEvent_Interface.arxml')
#print("interface = ",interfaceFile)
modeFile = os.path.join(os.path.dirname(__file__), 'af_ModeSwitchedAckEvent_ModeDeclaration.arxml')

#new mode declaration
modePack = autosarfactory.new_file(modeFile, defaultArPackage = 'af_EvMsa_ModeDeclaration', overWrite = 'true')
modeG1 = modePack.new_ModeDeclarationGroup('ECUMMode')
modeG1.set_category('EXPLICIT_ORDER')
mode1_STARTUP_SHUTDOWN = modeG1.new_ModeDeclaration('STARTUP_SHUTDOWN')
mode1_STARTUP_SHUTDOWN.set_value(100)
mode1_RUN = modeG1.new_ModeDeclaration('RUN')
mode1_RUN.set_value(101)
mode1_SLEEP = modeG1.new_ModeDeclaration('SLEEP')
mode1_SLEEP.set_value(1000)
modeG1.set_initialMode(mode1_STARTUP_SHUTDOWN)
modeG1.set_onTransitionValue(666)

#new senderRecever interface
interfacePack = autosarfactory.new_file(interfaceFile, defaultArPackage = 'af_EvMsa_Interface', overWrite = 'true') 
msIf = interfacePack.new_ModeSwitchInterface('IfModeSwitch1')
msIf_modeGP1 = msIf.new_ModeGroup('ECUMModePrototype1')
msIf_modeGP1.set_type(modeG1)

componentPack = autosarfactory.new_file(componentFile, defaultArPackage = 'af_EvMsa_Component', overWrite = 'true') 
#new applicaton component
asw1 = componentPack.new_ApplicationSwComponentType('SwctAppModeMgr')
pPort1 = asw1.new_PPortPrototype('PpAppMode')
pPort1.set_providedInterface(msIf)
pPort1.new_ModeSwitchSenderComSpec()

ibhSwcAppModeMgr1 = asw1.new_InternalBehavior('IbhSwctAppModeMgr')
ibhSwcAppModeMgr1_ReModeSwitchMgr = ibhSwcAppModeMgr1.new_Runnable('ReModeSwitchMgr')
modeSwitchPoint_modeG1 = ibhSwcAppModeMgr1_ReModeSwitchMgr.new_ModeSwitchPoint('ModeSwitchPoint_PpAppMode')
modeSwitchPoint_modeG1_InstanceRef = modeSwitchPoint_modeG1.new_ModeGroup()
modeSwitchPoint_modeG1_InstanceRef.set_contextPPort(pPort1)
modeSwitchPoint_modeG1_InstanceRef.set_targetModeGroup(msIf_modeGP1)

ibhSwcAppModeMgr1_ReModeSwitchComplete = ibhSwcAppModeMgr1.new_Runnable('ReModeSwitchComplete')

ibhSwcAppMOdeMgr1_EvMsa1 = ibhSwcAppModeMgr1.new_ModeSwitchedAckEvent('EvMsaAppMode')
ibhSwcAppMOdeMgr1_EvMsa1.set_startOnEvent(ibhSwcAppModeMgr1_ReModeSwitchComplete)
ibhSwcAppMOdeMgr1_EvMsa1.set_eventSource(modeSwitchPoint_modeG1)
autosarfactory.save()
print("SUCESS")

