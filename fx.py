
from sklearn import datasets
iris = datasets.load_iris()

x = iris.data  # features
y = iris.target  # labels

# y = f(x)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = .5)
# y_train = f(x_train)
# y_test = f(x_test)

from sklearn import tree
cls = tree.DecisionTreeClassifier()
cls.fit(x_train, y_train)

predications = cls.predict(x_test)
print(predications)

from sklearn.metrics import accuracy_score  # 准确性比较
print(accuracy_score(y_test, predications))


from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier()
clf.fit(x_train, y_train)

predications2 = clf.predict(x_test)
print(predications)


print(accuracy_score(y_test, predications2))
