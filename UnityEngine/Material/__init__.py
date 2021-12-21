from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class Material:
    def __new__(cls, arg1=None):
        '''
        :returns: Material
        :rtype: UnityEngine.Material
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
    @overload
    def SetTextureOffset(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    @overload
    def SetTextureOffset(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def SetTextureOffset(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def SetTextureScale(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    @overload
    def SetTextureScale(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def SetTextureScale(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def GetTextureOffset(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Vector2
        :rtype: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    @overload
    def GetTextureOffset(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Vector2
        :rtype: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def GetTextureOffset(arg1=None):
        pass

    @staticmethod
    @overload
    def GetTextureScale(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Vector2
        :rtype: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    @overload
    def GetTextureScale(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Vector2
        :rtype: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def GetTextureScale(arg1=None):
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
    def SetColorArray(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    @overload
    def SetColorArray(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    @overload
    def SetColorArray(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: ColorArray
        :type arg2: UnityEngine.ColorArray
        '''
        pass

    @staticmethod
    @overload
    def SetColorArray(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: ColorArray
        :type arg2: UnityEngine.ColorArray
        '''
        pass

    @staticmethod
    def SetColorArray(arg1=None, arg2=None):
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
    def GetInt(arg1=None):
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
    def GetColorArray(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: ColorArray
        :rtype: UnityEngine.ColorArray
        '''
        pass

    @staticmethod
    @overload
    def GetColorArray(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: ColorArray
        :rtype: UnityEngine.ColorArray
        '''
        pass

    @staticmethod
    @overload
    def GetColorArray(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    @overload
    def GetColorArray(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    def GetColorArray(arg1=None, arg2=None):
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
    def get_shader():
        '''
        :returns: Shader
        :rtype: UnityEngine.Shader
        '''
        pass

    @staticmethod
    def set_shader(arg1):
        '''
        :param arg1: Shader
        :type arg1: UnityEngine.Shader
        '''
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
    def get_mainTexture():
        '''
        :returns: Texture
        :rtype: UnityEngine.Texture
        '''
        pass

    @staticmethod
    def set_mainTexture(arg1):
        '''
        :param arg1: Texture
        :type arg1: UnityEngine.Texture
        '''
        pass

    @staticmethod
    def get_mainTextureOffset():
        '''
        :returns: Vector2
        :rtype: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def set_mainTextureOffset(arg1):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def get_mainTextureScale():
        '''
        :returns: Vector2
        :rtype: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def set_mainTextureScale(arg1):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    @overload
    def HasProperty(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def HasProperty(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def HasProperty(arg1=None):
        pass

    @staticmethod
    def get_renderQueue():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def set_renderQueue(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    def EnableKeyword(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        '''
        pass

    @staticmethod
    def DisableKeyword(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        '''
        pass

    @staticmethod
    def IsKeywordEnabled(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_globalIlluminationFlags():
        '''
        :returns: MaterialGlobalIlluminationFlags
        :rtype: UnityEngine.MaterialGlobalIlluminationFlags
        '''
        pass

    @staticmethod
    def set_globalIlluminationFlags(arg1):
        '''
        :param arg1: MaterialGlobalIlluminationFlags
        :type arg1: UnityEngine.MaterialGlobalIlluminationFlags
        '''
        pass

    @staticmethod
    def get_doubleSidedGI():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_doubleSidedGI(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_enableInstancing():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_enableInstancing(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_passCount():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def SetShaderPassEnabled(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        '''
        pass

    @staticmethod
    def GetShaderPassEnabled(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def GetPassName(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def FindPass(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def SetOverrideTag(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: String
        :type arg2: System.String or str
        '''
        pass

    @staticmethod
    @overload
    def GetTag(arg1, arg2, arg3):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        :param arg3: String
        :type arg3: System.String or str
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def GetTag(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def GetTag(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    def Lerp(arg1, arg2, arg3):
        '''
        :param arg1: Material
        :type arg1: UnityEngine.Material
        :param arg2: Material
        :type arg2: UnityEngine.Material
        :param arg3: Single
        :type arg3: System.Single or float
        '''
        pass

    @staticmethod
    def SetPass(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def CopyPropertiesFromMaterial(arg1):
        '''
        :param arg1: Material
        :type arg1: UnityEngine.Material
        '''
        pass

    @staticmethod
    def get_shaderKeywords():
        '''
        :returns: StringArray
        :rtype: System.StringArray
        '''
        pass

    @staticmethod
    def set_shaderKeywords(arg1):
        '''
        :param arg1: StringArray
        :type arg1: System.StringArray
        '''
        pass

    @staticmethod
    @overload
    def GetTexturePropertyNames():
        '''
        :returns: StringArray
        :rtype: System.StringArray
        '''
        pass

    @staticmethod
    @overload
    def GetTexturePropertyNames(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    def GetTexturePropertyNames(arg1=None):
        pass

    @staticmethod
    @overload
    def GetTexturePropertyNameIDs():
        '''
        :returns: Int32Array
        :rtype: System.Int32Array
        '''
        pass

    @staticmethod
    @overload
    def GetTexturePropertyNameIDs(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    def GetTexturePropertyNameIDs(arg1=None):
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
