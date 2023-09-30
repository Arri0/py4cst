from . import Project
from . import ComObjectWrapper
from . import w32com
import colorsys
from typing import Union
import numpy as np

class Material(ComObjectWrapper):
    TYPE_PEC = 'PEC'
    TYPE_NORMAL = 'Normal'
    TYPE_ANISOTROPIC = 'Anisotropic'
    TYPE_LOSSY_METAL = 'Lossy Metal'
    TYPE_CORRUGATED_WALL = 'Corrugated wall'
    TYPE_OHMIC_SHEET = 'Ohmic sheet'
    TYPE_TENSOR_FORMULA = 'Tensor formula'
    TYPE_NONLINEAR = 'Nonlinear'

    REF_COORD_SYSTEM_GLOBAL = 'Global'
    REF_COORD_SYSTEM_LOCAL = 'Solid'

    COORD_SYSTEM_CARTESIAN = 'Cartesian'
    COORD_SYSTEM_CYLINDRICAL = 'Cylindrical'
    COORD_SYSTEM_SPHERICAL = 'Spherical'

    TAB_SURF_IMP_MODEL_OPAQUE = 'Opaque'
    TAB_SURF_IMP_MODEL_TRANSPARENT = 'Transparent'

    DISP_FIT_SCHEME_TAB_SI_NTH_ORDER = 'Nth Order'

    ENTRY_BLOCK_UU = 'uu'
    ENTRY_BLOCK_VU = 'vu'
    ENTRY_BLOCK_UV = 'uv'
    ENTRY_BLOCK_VV = 'vv'

    TANGENT_DELTA_MODEL_CONST_SIGMA = 'ConstSigma'
    TANGENT_DELTA_MODEL_CONST_TAN_D = 'ConstTanD'

    CONST_TANGENT_DELTA_STRATEGY_AUTOMATIC_ORDER = 'AutomaticOrder'
    CONST_TANGENT_DELTA_STRATEGY_CUSTOM_ORDER = 'UserDefinedOrder'
    CONST_TANGENT_DELTA_STRATEGY_DJORDJEVIC_SARKAR = 'DjordjevicSarkar'

    DISP_MODEL_EPS_NONE = 'None'
    DISP_MODEL_EPS_DEBYE_1ST_ORDER = 'Debye1st'
    DISP_MODEL_EPS_DEBYE_2ND_ORDER = 'Debye2nd'
    DISP_MODEL_EPS_DRUDE = 'Drude'
    DISP_MODEL_EPS_LORENTZ = 'Lorentz'
    DISP_MODEL_EPS_GENERAL_1ST_ORDER = 'General1st'
    DISP_MODEL_EPS_GENERAL_2ND_ORDER = 'General2nd'
    DISP_MODEL_EPS_GENERAL = 'General'
    DISP_MODEL_EPS_NONLINEAR_2ND_ORDER = 'NonLinear2nd'
    DISP_MODEL_EPS_NONLINEAR_3RD_ORDER = 'NonLinear3rd'
    DISP_MODEL_EPS_NONLINEAR_KERR = 'NonLinearKerr'
    DISP_MODEL_EPS_NONLINEAR_RAMAN = 'NonLinearRaman'

    DISP_MODEL_MU_NONE = 'None'
    DISP_MODEL_MU_DEBYE_1ST_ORDER = 'Debye1st'
    DISP_MODEL_MU_DEBYE_2ND_ORDER = 'Debye2nd'
    DISP_MODEL_MU_DRUDE = 'Drude'
    DISP_MODEL_MU_LORENTZ = 'Lorentz'
    DISP_MODEL_MU_GYROTROPIC = 'Gyrotropic'
    DISP_MODEL_MU_GENERALIZED_DEBYE = 'GeneralizedDebye'
    DISP_MODEL_MU_GENERAL_1ST_ORDER = 'General1st'
    DISP_MODEL_MU_GENERAL_2ND_ORDER = 'General2nd'
    DISP_MODEL_MU_NONLINEAR_2ND_ORDER = 'NonLinear2nd'
    DISP_MODEL_MU_NONLINEAR_3RD_ORDER = 'NonLinear3rd'
    DISP_MODEL_MU_NONLINEAR_KERR = 'NonLinearKerr'
    DISP_MODEL_MU_NONLINEAR_RAMAN = 'NonLinearRaman'

    DISPERSIVE_FITTING_FORMAT_REAL_IMAG = 'Real_Imag'
    DISPERSIVE_FITTING_FORMAT_REAL_TAN_D = 'Real_Tand'

    DISPERSIVE_FITTING_SCHEME_CONDUCTIVITY = 'Conductivity'
    DISPERSIVE_FITTING_SCHEME_1ST_ORDER = '1st Order'
    DISPERSIVE_FITTING_SCHEME_2ND_ORDER = '2nd Order'
    DISPERSIVE_FITTING_SCHEME_NTH_ORDER = 'Nth Order'

    DIRECTION_X = 'x'
    DIRECTION_Y = 'y'
    DIRECTION_Z = 'z'

    SPATIALLY_VAR_MAT_PROP_EPS = 'eps'
    SPATIALLY_VAR_MAT_PROP_MU = 'mu'
    SPATIALLY_VAR_MAT_PROP_EL_SIGMA = 'sigma'
    SPATIALLY_VAR_MAT_PROP_MAG_SIGMA = 'sigmam'

    SPATIALLY_VAR_MAT_MODEL_CONSTANT = 'Constant'
    SPATIALLY_VAR_MAT_MODEL_LUNEBURG = 'Luneburg'
    SPATIALLY_VAR_MAT_MODEL_POWER_LAW = 'PowerLaw'
    SPATIALLY_VAR_MAT_MODEL_GRADED_INDEX = 'GradedIndex'

    SPATIALLY_VAR_MAT_PARAM_CONSTANT_CONSTANT = 'value_constant'
    SPATIALLY_VAR_MAT_PARAM_LUNEBURG_CENTER = 'value_center'
    SPATIALLY_VAR_MAT_PARAM_LUNEBURG_SURFACE = 'value_surface'
    SPATIALLY_VAR_MAT_PARAM_POWER_LAW_AXIS = 'value_axis'
    SPATIALLY_VAR_MAT_PARAM_POWER_LAW_CLADDING = 'value_cladding'
    SPATIALLY_VAR_MAT_PARAM_POWER_LAW_PROFILE = 'value_profile'
    SPATIALLY_VAR_MAT_PARAM_GRADED_INDEX_AXIS = 'value_axis'
    SPATIALLY_VAR_MAT_PARAM_GRADED_INDEX_GRADIENT = 'value_gradient'

    SPACE_MAP_MAT_PROP_EPS = 'eps'
    SPACE_MAP_MAT_PROP_MU = 'mu'
    SPACE_MAP_MAT_PROP_EL_SIGMA = 'sigma'
    SPACE_MAP_MAT_PROP_MAG_SIGMA = 'sigmam'
    SPACE_MAP_MAT_PROP_EPS_INF = 'epsinfinity'
    SPACE_MAP_MAT_PROP_MU_INF = 'muinfinity'
    SPACE_MAP_MAT_PROP_DISP_COEFF0_EPS = 'dispcoeff0eps'
    SPACE_MAP_MAT_PROP_DISP_COEFF0_MU = 'dispcoeff0mu'
    SPACE_MAP_MAT_PROP_DISP_COEFF1_EPS = 'dispcoeff0eps'
    SPACE_MAP_MAT_PROP_DISP_COEFF1_MU = 'dispcoeff0mu'
    SPACE_MAP_MAT_PROP_DISP_COEFF2_EPS = 'dispcoeff0eps'
    SPACE_MAP_MAT_PROP_DISP_COEFF2_MU = 'dispcoeff0mu'
    SPACE_MAP_MAT_PROP_DISP_COEFF3_EPS = 'dispcoeff0eps'
    SPACE_MAP_MAT_PROP_DISP_COEFF3_MU = 'dispcoeff0mu'
    SPACE_MAP_MAT_PROP_DISP_COEFF4_EPS = 'dispcoeff0eps'
    SPACE_MAP_MAT_PROP_DISP_COEFF4_MU = 'dispcoeff0mu'

    SPACE_MAP_MAT_MODEL_3D_CONSTANT = '3DConstant'
    SPACE_MAP_MAT_MODEL_3D_DEFAULT = '3DDefault'
    SPACE_MAP_MAT_MODEL_3D_IMPORT_HEX = '3DImportHex'
    SPACE_MAP_MAT_MODEL_3D_IMPORT_TET = '3DImportTet'

    SPACE_MAP_MAT_PARAM_3D_CONSTANT_CONSTANT = 'value_constant'
    SPACE_MAP_MAT_PARAM_3D_IMPORT_HEX_MAP_FILENAME = 'map_filename'
    SPACE_MAP_MAT_PARAM_3D_IMPORT_TET_MAP_FILENAME = 'map_filename'
    SPACE_MAP_MAT_PARAM_3D_IMPORT_TET_SLIM_MESH_FILENAME = 'slimmesh_filename'

    GENERALIZED_DEBYE_NON_LIN_DEP_NONE = 'None'
    GENERALIZED_DEBYE_NON_LIN_DEP_BH_CURVE = 'BHCurve'
    GENERALIZED_DEBYE_NON_LIN_DEP_TAB_MU_DIFF_CURVE = 'TabMuDiffCurve'

    COATING_TYPE_DEF_PERFECT_ABSORBER = 'PERFECT_ABSORBER'
    COATING_TYPE_DEF_SURFACE_IMPEDANCE_TABLE = 'SURFACE_IMPEDANCE_TABLE'
    COATING_TYPE_DEF_REFLECTION_FACTOR_TABLE = 'REFLECTION_FACTOR_TABLE'
    COATING_TYPE_DEF_REFLECTION_TRANSMISSION_FACTOR_TABLE = 'REFLECTION_TRANSMISSION_FACTOR_TABLE'

    PARTICLE_PROP_NONE = 'None'
    PARTICLE_PROP_SECONDARY_EMISSION = 'SecondaryEmission'
    PARTICLE_PROP_SHEET_TRANSPARENCY = 'SheetTransparency'

    SE_MODEL_NONE = 'None'
    SE_MODEL_FURMAN = 'Furman'
    SE_MODEL_IMPORT = 'Import'
    SE_MODEL_VAUGHAN = 'Vaughan'

    ION_SEE_MODEL_NONE = 'None'
    ION_SEE_MODEL_ION_IMPORT = 'Ion Import'

    PARTICLE_TRANSPARENCY_SETTINGS_SCALAR = 'Scalar'
    PARTICLE_TRANSPARENCY_SETTINGS_IMPORT = 'Import'

    THERMAL_TYPE_PTC = 'PTC'
    THERMAL_TYPE_NORMAL = 'Normal'
    THERMAL_TYPE_ANISOTROPIC = 'Anisotropic'

    SPECIFIC_HEAT_UNIT_J_K_KG = 'J/K/kg'
    SPECIFIC_HEAT_UNIT_KJ_K_KG = 'kJ/K/kg'

    MECHANICS_TYPE_UNUSED = 'Unused'
    MECHANICS_TYPE_ISOTROPIC = 'Isotropic'

    FLOW_RES_PRESSURE_LOSS_TYPE_UVW_BLOCKED = 'Blocked'
    FLOW_RES_PRESSURE_LOSS_TYPE_UVW_COEFFICIENT = 'Coefficient'
    FLOW_RES_PRESSURE_LOSS_TYPE_UVW_CURVE = 'Curve'

    FLOW_RES_PRESSURE_LOSS_TYPE_SHEET_BLOCKED = 'Blocked'
    FLOW_RES_PRESSURE_LOSS_TYPE_SHEET_COEFFICIENT = 'Coefficient'
    FLOW_RES_PRESSURE_LOSS_TYPE_SHEET_CURVE = 'Curve'
    FLOW_RES_PRESSURE_LOSS_TYPE_SHEET_PERFORATION = 'Perforation'
    FLOW_RES_PRESSURE_LOSS_TYPE_SHEET_FREE_AREA_RATIO = 'FreeAreaRatio'

    FLOW_RES_SHAPE_TYPE_HEXAGON = 'Hexagon'
    FLOW_RES_SHAPE_TYPE_CIRCLE = 'Circle'
    FLOW_RES_SHAPE_TYPE_SQUARE = 'Square'

    def __init__(self, project: Project) -> None:
        self.project = project
        self.com_object = project.com_object.Material

    def invoke_method(self, name, *args, **kwargs):
        self.project.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def reset(self):
        self.invoke_method('Reset')

    def create(self):
        self.invoke_method('Create')

    def set_name(self, name: str):
        self.invoke_method('Name', name)

    def set_folder_name(self, folder_name: str):
        self.invoke_method('Folder', folder_name)

    def set_type(self, mat_type: str):
        self.invoke_method('Type', mat_type)

    def set_frequency_unit(self, unit: str):
        self.invoke_method('MaterialUnit', 'Frequency', unit)

    def set_geometry_unit(self, unit: str):
        self.invoke_method('MaterialUnit', 'Geometry', unit)

    def set_time_unit(self, unit: str):
        self.invoke_method('MaterialUnit', 'Time', unit)

    def set_temperature_unit(self, unit: str):
        self.invoke_method('MaterialUnit', 'Temperature', unit)

    def delete(self, mat_name: str):
        self.invoke_method('Delete', mat_name)

    def rename(self, old_name: str, new_name: str):
        self.invoke_method('Rename', old_name, new_name)

    def create_folder(self, name: str):
        self.invoke_method('NewFolder', name)

    def delete_folder(self, name: str):
        self.invoke_method('DeleteFolder', name)

    def rename_folder(self, old_name: str, new_name: str):
        self.invoke_method('RenameFolder', old_name, new_name)

    def set_color_rgb(self, r: float, g: float, b: float):
        # rgb in range [0, 1]
        self.invoke_method('Colour', r, g, b)

    def set_color_hsv(self, h: float, s: float, v: float):
        # hsv in range [0, 1]
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        self.set_color_rgb(r, g, b)

    def set_color_hsl(self, h: float, s: float, l: float):
        # hsl in range [0, 1]
        r, g, b = colorsys.hls_to_rgb(h, l, s)
        self.set_color_rgb(r, g, b)

    def set_transparency(self, transparency: float):
        # The set value is not displayed correctly in the editor settings, but it works.
        self.invoke_method('Transparency', transparency)

    def set_color_alpha(self, alpha: float):
        self.set_transparency(1.0 - alpha)

    def set_color_rgba(self, r: float, g: float, b: float, alpha: float):
        self.set_color_rgb(r, g, b)
        self.set_color_alpha(alpha)

    def set_color_rgbt(self, r: float, g: float, b: float, transparency: float):
        self.set_color_rgb(r, g, b)
        self.set_transparency(transparency)

    def set_color_hsva(self, h: float, s: float, v: float, alpha: float):
        self.set_color_hsv(h, s, v)
        self.set_color_alpha(alpha)

    def set_color_hsvt(self, h: float, s: float, v: float, transparency: float):
        self.set_color_hsv(h, s, v)
        self.set_transparency(transparency)

    def set_color_hsla(self, h: float, s: float, l: float, alpha: float):
        self.set_color_hsl(h, s, l)
        self.set_color_alpha(alpha)

    def set_color_hslt(self, h: float, s: float, l: float, transparency: float):
        self.set_color_hsl(h, s, l)
        self.set_transparency(transparency)

    def set_wireframe(self, flag: bool = True):
        self.invoke_method('Wireframe', flag)

    def set_reflection(self, flag: bool = True):
        self.invoke_method('Reflection', flag)

    def set_allow_outlines(self, flag: bool = True):
        self.invoke_method('Allowoutline', flag)

    def set_transparent_solid_outlines(self, flag: bool = True):
        self.invoke_method('Transparentoutline', flag)

    def change_appearance(self):
        self.invoke_method('ChangeColour')

    def set_rel_permitivity(self, epsilon: float):
        self.invoke_method('Epsilon', epsilon)

    def set_rel_permitivity_x(self, epsilon: float):
        self.invoke_method('EpsilonX', epsilon)

    def set_rel_permitivity_y(self, epsilon: float):
        self.invoke_method('EpsilonY', epsilon)

    def set_rel_permitivity_z(self, epsilon: float):
        self.invoke_method('EpsilonZ', epsilon)

    def set_rel_permitivity_xyz(self, eps_x: float, eps_y: float, eps_z: float):
        self.set_rel_permitivity_x(eps_x)
        self.set_rel_permitivity_y(eps_y)
        self.set_rel_permitivity_z(eps_z)

    def set_rel_permeability(self, mu: float):
        self.invoke_method('Mu', mu)

    def set_rel_permeability_x(self, mu: float):
        self.invoke_method('MuX', mu)

    def set_rel_permeability_y(self, mu: float):
        self.invoke_method('MuY', mu)

    def set_rel_permeability_z(self, mu: float):
        self.invoke_method('MuZ', mu)

    def set_rel_permeability_xyz(self, mu_x: float, mu_y: float, mu_z: float):
        self.set_rel_permeability_y(mu_y)
        self.set_rel_permeability_x(mu_x)
        self.set_rel_permeability_z(mu_z)

    def set_material_density(self, rho_kg_per_m3: float):
        self.invoke_method('Rho', rho_kg_per_m3)

    def add_coated_material(self, mat_name: str, thickness: float):
        self.invoke_method('AddCoatedMaterial', mat_name, thickness)

    def set_reference_coord_system(self, name: str):
        self.invoke_method('ReferenceCoordSystem', name)

    def set_coord_system_type(self, name: str):
        self.invoke_method('CoordSystemType', name)

    def set_corrugation(self, depth: float, gap_width: float, tooth_width: float):
        self.invoke_method('Corrugation', depth, gap_width, tooth_width)

    def set_ohmic_sheet_impedance(self, impedance: complex):
        self.invoke_method('OhmicSheetImpedance', impedance.real, impedance.imag)

    def set_ohmic_sheet_frequency(self, frequency: float):
        self.invoke_method('OhmicSheetFreq', frequency)

    def set_tabulated_surface_impedance_model(self, model: str):
        self.invoke_method('SetTabulatedSurfaceImpedanceModel', model)

    def add_tabulated_surface_impedance_fitting_value(
            self, frequency: float, impedance: complex, weight: float):
        self.invoke_method(
            'AddTabulatedSurfaceImpedanceFittingValue', frequency,
            impedance.real, impedance.imag, weight)

    def add_tabulated_surface_impedance_value(self, frequency: float, impedance: complex):
        self.invoke_method(
            'AddTabulatedSurfaceImpedanceValue', frequency, impedance.real, impedance.imag)

    def set_dispersive_fitting_scheme_tab_surf_imp(self, scheme: str):
        self.invoke_method('DispersiveFittingSchemeTabSI', scheme)

    def set_max_order_nth_model_fit_tab_surf_imp(self, order: int):
        self.invoke_method('MaximalOrderNthModelFitTabSI', order)

    def set_use_only_data_in_sim_freq_range_nth_model_tab_surf_imp(self, flag: bool = True):
        self.invoke_method('UseOnlyDataInSimFreqRangeNthModelTabSI', flag)

    def set_error_limit_nth_model_fit_tab_surf_imp(self, limit: float):
        self.invoke_method('ErrorLimitNthModelFitTabSI', limit)

    def set_as_tabulated_compact_model(self, flag: bool = True):
        self.invoke_method('TabulatedCompactModel', flag)

    def reset_tabulated_compact_model_list(self):
        self.invoke_method('ResetTabulatedCompactModelList')

    def set_tabulated_compact_model_impedance(self, imp_p1: float, imp_p2: float):
        self.invoke_method('SetTabulatedCompactModelImpedance', imp_p1, imp_p2)

    def set_symm_tabulated_compact_model_impedance(self, imp_p: float):
        self.invoke_method('SetSymmTabulatedCompactModelImpedance', imp_p)

    def add_tabulated_compact_model_item(
            self, frequency: float, s11: complex, s21: complex, s12: complex,
            s22: complex, weight: float):
        self.invoke_method(
            'AddTabulatedCompactModelItem', frequency, s11.real, s11.imag, s21.real, s21.imag,
            s12.real, s12.imag, s22.real, s22.imag, weight)

    def add_symm_tabulated_compact_model_item(
            self, frequency: float, s11: complex, s21: complex, weight: float):
        self.invoke_method(
            'AddSymmTabulatedCompactModelItem', frequency, s11.real, s11.imag,
            s21.real, s21.imag, weight)

    def set_tabulated_compact_model_anisotropic(self, flag: bool = True):
        self.invoke_method('TabulatedCompactModelAnisotropic', flag)

    def add_aniso_tabulated_compact_model_item(
            self, entry_block: str, frequency: float, s11: complex, s21: complex, s12: complex,
            s22: complex, weight: float):
        self.invoke_method(
            'AddAnisoTabulatedCompactModelItem', entry_block, frequency,
            s11.real, s11.imag, s21.real, s21.imag,
            s12.real, s12.imag, s22.real, s22.imag, weight)

    def add_aniso_symm_tabulated_compact_model_item(
            self, entry_block: str, frequency: float, s11: complex, s21: complex, weight: float):
        self.invoke_method(
            'AddAnisoSymmTabulatedCompactModelItem', entry_block, frequency,
            s11.real, s11.imag, s21.real, s21.imag, weight)

    def set_max_order_fit_tabulated_compact_model(self, order: int):
        self.invoke_method('MaximalOrderFitTabulatedCompactModel', order)

    def set_use_only_data_in_sim_freq_range_tabulated_compact_model(self, flag: bool = True):
        self.invoke_method('UseOnlyDataInSimFreqRangeTabulatedCompactModel', flag)

    def set_error_limit_fit_tabulated_compact_model(self, limit: float):
        self.invoke_method('ErrorLimitFitTabulatedCompactModel', limit)

    def set_thickness(self, thickness: float):
        self.invoke_method('Thickness', thickness)

    def set_lossy_metal_surf_imp_roughness(self, roughness: float):
        self.invoke_method('LossyMetalSIRoughness', roughness)

    def set_el_conductivity(self, sigma: float):
        self.invoke_method('Sigma', sigma)

    def set_el_conductivity_x(self, sigma: float):
        self.invoke_method('SigmaX', sigma)

    def set_el_conductivity_y(self, sigma: float):
        self.invoke_method('SigmaY', sigma)

    def set_el_conductivity_z(self, sigma: float):
        self.invoke_method('SigmaZ', sigma)

    def set_el_parametric_conductivity(self, flag: bool = True):
        self.invoke_method('SetElParametricConductivity', flag)

    def add_je_value(self, dj: float, de: float):
        self.invoke_method('AddJEValue', dj, de)

    def reset_je_list(self):
        self.invoke_method('ResetJEList')

    def reset_el_time_dependent_conductivity_curve(self):
        self.invoke_method('ResetElTimeDepCond')

    def add_el_time_dependent_conductivity_value(self, d_time: float, d_cond: float):
        self.invoke_method('AddElTimeDepCondValue', d_time, d_cond)

    def add_el_time_dependent_conductivity_aniso_value(
            self, d_time: float, d_cond_x: float, d_cond_y: float, d_cond_z: float):
        self.invoke_method('AddElTimeDepCondAnisoValue', d_time, d_cond_x, d_cond_y, d_cond_z)

    def load_el_time_dependent_conductivity_from_file(self, file_path: str, time_unit: str):
        self.invoke_method('LoadElTimeDepConductivity', file_path, time_unit)

    def set_el_tangent_delta(self, tan_d: float):
        self.invoke_method('TanD', tan_d)

    def set_el_tangent_delta_x(self, tan_d: float):
        self.invoke_method('TanDX', tan_d)

    def set_el_tangent_delta_y(self, tan_d: float):
        self.invoke_method('TanDY', tan_d)

    def set_el_tangent_delta_z(self, tan_d: float):
        self.invoke_method('TanDZ', tan_d)

    def set_el_tangent_delta_given(self, flag: bool = True):
        self.invoke_method('TanDGiven', flag)

    def set_el_tangent_delta_frequency(self, frequency: float):
        self.invoke_method('TanDFreq', frequency)

    def set_el_tangent_delta_model(self, model: str):
        self.invoke_method('TanDModel', model)

    def set_el_const_tangent_delta_strategy_eps(self, strategy: str):
        self.invoke_method('SetConstTanDStrategyEps', strategy)

    def set_el_const_tangent_delta_model_order_eps(self, order: int):
        self.invoke_method('ConstTanDModelOrderEps', order)

    def set_djordjevic_sarkar_upper_freq_eps(self, frequency: float):
        self.invoke_method('DjordjevicSarkarUpperFreqEps', frequency)

    def set_mag_conductivity(self, sigma: float):
        self.invoke_method('SigmaM', sigma)

    def set_mag_conductivity_x(self, sigma: float):
        self.invoke_method('SigmaMX', sigma)

    def set_mag_conductivity_y(self, sigma: float):
        self.invoke_method('SigmaMY', sigma)

    def set_mag_conductivity_z(self, sigma: float):
        self.invoke_method('SigmaMZ', sigma)

    def set_mag_parametric_conductivity(self, flag: bool = True):
        self.invoke_method('SetMagParametricConductivity', flag)

    def reset_mag_time_dependent_conductivity_curve(self):
        self.invoke_method('ResetMagTimeDepCond')

    def add_mag_time_dependent_conductivity_value(self, d_time: float, d_cond: float):
        self.invoke_method('AddMagTimeDepCondValue', d_time, d_cond)

    def add_mag_time_dependent_conductivity_aniso_value(
            self, d_time: float, d_cond_x: float, d_cond_y: float, d_cond_z: float):
        self.invoke_method('AddMagTimeDepCondAnisoValue', d_time, d_cond_x, d_cond_y, d_cond_z)

    def load_mag_time_dependent_conductivity_from_file(self, file_path: str, time_unit: str):
        self.invoke_method('LoadMagTimeDepConductivity', file_path, time_unit)

    def set_mag_tangent_delta(self, tan_d: float):
        self.invoke_method('TanDM', tan_d)

    def set_mag_tangent_delta_x(self, tan_d: float):
        self.invoke_method('TanDMX', tan_d)

    def set_mag_tangent_delta_y(self, tan_d: float):
        self.invoke_method('TanDMY', tan_d)

    def set_mag_tangent_delta_z(self, tan_d: float):
        self.invoke_method('TanDMZ', tan_d)

    def set_mag_tangent_delta_given(self, flag: bool = True):
        self.invoke_method('TanDMGiven', flag)

    def set_mag_tangent_delta_frequency(self, frequency: float):
        self.invoke_method('TanDMFreq', frequency)

    def set_mag_tangent_delta_model(self, model: str):
        self.invoke_method('TanDMModel', model)

    def set_mag_const_tangent_delta_strategy_mu(self, strategy: str):
        self.invoke_method('SetConstTanDStrategyMu', strategy)

    def set_mag_const_tangent_delta_model_order_mu(self, order: int):
        self.invoke_method('ConstTanDModelOrderMu', order)

    def set_djordjevic_sarkar_upper_freq_mu(self, frequency: float):
        self.invoke_method('DjordjevicSarkarUpperFreqMu', frequency)

    def set_disp_model_esp(self, model: str):
        self.invoke_method('DispModelEps', model)

    def set_disp_model_mu(self, model: str):
        self.invoke_method('DispModelMu', model)

    def set_eps_infinity(self, eps: float):
        self.invoke_method('EpsInfinity', eps)

    def set_eps_infinity_x(self, eps: float):
        self.invoke_method('EpsInfinityX', eps)

    def set_eps_infinity_y(self, eps: float):
        self.invoke_method('EpsInfinityY', eps)

    def set_eps_infinity_z(self, eps: float):
        self.invoke_method('EpsInfinityZ', eps)

    def set_disp_coeff_eps(self, index: int, eps: float):
        if index < 0 or index > 4:
            raise ValueError('Invalid index.')
        self.invoke_method('DispCoeff'+str(index)+'Eps', eps)

    def set_disp_coeff_eps_x(self, index: int, eps: float):
        if index < 0 or index > 4:
            raise ValueError('Invalid index.')
        self.invoke_method('DispCoeff'+str(index)+'EpsX', eps)

    def set_disp_coeff_eps_y(self, index: int, eps: float):
        if index < 0 or index > 4:
            raise ValueError('Invalid index.')
        self.invoke_method('DispCoeff'+str(index)+'EpsY', eps)

    def set_disp_coeff_eps_z(self, index: int, eps: float):
        if index < 0 or index > 4:
            raise ValueError('Invalid index.')
        self.invoke_method('DispCoeff'+str(index)+'EpsZ', eps)

    def add_disp_eps_pole_1st_order(self, alpha0: float, beta0: float):
        self.invoke_method('AddDispEpsPole1stOrder', alpha0, beta0)

    def add_disp_eps_pole_1st_order_x(self, alpha0: float, beta0: float):
        self.invoke_method('AddDispEpsPole1stOrderX', alpha0, beta0)

    def add_disp_eps_pole_1st_order_y(self, alpha0: float, beta0: float):
        self.invoke_method('AddDispEpsPole1stOrderY', alpha0, beta0)

    def add_disp_eps_pole_1st_order_z(self, alpha0: float, beta0: float):
        self.invoke_method('AddDispEpsPole1stOrderZ', alpha0, beta0)

    def add_disp_eps_pole_2nd_order(
            self, alpha0: float, alpha1: float, beta0: float, beta1: float):
        self.invoke_method('AddDispEpsPole2ndOrder', alpha0, alpha1, beta0, beta1)

    def add_disp_eps_pole_2nd_order_x(
            self, alpha0: float, alpha1: float, beta0: float, beta1: float):
        self.invoke_method('AddDispEpsPole2ndOrderX', alpha0, alpha1, beta0, beta1)

    def add_disp_eps_pole_2nd_order_y(
            self, alpha0: float, alpha1: float, beta0: float, beta1: float):
        self.invoke_method('AddDispEpsPole2ndOrderY', alpha0, alpha1, beta0, beta1)

    def add_disp_eps_pole_2nd_order_z(
            self, alpha0: float, alpha1: float, beta0: float, beta1: float):
        self.invoke_method('AddDispEpsPole2ndOrderZ', alpha0, alpha1, beta0, beta1)

    def add_disp_mu_pole_1st_order(self, alpha0: float, beta0: float):
        self.invoke_method('AddDispMuPole1stOrder', alpha0, beta0)

    def add_disp_mu_pole_1st_order_x(self, alpha0: float, beta0: float):
        self.invoke_method('AddDispMuPole1stOrderX', alpha0, beta0)

    def add_disp_mu_pole_1st_order_y(self, alpha0: float, beta0: float):
        self.invoke_method('AddDispMuPole1stOrderY', alpha0, beta0)

    def add_disp_mu_pole_1st_order_z(self, alpha0: float, beta0: float):
        self.invoke_method('AddDispMuPole1stOrderZ', alpha0, beta0)

    def add_disp_mu_pole_2nd_order(
            self, alpha0: float, alpha1: float, beta0: float, beta1: float):
        self.invoke_method('AddDispMuPole2ndOrder', alpha0, alpha1, beta0, beta1)

    def add_disp_mu_pole_2nd_order_x(
            self, alpha0: float, alpha1: float, beta0: float, beta1: float):
        self.invoke_method('AddDispMuPole2ndOrderX', alpha0, alpha1, beta0, beta1)

    def add_disp_mu_pole_2nd_order_y(
            self, alpha0: float, alpha1: float, beta0: float, beta1: float):
        self.invoke_method('AddDispMuPole2ndOrderY', alpha0, alpha1, beta0, beta1)

    def add_disp_mu_pole_2nd_order_z(
            self, alpha0: float, alpha1: float, beta0: float, beta1: float):
        self.invoke_method('AddDispMuPole2ndOrderZ', alpha0, alpha1, beta0, beta1)

    def set_mu_infinity(self, mu: float):
        self.invoke_method('MuInfinity', mu)

    def set_mu_infinity_x(self, mu: float):
        self.invoke_method('MuInfinityX', mu)

    def set_mu_infinity_y(self, mu: float):
        self.invoke_method('MuInfinityY', mu)

    def set_mu_infinity_z(self, mu: float):
        self.invoke_method('MuInfinityZ', mu)

    def set_disp_coeff_mu(self, index: int, mu: float):
        if index < 0 or index > 4:
            raise ValueError('Invalid index.')
        self.invoke_method('DispCoeff'+str(index)+'Mu', mu)

    def set_disp_coeff_mu_x(self, index: int, mu: float):
        if index < 0 or index > 4:
            raise ValueError('Invalid index.')
        self.invoke_method('DispCoeff'+str(index)+'MuX', mu)

    def set_disp_coeff_mu_y(self, index: int, mu: float):
        if index < 0 or index > 4:
            raise ValueError('Invalid index.')
        self.invoke_method('DispCoeff'+str(index)+'MuY', mu)

    def set_disp_coeff_mu_z(self, index: int, mu: float):
        if index < 0 or index > 4:
            raise ValueError('Invalid index.')
        self.invoke_method('DispCoeff'+str(index)+'MuZ', mu)

    def set_use_si_unit_system(self, flag: bool = True):
        self.invoke_method('UseSISystem', flag)

    def set_gyro_mu_frequency(self, frequency: float):
        self.invoke_method('GyroMuFreq', frequency)

    def set_magnetostatic_dep_source_field(self, source_field: str):
        self.invoke_method('SetMagnetostaticDepSourceField', source_field)

    def set_dispersive_fitting_format_eps(self, format: str):
        self.invoke_method('DispersiveFittingFormatEps', format)

    def set_dispersive_fitting_format_mu(self, format: str):
        self.invoke_method('DispersiveFittingFormatMu', format)

    def add_dispersion_fitting_value_eps(self, d_freq: float, d_val: complex, d_weight: float):
        self.invoke_method('AddDispersionFittingValueEps', d_freq, d_val.real, d_val.imag, d_weight)

    def add_dispersion_fitting_value_mu(self, d_freq: float, d_val: complex, d_weight: float):
        self.invoke_method('AddDispersionFittingValueMu', d_freq, d_val.real, d_val.imag, d_weight)

    def add_dispersion_fitting_value_xyz_eps(
            self, d_freq: float, d_val_x: complex, d_val_y: complex,
            d_val_z: complex, d_weight: float):
        self.invoke_method(
            'AddDispersionFittingValueXYZEps', d_freq, d_val_x, d_val_y, d_val_z, d_weight)

    def add_dispersion_fitting_value_xyz_mu(
            self, d_freq: float, d_val_x: complex, d_val_y: complex,
            d_val_z: complex, d_weight: float):
        self.invoke_method(
            'AddDispersionFittingValueXYZMu', d_freq, d_val_x, d_val_y, d_val_z, d_weight)

    def set_dispersive_fitting_scheme_eps(self, scheme: str):
        self.invoke_method('DispersiveFittingSchemeEps', scheme)

    def set_dispersive_fitting_scheme_mu(self, scheme: str):
        self.invoke_method('DispersiveFittingSchemeMu', scheme)

    def set_max_order_nth_model_fit_eps(self, order: int):
        self.invoke_method('MaximalOrderNthModelFitEps', order)

    def set_max_order_nth_model_fit_mu(self, order: int):
        self.invoke_method('MaximalOrderNthModelFitMu', order)

    def set_error_limit_nth_model_fit_esp(self, limit: float):
        # not documented, found in the history list
        self.invoke_method('ErrorLimitNthModelFitEps', limit)

    def set_error_limit_nth_model_fit_mu(self, limit: float):
        # not documented, found in the history list
        self.invoke_method('ErrorLimitNthModelFitMu', limit)

    def set_use_only_data_in_sim_freq_range_nth_model_eps(self, flag: bool = True):
        self.invoke_method('UseOnlyDataInSimFreqRangeNthModelEps', flag)

    def set_use_only_data_in_sim_freq_range_nth_model_mu(self, flag: bool = True):
        self.invoke_method('UseOnlyDataInSimFreqRangeNthModelMu', flag)

    def set_use_general_dispersion_eps(self, flag: bool = True):
        self.invoke_method('UseGeneralDispersionEps', flag)

    def set_use_general_dispersion_mu(self, flag: bool = True):
        self.invoke_method('UseGeneralDispersionMu', flag)

    def set_tensor_formula_for_eps_r(self):
        self.invoke_method('TensorFormulaFor', 'epsilon_r')

    def set_tensor_formula_for_mu_r(self):
        self.invoke_method('TensorFormulaFor', 'mu_r')

    def set_tensor_formula_real(self, row: int, column: int, formula: str):
        self.invoke_method('TensorFormulaReal', row, column, formula)

    def set_tensor_formula_imag(self, row: int, column: int, formula: str):
        self.invoke_method('TensorFormulaImag', row, column, formula)

    def set_tensor_alignment(self, w_x: float, w_y: float, w_z: float):
        self.invoke_method('TensorAlignment', w_x, w_y, w_z)

    def set_tensor_alignment2(
            self, u_x: float, u_y: float, u_z: float, v_x: float, v_y: float, v_z: float):
        self.invoke_method('TensorAlignment2', u_x, u_y, u_z, v_x, v_y, v_z)

    def reset_spatially_varying_material_parameter(self, prop: str):
        self.invoke_method('ResetSpatiallyVaryingMaterialParameter', prop)

    def set_spatially_varying_material_model(self, prop: str, model: str):
        self.invoke_method('SpatiallyVaryingMaterialModel', prop, model)

    def set_spatially_varying_material_model_aniso(self, prop: str, direction: str, model: str):
        self.invoke_method('SpatiallyVaryingMaterialModelAniso', prop, direction, model)

    def add_spatially_varying_material_parameter(self, prop: str, param: str, value: float):
        self.invoke_method('AddSpatiallyVaryingMaterialParameter', prop, param, value)

    def add_spatially_varying_material_parameter_aniso(
            self, prop: str, direction: str, param: str, value: float):
        self.invoke_method(
            'AddSpatiallyVaryingMaterialParameterAniso', prop, direction, param, value)

    def reset_space_map_material(self, prop: str):
        self.invoke_method('ResetSpaceMapBasedMaterial', prop)

    def set_space_map_model(self, prop: str, model: str):
        self.invoke_method('SpaceMapBasedOperator', prop, model)

    def set_space_map_model_aniso(self, prop: str, direction: str, model: str):
        self.invoke_method('SpaceMapBasedOperatorAniso', prop, direction, model)

    def add_space_map_material_parameter(
            self, prop: str, param: str, value: Union[str, float, int]):
        if isinstance(value, str):
            self.invoke_method('AddSpaceMapBasedMaterialStringParameter', prop, param, value)
        else:
            self.invoke_method('AddSpaceMapBasedMaterialDoubleParameter', prop, param, value)

    def add_space_map_material_parameter_aniso(
            self, prop: str, direction: str, param: str, value: Union[str, float, int]):
        if isinstance(value, str):
            self.invoke_method(
                'AddSpaceMapBasedMaterialStringParameterAniso', prop, direction, param, value)
        else:
            self.invoke_method(
                'AddSpaceMapBasedMaterialDoubleParameterAniso', prop, direction, param, value)

    def convert_material_field(self, file_path_in: str, file_path_out: str):
        self.invoke_method('ConvertMaterialField', file_path_in, file_path_out)

    def reset_tab_mu_differential(self):
        self.invoke_method('ResetTabMuDifferential')

    def add_tab_mu_differential(self, h_field: float, mu_diff: float):
        self.invoke_method('AddTabMuDifferential', h_field, mu_diff)

    def set_generalized_debye_non_lin_dependency(self, dependency: str):
        self.invoke_method('GeneralizedDebyeNonLinDependency', dependency)

    def set_magnetostatic_dep_source_field(self, source_field: str):
        self.invoke_method('SetMagnetostaticDepSourceField', source_field)

    def set_coating_type_definition(self, prop: str):
        self.invoke_method('SetCoatingTypeDefinition', prop)

    def add_tabulated_surface_impedance_deg(
            self, frequency: float, angle: float, z_te: complex, z_tm: complex):
        self.invoke_method(
            'AddTabulatedSurfaceImpedance', frequency, angle,
            z_te.real, z_te.imag, z_tm.real, z_tm.imag)

    def add_tabulated_surface_impedance_rad(
            self, frequency: float, angle: float, z_te: complex, z_tm: complex):
        self.add_tabulated_surface_impedance_deg(
            frequency, np.rad2deg(angle), z_te.real, z_te.imag, z_tm.real, z_tm.imag)

    def add_tabulated_reflection_factor_deg(
            self, frequency: float, angle: float, r_te: complex, r_tm: complex):
        self.invoke_method(
            'AddTabulatedReflectionFactor', frequency, angle,
            r_te.real, r_te.imag, r_tm.real, r_tm.imag)

    def add_tabulated_reflection_factor_rad(
            self, frequency: float, angle: float, r_te: complex, r_tm: complex):
        self.add_tabulated_reflection_factor_deg(
            frequency, np.rad2deg(angle), r_te.real, r_te.imag, r_tm.real, r_tm.imag)

    def add_tabulated_reflection_transmission_factor_deg(
            self, frequency: float, angle: float,
            r_te: complex, r_tm: complex, t_te: complex, t_tm: complex):
        self.invoke_method(
            'AddTabulatedReflectionTransmissionFactor', frequency, angle,
            r_te.real, r_te.imag, r_tm.real, r_tm.imag, t_te.real, t_te.imag, t_tm.real, t_tm.imag)

    def add_tabulated_reflection_transmission_factor_rad(
            self, frequency: float, angle: float,
            r_te: complex, r_tm: complex, t_te: complex, t_tm: complex):
        self.add_tabulated_reflection_transmission_factor_deg(
            frequency, np.rad2deg(angle),
            r_te.real, r_te.imag, r_tm.real, r_tm.imag, t_te.real, t_te.imag, t_tm.real, t_tm.imag)

    def add_temperature_dep_eps(self, d_temperature: float, d_value: float):
        self.invoke_method('AddTemperatureDepEps', d_temperature, d_value)

    def reset_temperature_dep_eps(self):
        self.invoke_method('ResetTemperatureDepEps')

    def add_temperature_dep_mu(self, d_temperature: float, d_value: float):
        self.invoke_method('AddTemperatureDepMu', d_temperature, d_value)

    def reset_temperature_dep_mu(self):
        self.invoke_method('ResetTemperatureDepMu')

    def add_temperature_dep_sigma(self, d_temperature: float, d_value: float):
        self.invoke_method('AddTemperatureDepSigma', d_temperature, d_value)

    def reset_temperature_dep_sigma(self):
        self.invoke_method('ResetTemperatureDepSigma')

    def set_temperature_dep_source_field(self, field_name: str):
        self.invoke_method('SetTemperatureDepSourceField', field_name)

    def add_hb_value(self, h_value: float, b_value: float):
        self.invoke_method('AddHBValue', h_value, b_value)

    def reset_hb_list(self):
        self.invoke_method('ResetHBList')

    def set_use_nl_anisotropy(self, flag: bool = True):
        self.invoke_method('NLAnisotropy', flag)

    def set_nla_stacking_factor(self, factor: float):
        self.invoke_method('NLAStackingFactor', factor)

    def set_nla_direction_x(self, dir: float):
        self.invoke_method('NLADirectionX', dir)

    def set_nla_direction_y(self, dir: float):
        self.invoke_method('NLADirectionY', dir)

    def set_nla_direction_z(self, dir: float):
        self.invoke_method('NLADirectionZ', dir)

    def set_nla_direction(self, x: float, y: float, z: float):
        self.set_nla_direction_x(x)
        self.set_nla_direction_y(y)
        self.set_nla_direction_z(z)

    def set_particle_property(self, prop: str):
        self.invoke_method('ParticleProperty', prop)

    def set_se_mdoel(self, model: str):
        self.invoke_method('SeModel', model)

    def set_se_max_number_of_generations(self, number: int):
        self.invoke_method('SeMaxGenerations', number)

    def set_se_max_number_of_secondaries(self, number: int):
        self.invoke_method('SeMaxSecondaries', number)

    def set_se_ts_param_t1(self, value: float):
        self.invoke_method('SeTsParam_T1', value)

    def set_se_ts_param_t2(self, value: float):
        self.invoke_method('SeTsParam_T2', value)

    def set_se_ts_param_t3(self, value: float):
        self.invoke_method('SeTsParam_T3', value)

    def set_se_ts_param_t4(self, value: float):
        self.invoke_method('SeTsParam_T4', value)

    def set_se_ts_param_sey(self, value: float):
        self.invoke_method('SeTsParam_SEY', value)

    def set_se_ts_param_energy(self, value: float):
        self.invoke_method('SeTsParam_Energy', value)

    def set_se_ts_param_s(self, value: float):
        self.invoke_method('SeTsParam_S', value)

    def set_se_ts_param_pn(self, n: int, value: float):
        self.invoke_method('SeTsParam_PN', n, value)

    def set_se_ts_param_epsn(self, n: int, value: float):
        self.invoke_method('SeTsParam_EpsN', n, value)

    def set_se_rd_param_r(self, value: float):
        self.invoke_method('SeRdParam_R', value)

    def set_se_rd_param_r1(self, value: float):
        self.invoke_method('SeRdParam_R1', value)

    def set_se_rd_param_r2(self, value: float):
        self.invoke_method('SeRdParam_R2', value)

    def set_se_rd_param_q(self, value: float):
        self.invoke_method('SeRdParam_Q', value)

    def set_se_rd_param_p1inf(self, value: float):
        self.invoke_method('SeRdParam_P1Inf', value)

    def set_se_rd_param_energy(self, value: float):
        self.invoke_method('SeRdParam_Energy', value)

    def set_se_bs_param_sigma(self, value: float):
        self.invoke_method('SeBsParam_Sigma', value)

    def set_se_bs_param_e1(self, value: float):
        self.invoke_method('SeBsParam_E1', value)

    def set_se_bs_param_e2(self, value: float):
        self.invoke_method('SeBsParam_E2', value)

    def set_se_bs_param_p1hat(self, value: float):
        self.invoke_method('SeBsParam_P1Hat', value)

    def set_se_bs_param_p1inf(self, value: float):
        self.invoke_method('SeBsParam_P1Inf', value)

    def set_se_bs_param_energy(self, value: float):
        self.invoke_method('SeBsParam_Energy', value)

    def set_se_bs_param_p(self, value: float):
        self.invoke_method('SeBsParam_P', value)

    def set_se_bs_param_w(self, value: float):
        self.invoke_method('SeBsParam_W', value)

    def enable_se_plot_1d_deg(self, angle: float, energy: float):
        self.invoke_method('SePlot1D', True, angle, energy)

    def enable_se_plot_1d_rad(self, angle: float, energy: float):
        self.enable_se_plot_1d_deg(np.rad2deg(angle), energy)

    def disable_se_plot_1d_deg(self):
        self.invoke_method('SePlot1D', False, 0, 0)

    def setup_se_vaughan(
            self, energy_max: float, se_yield_max: float, energy_threshold: float,
            smoothness: float, temperature: float):
        self.invoke_method(
            'SeVaughan', energy_max, se_yield_max, energy_threshold, smoothness, temperature)

    def set_se_import_settings(self, file_name: str, temperature: float):
        self.invoke_method('SeImportSettings', file_name, temperature)

    def set_se_import_data(self, energy: float, sey: float):
        self.invoke_method('SeImportData', energy, sey)

    def set_ion_see_model(self, model: str):
        self.invoke_method('IonSEEModel', model)

    def set_ion_see_import_settings(self, file_name: str, temperature: float):
        self.invoke_method('IonSEEImportSettings', file_name, temperature)

    def set_ion_see_import_data(self, energy: float, sey: float):
        self.invoke_method('IonSEEImportData', energy, sey)

    def set_particle_transparency_settings(self, type: str, percent: float, file_name: str):
        self.invoke_method('ParticleTransparencySettings', type, percent, file_name)

    def set_particle_transparency_import_data(self, energy: float, transparency: float):
        self.invoke_method('ParticleTransparencyImportData', energy, transparency)

    def set_energy_step_for_sey_plots(self, step: float):
        self.invoke_method('SetEnergyStepForSEYPlots', step)

    def set_special_disp_param_for_pic(
            self, esp_inf: float, relax_freq: float, reson_freq: float, reson_width: float,
            lorentz_weight: float):
        self.invoke_method(
            'SpecialDispParamForPIC', esp_inf, relax_freq, reson_freq, reson_width, lorentz_weight)

    def set_special_disp_param_visual(self, max_freq: float, prop_dist: float):
        self.invoke_method('SpecialDispParamVisual', max_freq, prop_dist)

    def set_thermal_type(self, thermal_type: str):
        self.invoke_method('ThermalType', thermal_type)

    def set_thermal_conductivity(self, value: float):
        self.invoke_method('ThermalConductivity', value)

    def set_thermal_conductivity_x(self, value: float):
        self.invoke_method('ThermalConductivityX', value)

    def set_thermal_conductivity_y(self, value: float):
        self.invoke_method('ThermalConductivityY', value)

    def set_thermal_conductivity_z(self, value: float):
        self.invoke_method('ThermalConductivityZ', value)

    def set_specific_heat(self, value: float, unit: str):
        self.invoke_method('SpecificHeat', value, unit)

    def set_blood_flow(self, value: float):
        self.invoke_method('BloodFlow', value)

    def set_metabolic_rate(self, value: float):
        self.invoke_method('MetabolicRate', value)

    def set_voxel_convection(self, value: float):
        self.invoke_method('VoxelConvection', value)

    def set_dynamic_viscosity(self, value: float):
        self.invoke_method('DynamicViscosity', value)

    def set_emissivity(self, value: float):
        self.invoke_method('Emissivity', value)

    def reset_nl_thermal_cond(self):
        self.invoke_method('ResetNLThermalCond')

    def add_nl_thermal_cond(self, temperature: float, value: float):
        self.invoke_method('AddNLThermalCond', temperature, value)

    def add_nl_thermal_cond_aniso(
            self, temperature: float, value_x: float, value_y: float, value_z: float):
        self.invoke_method('AddNLThermalCondAniso', temperature, value_x, value_y, value_z)

    def reset_nl_heat_cap(self):
        self.invoke_method('ResetNLHeatCap')

    def add_nl_specific_heat(self, temperature: float, value: float, unit: str):
        self.invoke_method('AddNLSpecificHeat', temperature, value, unit)

    def reset_nl_blook_flow(self):
        self.invoke_method('ResetNLBloodFlow')

    def add_nl_blood_flow_min_temperature(self, value: float):
        self.invoke_method('SetNLBloodFlowMinTemperature', value)

    def add_nl_blood_flow_basal_value(self, value: float):
        self.invoke_method('SetNLBloodFlowBasalValue', value)

    def add_nl_blood_flow_local_vasodilation_param(self, value: float):
        self.invoke_method('SetNLBloodFlowLocalVasodilationParam', value)

    def add_nl_blood_flow_max_multiplier(self, value: float):
        self.invoke_method('SetNLBloodFlowMaxMultiplier', value)

    def add_nl_dynamic_viscosity(self, temperature: float, value: float):
        self.invoke_method('AddNLDynamicViscosity', temperature, value)

    def set_mechanics_type(self, mechanics_type: str):
        self.invoke_method('MechanicsType', mechanics_type)

    def set_youngs_modulus(self, value: float):
        self.invoke_method('YoungsModulus', value)

    def set_poisson_ratio(self, value: float):
        self.invoke_method('PoissonsRatio', value)

    def set_thermal_expansion_rate(self, value: float):
        self.invoke_method('ThermalExpansionRate', value)

    def reset_temp_dep_youngs_modulus(self):
        self.invoke_method('ResetTempDepYoungsModulus')

    def add_temp_dep_youngs_modulus(self, temperature: float, value: float):
        self.invoke_method('AddTempDepYoungsModulus', temperature, value)

    def set_intrinsic_carrier_density(self, value: float):
        self.invoke_method('IntrinsicCarrierDensity', value)

    def set_lattice_scattering(self, species: str, mobility: float, exponent: float):
        self.invoke_method('LatticeScattering', species, mobility, exponent)

    def set_effective_mass_for_conductivity(self, species: str, effective_mass: float):
        self.invoke_method('EffectiveMassForConductivity', species, effective_mass)

    def enable_auger_recombination(self, gamma_electron: float, gamma_hole: float):
        self.invoke_method('AugerRecombination', True, gamma_electron, gamma_hole)

    def disable_auger_recombination(self):
        self.invoke_method('AugerRecombination', False, 0, 0)

    def enable_band_to_band_recombination(self, rate: float):
        self.invoke_method('BandToBandRecombination', True, rate)

    def disable_band_to_band_recombination(self):
        self.invoke_method('BandToBandRecombination', False, 0)

    def enable_impact_ionization(
            self, electron_ionization_rate: float, electron_exponent: float,
            electron_critical_field: float, hole_ionization_rate: float, hole_exponent: float,
            hole_critical_field: float):
        self.invoke_method(
            'ImpactIonization', True, electron_ionization_rate, electron_exponent,
            electron_critical_field, hole_ionization_rate, hole_exponent, hole_critical_field)

    def disable_impact_ionization(self):
        self.invoke_method('ImpactIonization', False, 0, 0, 0, 0, 0, 0)

    def enable_optically_induced_carrier_generation(self, quantum_efficiency: float):
        self.invoke_method('OpticallyInducedCarrierGeneration', True, quantum_efficiency)

    def disable_optically_induced_carrier_generation(self):
        self.invoke_method('OpticallyInducedCarrierGeneration', False, 0)

    def enable_srh_recombination(
            self, trap_energy_level: float, electron_lifetime: float,
            electron_reference_density: float, hole_lifetime: float, hole_reference_density: float):
        self.invoke_method(
            'SRHRecombination', True, trap_energy_level, electron_lifetime,
            electron_reference_density, hole_lifetime, hole_reference_density)

    def disable_srh_recombination(self):
        self.invoke_method('SRHRecombination', False, 0, 0, 0, 0, 0)

    def set_flow_res_pressure_loss_type_u(self, value: str):
        self.invoke_method('FlowResPressureLossTypeU', value)

    def set_flow_res_pressure_loss_type_v(self, value: str):
        self.invoke_method('FlowResPressureLossTypeV', value)

    def set_flow_res_pressure_loss_type_w(self, value: str):
        self.invoke_method('FlowResPressureLossTypeW', value)

    def set_flow_res_loss_coefficient_u(self, value: float):
        self.invoke_method('FlowResLossCoefficientU', value)

    def set_flow_res_loss_coefficient_v(self, value: float):
        self.invoke_method('FlowResLossCoefficientV', value)

    def set_flow_res_loss_coefficient_w(self, value: float):
        self.invoke_method('FlowResLossCoefficientW', value)

    def set_flow_res_pressure_loss_type_sheet(self, value: str):
        self.invoke_method('FlowResPressureLossTypeSheet', value)

    def set_flow_res_loss_coefficient_sheet(self, value: float):
        self.invoke_method('FlowResLossCoefficientSheet', value)

    def set_flow_res_free_area_ratio(self, value: float):
        self.invoke_method('FlowResFreeAreaRatio', value)

    def set_flow_res_shape_type(self, value: str):
        self.invoke_method('FlowResShapeType', value)

    def set_flow_res_shape_size(self, value: float):
        self.invoke_method('FlowResShapeSize', value)

    def set_flow_res_shape_u_pitch(self, value: float):
        self.invoke_method('FlowResShapeUPitch', value)

    def set_flow_res_shape_v_pitch(self, value: float):
        self.invoke_method('FlowResShapeVPitch', value)

    def get_number_of_materials(self) -> int:
        return self.invoke_method('GetNumberOfMaterials')

    def get_name_of_material_from_index(self) -> str:
        return self.invoke_method('GetNameOfMaterialFromIndex')

    def is_background_material(self, material_name: str) -> bool:
        return self.invoke_method('IsBackgroundMaterial', material_name)

    def get_type_of_background_material(self) -> str:
        return self.invoke_method('GetTypeOfBackgroundMaterial')

    def get_type_of_material(self, material_name: str) -> str:
        return self.invoke_method('GetTypeOfMaterial', material_name)

    def get_color_rgb(self, material_name: str) -> tuple[float, float, float]:
        r = w32com.create_ref_double()
        g = w32com.create_ref_double()
        b = w32com.create_ref_double()
        self.invoke_method('GetColour', material_name, r, g, b)
        return (r.value, g.value, b.value)

    def get_epsilon(self, material_name: str) -> tuple[float, float, float]:
        eps_x = w32com.create_ref_double()
        eps_y = w32com.create_ref_double()
        eps_z = w32com.create_ref_double()
        self.invoke_method('GetEpsilon', material_name, eps_x, eps_y, eps_z)
        return (eps_x.value, eps_y.value, eps_z.value)

    def get_mu(self, material_name: str) -> tuple[float, float, float]:
        mu_x = w32com.create_ref_double()
        mu_y = w32com.create_ref_double()
        mu_z = w32com.create_ref_double()
        self.invoke_method('GetMu', material_name, mu_x, mu_y, mu_z)
        return (mu_x.value, mu_y.value, mu_z.value)

    def get_el_sigma(self, material_name: str) -> tuple[float, float, float]:
        sigma_x = w32com.create_ref_double()
        sigma_y = w32com.create_ref_double()
        sigma_z = w32com.create_ref_double()
        self.invoke_method('GetSigma', material_name, sigma_x, sigma_y, sigma_z)
        return (sigma_x.value, sigma_y.value, sigma_z.value)

    def get_mag_sigma(self, material_name: str) -> tuple[float, float, float]:
        sigma_x = w32com.create_ref_double()
        sigma_y = w32com.create_ref_double()
        sigma_z = w32com.create_ref_double()
        self.invoke_method('GetSigmaM', material_name, sigma_x, sigma_y, sigma_z)
        return (sigma_x.value, sigma_y.value, sigma_z.value)

    def get_corrugation(self, material_name: str) -> tuple[float, float, float]:
        depth = w32com.create_ref_double()
        gap_width = w32com.create_ref_double()
        tooth_width = w32com.create_ref_double()
        self.invoke_method('GetCorrugation', material_name, depth, gap_width, tooth_width)
        return (depth.value, gap_width.value, tooth_width.value)

    def get_ohmic_sheet_impedance(self, material_name: str) -> complex:
        resistance = w32com.create_ref_double()
        reactance = w32com.create_ref_double()
        self.invoke_method('GetOhmicSheetImpedance', material_name, resistance, reactance)
        return complex(resistance, reactance)

    def get_rho(self, material_name: str) -> float:
        rho = w32com.create_ref_double()
        self.invoke_method('GetRho', material_name, rho)
        return rho.value

    def get_dynamic_viscosity(self, material_name: str) -> float:
        viscosity = w32com.create_ref_double()
        self.invoke_method('GetDynamicViscosity', material_name, viscosity)
        return viscosity.value

    def get_dynamic_viscosity(self, material_name: str) -> float:
        emissivity = w32com.create_ref_double()
        self.invoke_method('GetEmissivity', material_name, emissivity)
        return emissivity.value

    def get_thermal_conductivity(self, material_name: str) -> tuple[float, float, float]:
        cond_x = w32com.create_ref_double()
        cond_y = w32com.create_ref_double()
        cond_z = w32com.create_ref_double()
        self.invoke_method('GetThermalConductivity', material_name, cond_x, cond_y, cond_z)
        return (cond_x.value, cond_y.value, cond_z.value)

    def get_specific_heat(self, material_name: str) -> float:
        specific_heat = w32com.create_ref_double()
        self.invoke_method('GetSpecificHeat', material_name, specific_heat)
        return specific_heat.value

    def get_specific_heat(self, material_name: str) -> float:
        heat_capacity = w32com.create_ref_double()
        self.invoke_method('GetHeatCapacity', material_name, heat_capacity)
        return heat_capacity.value

    def get_blood_flow(self, material_name: str) -> float:
        blood_flow = w32com.create_ref_double()
        self.invoke_method('GetBloodFlow', material_name, blood_flow)
        return blood_flow.value

    def get_metabolic_rate(self, material_name: str) -> float:
        metabolic_rate = w32com.create_ref_double()
        self.invoke_method('GetMetabolicRate', material_name, metabolic_rate)
        return metabolic_rate.value

    def get_voxel_convection(self, material_name: str) -> float:
        voxel_convection = w32com.create_ref_double()
        self.invoke_method('GetVoxelConvection', material_name, voxel_convection)
        return voxel_convection.value

    def exists(self, material_name: str) -> bool:
        return self.invoke_method('Exists', material_name)

    def change_background_material(self):
        #NOTE: not documented, found in the history list
        return self.invoke_method('ChangeBackgroundMaterial')

    def set_use_emissivity(self, flag: bool = True):
        #NOTE: not documented, found in the history list
        self.invoke_method('UseEmissivity', flag)