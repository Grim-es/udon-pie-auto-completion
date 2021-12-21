from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class Mesh:
    def __new__(cls, arg1=None):
        '''
        :returns: Mesh
        :rtype: UnityEngine.Mesh
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
    def CombineMeshes(arg1, arg2, arg3):
        '''
        :param arg1: CombineInstanceArray
        :type arg1: UnityEngine.CombineInstanceArray
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        :param arg3: Boolean
        :type arg3: System.Boolean or bool
        '''
        pass

    @staticmethod
    @overload
    def CombineMeshes(arg1, arg2):
        '''
        :param arg1: CombineInstanceArray
        :type arg1: UnityEngine.CombineInstanceArray
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        '''
        pass

    @staticmethod
    @overload
    def CombineMeshes(arg1):
        '''
        :param arg1: CombineInstanceArray
        :type arg1: UnityEngine.CombineInstanceArray
        '''
        pass

    @staticmethod
    @overload
    def CombineMeshes(arg1, arg2, arg3, arg4):
        '''
        :param arg1: CombineInstanceArray
        :type arg1: UnityEngine.CombineInstanceArray
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        :param arg3: Boolean
        :type arg3: System.Boolean or bool
        :param arg4: Boolean
        :type arg4: System.Boolean or bool
        '''
        pass

    @staticmethod
    def CombineMeshes(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    def get_vertices():
        '''
        :returns: Vector3Array
        :rtype: UnityEngine.Vector3Array
        '''
        pass

    @staticmethod
    def set_vertices(arg1):
        '''
        :param arg1: Vector3Array
        :type arg1: UnityEngine.Vector3Array
        '''
        pass

    @staticmethod
    def get_normals():
        '''
        :returns: Vector3Array
        :rtype: UnityEngine.Vector3Array
        '''
        pass

    @staticmethod
    def set_normals(arg1):
        '''
        :param arg1: Vector3Array
        :type arg1: UnityEngine.Vector3Array
        '''
        pass

    @staticmethod
    def get_tangents():
        '''
        :returns: Vector4Array
        :rtype: UnityEngine.Vector4Array
        '''
        pass

    @staticmethod
    def set_tangents(arg1):
        '''
        :param arg1: Vector4Array
        :type arg1: UnityEngine.Vector4Array
        '''
        pass

    @staticmethod
    def get_uv():
        '''
        :returns: Vector2Array
        :rtype: UnityEngine.Vector2Array
        '''
        pass

    @staticmethod
    def set_uv(arg1):
        '''
        :param arg1: Vector2Array
        :type arg1: UnityEngine.Vector2Array
        '''
        pass

    @staticmethod
    def get_uv2():
        '''
        :returns: Vector2Array
        :rtype: UnityEngine.Vector2Array
        '''
        pass

    @staticmethod
    def set_uv2(arg1):
        '''
        :param arg1: Vector2Array
        :type arg1: UnityEngine.Vector2Array
        '''
        pass

    @staticmethod
    def get_uv3():
        '''
        :returns: Vector2Array
        :rtype: UnityEngine.Vector2Array
        '''
        pass

    @staticmethod
    def set_uv3(arg1):
        '''
        :param arg1: Vector2Array
        :type arg1: UnityEngine.Vector2Array
        '''
        pass

    @staticmethod
    def get_uv4():
        '''
        :returns: Vector2Array
        :rtype: UnityEngine.Vector2Array
        '''
        pass

    @staticmethod
    def set_uv4(arg1):
        '''
        :param arg1: Vector2Array
        :type arg1: UnityEngine.Vector2Array
        '''
        pass

    @staticmethod
    def get_uv5():
        '''
        :returns: Vector2Array
        :rtype: UnityEngine.Vector2Array
        '''
        pass

    @staticmethod
    def set_uv5(arg1):
        '''
        :param arg1: Vector2Array
        :type arg1: UnityEngine.Vector2Array
        '''
        pass

    @staticmethod
    def get_uv6():
        '''
        :returns: Vector2Array
        :rtype: UnityEngine.Vector2Array
        '''
        pass

    @staticmethod
    def set_uv6(arg1):
        '''
        :param arg1: Vector2Array
        :type arg1: UnityEngine.Vector2Array
        '''
        pass

    @staticmethod
    def get_uv7():
        '''
        :returns: Vector2Array
        :rtype: UnityEngine.Vector2Array
        '''
        pass

    @staticmethod
    def set_uv7(arg1):
        '''
        :param arg1: Vector2Array
        :type arg1: UnityEngine.Vector2Array
        '''
        pass

    @staticmethod
    def get_uv8():
        '''
        :returns: Vector2Array
        :rtype: UnityEngine.Vector2Array
        '''
        pass

    @staticmethod
    def set_uv8(arg1):
        '''
        :param arg1: Vector2Array
        :type arg1: UnityEngine.Vector2Array
        '''
        pass

    @staticmethod
    def get_colors():
        '''
        :returns: ColorArray
        :rtype: UnityEngine.ColorArray
        '''
        pass

    @staticmethod
    def set_colors(arg1):
        '''
        :param arg1: ColorArray
        :type arg1: UnityEngine.ColorArray
        '''
        pass

    @staticmethod
    def get_colors32():
        '''
        :returns: Color32Array
        :rtype: UnityEngine.Color32Array
        '''
        pass

    @staticmethod
    def set_colors32(arg1):
        '''
        :param arg1: Color32Array
        :type arg1: UnityEngine.Color32Array
        '''
        pass

    @staticmethod
    def GetVertices(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    def SetVertices(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    def GetNormals(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    def SetNormals(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    def GetTangents(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    def SetTangents(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    @overload
    def GetColors(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    @overload
    def GetColors(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    def GetColors(arg1=None):
        pass

    @staticmethod
    @overload
    def SetColors(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    @overload
    def SetColors(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    def SetColors(arg1=None):
        pass

    @staticmethod
    @overload
    def SetUVs(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    @overload
    def SetUVs(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    @overload
    def SetUVs(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    def SetUVs(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def GetUVs(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    @overload
    def GetUVs(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    @overload
    def GetUVs(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    def GetUVs(arg1=None, arg2=None):
        pass

    @staticmethod
    def get_triangles():
        '''
        :returns: Int32Array
        :rtype: System.Int32Array
        '''
        pass

    @staticmethod
    def set_triangles(arg1):
        '''
        :param arg1: Int32Array
        :type arg1: System.Int32Array
        '''
        pass

    @staticmethod
    @overload
    def GetTriangles(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Int32Array
        :rtype: System.Int32Array
        '''
        pass

    @staticmethod
    @overload
    def GetTriangles(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        :returns: Int32Array
        :rtype: System.Int32Array
        '''
        pass

    @staticmethod
    @overload
    def GetTriangles(arg1, arg2):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg2: Int32
        :type arg2: System.Int32 or int
        '''
        pass

    @staticmethod
    @overload
    def GetTriangles(arg1, arg2, arg3):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Boolean
        :type arg3: System.Boolean or bool
        '''
        pass

    @staticmethod
    def GetTriangles(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    @overload
    def GetIndices(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Int32Array
        :rtype: System.Int32Array
        '''
        pass

    @staticmethod
    @overload
    def GetIndices(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        :returns: Int32Array
        :rtype: System.Int32Array
        '''
        pass

    @staticmethod
    @overload
    def GetIndices(arg1, arg2):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg2: Int32
        :type arg2: System.Int32 or int
        '''
        pass

    @staticmethod
    @overload
    def GetIndices(arg1, arg2, arg3):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Boolean
        :type arg3: System.Boolean or bool
        '''
        pass

    @staticmethod
    def GetIndices(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    def GetIndexStart(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: UInt32
        :rtype: System.UInt32
        '''
        pass

    @staticmethod
    def GetIndexCount(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: UInt32
        :rtype: System.UInt32
        '''
        pass

    @staticmethod
    def GetBaseVertex(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: UInt32
        :rtype: System.UInt32
        '''
        pass

    @staticmethod
    @overload
    def SetTriangles(arg1, arg2):
        '''
        :param arg1: Int32Array
        :type arg1: System.Int32Array
        :param arg2: Int32
        :type arg2: System.Int32 or int
        '''
        pass

    @staticmethod
    @overload
    def SetTriangles(arg1, arg2, arg3):
        '''
        :param arg1: Int32Array
        :type arg1: System.Int32Array
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Boolean
        :type arg3: System.Boolean or bool
        '''
        pass

    @staticmethod
    @overload
    def SetTriangles(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Int32Array
        :type arg1: System.Int32Array
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Boolean
        :type arg3: System.Boolean or bool
        :param arg4: Int32
        :type arg4: System.Int32 or int
        '''
        pass

    @staticmethod
    @overload
    def SetTriangles(arg1, arg2):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg2: Int32
        :type arg2: System.Int32 or int
        '''
        pass

    @staticmethod
    @overload
    def SetTriangles(arg1, arg2, arg3):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Boolean
        :type arg3: System.Boolean or bool
        '''
        pass

    @staticmethod
    @overload
    def SetTriangles(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Boolean
        :type arg3: System.Boolean or bool
        :param arg4: Int32
        :type arg4: System.Int32 or int
        '''
        pass

    @staticmethod
    def SetTriangles(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    @overload
    def SetIndices(arg1, arg2, arg3):
        '''
        :param arg1: Int32Array
        :type arg1: System.Int32Array
        :param arg2: MeshTopology
        :type arg2: UnityEngine.MeshTopology
        :param arg3: Int32
        :type arg3: System.Int32 or int
        '''
        pass

    @staticmethod
    @overload
    def SetIndices(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Int32Array
        :type arg1: System.Int32Array
        :param arg2: MeshTopology
        :type arg2: UnityEngine.MeshTopology
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Boolean
        :type arg4: System.Boolean or bool
        '''
        pass

    @staticmethod
    @overload
    def SetIndices(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Int32Array
        :type arg1: System.Int32Array
        :param arg2: MeshTopology
        :type arg2: UnityEngine.MeshTopology
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Boolean
        :type arg4: System.Boolean or bool
        :param arg5: Int32
        :type arg5: System.Int32 or int
        '''
        pass

    @staticmethod
    def SetIndices(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None):
        pass

    @staticmethod
    def GetBindposes(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    def GetBoneWeights(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    @overload
    def Clear(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    @overload
    def Clear():
        pass

    @staticmethod
    def Clear(arg1=None):
        pass

    @staticmethod
    def RecalculateBounds():
        pass

    @staticmethod
    def RecalculateNormals():
        pass

    @staticmethod
    def RecalculateTangents():
        pass

    @staticmethod
    def MarkDynamic():
        pass

    @staticmethod
    def UploadMeshData(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def GetTopology(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: MeshTopology
        :rtype: UnityEngine.MeshTopology
        '''
        pass

    @staticmethod
    def get_indexFormat():
        '''
        :returns: IndexFormat
        :rtype: UnityEngine.IndexFormat
        '''
        pass

    @staticmethod
    def set_indexFormat(arg1):
        '''
        :param arg1: IndexFormat
        :type arg1: UnityEngine.IndexFormat
        '''
        pass

    @staticmethod
    def get_vertexBufferCount():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def get_blendShapeCount():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def ClearBlendShapes():
        pass

    @staticmethod
    def GetBlendShapeName(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def GetBlendShapeIndex(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def GetBlendShapeFrameCount(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def GetBlendShapeFrameWeight(arg1, arg2):
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
    def GetBlendShapeFrameVertices(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Vector3Array
        :type arg3: UnityEngine.Vector3Array
        :param arg4: Vector3Array
        :type arg4: UnityEngine.Vector3Array
        :param arg5: Vector3Array
        :type arg5: UnityEngine.Vector3Array
        '''
        pass

    @staticmethod
    def AddBlendShapeFrame(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Vector3Array
        :type arg3: UnityEngine.Vector3Array
        :param arg4: Vector3Array
        :type arg4: UnityEngine.Vector3Array
        :param arg5: Vector3Array
        :type arg5: UnityEngine.Vector3Array
        '''
        pass

    @staticmethod
    def get_boneWeights():
        '''
        :returns: BoneWeightArray
        :rtype: UnityEngine.BoneWeightArray
        '''
        pass

    @staticmethod
    def set_boneWeights(arg1):
        '''
        :param arg1: BoneWeightArray
        :type arg1: UnityEngine.BoneWeightArray
        '''
        pass

    @staticmethod
    def get_bindposes():
        '''
        :returns: Matrix4x4Array
        :rtype: UnityEngine.Matrix4x4Array
        '''
        pass

    @staticmethod
    def set_bindposes(arg1):
        '''
        :param arg1: Matrix4x4Array
        :type arg1: UnityEngine.Matrix4x4Array
        '''
        pass

    @staticmethod
    def get_isReadable():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_vertexCount():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def get_subMeshCount():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def set_subMeshCount(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
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
    def set_bounds(arg1):
        '''
        :param arg1: Bounds
        :type arg1: UnityEngine.Bounds
        '''
        pass

    @staticmethod
    def GetUVDistributionMetric(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Single
        :rtype: System.Single
        '''
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
