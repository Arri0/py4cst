from . import IVBAProvider, VBAObjWrapper
import numpy as np

class Solid(VBAObjWrapper):
    KEY_INSIDE = 'Inside'
    KEY_OUTSIDE = 'Outside'
    KEY_CENTERED = 'Centered'

    MESH_APPROXIMATION_PBA = 'PBA'
    MESH_APPROXIMATION_STAIRCASE = 'Staircase'

    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'Solid')

    def delete(self, solid_name: str):
        self.record_method('Delete', solid_name)

    def rename(self, old_name: str, new_name: str):
        self.record_method('Rename', old_name, new_name)

    def change_component(self, solid_name: str, component_name: str):
        self.record_method('ChangeComponent', solid_name, component_name)

    def change_material(self, solid_name: str, material_name: str):
        self.record_method('ChangeMaterial', solid_name, material_name)

    def set_use_individual_color(self, flag: bool = True):
        self.record_method('SetUseIndividualColor', flag)

    def change_individual_color_rgb(self, solid_name: str, r: float, g: float, b: float):
        self.record_method('ChangeIndividualColor', solid_name, r, g, b)

    def set_fast_model_update(self, flag: bool = True):
        self.record_method('FastModelUpdate', flag)

    def perform_add_operation(self, solid1_name: str, solid2_name: str):
        self.record_method('Add', solid1_name, solid2_name)

    def perform_insert_operation(self, solid1_name: str, solid2_name: str):
        # insert solid2 into solid1
        self.record_method('Insert', solid1_name, solid2_name)

    def perform_intersect_operation(self, solid1_name: str, solid2_name: str):
        self.record_method('Intersect', solid1_name, solid2_name)

    def perform_subtract_operation(self, solid1_name: str, solid2_name: str):
        # subtract solid2 from solid1
        self.record_method('Subtract', solid1_name, solid2_name)

    def merge_materials_of_component(self, component_or_solid_name: str):
        self.record_method('MergeMaterialsOfComponent', component_or_solid_name)

    def set_shape_visualization_accuracy2(self, acc: int):
        self.record_method('ShapeVisualizationAccuracy2', acc)

    def set_shape_visualization_offset(self, offset: int):
        self.record_method('ShapeVisualizationOffset', offset)

    def attach_active_wcs(self, solid_name: str):
        self.record_method('AttachActiveWCS', solid_name)

    def blend_edge(self, radius: float):
        self.record_method('BlendEdge', radius)

    def chamfer_edge1_deg(self, depth: float, angle_deg: float, face_id: int):
        self.record_method('ChamferEdge', depth, angle_deg, False, face_id)

    def chamger_edge1_rad(self, depth: float, angle_rad: float, face_id: int):
        self.chamfer_edge1_deg(depth, np.rad2deg(angle_rad), face_id)

    def chamfer_edge2_deg(self, depth: float, angle_deg: float, face_id: int):
        self.record_method('ChamferEdge', depth, angle_deg, True, face_id)

    def chamger_edge2_rad(self, depth: float, angle_rad: float, face_id: int):
        self.chamfer_edge2_deg(depth, np.rad2deg(angle_rad), face_id)

    def slice_shape(self, solid_name: str, component_name: str):
        self.record_method('SliceShape', solid_name, component_name)

    def split_shape(self, solid_name: str, component_name: str):
        self.record_method('SplitShape', solid_name, component_name)

    def thicken_sheet_advanced(
            self, solid_name: str, key: str, thickness: float, clear_picks: bool = False):
        self.record_method('ThickenSheetAdvanced', solid_name, key, thickness, clear_picks)

    def shell_advanced(
            self, solid_name: str, key: str, thickness: float, clear_picks: bool = False):
        self.record_method('ShellAdvanced', solid_name, key, thickness, clear_picks)

    def fill_up_space_advanced(self, solid_name: str, component_name: str, material_name: str):
        self.record_method('FillupSpaceAdvanced', solid_name, component_name, material_name)

    def move_selected_face(self, dx: float, dy: float, dz: float):
        self.record_method('MoveSelectedFace', dx, dy, dz)

    def move_selected_planar_face(self, offset: float):
        self.record_method('MoveSelectedPlanarFace', offset)

    def offset_selected_faces(self, offset: float):
        self.record_method('OffsetSelectedFaces', offset)

    def remove_selected_faces(self):
        self.record_method('RemoveSelectedFaces')

    def set_selected_face_radius(self, radius: float):
        self.record_method('SelectedFaceRadius', radius)

    def set_mesh_step_width(self, solid_name: str, dx: float, dy: float, dz: float):
        self.record_method('SetMeshStepWidth', solid_name, dx, dy, dz)

    def set_mesh_extend_width(self, solid_name: str, dx: float, dy: float, dz: float):
        self.record_method('SetMeshExtendwidth', solid_name, dx, dy, dz)

    def set_automesh_fixpoints(self, solid_name: str, flag: bool = True):
        self.record_method('SetAutomeshFixpoints', solid_name, flag)

    def set_material_based_refinement(self, solid_name: str, flag: bool = True):
        self.record_method('SetMaterialBasedRefinement', solid_name, flag)

    def set_mesh_approximation(self, solid_name: str, approx: str, default_type: bool = False):
        self.record_method('SetMeshProperties', solid_name, approx, default_type)

    def set_use_for_simulation(self, solid_name: str, flag: bool = True):
        self.record_method('SetUseForSimulation', solid_name, flag)

    def set_use_thin_sheet_mesh_for_shape(self, solid_name: str, flag: bool = True):
        self.record_method('SetUseThinSheetMeshForShape', solid_name, flag)

    def set_mesh_refinement(
            self, solid_name: str, edge_refinement_factor: float, volume_refinement_factor: float):
        edge_refinement = edge_refinement_factor is not None
        volume_refinement = volume_refinement_factor is not None
        if not edge_refinement:
            edge_refinement_factor = 0
        if not volume_refinement:
            volume_refinement_factor = 0
        self.record_method(
            'SetMeshRefinement', edge_refinement, edge_refinement_factor,
            volume_refinement, volume_refinement_factor)

    # def set_solid_local_mesh_properties(self, )