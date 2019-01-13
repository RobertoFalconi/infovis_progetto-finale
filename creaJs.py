import csv
from time import time
import pandas as pd
import numpy as np
import seaborn as sns
from ggplot import *
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
from matplotlib.mlab import PCA as mlabPCA
import matplotlib.patheffects as PathEffects
from matplotlib.pyplot import scatter
from sklearn import preprocessing
from sklearn import manifold
from sklearn.manifold import MDS
from sklearn.manifold import TSNE
from sklearn.metrics import euclidean_distances
from matplotlib.collections import LineCollection
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import MaxAbsScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import QuantileTransformer
from sklearn.preprocessing import PowerTransformer

Input="dataset/dataset.csv"
OUTPUT="datasetRegioni.js"
f = open(Input, 'r')
reader = csv.reader(f)

df = pd.read_csv('dataset/dataset.csv', encoding="utf-8")
target = df.Regioni
#print(target)
df = df.drop('Regioni', axis=1).reset_index(drop=True)
X = df.values

# PCA

standardscaler = StandardScaler().fit_transform(X)              # distanzia sulla destra lombardia, lazio e 
minmaxscaler = MinMaxScaler().fit_transform(X)                  # come standardscaler
normalizer = Normalizer().fit_transform(X)                      # raccoglie molise, valle d'aosta e basilicata sulla destra
quantiletransformer = QuantileTransformer().fit_transform(X)    # distribuisce in modo omogeneo dalla meno accidentata (sx) alla più accidentata (dx)
powertransformer = PowerTransformer().fit_transform(X)          # come quantile
pca = PCA(n_components=2)
scaler = powertransformer
principalComponents = pca.fit_transform(scaler)
if (scaler is standardscaler):
    scaler = "StandardScaler"
elif (scaler is minmaxscaler):
    scaler = "MinMaxScaler"
elif (scaler is normalizer):
    scaler = "Normalizer"
elif (scaler is quantiletransformer):
    scaler = "QuantileTransformer"
elif (scaler is powertransformer):
    scaler = "PowerTransformer"
else:
    scaler = "OriginalData"
principalDf = pd.DataFrame(data = principalComponents
             , columns = ['principal component 1', 'principal component 2'])
#print(principalDf)

finalDf = pd.concat([principalDf, target], axis = 1)
#print(finalDf)

#print(target)
i = 0
for elem in target:
    if ("Italia" in elem or "Totale" in elem):
        target = target.drop(i)
    i = i + 1
#print(target)
i = 0
targets = target
for round in range(13):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1) 
    ax.set_xlabel('Principal Component 1', fontsize = 15)
    ax.set_ylabel('Principal Component 2', fontsize = 15)
    if (i < 9):
        title = "2-component PCA 200" + str(i+1) + " " + str(scaler)
    else:
        title = "2-component PCA 20" + str(i+1) + " " + str(scaler)
    ax.set_title(title, fontsize = 20)
    ax.set_facecolor('xkcd:light grey')
    colors = []
    if round == 0:
        colors = [
            'r', 'g', 'b', '#d104b5', '#fffa00', '#a8ff7c', '#00ff00',
        '#00ffa1', '#ff96ca', '#cca72e', '#ff8800', '#5977ff', '#563700',
        '#898500', '#ddff96', '#96ffe3', '#96f9ff', '#b599ff', '#8b5b8e',
        '#7c0000']
    elif round == 1:
        colors = [
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
        'r', 'g', 'b', '#d104b5', '#fffa00', '#a8ff7c', '#00ff00',
        '#00ffa1', '#ff96ca', '#cca72e', '#ff8800', '#5977ff', '#563700',
        '#898500', '#ddff96', '#96ffe3', '#96f9ff', '#b599ff', '#8b5b8e',
        '#7c0000']
    elif round == 2:
        colors = [
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
        'r', 'g', 'b', '#d104b5', '#fffa00', '#a8ff7c', '#00ff00',
        '#00ffa1', '#ff96ca', '#cca72e', '#ff8800', '#5977ff', '#563700',
        '#898500', '#ddff96', '#96ffe3', '#96f9ff', '#b599ff', '#8b5b8e',
        '#7c0000']
    elif round == 3:
        colors = [
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
        'r', 'g', 'b', '#d104b5', '#fffa00', '#a8ff7c', '#00ff00',
        '#00ffa1', '#ff96ca', '#cca72e', '#ff8800', '#5977ff', '#563700',
        '#898500', '#ddff96', '#96ffe3', '#96f9ff', '#b599ff', '#8b5b8e',
        '#7c0000']
    elif round == 4:
        colors = [
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
        'r', 'g', 'b', '#d104b5', '#fffa00', '#a8ff7c', '#00ff00',
        '#00ffa1', '#ff96ca', '#cca72e', '#ff8800', '#5977ff', '#563700',
        '#898500', '#ddff96', '#96ffe3', '#96f9ff', '#b599ff', '#8b5b8e',
        '#7c0000']
    elif round == 5:
        colors = [
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
        'r', 'g', 'b', '#d104b5', '#fffa00', '#a8ff7c', '#00ff00',
        '#00ffa1', '#ff96ca', '#cca72e', '#ff8800', '#5977ff', '#563700',
        '#898500', '#ddff96', '#96ffe3', '#96f9ff', '#b599ff', '#8b5b8e',
        '#7c0000']
    elif round == 6:
        colors = [
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
        'r', 'g', 'b', '#d104b5', '#fffa00', '#a8ff7c', '#00ff00',
        '#00ffa1', '#ff96ca', '#cca72e', '#ff8800', '#5977ff', '#563700',
        '#898500', '#ddff96', '#96ffe3', '#96f9ff', '#b599ff', '#8b5b8e',
        '#7c0000']
    elif round == 7:
        colors = [
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
        'r', 'g', 'b', '#d104b5', '#fffa00', '#a8ff7c', '#00ff00',
        '#00ffa1', '#ff96ca', '#cca72e', '#ff8800', '#5977ff', '#563700',
        '#898500', '#ddff96', '#96ffe3', '#96f9ff', '#b599ff', '#8b5b8e',
        '#7c0000']
    elif round == 8:
        colors = [
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
        'r', 'g', 'b', '#d104b5', '#fffa00', '#a8ff7c', '#00ff00',
        '#00ffa1', '#ff96ca', '#cca72e', '#ff8800', '#5977ff', '#563700',
        '#898500', '#ddff96', '#96ffe3', '#96f9ff', '#b599ff', '#8b5b8e',
        '#7c0000']
    elif round == 9:
        colors = [
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
        'r', 'g', 'b', '#d104b5', '#fffa00', '#a8ff7c', '#00ff00',
        '#00ffa1', '#ff96ca', '#cca72e', '#ff8800', '#5977ff', '#563700',
        '#898500', '#ddff96', '#96ffe3', '#96f9ff', '#b599ff', '#8b5b8e',
        '#7c0000']
    elif round == 10:
        colors = [
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
        'r', 'g', 'b', '#d104b5', '#fffa00', '#a8ff7c', '#00ff00',
        '#00ffa1', '#ff96ca', '#cca72e', '#ff8800', '#5977ff', '#563700',
        '#898500', '#ddff96', '#96ffe3', '#96f9ff', '#b599ff', '#8b5b8e',
        '#7c0000']
    elif round == 11:
        colors = [
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
        'r', 'g', 'b', '#d104b5', '#fffa00', '#a8ff7c', '#00ff00',
        '#00ffa1', '#ff96ca', '#cca72e', '#ff8800', '#5977ff', '#563700',
        '#898500', '#ddff96', '#96ffe3', '#96f9ff', '#b599ff', '#8b5b8e',
        '#7c0000']
    elif round == 12:
        colors = [
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
        'r', 'g', 'b', '#d104b5', '#fffa00', '#a8ff7c', '#00ff00',
        '#00ffa1', '#ff96ca', '#cca72e', '#ff8800', '#5977ff', '#563700',
        '#898500', '#ddff96', '#96ffe3', '#96f9ff', '#b599ff', '#8b5b8e',
        '#7c0000']
    elif round == 13:
        colors = [
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
            'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey', 'xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey','xkcd:light grey',
        'r', 'g', 'b', '#d104b5', '#fffa00', '#a8ff7c', '#00ff00',
        '#00ffa1', '#ff96ca', '#cca72e', '#ff8800', '#5977ff', '#563700',
        '#898500', '#ddff96', '#96ffe3', '#96f9ff', '#b599ff', '#8b5b8e',
        '#7c0000']
    else:
        break
    
    for target, color in zip(targets,colors):
        indicesToKeep = finalDf['Regioni'] == target
        ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
                    , finalDf.loc[indicesToKeep, 'principal component 2']
                    , c = color               
                    , s = 50)
    ax.legend(targets)
    #ax.grid()
    if (i < 9):
        plt.savefig("plots/pca200"+str(i+1)+str(scaler)+".png")
    else:
        plt.savefig("plots/pca20"+str(i+1)+str(scaler)+".png")
    #plt.show()
    
    plt.close(fig)

    i = i +1
    #print(pca.explained_variance_ratio_)

# D3
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

