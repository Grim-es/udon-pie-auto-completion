from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class VertexHelper:
    def __new__(cls, arg1=None):
        '''
        :returns: VertexHelper
        :rtype: UnityEngine.UI.VertexHelper
        '''
        pass

    @staticmethod
    @overload
    def ctor():
        '''
        :returns: VertexHelper
        :rtype: UnityEngine.VertexHelper
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1):
        '''
        :param arg1: Mesh
        :type arg1: UnityEngine.Mesh
        :returns: VertexHelper
        :rtype: UnityEngine.VertexHelper
        '''
        pass

    @staticmethod
    def ctor(arg1=None):
        pass

    @staticmethod
    def Dispose():
        pass

    @staticmethod
    def Clear():
        pass

    @staticmethod
    def get_currentVertCount():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def get_currentIndexCount():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def PopulateUIVertex(arg1, arg2):
        '''
        :param arg1: Undefined variable
        :type arg1: UIVertexRef.UIVertexRef
        :param arg2: Int32
        :type arg2: System.Int32 or int
        '''
        pass

    @staticmethod
    def SetUIVertex(arg1, arg2):
        '''
        :param arg1: UIVertex
        :type arg1: UnityEngine.UIVertex
        :param arg2: Int32
        :type arg2: System.Int32 or int
        '''
        pass

    @staticmethod
    def FillMesh(arg1):
        '''
        :param arg1: Mesh
        :type arg1: UnityEngine.Mesh
        '''
        pass

    @staticmethod
    @overload
    def AddVert(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Color32
        :type arg2: UnityEngine.Color32
        :param arg3: Vector2
        :type arg3: UnityEngine.Vector2
        :param arg4: Vector2
        :type arg4: UnityEngine.Vector2
        :param arg5: Vector3
        :type arg5: UnityEngine.Vector3
        :param arg6: Vector4
        :type arg6: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    @overload
    def AddVert(arg1, arg2, arg3):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Color32
        :type arg2: UnityEngine.Color32
        :param arg3: Vector2
        :type arg3: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    @overload
    def AddVert(arg1):
        '''
        :param arg1: UIVertex
        :type arg1: UnityEngine.UIVertex
        '''
        pass

    @staticmethod
    def AddVert(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None):
        pass

    @staticmethod
    def AddTriangle(arg1, arg2, arg3):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        '''
        pass

    @staticmethod
    def AddUIVertexQuad(arg1):
        '''
        :param arg1: UIVertexArray
        :type arg1: UnityEngine.UIVertexArray
        '''
        pass

    @staticmethod
    def AddUIVertexStream(arg1, arg2):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    def AddUIVertexTriangleStream(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    def GetUIVertexStream(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
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
    def GetHashCode():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def GetType():
        '''
        :returns: Type
        :rtype: System.Type
        '''
        pass

    @staticmethod
    def ToString():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass
