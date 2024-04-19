import pandas as pd
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

# Es carreguen les dades del arxiu CSV 
df = pd.read_csv('2beffac2-1c5a-4abf-8f4c-497f65887003.csv')

# S'extreuen les coordenadas X i Y del Dataframe
points = df[['COORD_X', 'COORD_Y']].values

# Es calcula el Convex Hull
hull = ConvexHull(points)

# Es crea la figura i l'eix
fig, ax = plt.subplots()

# Es grafiquen els punts originals
ax.plot(points[:, 0], points[:, 1], 'o', label='Punts', color='gray')

tipos_senal = df['TIPO_SENAL'].unique()
for tipo in tipos_senal:
    puntos_tipo = df[df['TIPO_SENAL'] == tipo]
    ax.plot(puntos_tipo['COORD_X'], puntos_tipo['COORD_Y'], 'o', label=tipo)

# Gràfic del Convex Hull
for simplex in hull.simplices:
    ax.plot(points[simplex, 0], points[simplex, 1], 'k-')

# Configurar etiquetas y leyenda
ax.set_xlabel('COORD_X')
ax.set_ylabel('COORD_Y')
ax.set_title('Convex Hull - Camino de Santiago')
ax.legend()

# Es mostra la visualització
plt.show()
