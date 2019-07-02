# Function to provide data structure for base parameters
# parameters can be overridden or new parameters added
# through function's key-word arguments.  e.g.:
# base_parameters(name='New Name', randomize=[1, 2, 3])
def base_parameters(**kwargs):
    base_model = {
        'name': 'Model Name',
        'use_for_type': 'Nebula/Diffuse',
        'enable_imposters': True,
        'enable_depth_test': False,
        'enable_depth_write': False,
        'enable_blend': True,
        'shader': 'nebula_raymarch.glsl',
        'shader_uniforms': 'nebula_raymarch_uniforms.cfg',
        'base_shape': 'box',
        'base_shape_dims': [30, 32, 32],
        'scale': [1, 1, 1],
        'bright': 2,
    }
    return  {
        **base_model,
        **kwargs
    }

def dust_parameters(**kwargs):
    dust_params = {
        'dust_enabled': True,
	    'dust_volume_height': 1,
	    'dust_absorption_factor': 0.4,
	    'dust_scattering_factor': 0.6,
	    'dust_volume_density_factor': 0.01,
	    'albedo': 0.6
    }
    return {
        **dust_params,
        **kwargs
    }

def emission_parameters(**kwargs):
    emission_params = {
        'Gas_emission_enabled': True,
	    'Gas_volume_height': 1,
	    'gas_scattering_factor': 0.025,
	    'gas_density_factor': 0.1
    }
    return {
        **emission_params,
        **kwargs
    }

def emission_gas_params(id, active, color=[0,0,0], **kwargs):
    # assign True/False, and Nebula Emission color
    base_params = {
        'emission_gas_{}'.format(id): active,
        'nebula_emission_color_{}'.format(id): color
    }

    eg_params = {
	    'direction': [0, 0, 1],
	    'coef_0': [0, 0, 0],
	    'coef_1': 0.371901,
	    'coef_2': 3.058,
	    'coef_3': 1.23967,
        **kwargs
    }

    eg_params = { 'emission_gas_{}_{}'.format(id, k): v for k, v in eg_params.items() }

    return {
        **base_params,
        **eg_params
    }
