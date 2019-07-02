import random

def get_emission_color(color_type, color_id):
    if color_id == 1:
        return get_emission_color_1(color_type)
    elif color_id == 2:
        return get_emission_color_2(color_type)
    elif color_id == 3:
        return get_emission_color_3(color_type)

def get_emission_color_1(color_type):
    if color_type == 1:
        return [random.uniform(0, 1) for x in range(3)]
    elif color_type == 2:
        return [0.811, random.uniform(0.25, 0.55), 0.236]
    elif color_type == 3:
        return [0.926, random.uniform(0.400, 0.600), 0.137]
    elif color_type == 4:
        return [0.938 , random.uniform(0, 0.2), 0.100]
    elif color_type == 5:
        colors = [
            [0.953, random.uniform(0.3, 0.55), 0.328],
            [0.883, random.uniform(0.49, 0.55), 0.490],
            [0.585, 0.232, random.uniform(0.4, 0.6)]
        ]
        return colors[random.randint(0,2)]
    elif color_type == 6:
        return get_emission_color_1(random.randint(2,5))

def get_emission_color_2(color_type):
    if color_type == 1:
        return [random.uniform(0, 1) for x in range(3)]
    elif color_type == 2:
        return [0.917969, 0.179291, random.uniform(0.25, 0.55)]
    elif color_type == 3:
        return [0.898, random.uniform(0.5, 0.7), 0.467]
    elif color_type == 4:
        return [0.844, random.uniform(0.450, 0.650), 0.488]
    elif color_type == 5:
        colors = [
            [random.uniform(0.55, 0.7), 0.424, 0.738],
            [0.746, 0.280, random.uniform(0.35, 0.65)],
            [0.746, random.uniform(0.28, 0.4), 0.280]
        ]
        return colors[random.randint(0,2)]
    elif color_type == 6:
        return get_emission_color_2(random.randint(2,5))

def get_emission_color_3(color_type):
    if color_type == 1:
        return [random.uniform(0, 1) for x in range(3)]
    elif color_type == 2:
        return [random.uniform(0.7, 0.9), random.uniform(0.75, 0.9), 0.533]
    elif color_type == 3:
        return [0.276, random.uniform(0.600, 0.800), 0.906]
    elif color_type == 4:
        return [0.088, random.uniform(0.55, 0.7), 0.863]
    elif color_type == 5:
        colors = [
            [0.358, random.uniform(0.6, 0.9), 0.926],
            [0.125, random.uniform(0.3, 0.45), 0.46],
            [0.67, 0.297, random.uniform(0.3, 0.45)]
        ]
        return colors[random.randint(0,2)]
    elif color_type == 6:
        return get_emission_color_3(random.randint(2,5))
