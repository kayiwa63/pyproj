from sklearn import datasets
irir_dataset = datasets.load_iris()
X = irir_dataset.data[:,:2]

x_count = len(X.flat)
x_min = X[:,0].min() - .5
x_max = X[:,0].min() + .5
x_mean = X[:,0].mean() 

p = x_count, x_min, x_max, x_mean

print(p)