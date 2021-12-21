from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class Matrix4x4:
    def __new__(cls, arg1=None):
        '''
        :returns: Matrix4x4
        :rtype: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    def ctor(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector4
        :type arg1: UnityEngine.Vector4
        :param arg2: Vector4
        :type arg2: UnityEngine.Vector4
        :param arg3: Vector4
        :type arg3: UnityEngine.Vector4
        :param arg4: Vector4
        :type arg4: UnityEngine.Vector4
        :returns: Matrix4x4
        :rtype: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    @overload
    def op_Multiply(arg1, arg2):
        '''
        :param arg1: Matrix4x4
        :type arg1: UnityEngine.Matrix4x4
        :param arg2: Matrix4x4
        :type arg2: UnityEngine.Matrix4x4
        :returns: Matrix4x4
        :rtype: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    @overload
    def op_Multiply(arg1, arg2):
        '''
        :param arg1: Matrix4x4
        :type arg1: UnityEngine.Matrix4x4
        :param arg2: Vector4
        :type arg2: UnityEngine.Vector4
        :returns: Vector4
        :rtype: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    def op_Multiply(arg1=None, arg2=None):
        pass

    @staticmethod
    def op_Equality(arg1, arg2):
        '''
        :param arg1: Matrix4x4
        :type arg1: UnityEngine.Matrix4x4
        :param arg2: Matrix4x4
        :type arg2: UnityEngine.Matrix4x4
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def op_Inequality(arg1, arg2):
        '''
        :param arg1: Matrix4x4
        :type arg1: UnityEngine.Matrix4x4
        :param arg2: Matrix4x4
        :type arg2: UnityEngine.Matrix4x4
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_m00():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_m00():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_m10():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_m10():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_m20():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_m20():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_m30():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_m30():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_m01():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_m01():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_m11():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_m11():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_m21():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_m21():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_m31():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_m31():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_m02():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_m02():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_m12():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_m12():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_m22():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_m22():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_m32():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_m32():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_m03():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_m03():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_m13():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_m13():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_m23():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_m23():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_m33():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_m33():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_rotation():
        '''
        :returns: Quaternion
        :rtype: UnityEngine.Quaternion
        '''
        pass

    @staticmethod
    def get_lossyScale():
        '''
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def get_isIdentity():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_determinant():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_decomposeProjection():
        '''
        :returns: FrustumPlanes
        :rtype: UnityEngine.FrustumPlanes
        '''
        pass

    @staticmethod
    def ValidTRS():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def Determinant(arg1):
        '''
        :param arg1: Matrix4x4
        :type arg1: UnityEngine.Matrix4x4
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def TRS(arg1, arg2, arg3):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Quaternion
        :type arg2: UnityEngine.Quaternion
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        :returns: Matrix4x4
        :rtype: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    def SetTRS(arg1, arg2, arg3):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Quaternion
        :type arg2: UnityEngine.Quaternion
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def Inverse(arg1):
        '''
        :param arg1: Matrix4x4
        :type arg1: UnityEngine.Matrix4x4
        :returns: Matrix4x4
        :rtype: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    def get_inverse():
        '''
        :returns: Matrix4x4
        :rtype: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    def Transpose(arg1):
        '''
        :param arg1: Matrix4x4
        :type arg1: UnityEngine.Matrix4x4
        :returns: Matrix4x4
        :rtype: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    def get_transpose():
        '''
        :returns: Matrix4x4
        :rtype: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    def Ortho(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Single
        :type arg5: System.Single or float
        :param arg6: Single
        :type arg6: System.Single or float
        :returns: Matrix4x4
        :rtype: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    def Perspective(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Single
        :type arg4: System.Single or float
        :returns: Matrix4x4
        :rtype: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    def LookAt(arg1, arg2, arg3):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        :returns: Matrix4x4
        :rtype: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    @overload
    def Frustum(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Single
        :type arg5: System.Single or float
        :param arg6: Single
        :type arg6: System.Single or float
        :returns: Matrix4x4
        :rtype: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    @overload
    def Frustum(arg1):
        '''
        :param arg1: FrustumPlanes
        :type arg1: UnityEngine.FrustumPlanes
        :returns: Matrix4x4
        :rtype: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    def Frustum(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None):
        pass

    @staticmethod
    @overload
    def get_Item(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def get_Item(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_Item(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def set_Item(arg1, arg2, arg3):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Single
        :type arg3: System.Single or float
        '''
        pass

    @staticmethod
    @overload
    def set_Item(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Single
        :type arg2: System.Single or float
        '''
        pass

    @staticmethod
    def set_Item(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    def GetHashCode():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def Equals(arg1):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def Equals(arg1):
        '''
        :param arg1: Matrix4x4
        :type arg1: UnityEngine.Matrix4x4
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def Equals(arg1=None):
        pass

    @staticmethod
    def GetColumn(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Vector4
        :rtype: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    def GetRow(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Vector4
        :rtype: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    def SetColumn(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Vector4
        :type arg2: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    def SetRow(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Vector4
        :type arg2: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    def MultiplyPoint(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def MultiplyPoint3x4(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def MultiplyVector(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def TransformPlane(arg1):
        '''
        :param arg1: Plane
        :type arg1: UnityEngine.Plane
        :returns: Plane
        :rtype: UnityEngine.Plane
        '''
        pass

    @staticmethod
    def Scale(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :returns: Matrix4x4
        :rtype: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    def Translate(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :returns: Matrix4x4
        :rtype: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    def Rotate(arg1):
        '''
        :param arg1: Quaternion
        :type arg1: UnityEngine.Quaternion
        :returns: Matrix4x4
        :rtype: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    def get_zero():
        '''
        :returns: Matrix4x4
        :rtype: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    def get_identity():
        '''
        :returns: Matrix4x4
        :rtype: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    @overload
    def ToString():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToString(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def ToString(arg1=None):
        pass

    @staticmethod
    def GetType():
        '''
        :returns: Type
        :rtype: System.Type
        '''
        pass
