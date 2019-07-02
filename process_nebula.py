import random

from jinja2 import Environment, FileSystemLoader

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

env = Environment(
    loader=FileSystemLoader('./templates')
)

template = env.get_template('custom-model-cfg.tpl')

preset = 2
dust = 'y'

if preset == 1:
    base_params = base_parameters(
        name='Preset 1- Nebula name',
        base_shape_dims=[18, 18, 18],
        randomize=[random.uniform(-1, 1) for x in range(1,4)],
        particle_color=[0.952393, 0.390625, 1]
    )

    dust_params = dust_parameters(
        dust_volume_height=random.uniform(1, 10),
        dust_volume_density_factor=random.uniform(0.5, 5) if dust == 'y' else 1,
    )

if preset == 2:
    base_params = base_parameters(
        name='Preset 2- Nebula name',
        base_shape_dims=[30, 30, 30],
    )

    dust_params = dust_parameters(
        dust_volume_height=random.uniform(1, 10),
        dust_volume_density_factor=random.uniform(0.5, 5) if dust == 'y' else 1,
    )

model = {
    **base_params,
    **dust_params
}

print(template.render(model=model))


