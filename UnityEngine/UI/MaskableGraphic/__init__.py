from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class MaskableGraphic:
    def __new__(cls, arg1=None):
        '''
        :returns: MaskableGraphic
        :rtype: UnityEngine.UI.MaskableGraphic
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
    def get_onCullStateChanged():
        '''
        :returns: MaskableGraphic+CullStateChangedEvent
        :rtype: UnityEngine.MaskableGraphic+CullStateChangedEvent
        '''
        pass

    @staticmethod
    def set_onCullStateChanged(arg1):
        '''
        :param arg1: CullStateChangedEvent
        :type arg1: UnityEngine.CullStateChangedEvent
        '''
        pass

    @staticmethod
    def get_maskable():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_maskable(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def GetModifiedMaterial(arg1):
        '''
        :param arg1: Material
        :type arg1: UnityEngine.Material
        :returns: Material
        :rtype: UnityEngine.Material
        '''
        pass

    @staticmethod
    def Cull(arg1, arg2):
        '''
        :param arg1: Rect
        :type arg1: UnityEngine.Rect
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        '''
        pass

    @staticmethod
    def SetClipRect(arg1, arg2):
        '''
        :param arg1: Rect
        :type arg1: UnityEngine.Rect
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        '''
        pass

    @staticmethod
    def RecalculateClipping():
        pass

    @staticmethod
    def RecalculateMasking():
        pass

    @staticmethod
    def get_color():
        '''
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def set_color(arg1):
        '''
        :param arg1: Color
        :type arg1: UnityEngine.Color
        '''
        pass

    @staticmethod
    def get_raycastTarget():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_raycastTarget(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def SetAllDirty():
        pass

    @staticmethod
    def SetLayoutDirty():
        pass

    @staticmethod
    def SetVerticesDirty():
        pass

    @staticmethod
    def SetMaterialDirty():
        pass

    @staticmethod
    def get_depth():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def get_rectTransform():
        '''
        :returns: RectTransform
        :rtype: UnityEngine.RectTransform
        '''
        pass

    @staticmethod
    def get_canvas():
        '''
        :returns: Canvas
        :rtype: UnityEngine.Canvas
        '''
        pass

    @staticmethod
    def get_canvasRenderer():
        '''
        :returns: CanvasRenderer
        :rtype: UnityEngine.CanvasRenderer
        '''
        pass

    @staticmethod
    def get_defaultMaterial():
        '''
        :returns: Material
        :rtype: UnityEngine.Material
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
    def get_materialForRendering():
        '''
        :returns: Material
        :rtype: UnityEngine.Material
        '''
        pass

    @staticmethod
    def get_mainTexture():
        '''
        :returns: Texture
        :rtype: UnityEngine.Texture
        '''
        pass

    @staticmethod
    def OnCullingChanged():
        pass

    @staticmethod
    def Rebuild(arg1):
        '''
        :param arg1: CanvasUpdate
        :type arg1: UnityEngine.CanvasUpdate
        '''
        pass

    @staticmethod
    def LayoutComplete():
        pass

    @staticmethod
    def GraphicUpdateComplete():
        pass

    @staticmethod
    def SetNativeSize():
        pass

    @staticmethod
    def Raycast(arg1, arg2):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Camera
        :type arg2: UnityEngine.Camera
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def PixelAdjustPoint(arg1):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :returns: Vector2
        :rtype: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def GetPixelAdjustedRect():
        '''
        :returns: Rect
        :rtype: UnityEngine.Rect
        '''
        pass

    @staticmethod
    @overload
    def CrossFadeColor(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Color
        :type arg1: UnityEngine.Color
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Boolean
        :type arg3: System.Boolean or bool
        :param arg4: Boolean
        :type arg4: System.Boolean or bool
        '''
        pass

    @staticmethod
    @overload
    def CrossFadeColor(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Color
        :type arg1: UnityEngine.Color
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Boolean
        :type arg3: System.Boolean or bool
        :param arg4: Boolean
        :type arg4: System.Boolean or bool
        :param arg5: Boolean
        :type arg5: System.Boolean or bool
        '''
        pass

    @staticmethod
    def CrossFadeColor(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None):
        pass

    @staticmethod
    def CrossFadeAlpha(arg1, arg2, arg3):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Boolean
        :type arg3: System.Boolean or bool
        '''
        pass

    @staticmethod
    def IsActive():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def IsDestroyed():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
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
