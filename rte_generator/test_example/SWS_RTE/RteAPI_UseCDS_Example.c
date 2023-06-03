typedef struct Rte_DE_uint8 {
    unsigned char value;
} Rte_DE_uint8;
/*
 * [SWS_Rte_02310] ⌈The Application Header File shall include a structure declaration for the component data structure as follows:  
 * struct Rte_CDS_<cts> { <component data sections> }; where <cts> is the component type symbol of the AtomicSwComponentType. 
 */
struct Rte_CDS_c{
    Rte_DE_uint8* re1_rport_a;
    Rte_DE_uint8* re1_pport_a;
    /* 
     * [SWS_Rte_03733] ⌈Data Handles shall be named <re>_<p>_<o> where <re> is the runnable entity name 
     * that reads (or writes) the data item, <p> the port name, <o> the data element.⌋(SRS_BSW_00305, SRS_Rte_00051)
     */
};

typedef struct Rte_CDS_c Rte_CDS_c;

Rte_DE_uint8 implicit_read_buffer_a = {100}; Rte_DE_uint8 implicit_write_buffer_a = {100};

const Rte_CDS_c Rte_Instance_c1 =
{
    &implicit_read_buffer_a,  &implicit_write_buffer_a  
};

Rte_DE_uint8 Rte_IRead_re1_rport_a(){
    Rte_DE_uint8 returnValue =  *Rte_Instance_c1.re1_rport_a; 
    return returnValue;
}

void Rte_IWrite_re1_pport_a(Rte_DE_uint8 writeValue ){
    *Rte_Instance_c1.re1_pport_a = writeValue; 
}

void Run1_UpdateTemp(){
    Rte_DE_uint8 readValue = Rte_IRead_re1_rport_a();
    readValue.value = readValue.value + (unsigned char)100; 
    Rte_IWrite_re1_pport_a(readValue);
}

OSTASK1(){
    Run1_UpdateTemp(); 
    TerminateTask();
}