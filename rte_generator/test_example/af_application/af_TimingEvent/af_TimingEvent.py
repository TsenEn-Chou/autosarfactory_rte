from autosarfactory import autosarfactory
import os, sys
mod_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, mod_path)

componentFile = os.path.join(os.path.dirname(__file__), 'af_TimingEvent_Component.arxml')
#print("component = ",componentFile)
interfaceFile = os.path.join(os.path.dirname(__file__), 'af_TimingEvent_Interface.arxml')
#print("interface = ",interfaceFile)

#new senderRecever interface
interfacePack = autosarfactory.new_file(interfaceFile, defaultArPackage = 'af_EvTi_Interface', overWrite = 'true') 
srIf = interfacePack.new_SenderReceiverInterface('IfSenderReceiver1')
dataElementAcc = srIf.new_DataElement('Acc') 
dataElementSpd = srIf.new_DataElement('Spd')
SwDDP_Acc = dataElementAcc.new_SwDataDefProps()
SwDDP_Variant1_Acc = SwDDP_Acc.new_SwDataDefPropsVariant()
SwDDP_Variant1_Acc.set_swImplPolicy('queued')


componentPack = autosarfactory.new_file(componentFile, defaultArPackage = 'af_EvTi_Component', overWrite = 'true') 
aswct1 = componentPack.new_ApplicationSwComponentType('SwctTiming')
pPort1 = aswct1.new_PPortPrototype('PpIfVehMov')
pPort1.set_providedInterface(srIf)

ibhSwctTiming = aswct1.new_InternalBehavior('IbhSwctTiming')
ibhSwctTiming_ReTxSpd = ibhSwctTiming.new_Runnable('ReTxSpd')
ibhSwctTiming_ReTxSpd_DSP = ibhSwctTiming_ReTxSpd.new_DataSendPoint('SendPoint_PpIfVehMov_Spd')
ibhSwctTiming_ReTxSpd_DSP_AV = ibhSwctTiming_ReTxSpd_DSP.new_AccessedVariable()
ibhSwctTiming_ReTxSpd_DSP_AV_AV = ibhSwctTiming_ReTxSpd_DSP_AV.new_AutosarVariable()
ibhSwctTiming_ReTxSpd_DSP_AV_AV.set_portPrototype(pPort1)
ibhSwctTiming_ReTxSpd_DSP_AV_AV.set_targetDataPrototype(dataElementSpd)

ibhSwctTiming_ReRxAcc = ibhSwctTiming.new_Runnable('ReRxAcc')
ibhSwctTiming_ReRxAcc_DSP = ibhSwctTiming_ReRxAcc.new_DataReadAcces('DataReadAccess_PpIfVehMov_Acc')
ibhSwctTiming_ReRxAcc_DSP_AV = ibhSwctTiming_ReRxAcc_DSP.new_AccessedVariable()
ibhSwctTiming_ReRxAcc_DSP_AV_AV = ibhSwctTiming_ReRxAcc_DSP_AV.new_AutosarVariable()
ibhSwctTiming_ReRxAcc_DSP_AV_AV.set_portPrototype(pPort1)
ibhSwctTiming_ReRxAcc_DSP_AV_AV.set_targetDataPrototype(dataElementAcc)

ibhSwctTiming_EvTiSpd_20ms = ibhSwctTiming.new_TimingEvent('EvTiSpd_20ms')
ibhSwctTiming_EvTiSpd_20ms.set_startOnEvent(ibhSwctTiming_ReTxSpd)
ibhSwctTiming_EvTiSpd_20ms.set_period('0.02')
autosarfactory.save()
print("SUCCESS")

