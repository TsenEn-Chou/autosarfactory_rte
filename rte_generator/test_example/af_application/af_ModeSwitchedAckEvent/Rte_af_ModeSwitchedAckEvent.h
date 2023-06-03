//#ifndef RTE_MODE_<ModeDeclarationGroup>_<ModeDeclaration>
//#define RTE_MODE_<ModeDeclarationGroup>_<ModeDeclaration> <value>U
//#endif

//[SWS_Rte_02659]
//#ifndef RTE_TRANSITION_<prefix><ModeDeclarationGroup>
//#define RTE_TRANSITION_<prefix><ModeDeclarationGroup> \
<n>U
//#endif
#ifndef RTE_TRANSITION_ECUMMode
#define RTE_TRANSITION_ECUMMode <n>U
#endif

//[SWS_Rte_03858]
//#ifndef RTE_TRANSITION_<prefix><ModeDeclarationGroup>
//#define RTE_TRANSITION_<prefix><ModeDeclarationGroup> \
//<onTransitionValue>U
//#endif
#ifndef RTE_TRANSITION_ECUMMode
#define RTE_TRANSITION_ECUMMode 666U
#endif

#ifndef RTE_MODE_ECUMMode_STARTUP_SHUTDOWN
#define RTE_MODE_ECUMMode_STARTUP_SHUTDOWN 100
#endif

#ifndef RTE_MODE_ECUMMode_RUN
#define RTE_MODE_ECUMMode_RUN 101
#endif

#ifndef RTE_MODE_ECUMMode_SLEEP
#define RTE_MODE_ECUMMode_SLEEP 2
#endif

typedef struct
{
        unsigned int value;
} ModeDelaration;

typedef struct
{
        ModeDelaration* initialMode;
        ModeDelaration* modeDeclaration;
        unsigned int onTransitionValue;
        //.....
} ModeDeclarationGroup;

typedef enum
{
        notAccessible = 0,
        readOnly = 1,
        readWrite = 2,
} SwCalibrationAccessEnum;

typedef struct
{
        SwCalibrationAccessEnum swCalibrationAccess;
        ModeDeclarationGroup* type;
} ModeDeclarationGroupPrototype;

typedef struct
{
        ModeDeclarationGroupPrototype* modeGroup;
} ModeSwitchPoint;

typedef struct
{
        ModeSwitchPoint* modeSwitchPoint;
        //...
} RunnableEntity;

typedef enum
{
        comManager = 2,
        ecuManager = 4,
        //...
} ServiceProviderEnum;

typedef struct
{
        bool _isService;
        ServiceProviderEnum _serviceKind;
} PortInterface;

typedef struct
{
        PortInterface parent;
        ModeDeclarationGroupPrototype modeGroup;
} ModeSwitchInterface;


ModeSwitchPoint ofReModeSwitchMgr[0] = {ECUMModeDeclarationPrototype1};

typedef struct
{
        RunnableEntity runnable;
        //...
} SwcInternalBehavior;

typedef struct
{
        SwcInternalBehavior internalBehavior;
        //...
} ApplicationSwComponentType;

ApplicationSwComponentType SwctAppModeMgr;
