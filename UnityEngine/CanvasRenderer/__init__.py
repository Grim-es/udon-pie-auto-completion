from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class CanvasRenderer:
    def __new__(cls, arg1=None):
        '''
        :returns: CanvasRenderer
        :rtype: UnityEngine.CanvasRenderer
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
    def get_hasPopInstruction():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_hasPopInstruction(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_materialCount():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def set_materialCount(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    def get_popMaterialCount():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def set_popMaterialCount(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    def get_absoluteDepth():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def get_hasMoved():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_cullTransparentMesh():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_cullTransparentMesh(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_hasRectClipping():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_relativeDepth():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def get_cull():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_cull(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def SetColor(arg1):
        '''
        :param arg1: Color
        :type arg1: UnityEngine.Color
        '''
        pass

    @staticmethod
    def GetColor():
        '''
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def EnableRectClipping(arg1):
        '''
        :param arg1: Rect
        :type arg1: UnityEngine.Rect
        '''
        pass

    @staticmethod
    def DisableRectClipping():
        pass

    @staticmethod
    @overload
    def SetMaterial(arg1, arg2):
        '''
        :param arg1: Material
        :type arg1: UnityEngine.Material
        :param arg2: Int32
        :type arg2: System.Int32 or int
        '''
        pass

    @staticmethod
    @overload
    def SetMaterial(arg1, arg2):
        '''
        :param arg1: Material
        :type arg1: UnityEngine.Material
        :param arg2: Texture
        :type arg2: UnityEngine.Texture
        '''
        pass

    @staticmethod
    def SetMaterial(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def GetMaterial(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Material
        :rtype: UnityEngine.Material
        '''
        pass

    @staticmethod
    @overload
    def GetMaterial():
        '''
        :returns: Material
        :rtype: UnityEngine.Material
        '''
        pass

    @staticmethod
    def GetMaterial(arg1=None):
        pass

    @staticmethod
    def SetPopMaterial(arg1, arg2):
        '''
        :param arg1: Material
        :type arg1: UnityEngine.Material
        :param arg2: Int32
        :type arg2: System.Int32 or int
        '''
        pass

    @staticmethod
    def GetPopMaterial(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Material
        :rtype: UnityEngine.Material
        '''
        pass

    @staticmethod
    def SetTexture(arg1):
        '''
        :param arg1: Texture
        :type arg1: UnityEngine.Texture
        '''
        pass

    @staticmethod
    def SetAlphaTexture(arg1):
        '''
        :param arg1: Texture
        :type arg1: UnityEngine.Texture
        '''
        pass

    @staticmethod
    def SetMesh(arg1):
        '''
        :param arg1: Mesh
        :type arg1: UnityEngine.Mesh
        '''
        pass

    @staticmethod
    def Clear():
        pass

    @staticmethod
    def GetAlpha():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def SetAlpha(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def GetInheritedAlpha():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def SplitUIVertexStreams(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg3: Undefined variable
        :type arg3: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg4: Undefined variable
        :type arg4: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg5: Undefined variable
        :type arg5: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg6: Undefined variable
        :type arg6: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg7: Undefined variable
        :type arg7: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg8: Undefined variable
        :type arg8: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    @overload
    def SplitUIVertexStreams(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg3: Undefined variable
        :type arg3: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg4: Undefined variable
        :type arg4: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg5: Undefined variable
        :type arg5: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg6: Undefined variable
        :type arg6: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg7: Undefined variable
        :type arg7: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg8: Undefined variable
        :type arg8: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg9: Undefined variable
        :type arg9: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg10: Undefined variable
        :type arg10: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    def SplitUIVertexStreams(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None, arg8=None, arg9=None, arg10=None):
        pass

    @staticmethod
    @overload
    def CreateUIVertexStream(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg3: Undefined variable
        :type arg3: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg4: Undefined variable
        :type arg4: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg5: Undefined variable
        :type arg5: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg6: Undefined variable
        :type arg6: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg7: Undefined variable
        :type arg7: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg8: Undefined variable
        :type arg8: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    @overload
    def CreateUIVertexStream(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg3: Undefined variable
        :type arg3: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg4: Undefined variable
        :type arg4: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg5: Undefined variable
        :type arg5: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg6: Undefined variable
        :type arg6: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg7: Undefined variable
        :type arg7: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg8: Undefined variable
        :type arg8: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg9: Undefined variable
        :type arg9: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg10: Undefined variable
        :type arg10: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    def CreateUIVertexStream(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None, arg8=None, arg9=None, arg10=None):
        pass

    @staticmethod
    @overload
    def AddUIVertexStream(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg3: Undefined variable
        :type arg3: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg4: Undefined variable
        :type arg4: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg5: Undefined variable
        :type arg5: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg6: Undefined variable
        :type arg6: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg7: Undefined variable
        :type arg7: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    @overload
    def AddUIVertexStream(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg3: Undefined variable
        :type arg3: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg4: Undefined variable
        :type arg4: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg5: Undefined variable
        :type arg5: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg6: Undefined variable
        :type arg6: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg7: Undefined variable
        :type arg7: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg8: Undefined variable
        :type arg8: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg9: Undefined variable
        :type arg9: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    def AddUIVertexStream(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None, arg8=None, arg9=None):
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
