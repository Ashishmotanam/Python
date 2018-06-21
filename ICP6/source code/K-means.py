import pandas
import pylab as pl
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
variables = pandas.read_csv('sample_stocks.csv') # reading data using panda library
Y = variables[['returns']]       #Storing returns and dividendyeildto x and y
X = variables[['dividendyield']]
X_norm = (X - X.mean()) / (X.max() - X.min()) # noramlizing the data for both x and y
Y_norm = (Y - Y.mean()) / (Y.max() - Y.min())
# finding number of clusters
Nc = range(1, 20)
kmeans = [KMeans(n_clusters=i) for i in Nc]  #kmeans
score = [kmeans[i].fit(Y).score(Y) for i in range(len(kmeans))]
# plotting data inorder to display elbow curve
pl.plot(Nc,score)
pl.xlabel('Number of Clusters')
pl.ylabel('Score')
pl.title('Elbow Curve')
pl.show()
pca = PCA(n_components=1).fit(Y) #principle component analysis
pca_d = pca.transform(Y)
pca_c = pca.transform(X)
kmeans=KMeans(n_clusters=3) # plotting data with repect to clusters we find in the elbow curve
kmeansoutput=kmeans.fit(Y)
pl.figure('3 Cluster K-Means')
pl.scatter(pca_c[:, 0], pca_d[:, 0], c=kmeansoutput.labels_)
pl.xlabel('Dividend Yield')
pl.ylabel('Returns')
pl.title('3 Cluster K-Means')
pl.show()