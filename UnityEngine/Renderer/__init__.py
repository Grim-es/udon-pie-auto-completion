from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class Renderer:
    def __new__(cls, arg1=None):
        '''
        :returns: Renderer
        :rtype: UnityEngine.Renderer
        '''
        pass

    @staticmethod
    def op_Implicit(arg1):
        '''
        :param arg1: Object
        :type arg1: UnityEngine.Object
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def op_Equality(arg1, arg2):
        '''
        :param arg1: Object
        :type arg1: UnityEngine.Object
        :param arg2: Object
        :type arg2: UnityEngine.Object
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def op_Inequality(arg1, arg2):
        '''
        :param arg1: Object
        :type arg1: UnityEngine.Object
        :param arg2: Object
        :type arg2: UnityEngine.Object
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_lightmapIndex():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def set_lightmapIndex(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    def get_realtimeLightmapIndex():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def set_realtimeLightmapIndex(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    def get_lightmapScaleOffset():
        '''
        :returns: Vector4
        :rtype: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    def set_lightmapScaleOffset(arg1):
        '''
        :param arg1: Vector4
        :type arg1: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    def get_realtimeLightmapScaleOffset():
        '''
        :returns: Vector4
        :rtype: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    def set_realtimeLightmapScaleOffset(arg1):
        '''
        :param arg1: Vector4
        :type arg1: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    def get_materials():
        '''
        :returns: MaterialArray
        :rtype: UnityEngine.MaterialArray
        '''
        pass

    @staticmethod
    def set_materials(arg1):
        '''
        :param arg1: MaterialArray
        :type arg1: UnityEngine.MaterialArray
        '''
        pass

    @staticmethod
    def get_material():
        '''
        :returns: Material
        :rtype: UnityEngine.Material
        '''
        pass

    @staticmethod
    def set_material(arg1):
        '''
        :param arg1: Material
        :type arg1: UnityEngine.Material
        '''
        pass

    @staticmethod
    def get_sharedMaterial():
        '''
        :returns: Material
        :rtype: UnityEngine.Material
        '''
        pass

    @staticmethod
    def set_sharedMaterial(arg1):
        '''
        :param arg1: Material
        :type arg1: UnityEngine.Material
        '''
        pass

    @staticmethod
    def get_sharedMaterials():
        '''
        :returns: MaterialArray
        :rtype: UnityEngine.MaterialArray
        '''
        pass

    @staticmethod
    def set_sharedMaterials(arg1):
        '''
        :param arg1: MaterialArray
        :type arg1: UnityEngine.MaterialArray
        '''
        pass

    @staticmethod
    def GetMaterials(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    def GetSharedMaterials(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    def GetClosestReflectionProbes(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericListUnityEngineRenderingReflectionProbeBlendInfo.SystemCollectionsGenericListUnityEngineRenderingReflectionProbeBlendInfo
        '''
        pass

    @staticmethod
    def get_bounds():
        '''
        :returns: Bounds
        :rtype: UnityEngine.Bounds
        '''
        pass

    @staticmethod
    def HasPropertyBlock():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def SetPropertyBlock(arg1):
        '''
        :param arg1: MaterialPropertyBlock
        :type arg1: UnityEngine.MaterialPropertyBlock
        '''
        pass

    @staticmethod
    @overload
    def SetPropertyBlock(arg1, arg2):
        '''
        :param arg1: MaterialPropertyBlock
        :type arg1: UnityEngine.MaterialPropertyBlock
        :param arg2: Int32
        :type arg2: System.Int32 or int
        '''
        pass

    @staticmethod
    def SetPropertyBlock(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def GetPropertyBlock(arg1):
        '''
        :param arg1: MaterialPropertyBlock
        :type arg1: UnityEngine.MaterialPropertyBlock
        '''
        pass

    @staticmethod
    @overload
    def GetPropertyBlock(arg1, arg2):
        '''
        :param arg1: MaterialPropertyBlock
        :type arg1: UnityEngine.MaterialPropertyBlock
        :param arg2: Int32
        :type arg2: System.Int32 or int
        '''
        pass

    @staticmethod
    def GetPropertyBlock(arg1=None, arg2=None):
        pass

    @staticmethod
    def get_enabled():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_enabled(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_isVisible():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_shadowCastingMode():
        '''
        :returns: ShadowCastingMode
        :rtype: UnityEngine.ShadowCastingMode
        '''
        pass

    @staticmethod
    def set_shadowCastingMode(arg1):
        '''
        :param arg1: ShadowCastingMode
        :type arg1: UnityEngine.ShadowCastingMode
        '''
        pass

    @staticmethod
    def get_receiveShadows():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_receiveShadows(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_motionVectorGenerationMode():
        '''
        :returns: MotionVectorGenerationMode
        :rtype: UnityEngine.MotionVectorGenerationMode
        '''
        pass

    @staticmethod
    def set_motionVectorGenerationMode(arg1):
        '''
        :param arg1: MotionVectorGenerationMode
        :type arg1: UnityEngine.MotionVectorGenerationMode
        '''
        pass

    @staticmethod
    def get_lightProbeUsage():
        '''
        :returns: LightProbeUsage
        :rtype: UnityEngine.LightProbeUsage
        '''
        pass

    @staticmethod
    def set_lightProbeUsage(arg1):
        '''
        :param arg1: LightProbeUsage
        :type arg1: UnityEngine.LightProbeUsage
        '''
        pass

    @staticmethod
    def get_reflectionProbeUsage():
        '''
        :returns: Undefined variable
        :rtype: UnityEngineRenderingReflectionProbeUsage
        '''
        pass

    @staticmethod
    def set_reflectionProbeUsage(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: UnityEngineRenderingReflectionProbeUsage.UnityEngineRenderingReflectionProbeUsage
        '''
        pass

    @staticmethod
    def get_renderingLayerMask():
        '''
        :returns: UInt32
        :rtype: System.UInt32
        '''
        pass

    @staticmethod
    def set_renderingLayerMask(arg1):
        '''
        :param arg1: UInt32
        :type arg1: System.UInt32
        '''
        pass

    @staticmethod
    def get_rendererPriority():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def set_rendererPriority(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    def get_sortingLayerName():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def set_sortingLayerName(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        '''
        pass

    @staticmethod
    def get_sortingLayerID():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def set_sortingLayerID(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    def get_sortingOrder():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def set_sortingOrder(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    def get_allowOcclusionWhenDynamic():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_allowOcclusionWhenDynamic(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_isPartOfStaticBatch():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_worldToLocalMatrix():
        '''
        :returns: Matrix4x4
        :rtype: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    def get_localToWorldMatrix():
        '''
        :returns: Matrix4x4
        :rtype: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    def get_lightProbeProxyVolumeOverride():
        '''
        :returns: GameObject
        :rtype: UnityEngine.GameObject
        '''
        pass

    @staticmethod
    def set_lightProbeProxyVolumeOverride(arg1):
        '''
        :param arg1: GameObject
        :type arg1: UnityEngine.GameObject
        '''
        pass

    @staticmethod
    def get_probeAnchor():
        '''
        :returns: Transform
        :rtype: UnityEngine.Transform
        '''
        pass

    @staticmethod
    def set_probeAnchor(arg1):
        '''
        :param arg1: Transform
        :type arg1: UnityEngine.Transform
        '''
        pass

    @staticmethod
    def get_transform():
        '''
        :returns: Transform
        :rtype: UnityEngine.Transform
        '''
        pass

    @staticmethod
    def get_gameObject():
        '''
        :returns: GameObject
        :rtype: UnityEngine.GameObject
        '''
        pass

    @staticmethod
    @overload
    def GetComponent(arg1):
        '''
        :param arg1: Type
        :type arg1: System.Type
        :returns: Component
        :rtype: UnityEngine.Component
        '''
        pass

    @staticmethod
    @overload
    def GetComponent(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Component
        :rtype: UnityEngine.Component
        '''
        pass

    @staticmethod
    def GetComponent(arg1=None):
        pass

    @staticmethod
    @overload
    def GetComponentInChildren(arg1, arg2):
        '''
        :param arg1: Type
        :type arg1: System.Type
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        :returns: Component
        :rtype: UnityEngine.Component
        '''
        pass

    @staticmethod
    @overload
    def GetComponentInChildren(arg1):
        '''
        :param arg1: Type
        :type arg1: System.Type
        :returns: Component
        :rtype: UnityEngine.Component
        '''
        pass

    @staticmethod
    def GetComponentInChildren(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def GetComponentsInChildren(arg1, arg2):
        '''
        :param arg1: Type
        :type arg1: System.Type
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        :returns: ComponentArray
        :rtype: UnityEngine.ComponentArray
        '''
        pass

    @staticmethod
    @overload
    def GetComponentsInChildren(arg1):
        '''
        :param arg1: Type
        :type arg1: System.Type
        :returns: ComponentArray
        :rtype: UnityEngine.ComponentArray
        '''
        pass

    @staticmethod
    @overload
    def GetComponentsInChildren(arg1, arg2):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :param arg2: Undefined variable
        :type arg2: ListT.ListT
        '''
        pass

    @staticmethod
    @overload
    def GetComponentsInChildren(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: ListT.ListT
        '''
        pass

    @staticmethod
    def GetComponentsInChildren(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def GetComponentInParent(arg1):
        '''
        :param arg1: Type
        :type arg1: System.Type
        :returns: Component
        :rtype: UnityEngine.Component
        '''
        pass

    @staticmethod
    def GetComponentInParent(arg1=None):
        pass

    @staticmethod
    @overload
    def GetComponentsInParent(arg1, arg2):
        '''
        :param arg1: Type
        :type arg1: System.Type
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        :returns: ComponentArray
        :rtype: UnityEngine.ComponentArray
        '''
        pass

    @staticmethod
    @overload
    def GetComponentsInParent(arg1):
        '''
        :param arg1: Type
        :type arg1: System.Type
        :returns: ComponentArray
        :rtype: UnityEngine.ComponentArray
        '''
        pass

    @staticmethod
    @overload
    def GetComponentsInParent(arg1, arg2):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :param arg2: Undefined variable
        :type arg2: ListT.ListT
        '''
        pass

    @staticmethod
    def GetComponentsInParent(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def GetComponents(arg1):
        '''
        :param arg1: Type
        :type arg1: System.Type
        :returns: ComponentArray
        :rtype: UnityEngine.ComponentArray
        '''
        pass

    @staticmethod
    @overload
    def GetComponents(arg1, arg2):
        '''
        :param arg1: Type
        :type arg1: System.Type
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    @overload
    def GetComponents(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: ListT.ListT
        '''
        pass

    @staticmethod
    def GetComponents(arg1=None, arg2=None):
        pass

    @staticmethod
    def GetInstanceID():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def GetHashCode():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def Equals(arg1):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_name():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def set_name(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        '''
        pass

    @staticmethod
    def ToString():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def GetType():
        '''
        :returns: Type
        :rtype: System.Type
        '''
        pass
