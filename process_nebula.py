import random
from default_parameters import *

from color_calcs import get_emission_color
from jinja2 import Environment, FileSystemLoader

env = Environment(
    loader=FileSystemLoader('./templates')
)

template = env.get_template('custom-model-cfg.tpl')

preset = 1
dust = 'y'
color = 6

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

    eg_1_kwargs = {
        'direction': [0, 0, 1],
        'coef_0': [0, 0, 0],
        'coef_1': 0.140496,
        'coef_2': 3.96694,
        'coef_3': 0.75
    }
    eg_2_kwargs = {
        'direction': [0, 1, 0],
        'coef_0': [0, 1, 0],
        'coef_1': 0.446281,
        'coef_2': random.uniform(1.2, 1.8),
        'coef_3': 1.364
    }
    eg_3_kwargs = {
        'direction': [0, 1, 0],
        'coef_0': [0, 0, 0.5],
        'coef_1': 0.35,
        'coef_2': random.uniform(0.8, 1.1),
        'coef_3': random.uniform(1.3, 1.5)
    }

if preset == 2:
    base_params = base_parameters(
        name='Preset 2- Nebula name',
        base_shape_dims=[30, 30, 30],
    )

    dust_params = dust_parameters(
        dust_volume_height=random.uniform(1, 10),
        dust_volume_density_factor=random.uniform(0.5, 5) if dust == 'y' else 1,
    )

    eg_1_kwargs = {
        'direction': [0.14876, 0.247934, 0],
        'coef_0': [4.2562, 0.53719, 0.867769],
        'coef_1': 0.0909091,
        'coef_2': 1.28099,
        'coef_3': 2.19008
    }
    eg_2_kwargs = {
        'direction': [0.77686, 0, 0],
        'coef_0': [4.58678, -0.619835, -0.702479],
        'coef_1': 0.0909091,
        'coef_2': 1.1157,
        'coef_3': 0.867769
    }
    eg_3_kwargs = {
        'direction': [0, 0, 0.479339],
        'coef_0': [5, 3.34711, 5],
        'coef_1': 0.00826446,
        'coef_2': 0.578512,
        'coef_3': 0.826446
    }

eg_1_color = get_emission_color(color, 1)
eg_1_params = emission_gas_params(1, True, eg_1_color, **eg_1_kwargs)

eg_2_color = get_emission_color(color, 2)
eg_2_params = emission_gas_params(2, True, eg_2_color, **eg_2_kwargs)

eg_3_color = get_emission_color(color, 3)
eg_3_params = emission_gas_params(3, True, eg_3_color, **eg_3_kwargs)

model = {
    **base_params,
    **dust_params,
    **eg_1_params,
    **eg_2_params,
    **eg_3_params
}

print(template.render(model=model))


