import math
import geopandas as gpd
from shapely.geometry import Point
import math
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt


# Crear un GeoDataFrame con un rectángulo de 4 lados
rectangle = gpd.GeoDataFrame(geometry=[Polygon([(1, 1), (3, 1), (3, 2), (1, 2)])])
print('Rectángulo original:')
print(rectangle)

# Rotar el rectángulo 45 grados
angle = 45
rad = math.radians(angle)
rotated_rectangle = rectangle.rotate(rad, origin=(2, 1.5))
rotated_rectangle.reset_index(drop=True, inplace=True)
print('Rectángulo rotado:')
print(rotated_rectangle)

# Crear un GeoSeries con un punto
point = gpd.GeoSeries(Point(2, 1.5))

# Crear una figura y unos ejes
fig, ax = plt.subplots()

# Graficar el rectángulo original
rectangle.plot(ax=ax, color='blue', alpha=0.1, edgecolor='none')

# Graficar el rectángulo rotado
rotated_rectangle.plot(ax=ax, color='red', alpha=0.1, edgecolor='none')

# Verificar si el punto se encuentra dentro del rectángulo rotado
if rotated_rectangle.contains(point.iloc[0]):
    print('El punto se encuentra dentro del rectángulo rotado.')
    point.plot(ax=ax, color='green', markersize=100)
else:
    print('El punto no se encuentra dentro del rectángulo rotado.')
    point.plot(ax=ax, color='red', markersize=100)

# Configurar la figura y mostrarla
ax.set_title('Rectángulo original y rectángulo rotado')
ax.set_aspect('equal')
plt.show()