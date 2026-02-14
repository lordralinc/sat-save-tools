# Objects

[← Back](/notes/README.md)

A list of objects contained in the save file.

# Content:

- `Game`
  - `FactoryGame`
    - `-Shared`
      - `Blueprint`
        - [`BP_BlueprintSusbystem.BP_BlueprintSusbystem_C`](#43f2062f1d7e9bcb357a799f22e1c02a)
        - [`BP_BuildableSubsystem.BP_BuildableSubsystem_C`](#13be4d096a7057b1aed35a375538ac51)
        - [`BP_CircuitSubsystem.BP_CircuitSubsystem_C`](#9a50aeea42a31706787ab070eebcec65)
        - [`BP_GameMode.BP_GameMode_C`](#15932108758848e1468c1d60992f7b10)
        - [`BP_GameState.BP_GameState_C`](#30d5aa37fc70663fddf7a1a1aca6322d)
        - [`BP_IconDatabaseSubsystem.BP_IconDatabaseSubsystem_C`](#5dcb68d8ca853e2b5ee7c976a615c1c8)
        - [`BP_RailroadSubsystem.BP_RailroadSubsystem_C`](#2efb094ad027c82de6fdd502a08ce2c1)
        - [`BP_StorySubsystem.BP_StorySubsystem_C`](#5e177cf5245a24317739aaa231d427d4)
        - [`BP_TimeOfDaySubsystem.BP_TimeOfDaySubsystem_C`](#a81f6dd298205076513984f2e0d1b6d1)
        - [`BP_TutorialIntroManager.BP_TutorialIntroManager_C`](#d75dafa7313eb5eb3dfbc6e7f91fd354)
        - [`BP_VehicleSubsystem.BP_VehicleSubsystem_C`](#d45e4c07d39a8fe16aa05266141f3758)
    - `Buildable`
      - `Building`
        - `ConveyorHole`
          - [`Build_ConveyorWallHole.Build_ConveyorWallHole_C`](#a7b2dee30a7613737978d312d66be8ed)
        - `Ladder`
          - [`Build_Ladder.Build_Ladder_C`](#6f017e2b4093a549e07c4f2ce1d2946a)
        - `Potty`
          - [`BUILD_Potty_mk1.BUILD_Potty_mk1_C`](#eb0c85a2263290b0a77dc5cbcb771a5f)
      - `Factory`
        - `AssemblerMk1`
          - [`Build_AssemblerMk1.Build_AssemblerMk1_C`](#a2da0f1c9ea54dcf2708b4112044625f)
        - `Blender`
          - [`Build_Blender.Build_Blender_C`](#c0d14a96f9e819e7c9f7087ffbab92d5)
        - `BlueprintDesigner`
          - [`Build_BlueprintDesigner.Build_BlueprintDesigner_C`](#64ba976ff7c13d6a78b97d48874edd7d)
        - `CA_MergerPriority`
          - [`Build_ConveyorAttachmentMergerPriority.Build_ConveyorAttachmentMergerPriority_C`](#28339abdfe624cc3eda2e974b56375e6)
        - `CA_Merger`
          - [`Build_ConveyorAttachmentMerger.Build_ConveyorAttachmentMerger_C`](#e12677762eb562ab84a64a43e677acd6)
        - `CA_SplitterProgrammable`
          - [`Build_ConveyorAttachmentSplitterProgrammable.Build_ConveyorAttachmentSplitterProgrammable_C`](#1d84a16d789d3169cca29a662b15d1a9)
        - `CA_SplitterSmart`
          - [`Build_ConveyorAttachmentSplitterSmart.Build_ConveyorAttachmentSplitterSmart_C`](#d503c70fefe92bf962cb779774296d44)
        - `CA_Splitter`
          - [`Build_ConveyorAttachmentSplitter.Build_ConveyorAttachmentSplitter_C`](#1144ead904286c2b48fe4be3dc409207)
        - `CeilingLight`
          - [`Build_CeilingLight.Build_CeilingLight_C`](#695f9f789761131285fe9105ffcd6dbc)
        - `CentralStorage`
          - [`Build_CentralStorage.Build_CentralStorage_C`](#c627972ae3a108a85d7e6524b304dc4e)
        - `ConstructorMk1`
          - [`Build_ConstructorMk1.Build_ConstructorMk1_C`](#205f783d3131c6f13d6a52e5ac9c2fe7)
        - `Converter`
          - [`Build_Converter.Build_Converter_C`](#1aa76086f37ebd8ec43478ac776d133e)
        - `ConveyorBeltMk1`
          - [`Build_ConveyorBeltMk1.Build_ConveyorBeltMk1_C`](#d0ea31d73878b0e0b7a78ff94673a221)
        - `ConveyorBeltMk2`
          - [`Build_ConveyorBeltMk2.Build_ConveyorBeltMk2_C`](#1f68db034b1ea75bec863a3718707fa4)
        - `ConveyorBeltMk3`
          - [`Build_ConveyorBeltMk3.Build_ConveyorBeltMk3_C`](#ee5b5a833dfd38557755c3c15216dee3)
        - `ConveyorBeltMk4`
          - [`Build_ConveyorBeltMk4.Build_ConveyorBeltMk4_C`](#e8378d7af763423090f0b3c55e412d24)
        - `ConveyorBeltMk5`
          - [`Build_ConveyorBeltMk5.Build_ConveyorBeltMk5_C`](#ccdcdd175a445d7db2ca3197b9002f60)
        - `ConveyorBeltMk6`
          - [`Build_ConveyorBeltMk6.Build_ConveyorBeltMk6_C`](#af08bb4d7003f70249e5ca247e432ab2)
        - `ConveyorLiftMk1`
          - [`Build_ConveyorLiftMk1.Build_ConveyorLiftMk1_C`](#2b9021bfdd217181bc2a3258cbfce6d6)
        - `ConveyorLiftMk2`
          - [`Build_ConveyorLiftMk2.Build_ConveyorLiftMk2_C`](#49d0d4acfa62f0923e3c7c734d25eabf)
        - `ConveyorLiftMk3`
          - [`Build_ConveyorLiftMk3.Build_ConveyorLiftMk3_C`](#2df4182e7cfdbcc2587cfb80b5126dfb)
        - `ConveyorLiftMk4`
          - [`Build_ConveyorLiftMk4.Build_ConveyorLiftMk4_C`](#33cd3fb848039688b577573485554692)
        - `ConveyorLiftMk5`
          - [`Build_ConveyorLiftMk5.Build_ConveyorLiftMk5_C`](#7563582a6bfcd822cfd8769df1c0ece3)
        - `ConveyorLiftMk6`
          - [`Build_ConveyorLiftMk6.Build_ConveyorLiftMk6_C`](#7524949c010a1956665c784f0cb0e6bb)
        - `ConveyorMonitor`
          - [`Build_ConveyorMonitor.Build_ConveyorMonitor_C`](#9a3202f0de8a34c4e0ec5a7d8bd5c361)
        - `ConveyorPoleStackable`
          - [`Build_ConveyorPoleStackable.Build_ConveyorPoleStackable_C`](#6dca9aff96836c7e9552a9ba0427e691)
        - `ConveyorPoleWall`
          - [`Build_ConveyorCeilingAttachment.Build_ConveyorCeilingAttachment_C`](#475c9415ef0582458e208afefaecd5cf)
          - [`Build_ConveyorPoleWall.Build_ConveyorPoleWall_C`](#869b136c38226fad3affdfb4e7458a63)
        - `ConveyorPole`
          - [`Build_ConveyorPole.Build_ConveyorPole_C`](#96b541ad54803b9a9a0c0c6501b34b71)
        - `Elevator`
          - [`BP_ElevatorCabin.BP_ElevatorCabin_C`](#5b73508f96f242c071bda5157b5b9ccb)
          - [`Build_Elevator.Build_Elevator_C`](#9a4f15f614b5a853b1630f4abd2b5991)
          - [`Build_ElevatorFloorStop.Build_ElevatorFloorStop_C`](#c7902e457c389891906f000b5c2cd491)
        - `Floodlight`
          - [`Build_FloodlightWall.Build_FloodlightWall_C`](#15674156724758cdb4c05f7c04eb1b45)
        - `FoundationPassthrough`
          - [`Build_FoundationPassthrough_Hypertube.Build_FoundationPassthrough_Hypertube_C`](#a19a4f19be2fb74a0538c20f5769e0aa)
          - [`Build_FoundationPassthrough_Lift.Build_FoundationPassthrough_Lift_C`](#a423f2f2d856ab32b6186cf3583e6433)
          - [`Build_FoundationPassthrough_Pipe.Build_FoundationPassthrough_Pipe_C`](#7e61ee15a562bb2437326157fdc72f4c)
        - `GeneratorBiomass`
          - [`Build_GeneratorBiomass_Automated.Build_GeneratorBiomass_Automated_C`](#2625999ec4d6d208c75242e324428ecb)
          - [`Build_GeneratorIntegratedBiomass.Build_GeneratorIntegratedBiomass_C`](#83d14b5a11387466f4b982ff339843c5)
        - `GeneratorCoal`
          - [`Build_GeneratorCoal.Build_GeneratorCoal_C`](#30aa9b953993b6744a2d60ebd28a517e)
        - `GeneratorFuel`
          - [`Build_GeneratorFuel.Build_GeneratorFuel_C`](#3f0761b600eb559677ecb497d34e907b)
        - `GeneratorNuclear`
          - [`Build_GeneratorNuclear.Build_GeneratorNuclear_C`](#ca30c56529395c9afb8011617e053454)
        - `HadronCollider`
          - [`Build_HadronCollider.Build_HadronCollider_C`](#13931735969722b08fc71e86316ef296)
        - `HubTerminal`
          - [`Build_HubTerminal.Build_HubTerminal_C`](#f7f53cca5fbdbeabb952bdea027856ab)
        - `HyperTubeWallSupport`
          - [`Build_HyperTubeWallSupport.Build_HyperTubeWallSupport_C`](#77897d56578a11014d334ffb4d867e85)
        - `IndustrialFluidContainer`
          - [`Build_IndustrialTank.Build_IndustrialTank_C`](#152fe74c629323e7116bee97ebc4de28)
        - `JumpPad`
          - [`Build_JumpPadAdjustable.Build_JumpPadAdjustable_C`](#d1dc39666c1e82c0d5602eba04f7521c)
        - `LandingPad`
          - [`Build_LandingPad.Build_LandingPad_C`](#cc1ce63b01f4083689f8d3db12f3be45)
        - `LightsControlPanel`
          - [`Build_LightsControlPanel.Build_LightsControlPanel_C`](#7bd78bd8de5d479fe5b2d68ce8246c34)
        - `LookoutTower`
          - [`Build_LookoutTower.Build_LookoutTower_C`](#6679c07cc22b24c8e99ed031fc9ef3d3)
        - `Mam`
          - [`Build_Mam.Build_Mam_C`](#2b81e3de4628d3227164445ecadd186e)
        - `ManufacturerMk1`
          - [`Build_ManufacturerMk1.Build_ManufacturerMk1_C`](#883398a30bcbcf900abac8d668963041)
        - `OilRefinery`
          - [`Build_OilRefinery.Build_OilRefinery_C`](#5dfb84185338e0b36a56667cabb4e6c6)
        - `Packager`
          - [`Build_Packager.Build_Packager_C`](#2e4ed689d331e86b79009f5b0c344d15)
        - `PipeHyperJunction`
          - [`Build_HyperTubeJunction.Build_HyperTubeJunction_C`](#8de6669d73d61ccc61eff7e7e5a240f9)
        - `PipeHyperStart`
          - [`Build_PipeHyperStart.Build_PipeHyperStart_C`](#7668c9184f85e9effc5abeb07938c7b9)
        - `PipeHyperSupport`
          - [`Build_PipeHyperSupport.Build_PipeHyperSupport_C`](#d594712721af9a8f0f32f5989d7acacb)
        - `PipeHyperTJunction`
          - [`Build_HypertubeTJunction.Build_HypertubeTJunction_C`](#1251f7f99dd9b313c5c319a7237a9e70)
        - `PipeHyper`
          - [`Build_PipeHyper.Build_PipeHyper_C`](#fe25175d65aa5ef9a67cfd72311a54f3)
        - `PipeJunction`
          - [`Build_PipelineJunction_Cross.Build_PipelineJunction_Cross_C`](#d3a1f4e5346657c7a370db189fa6639b)
        - `PipePumpMk2`
          - [`Build_PipelinePumpMK2.Build_PipelinePumpMk2_C`](#d4cc6d973a4cb9e7d6e9dccf5ad77d0f)
        - `PipePump`
          - [`Build_PipelinePump.Build_PipelinePump_C`](#8e66af14a278783bfc925a8c4438b4c9)
        - `PipeValve`
          - [`Build_Valve.Build_Valve_C`](#f871ebc0fd0aff0df7df0cdca9bce38b)
        - `PipelineMk2`
          - [`Build_PipelineMK2.Build_PipelineMK2_C`](#fd4e2eee24bd6581c74dabf8b5a5b827)
          - [`Build_PipelineMK2_NoIndicator.Build_PipelineMK2_NoIndicator_C`](#906b7894316e76793ae494b9c150a364)
        - `PipelineSupportWallHole`
          - [`Build_PipelineSupportWallHole.Build_PipelineSupportWallHole_C`](#317d9d7ecea81d77ab066492db93cdf3)
        - `PipelineSupportWall`
          - [`Build_PipelineSupportWall.Build_PipelineSupportWall_C`](#0b581b8298bdffe861f0f823c44dc4b2)
        - `PipelineSupport`
          - [`Build_HyperPoleStackable.Build_HyperPoleStackable_C`](#9fabe111295dc0176ab3dce2791bf4ad)
          - [`Build_PipeSupportStackable.Build_PipeSupportStackable_C`](#71c01c8db12200fee4a30ec17fa0c69c)
          - [`Build_PipelineSupport.Build_PipelineSupport_C`](#bff7c31118017beb253860c4318180e1)
        - `Pipeline`
          - [`Build_Pipeline.Build_Pipeline_C`](#109c5b7382c0b125962d3b0b0b25a649)
          - [`Build_Pipeline_NoIndicator.Build_Pipeline_NoIndicator_C`](#c90bebba6ea367f02157102940522456)
          - `FlowIndicator`
            - [`Build_PipelineFlowIndicator.Build_PipelineFlowIndicator_C`](#e30d99eeeccec8e638ce88d55dc29fcb)
        - `Portal`
          - [`Build_Portal.Build_Portal_C`](#76a3559a86332108d8d2a5a8d61d6138)
          - [`Build_PortalSatellite.Build_PortalSatellite_C`](#1a3ac5f3961aa7bf322a6016a0649880)
        - `PowerLine`
          - [`Build_PowerLine.Build_PowerLine_C`](#c2a1666d2d32223655c85a0eab946082)
        - `PowerPoleMk1`
          - [`Build_PowerPoleMk1.Build_PowerPoleMk1_C`](#a5031bd2cf9fb62fc171eef0c4f3b515)
        - `PowerPoleMk2`
          - [`Build_PowerPoleMk2.Build_PowerPoleMk2_C`](#644cea3e20cc4329125507e5c30bb9d0)
        - `PowerPoleMk3`
          - [`Build_PowerPoleMk3.Build_PowerPoleMk3_C`](#1358d70fc43a8f27545c109daeffeceb)
        - `PowerPoleWallDouble`
          - [`Build_PowerPoleWallDouble.Build_PowerPoleWallDouble_C`](#8759597f2c890362d3e49fe25c4c1954)
          - [`Build_PowerPoleWallDouble_Mk2.Build_PowerPoleWallDouble_Mk2_C`](#4a8d6bd7f9b8c120a05dca591f5ea856)
          - [`Build_PowerPoleWallDouble_Mk3.Build_PowerPoleWallDouble_Mk3_C`](#cddf9902f0b4f64c0c7bd3bdc67d934c)
        - `PowerPoleWall`
          - [`Build_PowerPoleWall.Build_PowerPoleWall_C`](#e038a60b251b04817890828ef9245905)
          - [`Build_PowerPoleWall_Mk2.Build_PowerPoleWall_Mk2_C`](#77873dd9650014322d2fc2585297f98e)
          - [`Build_PowerPoleWall_Mk3.Build_PowerPoleWall_Mk3_C`](#c0006ed6b8fcb8c85c6088a3ea732849)
        - `PowerStorage`
          - [`Build_PowerStorageMk1.Build_PowerStorageMk1_C`](#0b15e2ccf1031db98165684c6d099f8a)
        - `PowerSwitch`
          - [`Build_PowerSwitch.Build_PowerSwitch_C`](#cb765739a0a1248c85bcc7c1739feb05)
        - `PriorityPowerSwitch`
          - [`Build_PriorityPowerSwitch.Build_PriorityPowerSwitch_C`](#488f69fa669c9a8c4edb3110431eba80)
        - `ProjectAssembly`
          - [`BP_ProjectAssembly.BP_ProjectAssembly_C`](#cc4062b65145df45b4793975e557d60f)
        - `QuantumEncoder`
          - [`Build_QuantumEncoder.Build_QuantumEncoder_C`](#5f162d7bcf5c10c42e0c336279fcee88)
        - `RadarTower`
          - [`Build_RadarTower.Build_RadarTower_C`](#efe487d8b652f31ffde5ac24f3df4072)
        - `ResourceSinkShop`
          - [`Build_ResourceSinkShop.Build_ResourceSinkShop_C`](#908e3d0ac3690935d2a512816df6aee1)
        - `ResourceSink`
          - [`Build_ResourceSink.Build_ResourceSink_C`](#ed25d32dadab59d85e4b83b81eaf626a)
        - `SignDigital`
          - [`Build_StandaloneWidgetSign_Huge.Build_StandaloneWidgetSign_Huge_C`](#23314fb3e9c56849282f3ee2ac5e3a86)
          - [`Build_StandaloneWidgetSign_Large.Build_StandaloneWidgetSign_Large_C`](#c85c77bf6e316aa7e76e358fec7a9298)
          - [`Build_StandaloneWidgetSign_Medium.Build_StandaloneWidgetSign_Medium_C`](#d153e92dbe82600a014df8c3d25dd381)
          - [`Build_StandaloneWidgetSign_Portrait.Build_StandaloneWidgetSign_Portrait_C`](#66f52e1ae3a6e6f73fd9ecbfa3b2aad6)
          - [`Build_StandaloneWidgetSign_Small.Build_StandaloneWidgetSign_Small_C`](#6ddb57e8d88ddbaa9833d59a939ec104)
          - [`Build_StandaloneWidgetSign_SmallVeryWide.Build_StandaloneWidgetSign_SmallVeryWide_C`](#ac4b3ff90be8ecb177b8ad985d0ab058)
          - [`Build_StandaloneWidgetSign_SmallWide.Build_StandaloneWidgetSign_SmallWide_C`](#533579ef1d8a896b76e522419d605797)
          - [`Build_StandaloneWidgetSign_Square.Build_StandaloneWidgetSign_Square_C`](#dd188ab826c74a9a65ea420b62f03fb9)
          - [`Build_StandaloneWidgetSign_Square_Small.Build_StandaloneWidgetSign_Square_Small_C`](#a9f633f9fce31bec9f498740d149d1e2)
          - [`Build_StandaloneWidgetSign_Square_Tiny.Build_StandaloneWidgetSign_Square_Tiny_C`](#6d3ad2fea313ad0be49ecfbd96a9451b)
        - `SmelterMk1`
          - [`Build_SmelterMk1.Build_SmelterMk1_C`](#33db324bf55726bcb98eff151bbd5ca3)
        - `SpaceElevator`
          - [`Build_SpaceElevator.Build_SpaceElevator_C`](#208b4ade215d9617b57e57ad85ef7217)
        - `StorageContainerMk1`
          - [`Build_StorageContainerMk1.Build_StorageContainerMk1_C`](#c2dd81c7c3bbc4a8a2523eeefb449598)
        - `StorageContainerMk2`
          - [`Build_StorageContainerMk2.Build_StorageContainerMk2_C`](#4c79059a1fe6c1d19b4d40f7a7e16d8b)
        - `StoragePlayer`
          - [`Build_StorageBlueprint.Build_StorageBlueprint_C`](#c37d05dec915a36424fea249e7253738)
          - [`Build_StorageHazard.Build_StorageHazard_C`](#c01059d0cd4b969a34e20dbd3fa694c0)
          - [`Build_StorageIntegrated.Build_StorageIntegrated_C`](#677abe355cdd75e08b678b56fe7da471)
          - [`Build_StorageMedkit.Build_StorageMedkit_C`](#dc60c10512e37bd077771adc69ac847a)
          - [`Build_StoragePlayer.Build_StoragePlayer_C`](#0ad0ed2f1bee8c38a078f11e25633a8a)
        - `StorageTank`
          - [`Build_PipeStorageTank.Build_PipeStorageTank_C`](#fddab7360d0f275272c3d113a75f6543)
        - `StreetLight`
          - [`Build_StreetLight.Build_StreetLight_C`](#8d9c39ef7aabaa4b7b795864720336b3)
        - `TradingPost`
          - [`Build_TradingPost.Build_TradingPost_C`](#19668bc57e13646a04a8a8d6de23298c)
          - `InteractableProps`
            - [`BP_SoundTrigger.BP_SoundTrigger_C`](#df2a4cc05cd0d297e89772c55ee52205)
        - `Train`
          - `EndStop`
            - [`Build_RailroadEndStop.Build_RailroadEndStop_C`](#4adebf471a640cc10382dbf226cf3090)
          - `Signal`
            - [`Build_RailroadBlockSignal.Build_RailroadBlockSignal_C`](#f707a0a5581fb51736063d722bd982e4)
            - [`Build_RailroadPathSignal.Build_RailroadPathSignal_C`](#d3516d320f4415d89642a765d7eee0d6)
          - `Station`
            - [`Build_TrainDockingStation.Build_TrainDockingStation_C`](#7e601c8a33a08a309066beb79f9c87a7)
            - [`Build_TrainDockingStationLiquid.Build_TrainDockingStationLiquid_C`](#155ddcf2d849faee338d172ccffc72a3)
            - [`Build_TrainPlatformEmpty.Build_TrainPlatformEmpty_C`](#b3cc270386e4acc3c302a9006358151f)
            - [`Build_TrainStation.Build_TrainStation_C`](#715eacd08a801948677f99f58ca217ad)
          - `Track`
            - [`Build_RailroadTrack.Build_RailroadTrack_C`](#41c917e27fd4b56671378d7a1609b58d)
            - [`Build_RailroadTrackIntegrated.Build_RailroadTrackIntegrated_C`](#7aa7f132090295acb828360d9127599f)
        - `TruckStation`
          - [`Build_TruckStation.Build_TruckStation_C`](#07403e7c3e8776633bdb2052f6574dca)
        - `WorkBench`
          - [`Build_WorkBench.Build_WorkBench_C`](#f1be50a7d5aeb233f104df44fa857637)
          - [`Build_WorkBenchIntegrated.Build_WorkBenchIntegrated_C`](#722a3658f102dbde79c294836a2e9561)
      - `Vehicle`
        - `Explorer`
          - [`BP_Explorer.BP_Explorer_C`](#79bc5407522d56f154bd23a04e1adc75)
        - `Tractor`
          - [`BP_Tractor.BP_Tractor_C`](#8c7b54f82eb3deb4b0ff27bebba451ec)
        - `Truck`
          - [`BP_Truck.BP_Truck_C`](#203ec0cccdaa63eb364b6bfaf36affcf)
    - `Character`
      - `Creature`
        - [`BP_CreatureSpawner.BP_CreatureSpawner_C`](#300f34b684b8e9e734a8d1aca74e0b2a)
        - `Enemy`
          - `Hog`
            - [`Char_Hog.Char_Hog_C`](#51acaa1a61f4b8251eed733a9894a132)
        - `Wildlife`
          - `SpaceGiraffe`
            - [`Char_SpaceGiraffe.Char_SpaceGiraffe_C`](#53cad3725573653ef10d1547482a2543)
      - `Player`
        - [`BP_PlayerState.BP_PlayerState_C`](#4c001bfe67d1ec5cacd2a1a2c3539513)
        - [`Char_Player.Char_Player_C`](#d9af50be26eb7b8c38428115c2ede530)
    - `Equipment`
      - `BuildGun`
        - [`BP_BuildGun.BP_BuildGun_C`](#4eb723956348782d5f77699315e4795c)
      - `ResourceCollector`
        - [`Equip_ResourceMiner.Equip_ResourceMiner_C`](#9c74b4b939b914a754c6692ca1e64bbe)
      - `ResourceScanner`
        - [`BP_ResourceScanner.BP_ResourceScanner_C`](#8025b0306acb30fa3f366289a8ccc332)
    - `Events`
      - [`BP_EventSubsystem.BP_EventSubsystem_C`](#2324d8c38645407dd6280beaf853fe75)
    - `Prototype`
      - `WAT`
        - [`BP_MercerShrine.BP_MercerShrine_C`](#f56ac338ad96fda0ea5358d45906285c)
        - [`BP_WAT1.BP_WAT1_C`](#fc650aeefc9b2d9add738477f1c1dedb)
        - [`BP_WAT2.BP_WAT2_C`](#2be6bc2bcc466a9dad93108133c782e5)
    - `Recipes`
      - `Research`
        - [`BP_ResearchManager.BP_ResearchManager_C`](#39005cdae90dca3f7dbac301ffd81880)
    - `Resource`
      - [`BP_FrackingCore.BP_FrackingCore_C`](#f0c4658a642d72081e990ab202de1a0a)
      - [`BP_FrackingSatellite.BP_FrackingSatellite_C`](#484c1834a208912553a8795c06958b7e)
      - [`BP_ResourceDeposit.BP_ResourceDeposit_C`](#2e9e09aede2ddcb19b0aed4814af2975)
      - [`BP_ResourceNode.BP_ResourceNode_C`](#85705afaffabf7c452f00c7a8a1bc7b1)
      - [`BP_ResourceNodeGeyser.BP_ResourceNodeGeyser_C`](#4fd37a57430ae43c28aef92e846e0e21)
      - `Environment`
        - `Crystal`
          - [`BP_Crystal.BP_Crystal_C`](#3f8e1a0e2d75508910d3faf8114ebf15)
          - [`BP_Crystal_mk2.BP_Crystal_mk2_C`](#fea2688b4d8184a6a1e67ec0794e2e35)
          - [`BP_Crystal_mk3.BP_Crystal_mk3_C`](#c04498d4c31a5f47f701f54b62db4573)
    - `Schematics`
      - `Progression`
        - [`BP_GamePhaseManager.BP_GamePhaseManager_C`](#54ac3280549cdec7b427904fd9493639)
        - [`BP_SchematicManager.BP_SchematicManager_C`](#5ae82c5bafc766e5d6fab05c260e93bc)
    - `Testing`
      - `BoomBox`
        - [`BP_TapePickup.BP_TapePickup_C`](#dbc58698f92e7898634e7cdd4c2490f8)
    - `Unlocks`
      - [`BP_UnlockSubsystem.BP_UnlockSubsystem_C`](#7616bd73471496c34969d54c9785569a)
    - `VFX`
      - `World`
        - `GasPerimeter`
          - [`BP_VolumeGas_01.BP_VolumeGas_01_C`](#3a1ebf198e2c9696dff386e541565ed1)
    - `World`
      - `Benefit`
        - `BerryBush`
          - [`BP_BerryBush.BP_BerryBush_C`](#52d78c8a5385711021f658e93dcf085d)
        - `DropPod`
          - [`BP_CrashSiteDebris.BP_CrashSiteDebris_C`](#c8cec8e92b0af4f0c7e45961beb0bb65)
          - [`BP_DebrisActor_02.BP_DebrisActor_02_C`](#db52f3627f7fd0f329e3b03f4e6d1fab)
          - [`BP_DebrisActor_03.BP_DebrisActor_03_C`](#a10b22cbb2752f86c6f3fe6fc94ad383)
          - [`BP_DropPod.BP_DropPod_C`](#d474aff3696e9477a9365db146b59e48)
          - [`BP_Ship.BP_Ship_C`](#f1b5efcdf724c21cde7f9f2edc448e93)
        - `Mushroom`
          - [`BP_Shroom_01.BP_Shroom_01_C`](#458e1ed7ce81f7dda8d8a08f1548eac6)
        - `NutBush`
          - [`BP_NutBush.BP_NutBush_C`](#9326b718458ece68e08f4fdc018366fa)
      - `Hazard`
        - `SporeCloudPlant`
          - [`BP_SporeFlower.BP_SporeFlower_C`](#ad7462f0dfad0974a8518ce1dfd63ffb)
- `Script`
  - [`FactoryGame.FGCentralStorageSubsystem`](#9443a65a4ea801981f18290aac226aed)
  - [`FactoryGame.FGConveyorChainActor`](#9cd04441c0a87b984b69e6b76bc66a75)
  - [`FactoryGame.FGDockingStationInfo`](#295f1939601ed02e105faf2782f151fe)
  - [`FactoryGame.FGEmoteShortcut`](#0aa5edf3df6f2117ad44b4c510097223)
  - [`FactoryGame.FGFactoryConnectionComponent`](#a8e0e526befbb4d556fb2cc9cfdf8db0)
  - [`FactoryGame.FGFactoryLegsComponent`](#d97c885e8421a25037fd6c412f67a9cb)
  - [`FactoryGame.FGFoliageRemovalSubsystem`](#fa364343535e98f255fc3be4e8df837d)
  - [`FactoryGame.FGGameRulesSubsystem`](#dd00101ae2edc3e9ba4e5830953ae581)
  - [`FactoryGame.FGHealthComponent`](#d2ef6ea371a1ccbed102d21ee1cffc01)
  - [`FactoryGame.FGHighlightedMarker_MapMarker`](#1d93764e1b0b912afba78502d3c9d4bb)
  - [`FactoryGame.FGInventoryComponentEquipment`](#c4235f10d403f57878a78675a193aa63)
  - [`FactoryGame.FGInventoryComponentTrash`](#8436ded31224c2aa2112a1e1a2bb0fa9)
  - [`FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)
  - [`FactoryGame.FGItemPickup_Spawnable`](#0c638488b1f184fc2e968ea6863c527e)
  - [`FactoryGame.FGLightweightBuildableSubsystem`](#50a1e40987137f4ddcd5332470429f28)
  - [`FactoryGame.FGMapManager`](#9369a5ae02682133632dfcf4d28534b3)
  - [`FactoryGame.FGPipeConnectionComponentHyper`](#a7fec9e0f15489bb873fe11129880d28)
  - [`FactoryGame.FGPipeConnectionComponent`](#55a9b1f07fd285508cbcb6f397f29af5)
  - [`FactoryGame.FGPipeConnectionFactory`](#e0cccef0faa5d243b6568aed256337be)
  - [`FactoryGame.FGPipeNetwork`](#020fef76c2da6dc5cfd4bc301f34fe58)
  - [`FactoryGame.FGPipeSubsystem`](#af9cc6d6afbb8640b1567cf751c8d8a5)
  - [`FactoryGame.FGPlayerHotbar`](#0b7c1c7032b9ea87265ea8ba1481bdef)
  - [`FactoryGame.FGPowerCircuit`](#0ddb98cf34a68ae1903a1010f5c0a8e6)
  - [`FactoryGame.FGPowerConnectionComponent`](#31b818765a0cf23f5e6dc6a408ea2768)
  - [`FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)
  - [`FactoryGame.FGRailroadTrackConnectionComponent`](#2c45b43d762f093a3665015ef7da7485)
  - [`FactoryGame.FGRecipeManager`](#2da486937abc3945f1f9a859ffe5e7da)
  - [`FactoryGame.FGRecipeShortcut`](#01726ecec9cdf6f0ac6c7a38761ed930)
  - [`FactoryGame.FGResourceSinkSubsystem`](#38a6e187c8a33cf7490018758ffc4cb4)
  - [`FactoryGame.FGScannableSubsystem`](#7dcc6ff932e920e66f5fe3a3ea157a4d)
  - [`FactoryGame.FGShoppingListComponent`](#69b9138f542b129c542963d4e4c41bcd)
  - [`FactoryGame.FGStatisticsSubsystem`](#0501d307ebfb9395f55084e661d0e783)
  - [`FactoryGame.FGTrainPlatformConnection`](#d15f5884c4957920d0f9928fbed83352)
  - [`FactoryGame.FGTrainStationIdentifier`](#a9689d2fb8c219f08fcf8629a50137db)
  - [`FactoryGame.FGWheeledVehicleInfo`](#c3453bc41814a7ab61761d4d0df33783)
  - [`FactoryGame.FGWorldSettings`](#6186464d789eabc6d83d97b9b8c0e62d)

## `/Game/FactoryGame/Character/Creature/BP_CreatureSpawner.BP_CreatureSpawner_C` <a id="300f34b684b8e9e734a8d1aca74e0b2a"></a>

**Component type** `ACTOR`

## Properties

| Name              | Type                           |
| ----------------- | ------------------------------ |
| mSpawnData        | `Array`<`Struct`<`SpawnData`>> |
| mCachedIsNearBase | `Bool`                         |

## `/Game/FactoryGame/Prototype/WAT/BP_MercerShrine.BP_MercerShrine_C` <a id="f56ac338ad96fda0ea5358d45906285c"></a>

**Component type** `ACTOR`

## `/Game/FactoryGame/World/Benefit/BerryBush/BP_BerryBush.BP_BerryBush_C` <a id="52d78c8a5385711021f658e93dcf085d"></a>

**Component type** `ACTOR`

## Properties

| Name           | Type                                                  |
| -------------- | ----------------------------------------------------- |
| mBerryIndex    | `Int`                                                 |
| mPickupItems   | [`InventoryStack`](#4bbe9209e8486bf4b08ef002709eeeee) |
| mSavedNumItems | `Int`                                                 |

## `/Game/FactoryGame/Prototype/WAT/BP_WAT2.BP_WAT2_C` <a id="2be6bc2bcc466a9dad93108133c782e5"></a>

**Component type** `ACTOR`

## `/Game/FactoryGame/Resource/Environment/Crystal/BP_Crystal.BP_Crystal_C` <a id="3f8e1a0e2d75508910d3faf8114ebf15"></a>

**Component type** `ACTOR`

## `/Game/FactoryGame/World/Benefit/NutBush/BP_NutBush.BP_NutBush_C` <a id="9326b718458ece68e08f4fdc018366fa"></a>

**Component type** `ACTOR`

## Properties

| Name           | Type  |
| -------------- | ----- |
| mSavedNumItems | `Int` |

## `/Game/FactoryGame/Resource/Environment/Crystal/BP_Crystal_mk2.BP_Crystal_mk2_C` <a id="fea2688b4d8184a6a1e67ec0794e2e35"></a>

**Component type** `ACTOR`

## `/Game/FactoryGame/VFX/World/GasPerimeter/BP_VolumeGas_01.BP_VolumeGas_01_C` <a id="3a1ebf198e2c9696dff386e541565ed1"></a>

**Component type** `ACTOR`

## `/Game/FactoryGame/World/Hazard/SporeCloudPlant/BP_SporeFlower.BP_SporeFlower_C` <a id="ad7462f0dfad0974a8518ce1dfd63ffb"></a>

**Component type** `ACTOR`

## `/Game/FactoryGame/World/Benefit/Mushroom/BP_Shroom_01.BP_Shroom_01_C` <a id="458e1ed7ce81f7dda8d8a08f1548eac6"></a>

**Component type** `ACTOR`

## `/Game/FactoryGame/Resource/Environment/Crystal/BP_Crystal_mk3.BP_Crystal_mk3_C` <a id="c04498d4c31a5f47f701f54b62db4573"></a>

**Component type** `ACTOR`

## `/Game/FactoryGame/Prototype/WAT/BP_WAT1.BP_WAT1_C` <a id="fc650aeefc9b2d9add738477f1c1dedb"></a>

**Component type** `ACTOR`

## `/Game/FactoryGame/Resource/BP_ResourceDeposit.BP_ResourceDeposit_C` <a id="2e9e09aede2ddcb19b0aed4814af2975"></a>

**Component type** `ACTOR`

## Properties

| Name                       | Type  |
| -------------------------- | ----- |
| mResourceDepositTableIndex | `Int` |
| mMineAmount                | `Int` |
| mResourcesLeft             | `Int` |

## `/Game/FactoryGame/Buildable/Factory/TradingPost/InteractableProps/BP_SoundTrigger.BP_SoundTrigger_C` <a id="df2a4cc05cd0d297e89772c55ee52205"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |

## `/Script/FactoryGame.FGItemPickup_Spawnable` <a id="0c638488b1f184fc2e968ea6863c527e"></a>

**Component type** `ACTOR`

## Properties

| Name         | Type                                                  |
| ------------ | ----------------------------------------------------- |
| mPickupItems | [`InventoryStack`](#4bbe9209e8486bf4b08ef002709eeeee) |

## `/Game/FactoryGame/World/Benefit/DropPod/BP_DebrisActor_02.BP_DebrisActor_02_C` <a id="db52f3627f7fd0f329e3b03f4e6d1fab"></a>

**Component type** `ACTOR`

## Properties

| Name                   | Type  |
| ---------------------- | ----- |
| mDismantleRefundsIndex | `Int` |

## `/Game/FactoryGame/World/Benefit/DropPod/BP_CrashSiteDebris.BP_CrashSiteDebris_C` <a id="c8cec8e92b0af4f0c7e45961beb0bb65"></a>

**Component type** `ACTOR`

## Properties

| Name                   | Type  |
| ---------------------- | ----- |
| mDismantleRefundsIndex | `Int` |

## `/Game/FactoryGame/World/Benefit/DropPod/BP_DebrisActor_03.BP_DebrisActor_03_C` <a id="a10b22cbb2752f86c6f3fe6fc94ad383"></a>

**Component type** `ACTOR`

## Properties

| Name                   | Type  |
| ---------------------- | ----- |
| mDismantleRefundsIndex | `Int` |

## `/Game/FactoryGame/World/Benefit/DropPod/BP_Ship.BP_Ship_C` <a id="f1b5efcdf724c21cde7f9f2edc448e93"></a>

**Component type** `ACTOR`

## Properties

| Name                   | Type  |
| ---------------------- | ----- |
| mDismantleRefundsIndex | `Int` |

## `/Game/FactoryGame/World/Benefit/DropPod/BP_DropPod.BP_DropPod_C` <a id="d474aff3696e9477a9365db146b59e48"></a>

**Component type** `ACTOR`

## Properties

| Name                   | Type  |
| ---------------------- | ----- |
| mDismantleRefundsIndex | `Int` |

## `/Script/FactoryGame.FGPowerConnectionComponent` <a id="31b818765a0cf23f5e6dc6a408ea2768"></a>

**Component type** `COMPONENT`

## Properties

| Name               | Type                                                                                                                                               |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| mHiddenConnections | `Array`<`Struct`<`Union`<[`/Script/FactoryGame.FGPowerConnectionComponent`](#31b818765a0cf23f5e6dc6a408ea2768)>>>                                  |
| mWires             | `Array`<`Struct`<`Union`<[`/Game/FactoryGame/Buildable/Factory/PowerLine/Build_PowerLine.Build_PowerLine_C`](#c2a1666d2d32223655c85a0eab946082)>>> |

## `/Script/FactoryGame.FGPowerInfoComponent` <a id="3e8784c9adfe12165c1b84b89f26722e"></a>

**Component type** `COMPONENT`

## Properties

| Name               | Type    |
| ------------------ | ------- |
| mTargetConsumption | `Float` |
| mIsFullBlast       | `Bool`  |

## `/Script/FactoryGame.FGInventoryComponent` <a id="53d1ef1c40a8b7ebe5a1830ebf2cac40"></a>

**Component type** `COMPONENT`

## Properties

| Name                    | Type                                 |
| ----------------------- | ------------------------------------ |
| mAdjustedSizeDiff       | `Int`                                |
| mInventoryStacks        | `Array`<`Struct`<`InventoryStack`>>  |
| mArbitrarySlotSizes     | `Array`<`IntProperty`>               |
| mAllowedItemDescriptors | `Array`<`Struct`<`ObjectReference`>> |

## `/Script/FactoryGame.FGWorldSettings` <a id="6186464d789eabc6d83d97b9b8c0e62d"></a>

**Component type** `ACTOR`

## Properties

| Name                           | Type                                                                                                                                        |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| mBuildableSubsystem            | `ObjectReference`<[`/Game/FactoryGame/-Shared/Blueprint/BP_BuildableSubsystem.BP_BuildableSubsystem_C`](#13be4d096a7057b1aed35a375538ac51)> |
| mLightweightBuildableSubsystem | `ObjectReference`<[`/Script/FactoryGame.FGLightweightBuildableSubsystem`](#50a1e40987137f4ddcd5332470429f28)>                               |

## `/Script/FactoryGame.FGFoliageRemovalSubsystem` <a id="fa364343535e98f255fc3be4e8df837d"></a>

**Component type** `ACTOR`

## Properties

| Name                  | Type     |
| --------------------- | -------- |
| mSavedFoliageGridSize | `UInt32` |

## `/Game/FactoryGame/-Shared/Blueprint/BP_GameMode.BP_GameMode_C` <a id="15932108758848e1468c1d60992f7b10"></a>

**Component type** `ACTOR`

## Properties

| Name                  | Type           |
| --------------------- | -------------- |
| mSaveSessionName      | `Str`          |
| mLastAutoSaveId       | `Byte`         |
| mStartingPointTagName | `NameProperty` |

## `/Game/FactoryGame/-Shared/Blueprint/BP_BuildableSubsystem.BP_BuildableSubsystem_C` <a id="13be4d096a7057b1aed35a375538ac51"></a>

**Component type** `ACTOR`

## Properties

| Name             | Type                                               |
| ---------------- | -------------------------------------------------- |
| mColorSlots_Data | `Array`<`Struct`<`FactoryCustomizationColorSlot`>> |

## `/Script/FactoryGame.FGLightweightBuildableSubsystem` <a id="50a1e40987137f4ddcd5332470429f28"></a>

**Component type** `ACTOR`

## `/Script/FactoryGame.FGPipeNetwork` <a id="020fef76c2da6dc5cfd4bc301f34fe58"></a>

**Component type** `ACTOR`

## Properties

| Name                            | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| mFluidIntegrantScriptInterfaces | `Union`<`Array`<`Struct`<`Union`<[`/Game/FactoryGame/Buildable/Factory/Pipeline/Build_Pipeline_NoIndicator.Build_Pipeline_NoIndicator_C`](#c90bebba6ea367f02157102940522456)>>>, `Array`<`Struct`<`Union`<[`/Game/FactoryGame/Buildable/Factory/Pipeline/Build_Pipeline.Build_Pipeline_C`](#109c5b7382c0b125962d3b0b0b25a649)>>>, `Array`<`Struct`<`Union`<[`/Game/FactoryGame/Buildable/Factory/PipelineMk2/Build_PipelineMK2_NoIndicator.Build_PipelineMK2_NoIndicator_C`](#906b7894316e76793ae494b9c150a364)>>>, `Array`<`Struct`<`Union`<[`/Game/FactoryGame/Buildable/Factory/PipelineMk2/Build_PipelineMK2.Build_PipelineMK2_C`](#fd4e2eee24bd6581c74dabf8b5a5b827)>>>, `Array`<`Struct`<`Union`<`/Game/FactoryGame/Buildable/Factory/PipelineMk2/Build_PipelineMK2_NoIndicator.Build_PipelineMK2_NoIndicator_C`, `/Game/FactoryGame/Buildable/Factory/PipePump/Build_PipelinePump.Build_PipelinePump_C`, `/Game/FactoryGame/Buildable/Factory/PipeJunction/Build_PipelineJunction_Cross.Build_PipelineJunction_Cross_C`>>>, `Array`<`Struct`<`Union`<`/Game/FactoryGame/Buildable/Factory/PipelineMk2/Build_PipelineMK2_NoIndicator.Build_PipelineMK2_NoIndicator_C`, `/Game/FactoryGame/Buildable/Factory/PipePumpMk2/Build_PipelinePumpMK2.Build_PipelinePumpMk2_C`, `/Game/FactoryGame/Buildable/Factory/PipeValve/Build_Valve.Build_Valve_C`>>>, `Array`<`Struct`<`Union`<[`/Game/FactoryGame/Buildable/Factory/StorageTank/Build_PipeStorageTank.Build_PipeStorageTank_C`](#fddab7360d0f275272c3d113a75f6543)>>>, `Array`<`Struct`<`Union`<[`/Game/FactoryGame/Buildable/Factory/IndustrialFluidContainer/Build_IndustrialTank.Build_IndustrialTank_C`](#152fe74c629323e7116bee97ebc4de28)>>>> |
| mPipeNetworkID                  | `Int`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

## `/Game/FactoryGame/Resource/BP_ResourceNode.BP_ResourceNode_C` <a id="85705afaffabf7c452f00c7a8a1bc7b1"></a>

**Component type** `ACTOR`

## Properties

| Name           | Type  |
| -------------- | ----- |
| mResourcesLeft | `Int` |

## `/Game/FactoryGame/Resource/BP_FrackingSatellite.BP_FrackingSatellite_C` <a id="484c1834a208912553a8795c06958b7e"></a>

**Component type** `ACTOR`

## `/Game/FactoryGame/Resource/BP_FrackingCore.BP_FrackingCore_C` <a id="f0c4658a642d72081e990ab202de1a0a"></a>

**Component type** `ACTOR`

## `/Game/FactoryGame/Testing/BoomBox/BP_TapePickup.BP_TapePickup_C` <a id="dbc58698f92e7898634e7cdd4c2490f8"></a>

**Component type** `ACTOR`

## Properties

| Name         | Type                            |
| ------------ | ------------------------------- |
| mPickupState | `Enum`<`ESchematicPickupState`> |

## `/Game/FactoryGame/Resource/BP_ResourceNodeGeyser.BP_ResourceNodeGeyser_C` <a id="4fd37a57430ae43c28aef92e846e0e21"></a>

**Component type** `ACTOR`

## `/Game/FactoryGame/-Shared/Blueprint/BP_TimeOfDaySubsystem.BP_TimeOfDaySubsystem_C` <a id="a81f6dd298205076513984f2e0d1b6d1"></a>

**Component type** `ACTOR`

## Properties

| Name                        | Type    |
| --------------------------- | ------- |
| mDaySeconds                 | `Float` |
| mNumberOfPassedDays         | `Int`   |
| mNumberOfDaysSinceLastDeath | `Int`   |

## `/Game/FactoryGame/-Shared/Blueprint/BP_GameState.BP_GameState_C` <a id="30d5aa37fc70663fddf7a1a1aca6322d"></a>

**Component type** `ACTOR`

## Properties

| Name                                | Type                                                                                                                                                  |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| mStorySubsystem                     | `ObjectReference`<[`/Game/FactoryGame/-Shared/Blueprint/BP_StorySubsystem.BP_StorySubsystem_C`](#5e177cf5245a24317739aaa231d427d4)>                   |
| mRailroadSubsystem                  | `ObjectReference`<[`/Game/FactoryGame/-Shared/Blueprint/BP_RailroadSubsystem.BP_RailroadSubsystem_C`](#2efb094ad027c82de6fdd502a08ce2c1)>             |
| mCircuitSubsystem                   | `ObjectReference`<[`/Game/FactoryGame/-Shared/Blueprint/BP_CircuitSubsystem.BP_CircuitSubsystem_C`](#9a50aeea42a31706787ab070eebcec65)>               |
| mRecipeManager                      | `ObjectReference`<[`/Script/FactoryGame.FGRecipeManager`](#2da486937abc3945f1f9a859ffe5e7da)>                                                         |
| mSchematicManager                   | `ObjectReference`<[`/Game/FactoryGame/Schematics/Progression/BP_SchematicManager.BP_SchematicManager_C`](#5ae82c5bafc766e5d6fab05c260e93bc)>          |
| mGamePhaseManager                   | `ObjectReference`<[`/Game/FactoryGame/Schematics/Progression/BP_GamePhaseManager.BP_GamePhaseManager_C`](#54ac3280549cdec7b427904fd9493639)>          |
| mResearchManager                    | `ObjectReference`<[`/Game/FactoryGame/Recipes/Research/BP_ResearchManager.BP_ResearchManager_C`](#39005cdae90dca3f7dbac301ffd81880)>                  |
| mTutorialIntroManager               | `ObjectReference`<[`/Game/FactoryGame/-Shared/Blueprint/BP_TutorialIntroManager.BP_TutorialIntroManager_C`](#d75dafa7313eb5eb3dfbc6e7f91fd354)>       |
| mActorRepresentationManager         | `ObjectReference`                                                                                                                                     |
| mMapManager                         | `ObjectReference`<[`/Script/FactoryGame.FGMapManager`](#9369a5ae02682133632dfcf4d28534b3)>                                                            |
| mCentralStorageSubsystem            | `ObjectReference`<[`/Script/FactoryGame.FGCentralStorageSubsystem`](#9443a65a4ea801981f18290aac226aed)>                                               |
| mPipeSubsystem                      | `ObjectReference`<[`/Script/FactoryGame.FGPipeSubsystem`](#af9cc6d6afbb8640b1567cf751c8d8a5)>                                                         |
| mUnlockSubsystem                    | `ObjectReference`<[`/Game/FactoryGame/Unlocks/BP_UnlockSubsystem.BP_UnlockSubsystem_C`](#7616bd73471496c34969d54c9785569a)>                           |
| mResourceSinkSubsystem              | `ObjectReference`<[`/Script/FactoryGame.FGResourceSinkSubsystem`](#38a6e187c8a33cf7490018758ffc4cb4)>                                                 |
| mStatisticsSubsystem                | `ObjectReference`<[`/Script/FactoryGame.FGStatisticsSubsystem`](#0501d307ebfb9395f55084e661d0e783)>                                                   |
| mBlueprintSubsystem                 | `ObjectReference`<[`/Game/FactoryGame/-Shared/Blueprint/BP_BlueprintSusbystem.BP_BlueprintSusbystem_C`](#43f2062f1d7e9bcb357a799f22e1c02a)>           |
| mGameRulesSubsystem                 | `ObjectReference`<[`/Script/FactoryGame.FGGameRulesSubsystem`](#dd00101ae2edc3e9ba4e5830953ae581)>                                                    |
| mIconDatabaseSubsystem              | `ObjectReference`<[`/Game/FactoryGame/-Shared/Blueprint/BP_IconDatabaseSubsystem.BP_IconDatabaseSubsystem_C`](#5dcb68d8ca853e2b5ee7c976a615c1c8)>     |
| mWorldEventSubsystem                | `ObjectReference`                                                                                                                                     |
| mProjectAssembly                    | `ObjectReference`<[`/Game/FactoryGame/Buildable/Factory/ProjectAssembly/BP_ProjectAssembly.BP_ProjectAssembly_C`](#cc4062b65145df45b4793975e557d60f)> |
| mVisitedMapAreas                    | `Array`<`Struct`<`ObjectReference`>>                                                                                                                  |
| mPickedUpItems                      | `Array`<`Struct`<`ObjectReference`>>                                                                                                                  |
| mPlayDurationWhenLoaded             | `Int`                                                                                                                                                 |
| mReplicatedSessionName              | `Str`                                                                                                                                                 |
| mBuildableLightColorSlots           | `Array`<`Struct`<`LinearColor`>>                                                                                                                      |
| mIsTradingPostBuilt                 | `Bool`                                                                                                                                                |
| mHasInitalTradingPostLandAnimPlayed | `Bool`                                                                                                                                                |
| mIsSpaceElevatorBuilt               | `Bool`                                                                                                                                                |
| mHasGivenStartingRecipes            | `Bool`                                                                                                                                                |
| mIsCreativeModeEnabled              | `Bool`                                                                                                                                                |

## `/Game/FactoryGame/Events/BP_EventSubsystem.BP_EventSubsystem_C` <a id="2324d8c38645407dd6280beaf853fe75"></a>

**Component type** `ACTOR`

## `/Game/FactoryGame/-Shared/Blueprint/BP_CircuitSubsystem.BP_CircuitSubsystem_C` <a id="9a50aeea42a31706787ab070eebcec65"></a>

**Component type** `ACTOR`

## `/Game/FactoryGame/-Shared/Blueprint/BP_RailroadSubsystem.BP_RailroadSubsystem_C` <a id="2efb094ad027c82de6fdd502a08ce2c1"></a>

**Component type** `ACTOR`

## Properties

| Name                     | Type                                                                                                            |
| ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| mTrainStationIdentifiers | `Array`<`Struct`<`Union`<[`/Script/FactoryGame.FGTrainStationIdentifier`](#a9689d2fb8c219f08fcf8629a50137db)>>> |

## `/Script/FactoryGame.FGRecipeManager` <a id="2da486937abc3945f1f9a859ffe5e7da"></a>

**Component type** `ACTOR`

## Properties

| Name                           | Type                                 |
| ------------------------------ | ------------------------------------ |
| mAvailableRecipes              | `Array`<`Struct`<`ObjectReference`>> |
| mAvailableCustomizationRecipes | `Array`<`Struct`<`ObjectReference`>> |

## `/Game/FactoryGame/Schematics/Progression/BP_SchematicManager.BP_SchematicManager_C` <a id="5ae82c5bafc766e5d6fab05c260e93bc"></a>

**Component type** `ACTOR`

## Properties

| Name                   | Type                                 |
| ---------------------- | ------------------------------------ |
| mPurchasedSchematics   | `Array`<`Struct`<`ObjectReference`>> |
| mLastActiveSchematic   | `ObjectReference`                    |
| mShipLandTimeStampSave | `Float`                              |

## `/Game/FactoryGame/Schematics/Progression/BP_GamePhaseManager.BP_GamePhaseManager_C` <a id="54ac3280549cdec7b427904fd9493639"></a>

**Component type** `ACTOR`

## Properties

| Name              | Type              |
| ----------------- | ----------------- |
| mCurrentGamePhase | `ObjectReference` |
| mTargetGamePhase  | `ObjectReference` |

## `/Game/FactoryGame/Recipes/Research/BP_ResearchManager.BP_ResearchManager_C` <a id="39005cdae90dca3f7dbac301ffd81880"></a>

**Component type** `ACTOR`

## Properties

| Name                   | Type                                 |
| ---------------------- | ------------------------------------ |
| mUnlockedResearchTrees | `Array`<`Struct`<`ObjectReference`>> |
| mIsActivated           | `Bool`                               |

## `/Game/FactoryGame/-Shared/Blueprint/BP_StorySubsystem.BP_StorySubsystem_C` <a id="5e177cf5245a24317739aaa231d427d4"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                 |
| ------------------ | ------------------------------------ |
| mAllPlayedMessages | `Array`<`Struct`<`ObjectReference`>> |

## `/Game/FactoryGame/-Shared/Blueprint/BP_TutorialIntroManager.BP_TutorialIntroManager_C` <a id="d75dafa7313eb5eb3dfbc6e7f91fd354"></a>

**Component type** `ACTOR`

## Properties

| Name                             | Type                                                                                                                                            |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| mTradingPostBuilt                | `Bool`                                                                                                                                          |
| mCurrentOnboardingStep           | `ObjectReference`                                                                                                                               |
| mHasCompletedIntroTutorial       | `Bool`                                                                                                                                          |
| mHasCompletedIntroSequence       | `Bool`                                                                                                                                          |
| mTradingPost                     | `ObjectReference`<[`/Game/FactoryGame/Buildable/Factory/TradingPost/Build_TradingPost.Build_TradingPost_C`](#19668bc57e13646a04a8a8d6de23298c)> |
| mTradingPostLevel                | `Int`                                                                                                                                           |
| mHasStartedProgression01Activity | `Bool`                                                                                                                                          |

## `/Script/FactoryGame.FGCentralStorageSubsystem` <a id="9443a65a4ea801981f18290aac226aed"></a>

**Component type** `ACTOR`

## `/Script/FactoryGame.FGMapManager` <a id="9369a5ae02682133632dfcf4d28534b3"></a>

**Component type** `ACTOR`

## Properties

| Name                | Type                                       |
| ------------------- | ------------------------------------------ |
| mFogOfWarRawData    | `Array`<`ByteProperty`>                    |
| mMapMarkers         | `Array`<`Struct`<`MapMarker`>>             |
| mHighlightedMarkers | `Array`<`Struct`<`HighlightedMarkerPair`>> |

## `/Game/FactoryGame/Unlocks/BP_UnlockSubsystem.BP_UnlockSubsystem_C` <a id="7616bd73471496c34969d54c9785569a"></a>

**Component type** `ACTOR`

## Properties

| Name                               | Type                                       |
| ---------------------------------- | ------------------------------------------ |
| mScannableResourcesPairs           | `Array`<`Struct`<`ScannableResourcePair`>> |
| mScannableObjectData               | `Array`<`Struct`<`ScannableObjectData`>>   |
| mIsMapUnlocked                     | `Bool`                                     |
| mIsBuildingEfficiencyUnlocked      | `Bool`                                     |
| mIsBuildingOverclockUnlocked       | `Bool`                                     |
| mIsBlueprintsUnlocked              | `Bool`                                     |
| mIsCustomizerUnlocked              | `Bool`                                     |
| mIsBuildingProductionBoostUnlocked | `Bool`                                     |
| mNumTotalInventorySlots            | `Int`                                      |
| mNumTotalArmEquipmentSlots         | `Int`                                      |
| mUnlockedEmotes                    | `Array`<`Struct`<`ObjectReference`>>       |
| mUnlockedTapes                     | `Array`<`Struct`<`ObjectReference`>>       |
| mUnlockedPlayerCustomizations      | `Array`<`Struct`<`ObjectReference`>>       |

## `/Script/FactoryGame.FGPipeSubsystem` <a id="af9cc6d6afbb8640b1567cf751c8d8a5"></a>

**Component type** `ACTOR`

## `/Script/FactoryGame.FGResourceSinkSubsystem` <a id="38a6e187c8a33cf7490018758ffc4cb4"></a>

**Component type** `ACTOR`

## `/Game/FactoryGame/-Shared/Blueprint/BP_VehicleSubsystem.BP_VehicleSubsystem_C` <a id="d45e4c07d39a8fe16aa05266141f3758"></a>

**Component type** `ACTOR`

## `/Script/FactoryGame.FGStatisticsSubsystem` <a id="0501d307ebfb9395f55084e661d0e783"></a>

**Component type** `ACTOR`

## Properties

| Name              | Type          |
| ----------------- | ------------- |
| mActorsBuiltCount | `MapProperty` |

## `/Script/FactoryGame.FGScannableSubsystem` <a id="7dcc6ff932e920e66f5fe3a3ea157a4d"></a>

**Component type** `ACTOR`

## `/Game/FactoryGame/-Shared/Blueprint/BP_BlueprintSusbystem.BP_BlueprintSusbystem_C` <a id="43f2062f1d7e9bcb357a799f22e1c02a"></a>

**Component type** `ACTOR`

## Properties

| Name                      | Type                                         |
| ------------------------- | -------------------------------------------- |
| mBlueprintCategoryRecords | `Array`<`Struct`<`BlueprintCategoryRecord`>> |

## `/Script/FactoryGame.FGGameRulesSubsystem` <a id="dd00101ae2edc3e9ba4e5830953ae581"></a>

**Component type** `ACTOR`

## Properties

| Name                     | Type   |
| ------------------------ | ------ |
| mStartingTier            | `Int`  |
| mHasInitialized          | `Bool` |
| mUnlockInstantAltRecipes | `Bool` |
| mNoUnlockCost            | `Bool` |

## `/Game/FactoryGame/-Shared/Blueprint/BP_IconDatabaseSubsystem.BP_IconDatabaseSubsystem_C` <a id="5dcb68d8ca853e2b5ee7c976a615c1c8"></a>

**Component type** `ACTOR`

## Properties

| Name                 | Type                          |
| -------------------- | ----------------------------- |
| mGlobalIconLibraries | `Array`<`SoftObjectProperty`> |

## `/Game/FactoryGame/Character/Player/BP_PlayerState.BP_PlayerState_C` <a id="4c001bfe67d1ec5cacd2a1a2c3539513"></a>

**Component type** `ACTOR`

## Properties

| Name                                 | Type                                                                                                                   |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| mPlayerHotbars                       | `Array`<`Struct`<`Union`<[`/Script/FactoryGame.FGPlayerHotbar`](#0b7c1c7032b9ea87265ea8ba1481bdef)>>>                  |
| mBuildableSubCategoryDefaultMatDesc  | `Array`<`Struct`<`SubCategoryMaterialDefault`>>                                                                        |
| mMaterialSubCategoryDefaultMatDesc   | `Array`<`Struct`<`SubCategoryMaterialDefault`>>                                                                        |
| mPlayerRules                         | [`PlayerRules`](#81b332f2070f04404a9ef41e7eafd9a3)                                                                     |
| mOwnedPawn                           | `ObjectReference`<[`/Game/FactoryGame/Character/Player/Char_Player.Char_Player_C`](#d9af50be26eb7b8c38428115c2ede530)> |
| mHasReceivedInitialItems             | `Bool`                                                                                                                 |
| mVisitedAreas                        | `Array`<`Struct`<`ObjectReference`>>                                                                                   |
| mShoppingListSettings                | [`ShoppingListSettings`](#178bbc1d599e54b7e500b56ea855f60d)                                                            |
| mClientIdentityInfo                  | `Struct`<`ClientIdentityInfo`>                                                                                         |
| mPlayedMessages                      | `Array`<`Struct`<`ObjectReference`>>                                                                                   |
| mRememberedFirstTimeEquipmentClasses | `Array`<`Struct`<`ObjectReference`>>                                                                                   |
| mNumObservedInventorySlots           | `Int`                                                                                                                  |
| mShoppingListComponent               | `ObjectReference`<[`/Script/FactoryGame.FGShoppingListComponent`](#69b9138f542b129c542963d4e4c41bcd)>                  |
| mLastSafeCharacterLocation           | `Struct`<`Vector`>                                                                                                     |

## `/Game/FactoryGame/Character/Player/Char_Player.Char_Player_C` <a id="d9af50be26eb7b8c38428115c2ede530"></a>

**Component type** `ACTOR`

## Properties

| Name                            | Type                                                                                                                                              |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| mBuildGun                       | `ObjectReference`<[`/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C`](#4eb723956348782d5f77699315e4795c)>                          |
| mResourceScanner                | `ObjectReference`<[`/Game/FactoryGame/Equipment/ResourceScanner/BP_ResourceScanner.BP_ResourceScanner_C`](#8025b0306acb30fa3f366289a8ccc332)>     |
| mResourceMiner                  | `ObjectReference`<[`/Game/FactoryGame/Equipment/ResourceCollector/Equip_ResourceMiner.Equip_ResourceMiner_C`](#9c74b4b939b914a754c6692ca1e64bbe)> |
| mLastSafeGroundPositions        | `Struct`<`Vector`>                                                                                                                                |
| mLastSafeGroundPositionLoopHead | `Int`                                                                                                                                             |
| mInventory                      | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)>                                                |
| mUploadInventory                | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)>                                                |
| mArmsEquipmentSlot              | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponentEquipment`](#c4235f10d403f57878a78675a193aa63)>                                       |
| mBackEquipmentSlot              | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponentEquipment`](#c4235f10d403f57878a78675a193aa63)>                                       |
| mLegsEquipmentSlot              | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponentEquipment`](#c4235f10d403f57878a78675a193aa63)>                                       |
| mHeadEquipmentSlot              | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponentEquipment`](#c4235f10d403f57878a78675a193aa63)>                                       |
| mBodyEquipmentSlot              | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponentEquipment`](#c4235f10d403f57878a78675a193aa63)>                                       |
| mUploadTimer                    | `Float`                                                                                                                                           |
| mCachedPlayerName               | `Str`                                                                                                                                             |
| mCachedPlayerCustomizationData  | [`PlayerCustomizationData`](#838788afcbb3999f32a37bfd88511a60)                                                                                    |
| mHealthComponent                | `ObjectReference`<[`/Script/FactoryGame.FGHealthComponent`](#d2ef6ea371a1ccbed102d21ee1cffc01)>                                                   |
| mLastSafeLoadLocation           | `Struct`<`Vector`>                                                                                                                                |

## `/Game/FactoryGame/Equipment/ResourceScanner/BP_ResourceScanner.BP_ResourceScanner_C` <a id="8025b0306acb30fa3f366289a8ccc332"></a>

**Component type** `ACTOR`

## `/Game/FactoryGame/Equipment/ResourceCollector/Equip_ResourceMiner.Equip_ResourceMiner_C` <a id="9c74b4b939b914a754c6692ca1e64bbe"></a>

**Component type** `ACTOR`

## `/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C` <a id="4eb723956348782d5f77699315e4795c"></a>

**Component type** `ACTOR`

## `/Game/FactoryGame/Buildable/Factory/SpaceElevator/Build_SpaceElevator.Build_SpaceElevator_C` <a id="208b4ade215d9617b57e57ad85ef7217"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mInputInventory              | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mIsProducing                 | `Bool`                                                                                             |
| mColorSlot                   | `Byte`                                                                                             |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/ProjectAssembly/BP_ProjectAssembly.BP_ProjectAssembly_C` <a id="cc4062b65145df45b4793975e557d60f"></a>

**Component type** `ACTOR`

## Properties

| Name           | Type                                                                                                                                                  |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| mSpaceElevator | `ObjectReference`<[`/Game/FactoryGame/Buildable/Factory/SpaceElevator/Build_SpaceElevator.Build_SpaceElevator_C`](#208b4ade215d9617b57e57ad85ef7217)> |

## `/Game/FactoryGame/Buildable/Factory/Mam/Build_Mam.Build_Mam_C` <a id="2b81e3de4628d3227164445ecadd186e"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe   | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/ResourceSinkShop/Build_ResourceSinkShop.Build_ResourceSinkShop_C` <a id="908e3d0ac3690935d2a512816df6aee1"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mShopInventory               | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mIsProducing                 | `Bool`                                                                                             |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/TradingPost/Build_TradingPost.Build_TradingPost_C` <a id="19668bc57e13646a04a8a8d6de23298c"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                                                                                                                        |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| mGenerators                  | `Array`<`Struct`<`Union`<[`/Game/FactoryGame/Buildable/Factory/GeneratorBiomass/Build_GeneratorIntegratedBiomass.Build_GeneratorIntegratedBiomass_C`](#83d14b5a11387466f4b982ff339843c5)>>> |
| mStorage                     | `ObjectReference`<[`/Game/FactoryGame/Buildable/Factory/StoragePlayer/Build_StorageIntegrated.Build_StorageIntegrated_C`](#677abe355cdd75e08b678b56fe7da471)>                               |
| mHubTerminal                 | `ObjectReference`<[`/Game/FactoryGame/Buildable/Factory/HubTerminal/Build_HubTerminal.Build_HubTerminal_C`](#f7f53cca5fbdbeabb952bdea027856ab)>                                             |
| mWorkBench                   | `ObjectReference`<[`/Game/FactoryGame/Buildable/Factory/WorkBench/Build_WorkBenchIntegrated.Build_WorkBenchIntegrated_C`](#722a3658f102dbde79c294836a2e9561)>                               |
| mLocker                      | `ObjectReference`                                                                                                                                                                           |
| mPioneerPotty                | `ObjectReference`<[`/Game/FactoryGame/Buildable/Building/Potty/BUILD_Potty_mk1.BUILD_Potty_mk1_C`](#eb0c85a2263290b0a77dc5cbcb771a5f)>                                                      |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)>                                                                                          |
| mTimeSinceStartStopProducing | `Float`                                                                                                                                                                                     |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)>                                                                                          |
| mIsProducing                 | `Bool`                                                                                                                                                                                      |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                                                                                                             |
| mBuiltWithRecipe             | `ObjectReference`                                                                                                                                                                           |

## `/Game/FactoryGame/Buildable/Building/Potty/BUILD_Potty_mk1.BUILD_Potty_mk1_C` <a id="eb0c85a2263290b0a77dc5cbcb771a5f"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                                                               |
| ------------------ | -------------------------------------------------------------------------------------------------- |
| mStorageInventory  | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |

## `/Game/FactoryGame/Buildable/Factory/GeneratorBiomass/Build_GeneratorIntegratedBiomass.Build_GeneratorIntegratedBiomass_C` <a id="83d14b5a11387466f4b982ff339843c5"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mFuelInventory               | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/StoragePlayer/Build_StorageIntegrated.Build_StorageIntegrated_C` <a id="677abe355cdd75e08b678b56fe7da471"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mStorageInventory            | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mIsProducing                 | `Bool`                                                                                             |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/HubTerminal/Build_HubTerminal.Build_HubTerminal_C` <a id="f7f53cca5fbdbeabb952bdea027856ab"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe   | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/WorkBench/Build_WorkBenchIntegrated.Build_WorkBenchIntegrated_C` <a id="722a3658f102dbde79c294836a2e9561"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe   | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/ResourceSink/Build_ResourceSink.Build_ResourceSink_C` <a id="ed25d32dadab59d85e4b83b81eaf626a"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mCouponInventory             | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/WorkBench/Build_WorkBench.Build_WorkBench_C` <a id="f1be50a7d5aeb233f104df44fa857637"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe   | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/ConstructorMk1/Build_ConstructorMk1.Build_ConstructorMk1_C` <a id="205f783d3131c6f13d6a52e5ac9c2fe7"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mInputInventory              | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mOutputInventory             | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |
| mCurrentRecipe               | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/AssemblerMk1/Build_AssemblerMk1.Build_AssemblerMk1_C` <a id="a2da0f1c9ea54dcf2708b4112044625f"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mInputInventory              | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mOutputInventory             | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |
| mCurrentRecipe               | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/SmelterMk1/Build_SmelterMk1.Build_SmelterMk1_C` <a id="33db324bf55726bcb98eff151bbd5ca3"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mInputInventory              | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mOutputInventory             | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/GeneratorBiomass/Build_GeneratorBiomass_Automated.Build_GeneratorBiomass_Automated_C` <a id="2625999ec4d6d208c75242e324428ecb"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mFuelInventory               | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/PowerPoleMk1/Build_PowerPoleMk1.Build_PowerPoleMk1_C` <a id="a5031bd2cf9fb62fc171eef0c4f3b515"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe   | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/PowerLine/Build_PowerLine.Build_PowerLine_C` <a id="c2a1666d2d32223655c85a0eab946082"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mWireInstances     | `Array`<`Struct`<`WireInstance`>>                               |
| mCachedLength      | `Float`                                                         |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe   | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/ConveyorBeltMk1/Build_ConveyorBeltMk1.Build_ConveyorBeltMk1_C` <a id="d0ea31d73878b0e0b7a78ff94673a221"></a>

**Component type** `ACTOR`

## Properties

| Name                | Type                                                                                                                                                              |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| mSplineData         | `Array`<`Struct`<`SplinePointData`>>                                                                                                                              |
| mConveyorChainActor | `ObjectReference`<[`/Script/FactoryGame.FGConveyorChainActor`](#9cd04441c0a87b984b69e6b76bc66a75)>                                                                |
| mCustomizationData  | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                                                                                   |
| mBuiltWithRecipe    | `ObjectReference`                                                                                                                                                 |
| mBlueprintDesigner  | `ObjectReference`<[`/Game/FactoryGame/Buildable/Factory/BlueprintDesigner/Build_BlueprintDesigner.Build_BlueprintDesigner_C`](#64ba976ff7c13d6a78b97d48874edd7d)> |

## `/Game/FactoryGame/Buildable/Factory/ConveyorPole/Build_ConveyorPole.Build_ConveyorPole_C` <a id="96b541ad54803b9a9a0c0c6501b34b71"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                                                                                                                              |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                                                                                   |
| mBuiltWithRecipe   | `ObjectReference`                                                                                                                                                 |
| mBlueprintDesigner | `ObjectReference`<[`/Game/FactoryGame/Buildable/Factory/BlueprintDesigner/Build_BlueprintDesigner.Build_BlueprintDesigner_C`](#64ba976ff7c13d6a78b97d48874edd7d)> |

## `/Script/FactoryGame.FGConveyorChainActor` <a id="9cd04441c0a87b984b69e6b76bc66a75"></a>

**Component type** `ACTOR`

## `/Game/FactoryGame/Buildable/Factory/ConveyorBeltMk2/Build_ConveyorBeltMk2.Build_ConveyorBeltMk2_C` <a id="1f68db034b1ea75bec863a3718707fa4"></a>

**Component type** `ACTOR`

## Properties

| Name                | Type                                                                                               |
| ------------------- | -------------------------------------------------------------------------------------------------- |
| mSplineData         | `Array`<`Struct`<`SplinePointData`>>                                                               |
| mConveyorChainActor | `ObjectReference`<[`/Script/FactoryGame.FGConveyorChainActor`](#9cd04441c0a87b984b69e6b76bc66a75)> |
| mCustomizationData  | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe    | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/ConveyorLiftMk2/Build_ConveyorLiftMk2.Build_ConveyorLiftMk2_C` <a id="49d0d4acfa62f0923e3c7c734d25eabf"></a>

**Component type** `ACTOR`

## Properties

| Name                 | Type                                                                                               |
| -------------------- | -------------------------------------------------------------------------------------------------- |
| mTopTransform        | [`Transform`](#2ff4148554480a37f85efd299df04850)                                                   |
| mSnappedPassthroughs | `Array`<`Struct`<`ObjectReference`>>                                                               |
| mConveyorChainActor  | `ObjectReference`<[`/Script/FactoryGame.FGConveyorChainActor`](#9cd04441c0a87b984b69e6b76bc66a75)> |
| mCustomizationData   | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe     | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/ConveyorLiftMk1/Build_ConveyorLiftMk1.Build_ConveyorLiftMk1_C` <a id="2b9021bfdd217181bc2a3258cbfce6d6"></a>

**Component type** `ACTOR`

## Properties

| Name                 | Type                                                                                               |
| -------------------- | -------------------------------------------------------------------------------------------------- |
| mTopTransform        | [`Transform`](#2ff4148554480a37f85efd299df04850)                                                   |
| mSnappedPassthroughs | `Array`<`Struct`<`ObjectReference`>>                                                               |
| mConveyorChainActor  | `ObjectReference`<[`/Script/FactoryGame.FGConveyorChainActor`](#9cd04441c0a87b984b69e6b76bc66a75)> |
| mCustomizationData   | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe     | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/ConveyorPoleStackable/Build_ConveyorPoleStackable.Build_ConveyorPoleStackable_C` <a id="6dca9aff96836c7e9552a9ba0427e691"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe   | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/CA_Merger/Build_ConveyorAttachmentMerger.Build_ConveyorAttachmentMerger_C` <a id="e12677762eb562ab84a64a43e677acd6"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                                                               |
| ------------------ | -------------------------------------------------------------------------------------------------- |
| mCurrentInputIndex | `Int`                                                                                              |
| mBufferInventory   | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mSavedDirections   | `Array`<`EnumProperty`>                                                                            |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe   | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/CA_Splitter/Build_ConveyorAttachmentSplitter.Build_ConveyorAttachmentSplitter_C` <a id="1144ead904286c2b48fe4be3dc409207"></a>

**Component type** `ACTOR`

## Properties

| Name                | Type                                                                                               |
| ------------------- | -------------------------------------------------------------------------------------------------- |
| mCurrentOutputIndex | `Int`                                                                                              |
| mBufferInventory    | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mSavedDirections    | `Array`<`EnumProperty`>                                                                            |
| mCustomizationData  | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe    | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/StorageContainerMk1/Build_StorageContainerMk1.Build_StorageContainerMk1_C` <a id="c2dd81c7c3bbc4a8a2523eeefb449598"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mStorageInventory            | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mIsProducing                 | `Bool`                                                                                             |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/StoragePlayer/Build_StoragePlayer.Build_StoragePlayer_C` <a id="0ad0ed2f1bee8c38a078f11e25633a8a"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mStorageInventory            | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mIsProducing                 | `Bool`                                                                                             |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/JumpPad/Build_JumpPadAdjustable.Build_JumpPadAdjustable_C` <a id="d1dc39666c1e82c0d5602eba04f7521c"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mLaunchAngle                 | `Float`                                                                                            |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/LandingPad/Build_LandingPad.Build_LandingPad_C` <a id="cc1ce63b01f4083689f8d3db12f3be45"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Building/Ladder/Build_Ladder.Build_Ladder_C` <a id="6f017e2b4093a549e07c4f2ce1d2946a"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mNumSegments       | `Int`                                                           |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe   | `ObjectReference`                                               |

## `/Game/FactoryGame/Character/Creature/Wildlife/SpaceGiraffe/Char_SpaceGiraffe.Char_SpaceGiraffe_C` <a id="53cad3725573653ef10d1547482a2543"></a>

**Component type** `ACTOR`

## Properties

| Name                  | Type                                                                                            |
| --------------------- | ----------------------------------------------------------------------------------------------- |
| mHealthComponent      | `ObjectReference`<[`/Script/FactoryGame.FGHealthComponent`](#d2ef6ea371a1ccbed102d21ee1cffc01)> |
| mLastSafeLoadLocation | `Struct`<`Vector`>                                                                              |

## `/Game/FactoryGame/Buildable/Factory/ManufacturerMk1/Build_ManufacturerMk1.Build_ManufacturerMk1_C` <a id="883398a30bcbcf900abac8d668963041"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mInputInventory              | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mOutputInventory             | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mCurrentRecipe               | `ObjectReference`                                                                                  |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/Packager/Build_Packager.Build_Packager_C` <a id="2e4ed689d331e86b79009f5b0c344d15"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mInputInventory              | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mOutputInventory             | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mCurrentRecipe               | `ObjectReference`                                                                                  |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/OilRefinery/Build_OilRefinery.Build_OilRefinery_C` <a id="5dfb84185338e0b36a56667cabb4e6c6"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mInputInventory              | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mOutputInventory             | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mCurrentRecipe               | `ObjectReference`                                                                                  |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/Blender/Build_Blender.Build_Blender_C` <a id="c0d14a96f9e819e7c9f7087ffbab92d5"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mInputInventory              | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mOutputInventory             | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mCurrentRecipe               | `ObjectReference`                                                                                  |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/HadronCollider/Build_HadronCollider.Build_HadronCollider_C` <a id="13931735969722b08fc71e86316ef296"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mInputInventory              | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mOutputInventory             | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mCurrentRecipe               | `ObjectReference`                                                                                  |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/Converter/Build_Converter.Build_Converter_C` <a id="1aa76086f37ebd8ec43478ac776d133e"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mInputInventory              | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mOutputInventory             | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mCurrentRecipe               | `ObjectReference`                                                                                  |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/QuantumEncoder/Build_QuantumEncoder.Build_QuantumEncoder_C` <a id="5f162d7bcf5c10c42e0c336279fcee88"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mInputInventory              | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mOutputInventory             | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mCurrentRecipe               | `ObjectReference`                                                                                  |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/GeneratorCoal/Build_GeneratorCoal.Build_GeneratorCoal_C` <a id="30aa9b953993b6744a2d60ebd28a517e"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mFuelInventory               | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/GeneratorFuel/Build_GeneratorFuel.Build_GeneratorFuel_C` <a id="3f0761b600eb559677ecb497d34e907b"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mFuelInventory               | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/GeneratorNuclear/Build_GeneratorNuclear.Build_GeneratorNuclear_C` <a id="ca30c56529395c9afb8011617e053454"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mOutputInventory             | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mFuelInventory               | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/PowerPoleMk2/Build_PowerPoleMk2.Build_PowerPoleMk2_C` <a id="644cea3e20cc4329125507e5c30bb9d0"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe   | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/PowerPoleMk3/Build_PowerPoleMk3.Build_PowerPoleMk3_C` <a id="1358d70fc43a8f27545c109daeffeceb"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe   | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/PowerSwitch/Build_PowerSwitch.Build_PowerSwitch_C` <a id="cb765739a0a1248c85bcc7c1739feb05"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe   | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/PriorityPowerSwitch/Build_PriorityPowerSwitch.Build_PriorityPowerSwitch_C` <a id="488f69fa669c9a8c4edb3110431eba80"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe   | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/PowerStorage/Build_PowerStorageMk1.Build_PowerStorageMk1_C` <a id="0b15e2ccf1031db98165684c6d099f8a"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/PowerPoleWall/Build_PowerPoleWall.Build_PowerPoleWall_C` <a id="e038a60b251b04817890828ef9245905"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe   | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/PowerPoleWallDouble/Build_PowerPoleWallDouble.Build_PowerPoleWallDouble_C` <a id="8759597f2c890362d3e49fe25c4c1954"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe   | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/PowerPoleWall/Build_PowerPoleWall_Mk2.Build_PowerPoleWall_Mk2_C` <a id="77873dd9650014322d2fc2585297f98e"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe   | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/PowerPoleWallDouble/Build_PowerPoleWallDouble_Mk2.Build_PowerPoleWallDouble_Mk2_C` <a id="4a8d6bd7f9b8c120a05dca591f5ea856"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe   | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/PowerPoleWall/Build_PowerPoleWall_Mk3.Build_PowerPoleWall_Mk3_C` <a id="c0006ed6b8fcb8c85c6088a3ea732849"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe   | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/PowerPoleWallDouble/Build_PowerPoleWallDouble_Mk3.Build_PowerPoleWallDouble_Mk3_C` <a id="cddf9902f0b4f64c0c7bd3bdc67d934c"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe   | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/ConveyorBeltMk3/Build_ConveyorBeltMk3.Build_ConveyorBeltMk3_C` <a id="ee5b5a833dfd38557755c3c15216dee3"></a>

**Component type** `ACTOR`

## Properties

| Name                | Type                                                                                               |
| ------------------- | -------------------------------------------------------------------------------------------------- |
| mSplineData         | `Array`<`Struct`<`SplinePointData`>>                                                               |
| mConveyorChainActor | `ObjectReference`<[`/Script/FactoryGame.FGConveyorChainActor`](#9cd04441c0a87b984b69e6b76bc66a75)> |
| mCustomizationData  | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe    | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/ConveyorBeltMk4/Build_ConveyorBeltMk4.Build_ConveyorBeltMk4_C` <a id="e8378d7af763423090f0b3c55e412d24"></a>

**Component type** `ACTOR`

## Properties

| Name                | Type                                                                                               |
| ------------------- | -------------------------------------------------------------------------------------------------- |
| mSplineData         | `Array`<`Struct`<`SplinePointData`>>                                                               |
| mConveyorChainActor | `ObjectReference`<[`/Script/FactoryGame.FGConveyorChainActor`](#9cd04441c0a87b984b69e6b76bc66a75)> |
| mCustomizationData  | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe    | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/ConveyorBeltMk5/Build_ConveyorBeltMk5.Build_ConveyorBeltMk5_C` <a id="ccdcdd175a445d7db2ca3197b9002f60"></a>

**Component type** `ACTOR`

## Properties

| Name                | Type                                                                                               |
| ------------------- | -------------------------------------------------------------------------------------------------- |
| mSplineData         | `Array`<`Struct`<`SplinePointData`>>                                                               |
| mConveyorChainActor | `ObjectReference`<[`/Script/FactoryGame.FGConveyorChainActor`](#9cd04441c0a87b984b69e6b76bc66a75)> |
| mCustomizationData  | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe    | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/ConveyorBeltMk6/Build_ConveyorBeltMk6.Build_ConveyorBeltMk6_C` <a id="af08bb4d7003f70249e5ca247e432ab2"></a>

**Component type** `ACTOR`

## Properties

| Name                | Type                                                                                               |
| ------------------- | -------------------------------------------------------------------------------------------------- |
| mSplineData         | `Array`<`Struct`<`SplinePointData`>>                                                               |
| mConveyorChainActor | `ObjectReference`<[`/Script/FactoryGame.FGConveyorChainActor`](#9cd04441c0a87b984b69e6b76bc66a75)> |
| mCustomizationData  | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe    | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/ConveyorLiftMk3/Build_ConveyorLiftMk3.Build_ConveyorLiftMk3_C` <a id="2df4182e7cfdbcc2587cfb80b5126dfb"></a>

**Component type** `ACTOR`

## Properties

| Name                 | Type                                                                                               |
| -------------------- | -------------------------------------------------------------------------------------------------- |
| mTopTransform        | [`Transform`](#2ff4148554480a37f85efd299df04850)                                                   |
| mSnappedPassthroughs | `Array`<`Struct`<`ObjectReference`>>                                                               |
| mConveyorChainActor  | `ObjectReference`<[`/Script/FactoryGame.FGConveyorChainActor`](#9cd04441c0a87b984b69e6b76bc66a75)> |
| mCustomizationData   | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe     | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/ConveyorLiftMk6/Build_ConveyorLiftMk6.Build_ConveyorLiftMk6_C` <a id="7524949c010a1956665c784f0cb0e6bb"></a>

**Component type** `ACTOR`

## Properties

| Name                 | Type                                                                                               |
| -------------------- | -------------------------------------------------------------------------------------------------- |
| mTopTransform        | [`Transform`](#2ff4148554480a37f85efd299df04850)                                                   |
| mSnappedPassthroughs | `Array`<`Struct`<`ObjectReference`>>                                                               |
| mConveyorChainActor  | `ObjectReference`<[`/Script/FactoryGame.FGConveyorChainActor`](#9cd04441c0a87b984b69e6b76bc66a75)> |
| mCustomizationData   | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe     | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/ConveyorLiftMk4/Build_ConveyorLiftMk4.Build_ConveyorLiftMk4_C` <a id="33cd3fb848039688b577573485554692"></a>

**Component type** `ACTOR`

## Properties

| Name                      | Type                                                                                               |
| ------------------------- | -------------------------------------------------------------------------------------------------- |
| mTopTransform             | [`Transform`](#2ff4148554480a37f85efd299df04850)                                                   |
| mIsBeltUsingInputRotation | `Bool`                                                                                             |
| mSnappedPassthroughs      | `Array`<`Struct`<`ObjectReference`>>                                                               |
| mConveyorChainActor       | `ObjectReference`<[`/Script/FactoryGame.FGConveyorChainActor`](#9cd04441c0a87b984b69e6b76bc66a75)> |
| mCustomizationData        | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe          | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/ConveyorLiftMk5/Build_ConveyorLiftMk5.Build_ConveyorLiftMk5_C` <a id="7563582a6bfcd822cfd8769df1c0ece3"></a>

**Component type** `ACTOR`

## Properties

| Name                 | Type                                                                                               |
| -------------------- | -------------------------------------------------------------------------------------------------- |
| mTopTransform        | [`Transform`](#2ff4148554480a37f85efd299df04850)                                                   |
| mSnappedPassthroughs | `Array`<`Struct`<`ObjectReference`>>                                                               |
| mConveyorChainActor  | `ObjectReference`<[`/Script/FactoryGame.FGConveyorChainActor`](#9cd04441c0a87b984b69e6b76bc66a75)> |
| mCustomizationData   | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe     | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/ConveyorPoleWall/Build_ConveyorPoleWall.Build_ConveyorPoleWall_C` <a id="869b136c38226fad3affdfb4e7458a63"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe   | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/ConveyorPoleWall/Build_ConveyorCeilingAttachment.Build_ConveyorCeilingAttachment_C` <a id="475c9415ef0582458e208afefaecd5cf"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe   | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Building/ConveyorHole/Build_ConveyorWallHole.Build_ConveyorWallHole_C` <a id="a7b2dee30a7613737978d312d66be8ed"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe   | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/FoundationPassthrough/Build_FoundationPassthrough_Lift.Build_FoundationPassthrough_Lift_C` <a id="a423f2f2d856ab32b6186cf3583e6433"></a>

**Component type** `ACTOR`

## Properties

| Name                      | Type                                                            |
| ------------------------- | --------------------------------------------------------------- |
| mSnappedBuildingThickness | `Float`                                                         |
| mCustomizationData        | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe          | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/Pipeline/Build_Pipeline_NoIndicator.Build_Pipeline_NoIndicator_C` <a id="c90bebba6ea367f02157102940522456"></a>

**Component type** `ACTOR`

## Properties

| Name                 | Type                                                            |
| -------------------- | --------------------------------------------------------------- |
| mSplineData          | `Array`<`Struct`<`SplinePointData`>>                            |
| mSnappedPassthroughs | `Array`<`Struct`<`ObjectReference`>>                            |
| mCustomizationData   | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe     | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/PipelineSupport/Build_PipelineSupport.Build_PipelineSupport_C` <a id="bff7c31118017beb253860c4318180e1"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mHeight            | `Float`                                                         |
| mColorSlot         | `Byte`                                                          |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe   | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/Pipeline/Build_Pipeline.Build_Pipeline_C` <a id="109c5b7382c0b125962d3b0b0b25a649"></a>

**Component type** `ACTOR`

## Properties

| Name                 | Type                                                                                                                                                                           |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| mFlowIndicator       | `ObjectReference`<[`/Game/FactoryGame/Buildable/Factory/Pipeline/FlowIndicator/Build_PipelineFlowIndicator.Build_PipelineFlowIndicator_C`](#e30d99eeeccec8e638ce88d55dc29fcb)> |
| mSplineData          | `Array`<`Struct`<`SplinePointData`>>                                                                                                                                           |
| mSnappedPassthroughs | `Array`<`Struct`<`ObjectReference`>>                                                                                                                                           |
| mCustomizationData   | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                                                                                                |
| mBuiltWithRecipe     | `ObjectReference`                                                                                                                                                              |

## `/Game/FactoryGame/Buildable/Factory/Pipeline/FlowIndicator/Build_PipelineFlowIndicator.Build_PipelineFlowIndicator_C` <a id="e30d99eeeccec8e638ce88d55dc29fcb"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |

## `/Game/FactoryGame/Buildable/Factory/PipelineMk2/Build_PipelineMK2_NoIndicator.Build_PipelineMK2_NoIndicator_C` <a id="906b7894316e76793ae494b9c150a364"></a>

**Component type** `ACTOR`

## Properties

| Name                 | Type                                                            |
| -------------------- | --------------------------------------------------------------- |
| mSplineData          | `Array`<`Struct`<`SplinePointData`>>                            |
| mSnappedPassthroughs | `Array`<`Struct`<`ObjectReference`>>                            |
| mCustomizationData   | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe     | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/PipelineMk2/Build_PipelineMK2.Build_PipelineMK2_C` <a id="fd4e2eee24bd6581c74dabf8b5a5b827"></a>

**Component type** `ACTOR`

## Properties

| Name                 | Type                                                                                                                                                                           |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| mFlowIndicator       | `ObjectReference`<[`/Game/FactoryGame/Buildable/Factory/Pipeline/FlowIndicator/Build_PipelineFlowIndicator.Build_PipelineFlowIndicator_C`](#e30d99eeeccec8e638ce88d55dc29fcb)> |
| mSplineData          | `Array`<`Struct`<`SplinePointData`>>                                                                                                                                           |
| mSnappedPassthroughs | `Array`<`Struct`<`ObjectReference`>>                                                                                                                                           |
| mCustomizationData   | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                                                                                                |
| mBuiltWithRecipe     | `ObjectReference`                                                                                                                                                              |

## `/Game/FactoryGame/Buildable/Factory/PipeJunction/Build_PipelineJunction_Cross.Build_PipelineJunction_Cross_C` <a id="d3a1f4e5346657c7a370db189fa6639b"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`                                                                                  |
| mColorSlot                   | `Byte`                                                                                             |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/PipePump/Build_PipelinePump.Build_PipelinePump_C` <a id="8e66af14a278783bfc925a8c4438b4c9"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`                                                                                  |
| mColorSlot                   | `Byte`                                                                                             |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/PipePumpMk2/Build_PipelinePumpMK2.Build_PipelinePumpMk2_C` <a id="d4cc6d973a4cb9e7d6e9dccf5ad77d0f"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`                                                                                  |
| mColorSlot                   | `Byte`                                                                                             |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/PipeValve/Build_Valve.Build_Valve_C` <a id="f871ebc0fd0aff0df7df0cdca9bce38b"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`                                                                                  |
| mColorSlot                   | `Byte`                                                                                             |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/PipelineSupport/Build_PipeSupportStackable.Build_PipeSupportStackable_C` <a id="71c01c8db12200fee4a30ec17fa0c69c"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe   | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/PipelineSupportWall/Build_PipelineSupportWall.Build_PipelineSupportWall_C` <a id="0b581b8298bdffe861f0f823c44dc4b2"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mColorSlot         | `Byte`                                                          |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe   | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/PipelineSupportWallHole/Build_PipelineSupportWallHole.Build_PipelineSupportWallHole_C` <a id="317d9d7ecea81d77ab066492db93cdf3"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mColorSlot         | `Byte`                                                          |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe   | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/FoundationPassthrough/Build_FoundationPassthrough_Pipe.Build_FoundationPassthrough_Pipe_C` <a id="7e61ee15a562bb2437326157fdc72f4c"></a>

**Component type** `ACTOR`

## Properties

| Name                      | Type                                                            |
| ------------------------- | --------------------------------------------------------------- |
| mSnappedBuildingThickness | `Float`                                                         |
| mColorSlot                | `Byte`                                                          |
| mCustomizationData        | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe          | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/CA_MergerPriority/Build_ConveyorAttachmentMergerPriority.Build_ConveyorAttachmentMergerPriority_C` <a id="28339abdfe624cc3eda2e974b56375e6"></a>

**Component type** `ACTOR`

## Properties

| Name                 | Type                                                                                               |
| -------------------- | -------------------------------------------------------------------------------------------------- |
| mInputPriorities     | `Array`<`IntProperty`>                                                                             |
| mCurrentInputIndices | `Array`<`IntProperty`>                                                                             |
| mBufferInventory     | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mSavedDirections     | `Array`<`EnumProperty`>                                                                            |
| mCustomizationData   | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe     | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/CA_SplitterSmart/Build_ConveyorAttachmentSplitterSmart.Build_ConveyorAttachmentSplitterSmart_C` <a id="d503c70fefe92bf962cb779774296d44"></a>

**Component type** `ACTOR`

## Properties

| Name                 | Type                                                                                               |
| -------------------- | -------------------------------------------------------------------------------------------------- |
| mItemToLastOutputMap | `MapProperty`                                                                                      |
| mBufferInventory     | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mSavedDirections     | `Array`<`EnumProperty`>                                                                            |
| mCustomizationData   | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe     | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/CA_SplitterProgrammable/Build_ConveyorAttachmentSplitterProgrammable.Build_ConveyorAttachmentSplitterProgrammable_C` <a id="1d84a16d789d3169cca29a662b15d1a9"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                                                               |
| ------------------ | -------------------------------------------------------------------------------------------------- |
| mBufferInventory   | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mSavedDirections   | `Array`<`EnumProperty`>                                                                            |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe   | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/ConveyorMonitor/Build_ConveyorMonitor.Build_ConveyorMonitor_C` <a id="9a3202f0de8a34c4e0ec5a7d8bd5c361"></a>

**Component type** `ACTOR`

## Properties

| Name                    | Type                                                                                                                                                        |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| mOffsetAlongConveyor    | `Float`                                                                                                                                                     |
| mSnappedSplineBuildable | `ObjectReference`<[`/Game/FactoryGame/Buildable/Factory/ConveyorBeltMk6/Build_ConveyorBeltMk6.Build_ConveyorBeltMk6_C`](#af08bb4d7003f70249e5ca247e432ab2)> |
| mCustomizationData      | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                                                                             |
| mBuiltWithRecipe        | `ObjectReference`                                                                                                                                           |

## `/Game/FactoryGame/Buildable/Factory/StreetLight/Build_StreetLight.Build_StreetLight_C` <a id="8d9c39ef7aabaa4b7b795864720336b3"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                                                                                                                                                                                               |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                                                                                                                                                    |
| mBuiltWithRecipe   | `ObjectReference`                                                                                                                                                                                                                  |
| mLightControlData  | `Union`<`Struct`<[`LightSourceControlData`](#882260b0489081e91de74c64dafcbeb4)>, `Struct`<[`LightSourceControlData`](#882260b0489081e91de74c64dafcbeb4)>, `Struct`<[`LightSourceControlData`](#882260b0489081e91de74c64dafcbeb4)>> |

## `/Game/FactoryGame/Buildable/Factory/CeilingLight/Build_CeilingLight.Build_CeilingLight_C` <a id="695f9f789761131285fe9105ffcd6dbc"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe   | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/Floodlight/Build_FloodlightWall.Build_FloodlightWall_C` <a id="15674156724758cdb4c05f7c04eb1b45"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe   | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/LightsControlPanel/Build_LightsControlPanel.Build_LightsControlPanel_C` <a id="7bd78bd8de5d479fe5b2d68ce8246c34"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                                                                                                                      |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                                                                           |
| mBuiltWithRecipe   | `ObjectReference`                                                                                                                                         |
| mLightControlData  | `Union`<`Struct`<[`LightSourceControlData`](#882260b0489081e91de74c64dafcbeb4)>, `Struct`<[`LightSourceControlData`](#882260b0489081e91de74c64dafcbeb4)>> |

## `/Game/FactoryGame/Buildable/Factory/SignDigital/Build_StandaloneWidgetSign_Small.Build_StandaloneWidgetSign_Small_C` <a id="6ddb57e8d88ddbaa9833d59a939ec104"></a>

**Component type** `ACTOR`

## Properties

| Name                       | Type                                                            |
| -------------------------- | --------------------------------------------------------------- |
| mSoftActivePrefabLayout    | `Tuple`<`ObjectReference`, `Int`>                               |
| mPrefabTextElementSaveData | `Array`<`Struct`<`PrefabTextElementSaveData`>>                  |
| mPrefabIconElementSaveData | `Array`<`Struct`<`PrefabIconElementSaveData`>>                  |
| mForegroundColor           | `Struct`<`LinearColor`>                                         |
| mBackgroundColor           | `Struct`<`LinearColor`>                                         |
| mCustomizationData         | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe           | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/SignDigital/Build_StandaloneWidgetSign_SmallWide.Build_StandaloneWidgetSign_SmallWide_C` <a id="533579ef1d8a896b76e522419d605797"></a>

**Component type** `ACTOR`

## Properties

| Name                       | Type                                                            |
| -------------------------- | --------------------------------------------------------------- |
| mSoftActivePrefabLayout    | `Tuple`<`ObjectReference`, `Int`>                               |
| mPrefabTextElementSaveData | `Array`<`Struct`<`PrefabTextElementSaveData`>>                  |
| mPrefabIconElementSaveData | `Array`<`Struct`<`PrefabIconElementSaveData`>>                  |
| mForegroundColor           | `Struct`<`LinearColor`>                                         |
| mBackgroundColor           | `Struct`<`LinearColor`>                                         |
| mCustomizationData         | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe           | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/SignDigital/Build_StandaloneWidgetSign_SmallVeryWide.Build_StandaloneWidgetSign_SmallVeryWide_C` <a id="ac4b3ff90be8ecb177b8ad985d0ab058"></a>

**Component type** `ACTOR`

## Properties

| Name                       | Type                                                            |
| -------------------------- | --------------------------------------------------------------- |
| mSoftActivePrefabLayout    | `Tuple`<`ObjectReference`, `Int`>                               |
| mPrefabTextElementSaveData | `Array`<`Struct`<`PrefabTextElementSaveData`>>                  |
| mPrefabIconElementSaveData | `Array`<`Struct`<`PrefabIconElementSaveData`>>                  |
| mForegroundColor           | `Struct`<`LinearColor`>                                         |
| mBackgroundColor           | `Struct`<`LinearColor`>                                         |
| mCustomizationData         | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe           | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/SignDigital/Build_StandaloneWidgetSign_Square_Tiny.Build_StandaloneWidgetSign_Square_Tiny_C` <a id="6d3ad2fea313ad0be49ecfbd96a9451b"></a>

**Component type** `ACTOR`

## Properties

| Name                       | Type                                                            |
| -------------------------- | --------------------------------------------------------------- |
| mSoftActivePrefabLayout    | `Tuple`<`ObjectReference`, `Int`>                               |
| mPrefabTextElementSaveData | `Array`<`Struct`<`PrefabTextElementSaveData`>>                  |
| mPrefabIconElementSaveData | `Array`<`Struct`<`PrefabIconElementSaveData`>>                  |
| mForegroundColor           | `Struct`<`LinearColor`>                                         |
| mBackgroundColor           | `Struct`<`LinearColor`>                                         |
| mAuxilaryColor             | `Struct`<`LinearColor`>                                         |
| mCustomizationData         | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe           | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/SignDigital/Build_StandaloneWidgetSign_Square_Small.Build_StandaloneWidgetSign_Square_Small_C` <a id="a9f633f9fce31bec9f498740d149d1e2"></a>

**Component type** `ACTOR`

## Properties

| Name                       | Type                                                            |
| -------------------------- | --------------------------------------------------------------- |
| mSoftActivePrefabLayout    | `Tuple`<`ObjectReference`, `Int`>                               |
| mPrefabTextElementSaveData | `Array`<`Struct`<`PrefabTextElementSaveData`>>                  |
| mPrefabIconElementSaveData | `Array`<`Struct`<`PrefabIconElementSaveData`>>                  |
| mForegroundColor           | `Struct`<`LinearColor`>                                         |
| mBackgroundColor           | `Struct`<`LinearColor`>                                         |
| mAuxilaryColor             | `Struct`<`LinearColor`>                                         |
| mCustomizationData         | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe           | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/SignDigital/Build_StandaloneWidgetSign_Square.Build_StandaloneWidgetSign_Square_C` <a id="dd188ab826c74a9a65ea420b62f03fb9"></a>

**Component type** `ACTOR`

## Properties

| Name                       | Type                                                            |
| -------------------------- | --------------------------------------------------------------- |
| mSoftActivePrefabLayout    | `Tuple`<`ObjectReference`, `Int`>                               |
| mPrefabTextElementSaveData | `Array`<`Struct`<`PrefabTextElementSaveData`>>                  |
| mPrefabIconElementSaveData | `Array`<`Struct`<`PrefabIconElementSaveData`>>                  |
| mForegroundColor           | `Struct`<`LinearColor`>                                         |
| mBackgroundColor           | `Struct`<`LinearColor`>                                         |
| mAuxilaryColor             | `Struct`<`LinearColor`>                                         |
| mCustomizationData         | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe           | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/SignDigital/Build_StandaloneWidgetSign_Medium.Build_StandaloneWidgetSign_Medium_C` <a id="d153e92dbe82600a014df8c3d25dd381"></a>

**Component type** `ACTOR`

## Properties

| Name                       | Type                                                            |
| -------------------------- | --------------------------------------------------------------- |
| mSoftActivePrefabLayout    | `Tuple`<`ObjectReference`, `Int`>                               |
| mPrefabTextElementSaveData | `Array`<`Struct`<`PrefabTextElementSaveData`>>                  |
| mPrefabIconElementSaveData | `Array`<`Struct`<`PrefabIconElementSaveData`>>                  |
| mForegroundColor           | `Struct`<`LinearColor`>                                         |
| mBackgroundColor           | `Struct`<`LinearColor`>                                         |
| mAuxilaryColor             | `Struct`<`LinearColor`>                                         |
| mCustomizationData         | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe           | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/SignDigital/Build_StandaloneWidgetSign_Portrait.Build_StandaloneWidgetSign_Portrait_C` <a id="66f52e1ae3a6e6f73fd9ecbfa3b2aad6"></a>

**Component type** `ACTOR`

## Properties

| Name                       | Type                                                            |
| -------------------------- | --------------------------------------------------------------- |
| mSoftActivePrefabLayout    | `Tuple`<`ObjectReference`, `Int`>                               |
| mPrefabTextElementSaveData | `Array`<`Struct`<`PrefabTextElementSaveData`>>                  |
| mPrefabIconElementSaveData | `Array`<`Struct`<`PrefabIconElementSaveData`>>                  |
| mForegroundColor           | `Struct`<`LinearColor`>                                         |
| mBackgroundColor           | `Struct`<`LinearColor`>                                         |
| mCustomizationData         | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe           | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/SignDigital/Build_StandaloneWidgetSign_Huge.Build_StandaloneWidgetSign_Huge_C` <a id="23314fb3e9c56849282f3ee2ac5e3a86"></a>

**Component type** `ACTOR`

## Properties

| Name                       | Type                                                            |
| -------------------------- | --------------------------------------------------------------- |
| mSoftActivePrefabLayout    | `Tuple`<`ObjectReference`, `Int`>                               |
| mPrefabTextElementSaveData | `Array`<`Struct`<`PrefabTextElementSaveData`>>                  |
| mPrefabIconElementSaveData | `Array`<`Struct`<`PrefabIconElementSaveData`>>                  |
| mForegroundColor           | `Struct`<`LinearColor`>                                         |
| mBackgroundColor           | `Struct`<`LinearColor`>                                         |
| mAuxilaryColor             | `Struct`<`LinearColor`>                                         |
| mCustomizationData         | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe           | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/SignDigital/Build_StandaloneWidgetSign_Large.Build_StandaloneWidgetSign_Large_C` <a id="c85c77bf6e316aa7e76e358fec7a9298"></a>

**Component type** `ACTOR`

## Properties

| Name                       | Type                                                            |
| -------------------------- | --------------------------------------------------------------- |
| mSoftActivePrefabLayout    | `Tuple`<`ObjectReference`, `Int`>                               |
| mPrefabTextElementSaveData | `Array`<`Struct`<`PrefabTextElementSaveData`>>                  |
| mPrefabIconElementSaveData | `Array`<`Struct`<`PrefabIconElementSaveData`>>                  |
| mForegroundColor           | `Struct`<`LinearColor`>                                         |
| mBackgroundColor           | `Struct`<`LinearColor`>                                         |
| mAuxilaryColor             | `Struct`<`LinearColor`>                                         |
| mCustomizationData         | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe           | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/StorageContainerMk2/Build_StorageContainerMk2.Build_StorageContainerMk2_C` <a id="4c79059a1fe6c1d19b4d40f7a7e16d8b"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mStorageInventory            | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mIsProducing                 | `Bool`                                                                                             |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/CentralStorage/Build_CentralStorage.Build_CentralStorage_C` <a id="c627972ae3a108a85d7e6524b304dc4e"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mUploadTimer                 | `Float`                                                                                            |
| mStorageInventory            | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mIsProducing                 | `Bool`                                                                                             |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/StoragePlayer/Build_StorageMedkit.Build_StorageMedkit_C` <a id="dc60c10512e37bd077771adc69ac847a"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mStorageInventory            | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mIsProducing                 | `Bool`                                                                                             |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/StoragePlayer/Build_StorageHazard.Build_StorageHazard_C` <a id="c01059d0cd4b969a34e20dbd3fa694c0"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mStorageInventory            | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mIsProducing                 | `Bool`                                                                                             |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/StorageTank/Build_PipeStorageTank.Build_PipeStorageTank_C` <a id="fddab7360d0f275272c3d113a75f6543"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mIsProducing                 | `Bool`                                                                                             |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/IndustrialFluidContainer/Build_IndustrialTank.Build_IndustrialTank_C` <a id="152fe74c629323e7116bee97ebc4de28"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mIsProducing                 | `Bool`                                                                                             |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/LookoutTower/Build_LookoutTower.Build_LookoutTower_C` <a id="6679c07cc22b24c8e99ed031fc9ef3d3"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe   | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/RadarTower/Build_RadarTower.Build_RadarTower_C` <a id="efe487d8b652f31ffde5ac24f3df4072"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/TruckStation/Build_TruckStation.Build_TruckStation_C` <a id="07403e7c3e8776633bdb2052f6574dca"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mInfo                        | `ObjectReference`<[`/Script/FactoryGame.FGDockingStationInfo`](#295f1939601ed02e105faf2782f151fe)> |
| mInventory                   | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mFuelInventory               | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Script/FactoryGame.FGDockingStationInfo` <a id="295f1939601ed02e105faf2782f151fe"></a>

**Component type** `ACTOR`

## Properties

| Name     | Type                                                                                                                                               |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| mStation | `ObjectReference`<[`/Game/FactoryGame/Buildable/Factory/TruckStation/Build_TruckStation.Build_TruckStation_C`](#07403e7c3e8776633bdb2052f6574dca)> |

## `/Game/FactoryGame/Buildable/Vehicle/Tractor/BP_Tractor.BP_Tractor_C` <a id="8c7b54f82eb3deb4b0ff27bebba451ec"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                                                                                         |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| mFuelInventory     | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)>                           |
| mStorageInventory  | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)>                           |
| mInfo              | `ObjectReference`<[`/Script/FactoryGame.FGWheeledVehicleInfo`](#c3453bc41814a7ab61761d4d0df33783)>                           |
| mTargetList        | `ObjectReference`                                                                                                            |
| mHealthComponent   | `ObjectReference`<[`/Script/FactoryGame.FGHealthComponent`](#d2ef6ea371a1ccbed102d21ee1cffc01)>                              |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                                              |
| mBuiltWithRecipe   | `ObjectReference`                                                                                                            |
| mOwningPlayerState | `ObjectReference`<[`/Game/FactoryGame/Character/Player/BP_PlayerState.BP_PlayerState_C`](#4c001bfe67d1ec5cacd2a1a2c3539513)> |
| mLastSafeLocation  | `Struct`<`Vector`>                                                                                                           |

## `/Script/FactoryGame.FGWheeledVehicleInfo` <a id="c3453bc41814a7ab61761d4d0df33783"></a>

**Component type** `ACTOR`

## Properties

| Name     | Type                                                                                                                                                                                                                                                                                                                                                                                              |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| mVehicle | `Union`<`ObjectReference`<[`/Game/FactoryGame/Buildable/Vehicle/Tractor/BP_Tractor.BP_Tractor_C`](#8c7b54f82eb3deb4b0ff27bebba451ec)>, `ObjectReference`<[`/Game/FactoryGame/Buildable/Vehicle/Truck/BP_Truck.BP_Truck_C`](#203ec0cccdaa63eb364b6bfaf36affcf)>, `ObjectReference`<[`/Game/FactoryGame/Buildable/Vehicle/Explorer/BP_Explorer.BP_Explorer_C`](#79bc5407522d56f154bd23a04e1adc75)>> |

## `/Game/FactoryGame/Buildable/Vehicle/Truck/BP_Truck.BP_Truck_C` <a id="203ec0cccdaa63eb364b6bfaf36affcf"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                                                                                         |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| mFuelInventory     | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)>                           |
| mStorageInventory  | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)>                           |
| mInfo              | `ObjectReference`<[`/Script/FactoryGame.FGWheeledVehicleInfo`](#c3453bc41814a7ab61761d4d0df33783)>                           |
| mTargetList        | `ObjectReference`                                                                                                            |
| mHealthComponent   | `ObjectReference`<[`/Script/FactoryGame.FGHealthComponent`](#d2ef6ea371a1ccbed102d21ee1cffc01)>                              |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                                              |
| mBuiltWithRecipe   | `ObjectReference`                                                                                                            |
| mOwningPlayerState | `ObjectReference`<[`/Game/FactoryGame/Character/Player/BP_PlayerState.BP_PlayerState_C`](#4c001bfe67d1ec5cacd2a1a2c3539513)> |
| mLastSafeLocation  | `Struct`<`Vector`>                                                                                                           |

## `/Game/FactoryGame/Buildable/Vehicle/Explorer/BP_Explorer.BP_Explorer_C` <a id="79bc5407522d56f154bd23a04e1adc75"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                                                                                         |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| mFuelInventory     | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)>                           |
| mStorageInventory  | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)>                           |
| mInfo              | `ObjectReference`<[`/Script/FactoryGame.FGWheeledVehicleInfo`](#c3453bc41814a7ab61761d4d0df33783)>                           |
| mTargetList        | `ObjectReference`                                                                                                            |
| mHealthComponent   | `ObjectReference`<[`/Script/FactoryGame.FGHealthComponent`](#d2ef6ea371a1ccbed102d21ee1cffc01)>                              |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                                              |
| mBuiltWithRecipe   | `ObjectReference`                                                                                                            |
| mOwningPlayerState | `ObjectReference`<[`/Game/FactoryGame/Character/Player/BP_PlayerState.BP_PlayerState_C`](#4c001bfe67d1ec5cacd2a1a2c3539513)> |
| mLastSafeLocation  | `Struct`<`Vector`>                                                                                                           |

## `/Game/FactoryGame/Buildable/Factory/Train/Track/Build_RailroadTrack.Build_RailroadTrack_C` <a id="41c917e27fd4b56671378d7a1609b58d"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mSplineData        | `Array`<`Struct`<`SplinePointData`>>                            |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe   | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/Train/Station/Build_TrainStation.Build_TrainStation_C` <a id="715eacd08a801948677f99f58ca217ad"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                                                                                                    |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| mRailroadTrack               | `ObjectReference`<[`/Game/FactoryGame/Buildable/Factory/Train/Track/Build_RailroadTrackIntegrated.Build_RailroadTrackIntegrated_C`](#7aa7f132090295acb828360d9127599f)> |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)>                                                                      |
| mTimeSinceStartStopProducing | `Float`                                                                                                                                                                 |
| mInventoryPotential          | `ObjectReference`                                                                                                                                                       |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                                                                                         |
| mBuiltWithRecipe             | `ObjectReference`                                                                                                                                                       |

## `/Script/FactoryGame.FGTrainStationIdentifier` <a id="a9689d2fb8c219f08fcf8629a50137db"></a>

**Component type** `ACTOR`

## Properties

| Name         | Type                                                                                                                                                |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| mStation     | `ObjectReference`<[`/Game/FactoryGame/Buildable/Factory/Train/Station/Build_TrainStation.Build_TrainStation_C`](#715eacd08a801948677f99f58ca217ad)> |
| mStationName | `Text`                                                                                                                                              |

## `/Game/FactoryGame/Buildable/Factory/Train/Track/Build_RailroadTrackIntegrated.Build_RailroadTrackIntegrated_C` <a id="7aa7f132090295acb828360d9127599f"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mSplineData        | `Array`<`Struct`<`SplinePointData`>>                            |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe   | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/Train/Station/Build_TrainDockingStation.Build_TrainDockingStation_C` <a id="7e601c8a33a08a309066beb79f9c87a7"></a>

**Component type** `ACTOR`

## Properties

| Name                               | Type                                                                                                                                                                    |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| mInventory                         | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)>                                                                      |
| mTimeSinceLastLoadTransferUpdate   | `Float`                                                                                                                                                                 |
| mTimeSinceLastUnloadTransferUpdate | `Float`                                                                                                                                                                 |
| mRailroadTrack                     | `ObjectReference`<[`/Game/FactoryGame/Buildable/Factory/Train/Track/Build_RailroadTrackIntegrated.Build_RailroadTrackIntegrated_C`](#7aa7f132090295acb828360d9127599f)> |
| mPowerInfo                         | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)>                                                                      |
| mTimeSinceStartStopProducing       | `Float`                                                                                                                                                                 |
| mInventoryPotential                | `ObjectReference`                                                                                                                                                       |
| mCustomizationData                 | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                                                                                         |
| mBuiltWithRecipe                   | `ObjectReference`                                                                                                                                                       |

## `/Game/FactoryGame/Buildable/Factory/Train/Station/Build_TrainDockingStationLiquid.Build_TrainDockingStationLiquid_C` <a id="155ddcf2d849faee338d172ccffc72a3"></a>

**Component type** `ACTOR`

## Properties

| Name                               | Type                                                                                                                                                                    |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| mInventory                         | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)>                                                                      |
| mTimeSinceLastLoadTransferUpdate   | `Float`                                                                                                                                                                 |
| mTimeSinceLastUnloadTransferUpdate | `Float`                                                                                                                                                                 |
| mRailroadTrack                     | `ObjectReference`<[`/Game/FactoryGame/Buildable/Factory/Train/Track/Build_RailroadTrackIntegrated.Build_RailroadTrackIntegrated_C`](#7aa7f132090295acb828360d9127599f)> |
| mPowerInfo                         | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)>                                                                      |
| mTimeSinceStartStopProducing       | `Float`                                                                                                                                                                 |
| mInventoryPotential                | `ObjectReference`                                                                                                                                                       |
| mCustomizationData                 | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                                                                                         |
| mBuiltWithRecipe                   | `ObjectReference`                                                                                                                                                       |

## `/Game/FactoryGame/Buildable/Factory/Train/Station/Build_TrainPlatformEmpty.Build_TrainPlatformEmpty_C` <a id="b3cc270386e4acc3c302a9006358151f"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                                                                                                    |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| mRailroadTrack               | `ObjectReference`<[`/Game/FactoryGame/Buildable/Factory/Train/Track/Build_RailroadTrackIntegrated.Build_RailroadTrackIntegrated_C`](#7aa7f132090295acb828360d9127599f)> |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)>                                                                      |
| mTimeSinceStartStopProducing | `Float`                                                                                                                                                                 |
| mInventoryPotential          | `ObjectReference`                                                                                                                                                       |
| mIsProducing                 | `Bool`                                                                                                                                                                  |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                                                                                         |
| mBuiltWithRecipe             | `ObjectReference`                                                                                                                                                       |

## `/Game/FactoryGame/Buildable/Factory/Train/EndStop/Build_RailroadEndStop.Build_RailroadEndStop_C` <a id="4adebf471a640cc10382dbf226cf3090"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe   | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/Train/Signal/Build_RailroadBlockSignal.Build_RailroadBlockSignal_C` <a id="f707a0a5581fb51736063d722bd982e4"></a>

**Component type** `ACTOR`

## Properties

| Name                 | Type                                                                                                                      |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| mGuardedConnections  | `Array`<`Struct`<`Union`<[`/Script/FactoryGame.FGRailroadTrackConnectionComponent`](#2c45b43d762f093a3665015ef7da7485)>>> |
| mObservedConnections | `Array`<`Struct`<`Union`<[`/Script/FactoryGame.FGRailroadTrackConnectionComponent`](#2c45b43d762f093a3665015ef7da7485)>>> |
| mCustomizationData   | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                                           |
| mBuiltWithRecipe     | `ObjectReference`                                                                                                         |

## `/Game/FactoryGame/Buildable/Factory/Train/Signal/Build_RailroadPathSignal.Build_RailroadPathSignal_C` <a id="d3516d320f4415d89642a765d7eee0d6"></a>

**Component type** `ACTOR`

## Properties

| Name                 | Type                                                                                                                      |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| mGuardedConnections  | `Array`<`Struct`<`Union`<[`/Script/FactoryGame.FGRailroadTrackConnectionComponent`](#2c45b43d762f093a3665015ef7da7485)>>> |
| mObservedConnections | `Array`<`Struct`<`Union`<[`/Script/FactoryGame.FGRailroadTrackConnectionComponent`](#2c45b43d762f093a3665015ef7da7485)>>> |
| mCustomizationData   | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                                           |
| mBuiltWithRecipe     | `ObjectReference`                                                                                                         |

## `/Game/FactoryGame/Buildable/Factory/PipeHyperSupport/Build_PipeHyperSupport.Build_PipeHyperSupport_C` <a id="d594712721af9a8f0f32f5989d7acacb"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mHeight            | `Float`                                                         |
| mColorSlot         | `Byte`                                                          |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe   | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/PipeHyperStart/Build_PipeHyperStart.Build_PipeHyperStart_C` <a id="7668c9184f85e9effc5abeb07938c7b9"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/PipeHyper/Build_PipeHyper.Build_PipeHyper_C` <a id="fe25175d65aa5ef9a67cfd72311a54f3"></a>

**Component type** `ACTOR`

## Properties

| Name                 | Type                                                            |
| -------------------- | --------------------------------------------------------------- |
| mSplineData          | `Array`<`Struct`<`SplinePointData`>>                            |
| mSnappedPassthroughs | `Array`<`Struct`<`ObjectReference`>>                            |
| mCustomizationData   | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe     | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/PipeHyperTJunction/Build_HypertubeTJunction.Build_HypertubeTJunction_C` <a id="1251f7f99dd9b313c5c319a7237a9e70"></a>

**Component type** `ACTOR`

## Properties

| Name                             | Type                                                                                               |
| -------------------------------- | -------------------------------------------------------------------------------------------------- |
| mBuiltWithPipelineRecipe         | `ObjectReference`                                                                                  |
| mBuiltWithPipelineCostMultiplier | `Int`                                                                                              |
| mPowerInfo                       | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing     | `Float`                                                                                            |
| mInventoryPotential              | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mIsProducing                     | `Bool`                                                                                             |
| mCustomizationData               | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe                 | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/PipeHyperJunction/Build_HyperTubeJunction.Build_HyperTubeJunction_C` <a id="8de6669d73d61ccc61eff7e7e5a240f9"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mIsProducing                 | `Bool`                                                                                             |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/PipelineSupport/Build_HyperPoleStackable.Build_HyperPoleStackable_C` <a id="9fabe111295dc0176ab3dce2791bf4ad"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe   | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/HyperTubeWallSupport/Build_HyperTubeWallSupport.Build_HyperTubeWallSupport_C` <a id="77897d56578a11014d334ffb4d867e85"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe   | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/FoundationPassthrough/Build_FoundationPassthrough_Hypertube.Build_FoundationPassthrough_Hypertube_C` <a id="a19a4f19be2fb74a0538c20f5769e0aa"></a>

**Component type** `ACTOR`

## Properties

| Name                      | Type                                                                                                         |
| ------------------------- | ------------------------------------------------------------------------------------------------------------ |
| mConnection0              | `ObjectReference`<[`/Script/FactoryGame.FGPipeConnectionComponentHyper`](#a7fec9e0f15489bb873fe11129880d28)> |
| mConnection1              | `ObjectReference`<[`/Script/FactoryGame.FGPipeConnectionComponentHyper`](#a7fec9e0f15489bb873fe11129880d28)> |
| mSnappedBuildingThickness | `Float`                                                                                                      |
| mCustomizationData        | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                              |
| mBuiltWithRecipe          | `ObjectReference`                                                                                            |

## `/Game/FactoryGame/Buildable/Factory/Portal/Build_Portal.Build_Portal_C` <a id="76a3559a86332108d8d2a5a8d61d6138"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mFuelInventory               | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mCachedFactoryTickData       | [`FGPortalCachedFactoryTickData`](#bb7f3cb99e19336c996c2aaad6ce4838)                               |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/Portal/Build_PortalSatellite.Build_PortalSatellite_C` <a id="1a3ac5f3961aa7bf322a6016a0649880"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mCachedFactoryTickData       | [`FGPortalCachedFactoryTickData`](#bb7f3cb99e19336c996c2aaad6ce4838)                               |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Game/FactoryGame/Buildable/Factory/Elevator/Build_Elevator.Build_Elevator_C` <a id="9a4f15f614b5a853b1630f4abd2b5991"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                                                                       |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| mElevatorCabin               | `ObjectReference`<[`/Game/FactoryGame/Buildable/Factory/Elevator/BP_ElevatorCabin.BP_ElevatorCabin_C`](#5b73508f96f242c071bda5157b5b9ccb)> |
| mHeight                      | `Float`                                                                                                                                    |
| mFloorStopInfos              | `Array`<`Struct`<`ElevatorFloorStopInfo`>>                                                                                                 |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)>                                         |
| mTimeSinceStartStopProducing | `Float`                                                                                                                                    |
| mIsProductionPaused          | `Bool`                                                                                                                                     |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)>                                         |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                                                            |
| mBuiltWithRecipe             | `ObjectReference`                                                                                                                          |

## `/Game/FactoryGame/Buildable/Factory/Elevator/Build_ElevatorFloorStop.Build_ElevatorFloorStop_C` <a id="c7902e457c389891906f000b5c2cd491"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7) |
| mBuiltWithRecipe   | `ObjectReference`                                               |

## `/Game/FactoryGame/Buildable/Factory/Elevator/BP_ElevatorCabin.BP_ElevatorCabin_C` <a id="5b73508f96f242c071bda5157b5b9ccb"></a>

**Component type** `ACTOR`

## `/Game/FactoryGame/Character/Creature/Enemy/Hog/Char_Hog.Char_Hog_C` <a id="51acaa1a61f4b8251eed733a9894a132"></a>

**Component type** `ACTOR`

## Properties

| Name                  | Type                                                                                                                                   |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| mHealthComponent      | `ObjectReference`<[`/Script/FactoryGame.FGHealthComponent`](#d2ef6ea371a1ccbed102d21ee1cffc01)>                                        |
| mLastSafeLoadLocation | `Struct`<`Vector`>                                                                                                                     |
| mSpline               | `ObjectReference`                                                                                                                      |
| mOwningSpawner        | `ObjectReference`<[`/Game/FactoryGame/Character/Creature/BP_CreatureSpawner.BP_CreatureSpawner_C`](#300f34b684b8e9e734a8d1aca74e0b2a)> |

## `/Game/FactoryGame/Buildable/Factory/BlueprintDesigner/Build_BlueprintDesigner.Build_BlueprintDesigner_C` <a id="64ba976ff7c13d6a78b97d48874edd7d"></a>

**Component type** `ACTOR`

## Properties

| Name               | Type                                                                                                                                                                                                                        |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| mStorage           | `ObjectReference`<[`/Game/FactoryGame/Buildable/Factory/StoragePlayer/Build_StorageBlueprint.Build_StorageBlueprint_C`](#c37d05dec915a36424fea249e7253738)>                                                                 |
| mBuildables        | `Array`<`Struct`<`Union`<`/Game/FactoryGame/Buildable/Factory/ConveyorPole/Build_ConveyorPole.Build_ConveyorPole_C`, `/Game/FactoryGame/Buildable/Factory/ConveyorBeltMk1/Build_ConveyorBeltMk1.Build_ConveyorBeltMk1_C`>>> |
| mCurrentRecordData | [`BlueprintRecord`](#97cb3c52814c3296b485b314f5d4eaf7)                                                                                                                                                                      |
| mCustomizationData | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                                                                                                                                             |
| mBuiltWithRecipe   | `ObjectReference`                                                                                                                                                                                                           |

## `/Game/FactoryGame/Buildable/Factory/StoragePlayer/Build_StorageBlueprint.Build_StorageBlueprint_C` <a id="c37d05dec915a36424fea249e7253738"></a>

**Component type** `ACTOR`

## Properties

| Name                         | Type                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| mStorageInventory            | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mPowerInfo                   | `ObjectReference`<[`/Script/FactoryGame.FGPowerInfoComponent`](#3e8784c9adfe12165c1b84b89f26722e)> |
| mTimeSinceStartStopProducing | `Float`                                                                                            |
| mInventoryPotential          | `ObjectReference`<[`/Script/FactoryGame.FGInventoryComponent`](#53d1ef1c40a8b7ebe5a1830ebf2cac40)> |
| mIsProducing                 | `Bool`                                                                                             |
| mCustomizationData           | [`FactoryCustomizationData`](#3907ccdfb651047144091e52e10390c7)                                    |
| mBuiltWithRecipe             | `ObjectReference`                                                                                  |

## `/Script/FactoryGame.FGPowerCircuit` <a id="0ddb98cf34a68ae1903a1010f5c0a8e6"></a>

**Component type** `COMPONENT`

## Properties

| Name        | Type                                                                                                              |
| ----------- | ----------------------------------------------------------------------------------------------------------------- |
| mCircuitID  | `Int`                                                                                                             |
| mComponents | `Array`<`Struct`<`Union`<[`/Script/FactoryGame.FGPowerConnectionComponent`](#31b818765a0cf23f5e6dc6a408ea2768)>>> |

## `/Script/FactoryGame.FGHighlightedMarker_MapMarker` <a id="1d93764e1b0b912afba78502d3c9d4bb"></a>

**Component type** `COMPONENT`

## Properties

| Name       | Type                                             |
| ---------- | ------------------------------------------------ |
| mMapMarker | [`MapMarker`](#876da7352e32a199a1eab9f0a0864669) |

## `/Script/FactoryGame.FGPlayerHotbar` <a id="0b7c1c7032b9ea87265ea8ba1481bdef"></a>

**Component type** `COMPONENT`

## Properties

| Name       | Type                                                                                                                                                                                                                                                           |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| mShortcuts | `Union`<`Array`<`Struct`<`Union`<[`/Script/FactoryGame.FGRecipeShortcut`](#01726ecec9cdf6f0ac6c7a38761ed930)>>>, `Array`<`Struct`<`ObjectReference`>>, `Array`<`Struct`<`Union`<[`/Script/FactoryGame.FGEmoteShortcut`](#0aa5edf3df6f2117ad44b4c510097223)>>>> |

## `/Script/FactoryGame.FGShoppingListComponent` <a id="69b9138f542b129c542963d4e4c41bcd"></a>

**Component type** `COMPONENT`

## `/Script/FactoryGame.FGInventoryComponentEquipment` <a id="c4235f10d403f57878a78675a193aa63"></a>

**Component type** `COMPONENT`

## Properties

| Name                    | Type                                 |
| ----------------------- | ------------------------------------ |
| mSlottedInEquipments    | `Array`<`Struct`<`ObjectReference`>> |
| mAdjustedSizeDiff       | `Int`                                |
| mInventoryStacks        | `Array`<`Struct`<`InventoryStack`>>  |
| mArbitrarySlotSizes     | `Array`<`IntProperty`>               |
| mAllowedItemDescriptors | `Array`<`Struct`<`ObjectReference`>> |

## `/Script/FactoryGame.FGInventoryComponentTrash` <a id="8436ded31224c2aa2112a1e1a2bb0fa9"></a>

**Component type** `COMPONENT`

## `/Script/FactoryGame.FGHealthComponent` <a id="d2ef6ea371a1ccbed102d21ee1cffc01"></a>

**Component type** `COMPONENT`

## `/Script/FactoryGame.FGFactoryConnectionComponent` <a id="a8e0e526befbb4d556fb2cc9cfdf8db0"></a>

**Component type** `COMPONENT`

## Properties

| Name                | Type                                                                                                       |
| ------------------- | ---------------------------------------------------------------------------------------------------------- |
| mConnectedComponent | `ObjectReference`<[`/Script/FactoryGame.FGFactoryConnectionComponent`](#a8e0e526befbb4d556fb2cc9cfdf8db0)> |

## `/Script/FactoryGame.FGFactoryLegsComponent` <a id="d97c885e8421a25037fd6c412f67a9cb"></a>

**Component type** `COMPONENT`

## Properties

| Name              | Type                            |
| ----------------- | ------------------------------- |
| mCachedFeetOffset | `Array`<`Struct`<`FeetOffset`>> |

## `/Script/FactoryGame.FGPipeConnectionFactory` <a id="e0cccef0faa5d243b6568aed256337be"></a>

**Component type** `COMPONENT`

## `/Script/FactoryGame.FGPipeConnectionComponent` <a id="55a9b1f07fd285508cbcb6f397f29af5"></a>

**Component type** `COMPONENT`

## Properties

| Name                | Type                                                                                                    |
| ------------------- | ------------------------------------------------------------------------------------------------------- |
| mPipeNetworkID      | `Int`                                                                                                   |
| mConnectedComponent | `ObjectReference`<[`/Script/FactoryGame.FGPipeConnectionComponent`](#55a9b1f07fd285508cbcb6f397f29af5)> |

## `/Script/FactoryGame.FGRailroadTrackConnectionComponent` <a id="2c45b43d762f093a3665015ef7da7485"></a>

**Component type** `COMPONENT`

## Properties

| Name                 | Type                                                                                                                      |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| mConnectedComponents | `Array`<`Struct`<`Union`<[`/Script/FactoryGame.FGRailroadTrackConnectionComponent`](#2c45b43d762f093a3665015ef7da7485)>>> |

## `/Script/FactoryGame.FGTrainPlatformConnection` <a id="d15f5884c4957920d0f9928fbed83352"></a>

**Component type** `COMPONENT`

## Properties

| Name                     | Type                                                                                                             |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| mRailroadTrackConnection | `ObjectReference`<[`/Script/FactoryGame.FGRailroadTrackConnectionComponent`](#2c45b43d762f093a3665015ef7da7485)> |
| mConnectedTo             | `ObjectReference`<[`/Script/FactoryGame.FGTrainPlatformConnection`](#d15f5884c4957920d0f9928fbed83352)>          |

## `/Script/FactoryGame.FGPipeConnectionComponentHyper` <a id="a7fec9e0f15489bb873fe11129880d28"></a>

**Component type** `COMPONENT`

## Properties

| Name                | Type                                                                                                         |
| ------------------- | ------------------------------------------------------------------------------------------------------------ |
| mConnectedComponent | `ObjectReference`<[`/Script/FactoryGame.FGPipeConnectionComponentHyper`](#a7fec9e0f15489bb873fe11129880d28)> |

## `/Script/FactoryGame.FGRecipeShortcut` <a id="01726ecec9cdf6f0ac6c7a38761ed930"></a>

**Component type** `COMPONENT`

## Properties

| Name              | Type              |
| ----------------- | ----------------- |
| mRecipeToActivate | `ObjectReference` |
| mShortcutIndex    | `Int`             |

## `/Script/FactoryGame.FGEmoteShortcut` <a id="0aa5edf3df6f2117ad44b4c510097223"></a>

**Component type** `COMPONENT`

## Properties

| Name             | Type              |
| ---------------- | ----------------- |
| mEmoteToActivate | `ObjectReference` |

# Typed Data

## InventoryStack<a id="4bbe9209e8486bf4b08ef002709eeeee"></a>

| Name     | Type                      |
| -------- | ------------------------- |
| Item     | `Struct`<`InventoryItem`> |
| NumItems | `Int`                     |

## FactoryCustomizationData<a id="3907ccdfb651047144091e52e10390c7"></a>

| Name       | Type              |
| ---------- | ----------------- |
| SwatchDesc | `ObjectReference` |

## PlayerRules<a id="81b332f2070f04404a9ef41e7eafd9a3"></a>

| Name           | Type   |
| -------------- | ------ |
| HasInitialized | `Bool` |
| NoBuildCost    | `Bool` |
| FlightMode     | `Bool` |
| GodMode        | `Bool` |

## ShoppingListSettings<a id="178bbc1d599e54b7e500b56ea855f60d"></a>

| Name | Type    |
| ---- | ------- |
| Size | `Float` |

## PlayerCustomizationData<a id="838788afcbb3999f32a37bfd88511a60"></a>

| Name                       | Type                                 |
| -------------------------- | ------------------------------------ |
| PrimaryColor               | `Struct`<`LinearColor`>              |
| SecondaryColor             | `Struct`<`LinearColor`>              |
| DetailColor                | `Struct`<`LinearColor`>              |
| HelmetCustomizationDesc    | `ObjectReference`                    |
| TrinketCustomizationDesc   | `ObjectReference`                    |
| EquipmentCustomizationDesc | `Array`<`Struct`<`ObjectReference`>> |

## Transform<a id="2ff4148554480a37f85efd299df04850"></a>

| Name        | Type               |
| ----------- | ------------------ |
| Rotation    | `Struct`<`Quat`>   |
| Translation | `Struct`<`Vector`> |

## FGPortalCachedFactoryTickData<a id="bb7f3cb99e19336c996c2aaad6ce4838"></a>

| Name                    | Type    |
| ----------------------- | ------- |
| mCachedPowerConsumption | `Float` |

## TopLevelAssetPath<a id="b8eb7d49028f2861323b205e72f27b8a"></a>

| Name        | Type           |
| ----------- | -------------- |
| PackageName | `NameProperty` |
| AssetName   | `NameProperty` |

## PersistentGlobalIconId<a id="39a413951cb07a63b3d79117e931cc19"></a>

| Name        | Type                                                     |
| ----------- | -------------------------------------------------------- |
| IconLibrary | [`TopLevelAssetPath`](#b8eb7d49028f2861323b205e72f27b8a) |
| IconID      | `Int`                                                    |

## BlueprintRecord<a id="97cb3c52814c3296b485b314f5d4eaf7"></a>

| Name                 | Type                                                          |
| -------------------- | ------------------------------------------------------------- |
| BlueprintName        | `Str`                                                         |
| BlueprintDescription | `Str`                                                         |
| IconID               | [`PersistentGlobalIconId`](#39a413951cb07a63b3d79117e931cc19) |
| Color                | `Struct`<`LinearColor`>                                       |
| lastEditedBy         | `Array`<`Struct`<`LocalUserNetIdBundle`>>                     |

## Vector_NetQuantize<a id="56605402e390a6c6eebe9c5560cbb4dd"></a>

| Name | Type     |
| ---- | -------- |
| X    | `Double` |
| Y    | `Double` |
| Z    | `Double` |

## MapMarker<a id="876da7352e32a199a1eab9f0a0864669"></a>

| Name                    | Type                                                      |
| ----------------------- | --------------------------------------------------------- |
| markerGuid              | `Struct`<`Guid`>                                          |
| Location                | [`Vector_NetQuantize`](#56605402e390a6c6eebe9c5560cbb4dd) |
| Name                    | `Str`                                                     |
| MapMarkerType           | `Enum`<`ERepresentationType`>                             |
| IconID                  | `Int`                                                     |
| Color                   | `Struct`<`LinearColor`>                                   |
| MarkerPlacedByAccountID | `Str`                                                     |
