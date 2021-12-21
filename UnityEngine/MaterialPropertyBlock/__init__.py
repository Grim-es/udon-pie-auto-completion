from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class MaterialPropertyBlock:
    def __new__(cls, arg1=None):
        '''
        :returns: MaterialPropertyBlock
        :rtype: UnityEngine.MaterialPropertyBlock
        '''
        pass

    @staticmethod
    def ctor():
        '''
        :returns: MaterialPropertyBlock
        :rtype: UnityEngine.MaterialPropertyBlock
        '''
        pass

    @staticmethod
    @overload
    def GetInt(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def GetInt(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def GetInt(arg1=None):
        pass

    @staticmethod
    @overload
    def GetVector(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Vector4
        :rtype: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    @overload
    def GetVector(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Vector4
        :rtype: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    def GetVector(arg1=None):
        pass

    @staticmethod
    @overload
    def GetColor(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    @overload
    def GetColor(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def GetColor(arg1=None):
        pass

    @staticmethod
    @overload
    def GetMatrix(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Matrix4x4
        :rtype: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    @overload
    def GetMatrix(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Matrix4x4
        :rtype: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    def GetMatrix(arg1=None):
        pass

    @staticmethod
    @overload
    def GetTexture(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Texture
        :rtype: UnityEngine.Texture
        '''
        pass

    @staticmethod
    @overload
    def GetTexture(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Texture
        :rtype: UnityEngine.Texture
        '''
        pass

    @staticmethod
    def GetTexture(arg1=None):
        pass

    @staticmethod
    @overload
    def GetFloatArray(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: SingleArray
        :rtype: System.SingleArray
        '''
        pass

    @staticmethod
    @overload
    def GetFloatArray(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: SingleArray
        :rtype: System.SingleArray
        '''
        pass

    @staticmethod
    @overload
    def GetFloatArray(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    @overload
    def GetFloatArray(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    def GetFloatArray(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def GetVectorArray(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Vector4Array
        :rtype: UnityEngine.Vector4Array
        '''
        pass

    @staticmethod
    @overload
    def GetVectorArray(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Vector4Array
        :rtype: UnityEngine.Vector4Array
        '''
        pass

    @staticmethod
    @overload
    def GetVectorArray(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    @overload
    def GetVectorArray(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    def GetVectorArray(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def GetMatrixArray(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Matrix4x4Array
        :rtype: UnityEngine.Matrix4x4Array
        '''
        pass

    @staticmethod
    @overload
    def GetMatrixArray(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Matrix4x4Array
        :rtype: UnityEngine.Matrix4x4Array
        '''
        pass

    @staticmethod
    @overload
    def GetMatrixArray(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    @overload
    def GetMatrixArray(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    def GetMatrixArray(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def CopySHCoefficientArraysFrom(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    @overload
    def CopySHCoefficientArraysFrom(arg1):
        '''
        :param arg1: SphericalHarmonicsL2Array
        :type arg1: UnityEngine.SphericalHarmonicsL2Array
        '''
        pass

    @staticmethod
    @overload
    def CopySHCoefficientArraysFrom(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Int32
        :type arg4: System.Int32 or int
        '''
        pass

    @staticmethod
    @overload
    def CopySHCoefficientArraysFrom(arg1, arg2, arg3, arg4):
        '''
        :param arg1: SphericalHarmonicsL2Array
        :type arg1: UnityEngine.SphericalHarmonicsL2Array
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Int32
        :type arg4: System.Int32 or int
        '''
        pass

    @staticmethod
    def CopySHCoefficientArraysFrom(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    @overload
    def CopyProbeOcclusionArrayFrom(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    @overload
    def CopyProbeOcclusionArrayFrom(arg1):
        '''
        :param arg1: Vector4Array
        :type arg1: UnityEngine.Vector4Array
        '''
        pass

    @staticmethod
    @overload
    def CopyProbeOcclusionArrayFrom(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Int32
        :type arg4: System.Int32 or int
        '''
        pass

    @staticmethod
    @overload
    def CopyProbeOcclusionArrayFrom(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector4Array
        :type arg1: UnityEngine.Vector4Array
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Int32
        :type arg4: System.Int32 or int
        '''
        pass

    @staticmethod
    def CopyProbeOcclusionArrayFrom(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    def get_isEmpty():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def Clear():
        pass

    @staticmethod
    @overload
    def SetFloat(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Single
        :type arg2: System.Single or float
        '''
        pass

    @staticmethod
    @overload
    def SetFloat(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Single
        :type arg2: System.Single or float
        '''
        pass

    @staticmethod
    def SetFloat(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def SetInt(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        '''
        pass

    @staticmethod
    @overload
    def SetInt(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Int32
        :type arg2: System.Int32 or int
        '''
        pass

    @staticmethod
    def SetInt(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def SetVector(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Vector4
        :type arg2: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    @overload
    def SetVector(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Vector4
        :type arg2: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    def SetVector(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def SetColor(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Color
        :type arg2: UnityEngine.Color
        '''
        pass

    @staticmethod
    @overload
    def SetColor(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Color
        :type arg2: UnityEngine.Color
        '''
        pass

    @staticmethod
    def SetColor(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def SetMatrix(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Matrix4x4
        :type arg2: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    @overload
    def SetMatrix(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Matrix4x4
        :type arg2: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    def SetMatrix(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def SetBuffer(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: ComputeBuffer
        :type arg2: UnityEngine.ComputeBuffer
        '''
        pass

    @staticmethod
    @overload
    def SetBuffer(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: ComputeBuffer
        :type arg2: UnityEngine.ComputeBuffer
        '''
        pass

    @staticmethod
    def SetBuffer(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def SetTexture(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Texture
        :type arg2: UnityEngine.Texture
        '''
        pass

    @staticmethod
    @overload
    def SetTexture(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Texture
        :type arg2: UnityEngine.Texture
        '''
        pass

    @staticmethod
    def SetTexture(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def SetFloatArray(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    @overload
    def SetFloatArray(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    @overload
    def SetFloatArray(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: SingleArray
        :type arg2: System.SingleArray
        '''
        pass

    @staticmethod
    @overload
    def SetFloatArray(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: SingleArray
        :type arg2: System.SingleArray
        '''
        pass

    @staticmethod
    def SetFloatArray(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def SetVectorArray(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    @overload
    def SetVectorArray(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    @overload
    def SetVectorArray(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Vector4Array
        :type arg2: UnityEngine.Vector4Array
        '''
        pass

    @staticmethod
    @overload
    def SetVectorArray(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Vector4Array
        :type arg2: UnityEngine.Vector4Array
        '''
        pass

    @staticmethod
    def SetVectorArray(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def SetMatrixArray(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    @overload
    def SetMatrixArray(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    @overload
    def SetMatrixArray(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Matrix4x4Array
        :type arg2: UnityEngine.Matrix4x4Array
        '''
        pass

    @staticmethod
    @overload
    def SetMatrixArray(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Matrix4x4Array
        :type arg2: UnityEngine.Matrix4x4Array
        '''
        pass

    @staticmethod
    def SetMatrixArray(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def GetFloat(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def GetFloat(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def GetFloat(arg1=None):
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
