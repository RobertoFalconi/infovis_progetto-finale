import csv
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
from matplotlib.mlab import PCA as mlabPCA
from sklearn import preprocessing

Input="dataset/dataset.csv"
OUTPUT="datasetRegioni.js"
f = open(Input, 'r')
reader = csv.reader(f)


df = pd.read_csv('dataset/dataset.csv', encoding="utf-8")
target = df.Regioni
print(target)
df = df.drop('Regioni', axis=1).reset_index(drop=True)
X = df.values
scaler = StandardScaler().fit_transform(X)
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(scaler)
principalDf = pd.DataFrame(data = principalComponents
             , columns = ['principal component 1', 'principal component 2'])
print(principalDf)

finalDf = pd.concat([principalDf, target], axis = 1)
print(finalDf)

fig = plt.figure()
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2-component PCA', fontsize = 20)
ax.set_facecolor('xkcd:light grey')
targets = target
colors = ['r', 'g', 'b', '#d104b5', '#fffa00', '#a8ff7c', '#00ff00',
'#00ffa1', '#ff96ca', '#cca72e', '#ff8800', '#5977ff', '#563700',
'#898500', '#ddff96', '#96ffe3', '#96f9ff', '#b599ff', '#8b5b8e',
'#7c0000']
for target, color in zip(targets,colors):
    indicesToKeep = finalDf['Regioni'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2']
               , c = color
               , s = 50)
ax.legend(targets)
ax.grid()

plt.savefig("plots/pca.png")
plt.show()
plt.close(fig)

#print(pca.explained_variance_ratio_)



lista = []
for row in reader:
    lista.append(row)
lista.pop(0)
f2 = open(OUTPUT, 'w')
app=[] 
cont=0
for i in lista:
    if (i[0].find("Italia")==-1):
        if(i[0].find("Totale")==-1):
            b=i[0].replace(" ","").replace("'","") + i[1]
            app.append(b)
            anno=i[1]
            a = "var " + i[0].replace(" ","").replace("'","") + i[1] + " = {id: '" + i[0][0:3] + "', vu1t: " + i[4] + ", vu1m: " + i[
                5] + ", vu1f: " + i[6] + ", ve1t: " + i[7] + ", ve1m: " + i[8] + ", ve1f: " + i[9] + ", vu2t: " + i[
                    10] + ", vu2m: " + i[11] + ", vu2f: " + i[12] + ", ve2t: " + i[13] + ", ve2m: " + i[14] + ", ve2f: " + i[
                    15] + ", vu3t: " + i[16] + ", vu3m: " + i[17] + ", vu3f: " + i[18] + ", ve3t: " + i[19] + ", ve3m: " + i[
                    20] + ", ve3f: " + i[21] + ", vu4t: " + i[22] + ", vu4m: " + i[23] + ", vu4f: " + i[24] + ", ve4t: " + i[
                    25] + ", ve4m: " + i[26] + ", ve4f: " + i[27] + ", put: " + i[28] + ", pum: " + i[29] + ", puf: " + i[
                    30] + ", pet: " + i[31] + ", pem: " + i[32] + ", pef: " + i[33] + "};"
        else:
            a = "var " + i[0].replace(" ","").replace("'","") + " = {id: '" + i[0][0:3] + i[1][2:4] + "', vu1t: " + i[4] + ", vu1m: " + i[
                5] + ", vu1f: " + i[6] + ", ve1t: " + i[7] + ", ve1m: " + i[8] + ", ve1f: " + i[9] + ", vu2t: " + i[
                    10] + ", vu2m: " + i[11] + ", vu2f: " + i[12] + ", ve2t: " + i[13] + ", ve2m: " + i[14] + ", ve2f: " + i[
                    15] + ", vu3t: " + i[16] + ", vu3m: " + i[17] + ", vu3f: " + i[18] + ", ve3t: " + i[19] + ", ve3m: " + i[
                    20] + ", ve3f: " + i[21] + ", vu4t: " + i[22] + ", vu4m: " + i[23] + ", vu4f: " + i[24] + ", ve4t: " + i[
                    25] + ", ve4m: " + i[26] + ", ve4f: " + i[27] + ", put: " + i[28] + ", pum: " + i[29] + ", puf: " + i[
                    30] + ", pet: " + i[31] + ", pem: " + i[32] + ", pef: " + i[33] + "};"
        f2.writelines(a)
        f2.write("\n")
        cont+=1
    if(cont==21):
        a="var Regioni"+str(anno)+" = ["
        for reg in app:
            a+=reg+","
        a=a[:len(a)-1]
        a+="];"
        f2.writelines(a)
        f2.write("\n\n")
        cont=0
        app=[]
