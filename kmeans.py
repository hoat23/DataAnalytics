import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sb
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
# link: http://www.aprendemachinelearning.com/k-means-en-python-paso-a-paso/
#%matplotlib inline
print("[START] Iniciando kmeans.py")
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams['figure.figsize'] = (16,9)
plt.style.use('ggplot')

dataframe = pd.read_csv(r"analisis.csv")
print("########################################################################################################")
# Mostramos algunos datos
print(dataframe.head())
print("########################################################################################################")
# Calculamos las principales medidas estadisticas
print(dataframe.describe())
print("########################################################################################################")
# Contamos por categoria

print(dataframe.groupby('categoria').size())
print("########################################################################################################")
# Analizando la dispersion de los mismos
#dataframe.drop( ['categoria'],1).hist()

print("########################################################################################################")
# Elegimos 3 dimensiones: op, ex, ag y las cruzamos para ver si existe una pista de su agrupación y relación de sus categorías
sb.pairplot(dataframe.dropna(), hue='categoria', height=4, vars=["op","ex","ag"], kind='scatter') #ACP

print("########################################################################################################")
X = np.array(dataframe[["op","ex","ag"]])
Y = np.array(dataframe['categoria'])
print("x.shape={0} \t y.shape={1}".format(X.shape,Y.shape))

print("########################################################################################################")
fig = plt.figure()
ax = Axes3D(fig)
colores=['blue','red','green','blue','cyan','yellow','orange','black','pink','brown','purple']
asignar = []
for row in Y:
    asignar.append(colores[row])
ax.scatter(X[:,0], X[:,1], X[:,2], c=asignar, s=60)
#plt.show()

# Obtener el valor K
print("[END  ]")
