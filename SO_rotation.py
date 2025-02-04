import numpy as np

# Função para rodar um vetor na direção de rotação desejada
def rotate_vector(v, axis, theta):
    axis = axis / np.linalg.norm(axis)
    cos_theta = np.cos(theta)
    sin_theta = np.sin(theta)

    # Fórmula da rotação de Rodrigues
    rotated_v = (v * cos_theta +
                 np.cross(axis, v) * sin_theta +
                 axis * np.dot(axis, v) * (1 - cos_theta))
    return rotated_v

# Carregar coordenadas do arquivo
def load_coordinates(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    title = lines[1].strip()
    coordinates = [line.split() for line in lines[2:36]]
    return title, coordinates

# Salvar as coordenadas no arquivo
def save_coordinates(filename, title, coordinates):
    with open(filename, 'w') as file:
        file.write(f"{len(coordinates)}\n")
        file.write(title + "\n")
        for coord in coordinates:
            file.write(f"{coord[0]} {' '.join(map(str, coord[1:]))}\n")

# Converter as coordenadas lidas do arquivo numa matriz NumPy para facilitar os cálculos
def coordinates_to_array(coordinates):
    return np.array([[float(x), float(y), float(z)] for _, x, y, z in coordinates])

# Rodar monómero
def rotate_monomer(coordinates, axis_point, axis_direction, angle_degrees):
    angle_radians = np.radians(angle_degrees)
    rotated_coords = []

    for coord in coordinates:
        vector = coord - axis_point
        rotated_vector = rotate_vector(vector, axis_direction, angle_radians)
        new_coord = axis_point + rotated_vector
        rotated_coords.append(new_coord)

    return np.array(rotated_coords)

def main():
    # Dados do problema
    input_filename = "SO_coordinates_initial_rot.xyz"
    output_filename = "SO_coordinates_rot_5.xyz"
    angle = 5  # Rotaçao em graus

    # Carregar as coordenadas do arquivo
    title, coordinates = load_coordinates(input_filename)
    coordinates_array = coordinates_to_array(coordinates)

    # Separação de coordenadas
    static_monomer = coordinates[0:17]
    dynamic_monomer_coords_array = coordinates_array[17:34]

    # Posição do centro do anel hexagonal do segundo monómero
    # Tomamos as médias das posições dos átomos nas posições típicas do ciclo
    # (Baseado nos padrões de atomos de um benzeno 'C6H5O' composto tipo)
    center_point = np.mean(dynamic_monomer_coords_array[0:6], axis=0)

    # Defina uma direção de rotação em 90 graus no plano atual
    # Considerando um vetor normal ao plano usando produto vetorial
    vector1 = dynamic_monomer_coords_array[1] - dynamic_monomer_coords_array[0]
    vector2 = dynamic_monomer_coords_array[2] - dynamic_monomer_coords_array[1]
    normal_vector = np.cross(vector1, vector2)
    
    # Rodar coordenadas do segundo monómero
    rotated_dynamic_monomer_coords = rotate_monomer(dynamic_monomer_coords_array, center_point, normal_vector, angle)

    # Criar coordenadas finais substituindo as do segundo monómero
    final_coordinates = static_monomer + [[coordinates[i][0], *rotated_dynamic_monomer_coords[i - 17]] for i in range(17, 34)]

    # Gravar as novas coordenadas no novo arquivo
    save_coordinates(output_filename, title, final_coordinates)

if __name__ == "__main__":
    main()
