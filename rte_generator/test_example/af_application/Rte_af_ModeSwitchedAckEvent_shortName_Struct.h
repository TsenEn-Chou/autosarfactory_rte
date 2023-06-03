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

// <ModeDelcarationGroup.shortName>
typedef enum
{
        RTE_MODE_ECUMMode_STARTUP_SHUTDOWN = RTE_MODE_ECUMMode_STARTUP_SHUTDOWN,
        RTE_MODE_ECUMMode_RUN = RTE_MODE_ECUMMode_RUN,
        RTE_MODE_ECUMMode_SLEEP = RTE_MODE_ECUMMode_SLEEP,
        RTE_TRANSITION_ECUMMode = RTE_TRANSITION_ECUMMode,
} ECUMMode;

// <ModeDelcarationGroup.shortName>_ModeDeclarationGroup
/*
 *
 * 這邊沒有按照 Spec. Class 定義的原因是因為一個 SWC 可能會包含多個 ModeDeclarationGroup ，
 * 如果按照 Spec. 只定義 "ModeDeclarationGroup" class(in c called struct)，會遇到以下問題
 * 1. ModeDelcarationGroup 命名衝突，在 Arxml 中外部是 ModeDelcarationGroup，但是內部不一樣
 */
typedef struct
{
        ECUMMode initialMode;
        ECUMMode modeDeclaration;
        ECUMMode onTransitionValue;
        //.....
} ECUMMode_ModeDeclarationGroup;

typedef enum
{
        notAccessible = 0,
        readOnly = 1,
        readWrite = 2,
} SwCalibrationAccessEnum;


typedef struct
{
        SwCalibrationAccessEnum swCalibrationAccess;
        ECUMMode_ModeDeclarationGroup type;
} ECUMModePrototype1_ModeDeclarationGroupPrototype;

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
        ECUMModePrototype1_ModeDeclarationGroupPrototype modeGroup;
} IfModeSwitch1_ModeSwitchInterface;

typedef struct
{

} ModeSwitchSenderComSpec;

typedef struct
{

} AbstractProvidedPortPrototype;
