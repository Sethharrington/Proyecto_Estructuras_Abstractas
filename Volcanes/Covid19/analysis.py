## @knitr Item1 
import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

## @knitr Item2
class Analysis:
    def __init__(self,path): 
        self.df = pd.read_csv(path)
        self.df = self.df.set_index('canton')
        self.x = []
        self.y = []
    def canton(self,canton, fecha):   # canton = 'columna' (string) |  fecha = ['fecha_inical','fecha_final'] (formato de fecha: dia/mes/año)
        self.x = self.df.loc[:,fecha[0]:fecha[1]].columns.values
        self.y = self.df.loc[canton, fecha[0]:fecha[1]]
    def imprimirCanton(self, canton):    
        plt.plot(self.x,self.y, label = canton)
        plt.title("Casos activos de covid-19 por fecha (Cantones)")
        plt.xlabel("Fecha")
        plt.ylabel("Casos activos")
        plt.legend()
        plt.show()

    def Acotar(self, fecha, cantones):
        if(cantones == 0):
            self.df = self.df.loc[:,fecha[0]:fecha[1]]
        else:
            self.df = self.df.loc[cantones, fecha[0]:fecha[1]]

    def ACP(self):
        labels = self.df.index.tolist()
        print(len(labels))
        pca = PCA(n_components=2, svd_solver="auto")
        pca_data = pca.fit_transform(self.df)
        x , y = pca_data[:, 0] , pca_data[:, 1]
        plt.scatter(x, y)
        for i in range(len(x)):
            plt.annotate(labels[i], xy = (x[i], y[i]), xytext = (x[i]+0.1, y[i]+0.1))
        plt.title("Modelo ACP de casos covid activos (Cantones)")
        plt.show()
    
## @knitr Item3
##################################### main
'''fecha = ['21/04/2020','31/12/2020'] #fecha para pruebas
obj = Analysis('Covid19/archivosDeDatos/07_20_21_CSV_ACTIVOS_UTF8.csv')

## @knitr Item4
#### pruebas de metodo canton
obj.canton('Sarapiquí', fecha )
obj.canton('San Carlos', fecha )
#obj.canton('Montes de Oca', fecha )
#obj.canton('Pérez Zeledón', fecha )

## @knitr Item5
#### pruebas de metodo ACP
obj.Acotar(fecha, 0)
obj.ACP()

obj.Acotar(fecha,['Sarapiquí','San Carlos','Montes de Oca','Pérez Zeledón','Pococí','Limón','Alajuela','Tilarán','Santa Ana','Escazú','Belén'])
obj.ACP()'''
