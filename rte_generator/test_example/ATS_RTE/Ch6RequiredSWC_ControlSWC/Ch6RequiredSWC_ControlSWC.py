from autosarfactory import autosarfactory
import os, sys
mod_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, mod_path)

component_file = os.path.join(os.path.dirname(__file__), 'Ch6RequiredSWC_ControlSWC_Component.arxml')
#print("component = ",componentFile)
interface_file = os.path.join(os.path.dirname(__file__), 'Ch6RequiredSWC_ControlSWC_Interface.arxml')
#print("interface = ",interfaceFile)
datatype_file = os.path.join(os.path.dirname(__file__), 'Ch6RequiredSWC_ControlSWC_Datatype.arxml')


dataType_Packages = autosarfactory.new_file(datatype_file, defaultArPackage = 'ControlSWC_Datatypes', overWrite = 'true') 

baseType_Package = dataType_Packages.new_ARPackage('BaseTypes')
uint8_SwBaseType = baseType_Package.new_SwBaseType('uint8')
uint8_SwBaseType.set_category('FIXED_LENGTH')
uint8_SwBaseType_baseTypeDefinition = uint8_SwBaseType.new_BaseTypeDirectDefinition()
uint8_SwBaseType_baseTypeDefinition.set_baseTypeSize('8')
uint8_SwBaseType_baseTypeDefinition.set_baseTypeEncoding('NONE')
uint8_SwBaseType_baseTypeDefinition.set_nativeDeclaration('uint8')

float64_SwBaseType = baseType_Package.new_SwBaseType('Float64')
float64_SwBaseType.set_category('FIXED_LENGTH')
float64_SwBaseType_baseTypeDefinition = float64_SwBaseType.new_BaseTypeDirectDefinition()
float64_SwBaseType_baseTypeDefinition.set_baseTypeSize('64')
float64_SwBaseType_baseTypeDefinition.set_baseTypeEncoding('IEEE754')
float64_SwBaseType_baseTypeDefinition.set_nativeDeclaration('float64')


implType_Package = dataType_Packages.new_ARPackage('ImplementationDataTypes')
TYP_ExchangedData_uint8 = implType_Package.new_ImplementationDataType('TYP_ExchangedData_uint8')
TYP_ExchangedData_uint8.set_category('VALUE')
TYP_ExchangedData_uint8.set_typeEmitter('RTE')
TYP_ExchangedData_uint8.new_SwDataDefProps().new_SwDataDefPropsVariant().set_baseType(uint8_SwBaseType)
TYP_ExchangedData_uint8_SymbolProps = TYP_ExchangedData_uint8.new_SymbolProps('TYP_ExchangedData_uint8_symbol')
TYP_ExchangedData_uint8_SymbolProps.set_symbol('MyUint8OfVendorID')

TYP_ExchangedData_float64 = implType_Package.new_ImplementationDataType('TYP_ExchangedData_float64')
TYP_ExchangedData_float64.set_category('VALUE')
TYP_ExchangedData_float64.set_typeEmitter('sssssssssss.h')
TYP_ExchangedData_float64.new_SwDataDefProps().new_SwDataDefPropsVariant().set_baseType(float64_SwBaseType)
TYP_ExchangedData_float64_SymbolProps = TYP_ExchangedData_float64.new_SymbolProps('TYP_ExchangedData_float64_symbol')
TYP_ExchangedData_float64_SymbolProps.set_symbol('MyUint8OfVendorID')

TYP_ExchangedData_float32 = implType_Package.new_ImplementationDataType('TYP_ExchangedData_float32')
TYP_ExchangedData_float32.set_category('VALUE')
TYP_ExchangedData_float32.set_typeEmitter('RTE')
#TYP_ExchangedData_float32.new_SwDataDefProps().new_SwDataDefPropsVariant().set_baseType(float64_SwBaseType)

autosarfactory.save()