## @knitr Item1
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

## @knitr Item2
class Analysis:
    def __init__(self,path): 
        self.df = pd.read_csv(path)
        self.df = self.df.set_index('canton')
        self.fecha = ['14/07/2021','20/07/2021']
        self.x = []
        self.y = []
        self.labels = []

    def Acotar(self, cantones):
        if(cantones == 0):
            self.df = self.df.loc[:,self.fecha[0]:self.fecha[1]]
        else:
            self.df = self.df.loc[cantones, self.fecha[0]:self.fecha[1]]

    def canton(self,canton):   # canton = 'columna' (string) |  fecha = ['fecha_inical','fecha_final'] (formato de fecha: dia/mes/año)
        self.x = self.df.loc[:,self.fecha[0]:self.fecha[1]].columns.values
        self.y = list(self.df.loc[canton, self.fecha[0]:self.fecha[1]])
        self.labels = [canton]
        
    def provincia(self):   
        self.x = ['Otros','San José','Alajuela','Cartago','Heredia','Guanacaste','Puntarenas','Limón'] 
        self.df = self.df.set_index('cod_provin')
        self.df = self.df.loc[:,self.fecha[1]]
        prov, cant = 1, 0
        self.y.append(0)
        for i in range(len(self.df.index)):
            if prov == self.df.index[i]:
                cant+=self.df.iloc[i,]
            else:
                self.y.append(cant)
                cant = self.df.iloc[i,] 
                prov+=1
            if self.df.index[i]  == 9:
                self.y[0] = self.df.iloc[i,]
           
    def ACP(self,cantones):
        self.Acotar(cantones)
        self.labels = self.df.index.tolist()
        pca = PCA(n_components=2, svd_solver="auto")
        pca_data = pca.fit_transform(self.df)
        self.x = pca_data[:, 0] 
        self.y = pca_data[:, 1]
       

    def Plot(self, parametro):
        if parametro == 0:  #0 para graficar ACP
            plt.scatter(self.x, self.y)
            for i in range(len(self.x)):
                plt.annotate(self.labels[i], xy = (self.x[i], self.y[i]), xytext = (self.x[i]+0.1, self.y[i]+0.1))
            plt.title("Modelo ACP de casos covid activos (Cantones)")
            plt.show()
        elif parametro == 1: # 1 para cantones
            plt.plot(self.x,self.y, label = self.labels[0])
            plt.xticks(rotation=45)
            plt.title("Casos activos de covid-19 por fecha (Cantones)")
            plt.xlabel("Fecha")
            plt.ylabel("Casos activos")
            plt.legend()
            plt.show()
        elif parametro == 2: # 2 para provincias
            plt.bar(self.x,self.y)
            plt.title("Casos del dia")
            plt.xticks(rotation=45)
            plt.show()
        
    
## @knitr Item2
##################################### main

####Obtener datos#### 

##metodo provincias
obj1= Analysis('Covid19/archivosDeDatos/07_20_21_CSV_ACTIVOS_UTF8.csv') #path del csv con los datos
obj1.fecha = ['21/04/2020','11/5/20'] #intervalo de la fecha a analizar
obj1.provincia()  #aplicando metodo para obtener los ejes de datos que queremos graficar
# Estos serian x y
print(obj1.x) #['Otros', 'San José', 'Alajuela', 'Cartago', 'Heredia', 'Guanacaste', 'Puntarenas', 'Limón']
print(obj1.y) #[7, 144, 45, 21, 24, 15, 15, 6]
#el parametro de plot depende del tipo de grafica que queramos (0 para dispersion, modelo ACP), (1 para grafico de linea, metodo cantones), (2 para grafico de barras, metodo provincias) 
obj1.Plot(2) 

print("---------------")

##metodo canton
obj2= Analysis('Covid19/archivosDeDatos/07_20_21_CSV_ACTIVOS_UTF8.csv') #se pone como prarametro path del csv con los datos
obj2.fecha = ['21/04/2020','11/5/20'] #intervalo de la fecha a analizar
obj2.canton('San José') #Se le pasa el nombre del canton a analizar
# Estos serian x y
print(obj2.x) #['21/04/2020' '22/04/2020' '23/04/2020' '24/04/2020' '25/04/2020', ......., '11/5/20']
print(obj2.y) #[82, 85, 84, 82, 74, 72, 69, 67, 70, 68, 63, 58, 57, 55, 54, 49, 49, 50, 47, 43, 39]
#el parametro de plot depende del tipo de grafica que queramos (0 para dispersion, modelo ACP), (1 para grafico de linea, metodo cantones), (2 para grafico de barras, metodo provincias) 
obj2.Plot(1) 

print("---------------")

##metodo ACP
obj3 = Analysis('Covid19/archivosDeDatos/07_20_21_CSV_ACTIVOS_UTF8.csv') #se pone como prarametro path del csv con los datos
obj3.fecha = ['21/04/2020','11/5/20'] #intervalo de la fecha a analizar
obj3.ACP(['Sarapiquí','San Carlos','Montes de Oca','Pérez Zeledón','Pococí','Limón','Alajuela','Tilarán','Santa Ana','Escazú','Belén']) # parametro es vector con cantones a analizar 
#Estos serian x y
print(obj3.x) #[-3.66144504e+01  3.46683145e+01 -4.09307286e-03 -3.60899283e+01, ........, -3.08982622e+01]
print(obj3.y) #[-1.62344799 13.55067112 11.12623988 -3.00321285 -5.461465   -2.6140506, ....... , 2.00607259]
#el parametro de plot depende del tipo de grafica que queramos (0 para dispersion, modelo ACP), (1 para grafico de linea, metodo cantones), (2 para grafico de barras, metodo provincias) 
obj3.Plot(0) 
