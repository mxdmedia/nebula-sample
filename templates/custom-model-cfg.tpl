CustomModel  "{{ model.name }}"
{
	UseForType		"{{ model.use_for_type }}"

	EnableImpostors  {{ model.enable_imposters | lower }}
	EnableDepthTest  {{ model.enable_depth_test | lower }}
	EnableDepthWrite {{ model.enable_depth_write | lower }}
	EnableBlend      {{ model.enable_blend | lower }}

	Shader           "{{ model.shader }}"
	ShaderUniforms   "{{ model.shader_uniforms }}"

	BaseShape      "{{ model.base_shape }}"
	BaseShapeDims  ({{ model.base_shape_dims|join(' ')}})
	Scale          ({{ model.scale|join(' ')}})
    {% if model.randomize is defined %}
        Randomize      ({{ model.randomize|join(' ')}})
    {% endif %}
	Bright         {{ model.bright }}
	{% if model.particle_color is defined %}
        ParticleColor  ({{ model.particle_color|join(' ')}})
    {% endif %}

	//Dust volume parametrization
	Dust_enabled {{ model.dust_enabled|lower }}
	Dust_volume_height {{ model.dust_volume_height }}
	dust_absorption_factor {{ model.dust_absorption_factor }}
	dust_scattering_factor {{ model.dust_scattering_factor }}
	Dust_volume_density_factor {{ model.dust_volume_density_factor }}
	Albedo {{ model.albedo }}

	//Scale
	Internal_scale 32
	//Raymarcher
	Raymarch_step_count 128
	td_break_value 2.5
	sum_transparency_break (0.01 0.01 0.01)
	//Lights & Stars
	Light_intensivity 0
	Light_Color_11 (1 0.894531 0.894531)
	Light_radius_single_star 20
	Ambient_Light_intensivity 0.3583284695465513
	Ambient_Light_Color_11 (0.836 0.536 0.536)

	Single_star false
	Star_position (4.95868 0 0)
	star_empty_sphere_radius 0
	Star_field_scale 0.550413

	Render_star false
	Star_light_coef_1 13.3884
	Star_light_coef_2 330.579
	Render_star_bloom false
	Bloom_light_coef_1 0.0578512
	Bloom_light_coef_2 578.512

	//HG phase function
	Forward_scattering_g 0.6
	Backward_scattering_g -0.05
	HG_mix_coef 0.75

	//Emission
	Gas_emission_enabled true
	Gas_volume_height 1
	gas_scattering_factor 0.025
	gas_density_factor 0.1
	Emission_gas_1 true
	//Emission_gas_1_external true
	Nebula_emission_color_1 (0.852 0.24270730724502898 0.06)
	Emission_gas_1_direction (0 0 1)
	Emission_gas_1_coef_0 (0 0 0)
	Emission_gas_1_coef_1 0.371901
	Emission_gas_1_coef_2 3.058
	Emission_gas_1_coef_3 1.23967
	Emission_gas_2 true
	//Emission_gas_2_external false
	Nebula_emission_color_2 (0.625 0.20850354608761998 0.186)
	Emission_gas_2_direction (0 1 0)
	Emission_gas_2_coef_0 (0 1.03306 0)
	Emission_gas_2_coef_1 0.5868
	Emission_gas_2_coef_2 1.074
	Emission_gas_2_coef_3 1.57
	Emission_gas_3 true
	//Emission_gas_3_external false
	Nebula_emission_color_3 (0.067 0.2764083005934244 0.613)
	Emission_gas_3_direction (0 1 0)
	Emission_gas_3_coef_0 (0 0 0.5)
	Emission_gas_3_coef_1 0.380165
	Emission_gas_3_coef_2 0.8391283257324944
	Emission_gas_3_coef_3 1.4643548275935205

	Emission_intensivity_coef 80

	NebulaCentPos (0 0 0)

	// SCALE
	NebScaleAbsBoth false
	NebScaleAbsX true
	NebScaleAbsY false
	NebScale 1.32231
	NebScaleCoef (0.991737 0.991737)

	// Spiral noise
	SpirNoiseNudge (4.172823130838111 5.524340788815399)
	SpirNoiseAmount (-1 -1)
	SpirNoiseIter (2 2)
	SpirNoiseCoef (1.73373 1.73373)
	//Spiral Noise 3D
	Nudge_3D_2 (1.90083 1.90083)
	Noise_amount_3D_2 (-1.90083 -3.22314)
	Frequency_iteration_count_3D_2 (0.702479 2.56198)
	SpirNoise3DCoef_2 (6.28099 6.19835)

	// FORM
	NebulaFormPlane false
	NebulaFormPlaneSign (1.03306 0.206612)
	NebulaFormPlaneXYZ (0.909091 1 -0.413223)
	NebulaFormPlaneHeight 0.0826445

	NebulaFormDsk true
	NebulaFormDskSign (0.029576188342858384 0.029576188342858384)
	NebulaFormDskParam (2.0893640432410665 4.184738250589496 0.7787042130893607)

	NebulaFormCyl false
	NebulaFormCylSign (-0.785124 -0.785124)
	NebulaFormCylParam (6.551844226683222 6.988295882796854)

	NebulaFormSph true
	NebulaFormSphSign (1.19835 1.19835)
	NebulaFormSphRad 0.22993781307913758

	NebulaFormCapsule false
	NebulaFormCapsuleSign (0.206612 0.206612)
	NebulaFormCapsulePos_1 (-19.6694 -20 10.0826)
	NebulaFormCapsulePos_2 (20 -9.09091 5.45455)
	NebulaFormCapsuleRadius 22.4793

	NebulaFormTorus true
	NebulaFormTorusSign (-0.206612 -0.289256)
	NebulaFormTorusRadius_1 21.0744
	NebulaFormTorusRadius_2 23.323557543025927

	NebulaFormSpir false
	NebulaFormSpirSign (0.0413223 -0.0413223)
	NebulaFormSpirParam (1.98347 3.01653 1.07438 1)

	NebulaFormNoise true
	NebulaFormNoiseSign (-0.2 -0.2)
	NebulaFormNoiseCoef1 11.9008
	NebulaFormNoiseCoef2 0.785124

	NebulaFormFBMNoise true
	NebulaFormFBMNoiseSign (-0.7399867083310339 0.4570931043738877)
	NebulaFormFBMNoiseCoef 16.777396977889172

	NebulaFormSpirNoise true
	NebulaFormSpirNoiseSign (0.785124 0.785124)
	NebulaFormSpirNoiseCoef1 0.009378531825273706
	NebulaFormSpirNoiseCoef2 160.78542817843055
	NebulaFormSpirNoiseCoef3 0.5477913249088476

	NebulaFormSpirIQNoise true
	NebulaFormSpirIQNoiseSign (1.1157 1.1157)
	NebulaFormSpirIQNoiseCoef1 0.5257665397451281
	NebulaFormSpirIQNoiseCoef2 204.15262807302216
	NebulaFormSpirIQNoiseCoef3 4.46281
	NebulaFormSpirIQNoiseCoef4 1.7514485328427074

	NebulaFormSpirNoise3D false
	NebulaFormSpirNoise3DSign (1 1)
	NebulaFormSpirNoise3DCoef 1

	// Map
	NebulaMapTwist false
	NebulaMapTwistCoef1 0
	NebulaMapTwistCoef2 0.0247934

	NebulaMapThickCoef (-0.5 -1.1157)
	ExpansionBegin	2.451545000000000e+06
	ExpansionDuration	0.000000000000000e+00
}